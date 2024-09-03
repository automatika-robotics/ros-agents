import base64
import inspect
import uuid
from functools import wraps
from enum import Enum
from io import BytesIO
from pathlib import Path
from types import GenericAlias, UnionType
from typing import Optional, Union, _UnionGenericAlias, get_args, get_origin

import cv2
import numpy as np
from attrs import Attribute
from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError
from jinja2.environment import Template
from PIL import Image
from pypdf import PdfReader
from rclpy.logging import get_logger
from .pluralize import pluralize


def create_detection_context(obj_list: list | None) -> str:
    """
    Creates a context prompt based on detections.
    :param      detections:  The detections
    :type       detections:  str
    :returns:   Context string
    :rtype:     str
    """
    if not obj_list:
        return ""
    context_list = []
    for obj_class in set(obj_list):
        obj_count = obj_list.count(obj_class)
        if obj_count > 1:
            context_list.append(f"{str(obj_count)} {pluralize(obj_class)}")
        else:
            context_list.append(f"{str(obj_count)} {obj_class}")

    if len(obj_list) > 1:
        return f'{", ".join(context_list)}'
    return f"{context_list[0]}"


def get_prompt_template(template: Union[str, Path]) -> Template:
    """Method to read prompt jinja prompt templates
    :param template:
    :type template: str | Path
    :rtype: None
    """
    if Path(template).exists():
        try:
            env = Environment(
                loader=FileSystemLoader(Path(template).parent), autoescape=True
            )
            return env.get_template(Path(template).name)
        except TemplateSyntaxError:
            get_logger("leibniz").error("Incorrectly specified jinja2 template")
            raise
        except Exception as e:
            get_logger("leibniz").error(
                f"Exception occured while reading template from file: {e}"
            )
            raise
    else:
        # read from string
        try:
            env = Environment()
            return env.from_string(format(template))
        except TemplateSyntaxError:
            get_logger("leibniz").error("Incorrectly specified jinja2 template")
            raise


def validate_kwargs(_, attribute: Attribute, value: dict):
    """Validate kwargs
    :param attribute:
    :type attribute: Attribute
    :param value:
    :type value: dict
    """

    def _create_default_type_str():
        """_create_default_type_str."""
        return "\n".join([f"{k}: {type(v)}" for k, v in attribute.default.items()])

    try:
        value_keys = value.keys()
    except AttributeError as e:
        raise AttributeError(f"{attribute.name} needs to be set with a dict") from e

    for key in value_keys:
        if key not in attribute.default:
            raise AttributeError(
                f"{attribute.name} can be one of the following:\n{_create_default_type_str()}"
            )
    # add missings to final value of attribute
    for k, v in attribute.default.items():
        if k not in value_keys:
            value[k] = v


def check_type_from_signature(value, fn_param: inspect.Parameter) -> None:
    """Check parameter value type based on parameter signature.
    :param value:
    :param fn_param:
    :type fn_param: inspect.Parameter
    :rtype: None
    """
    # Handles only one layer of Union
    if isinstance(fn_param.annotation, (_UnionGenericAlias, UnionType)):
        _annotated_types = get_args(fn_param.annotation)
    else:
        _annotated_types = [fn_param.annotation]

    # Handles only the origin of GenericAlias (dict, list)
    _annotated_types = [
        get_origin(t) if isinstance(t, GenericAlias) else t for t in _annotated_types
    ]

    type_check = any(isinstance(value, t) for t in _annotated_types)
    if not type_check:
        raise TypeError(
            f"Invalid type encountered for {fn_param.name}. Should be of type(s) {fn_param.annotation}"
        )


def check_type_from_default(value, fn_param: inspect.Parameter) -> None:
    """Check parameter value type based on default value.
    :param value:
    :param fn_param:
    :type fn_param: inspect.Parameter
    :rtype: None
    """
    # for parameters with default value
    _default = fn_param.default
    # Flag to skip parameters with None as default value
    is_none = _default is None or value is None

    if not is_none and not isinstance(value, type(_default)):
        raise TypeError(
            f"Invalid type encountered for {fn_param.name}. Expected type {type(_default)}"
        )


def validate_func_args(func):
    """Decorator for validating function parameters based on function signature
    :param func:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper.
        :param args:
        :param kwargs:
        """
        args_count = len(args)
        fn_params = inspect.signature(func).parameters

        # for parameters with annotation, preference is given to checking by annotation
        for arg, param in zip(args, list(fn_params)[:args_count]):
            if fn_params[param].annotation is not fn_params[param].empty:
                check_type_from_signature(arg, fn_params[param])
            elif fn_params[param].default is not fn_params[param].empty:
                check_type_from_default(arg, fn_params[param])

        for kwarg, value in kwargs.items():
            param = fn_params.get(kwarg)
            if not param:
                continue
            if fn_params[kwarg].annotation is not fn_params[kwarg].empty:
                check_type_from_signature(value, fn_params[kwarg])
            elif fn_params[kwarg].default is not fn_params[kwarg].empty:
                check_type_from_default(value, fn_params[kwarg])

        # Call the function after validation
        result = func(*args, **kwargs)
        return result

    return wrapper


def encode_arr_base64(img: np.ndarray) -> str:
    """Encode a numpy array to a base64 str.
    :param img:
    :type img: np.ndarray
    :rtype: str
    """
    encode_params = [int(cv2.IMWRITE_PNG_COMPRESSION), 9]
    _, buffer = cv2.imencode(".png", img, encode_params)
    return base64.b64encode(buffer).decode("utf-8")


class VADStatus(Enum):
    """VAD Status for start and end of detected speech"""

    START = 0
    END = 1


class PDFReader:
    """Load pdf using pdfreader. Used for testing"""

    @validate_func_args
    def __init__(
        self,
        pdf_file: Union[str, Path],
        password: Optional[str] = None,
    ) -> None:
        """__init__.
        :param pdf_file:
        :type pdf_file: Union[str, Path]
        :param password:
        :type password: Optional[str]
        :rtype: None
        """
        if not Path(pdf_file).is_file():
            raise TypeError(f"{pdf_file} is not a valid file")
        try:
            self.reader = PdfReader(pdf_file, password=password)
        except Exception as e:
            raise TypeError(f"{pdf_file} is not a valid PDF") from e

    def extract(self, extract_images: bool = False):
        """Extract text from PDF documents.
        :param extract_images
        :type extract_images: bool
        """
        metadatas = []
        documents = []
        images = []
        ids = []

        for page_num, page in enumerate(self.reader.pages):
            # add pdf metadata as reader metadata and add pagenumber to it
            metadata = self.reader.metadata if self.reader.metadata else {}
            metadata["page"] = page_num
            metadatas.append(metadata)
            # get content
            content = page.get_contents()
            documents.append(content)
            # create a unique ID
            ids.append(str(uuid.uuid5(uuid.NAMESPACE_DNS, content)))
            # get images if asked
            if extract_images:
                page_images = [Image.open(BytesIO(img.data)) for img in page.images]
                images += page_images

        return ids, metadatas, documents
