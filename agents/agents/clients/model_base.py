from abc import ABC, abstractmethod
from typing import Any, Optional

from rclpy import logging

from ..models import Model
from ..utils import validate_func_args


class ModelClient(ABC):
    """MLClient."""

    @validate_func_args
    def __init__(
        self,
        model: Model,
        host: Optional[str] = None,
        port: Optional[int] = None,
        inference_timeout: int = 30,
        init_on_activation: bool = True,
        logging_level: str = "info",
    ):
        """__init__.
        :param model:
        :type model: Model
        :param host:
        :type host: Optional[str]
        :param port:
        :type port: Optional[int]
        :param inference_timeout:
        :type inference_timeout: int
        :param logging_level:
        :type logging_level: str
        """
        self.model = model
        self.model_type = model.__class__.__name__
        self.host = host
        self.port = port
        self.init_on_activation = init_on_activation
        self.logger = logging.get_logger(self.model.name)
        logging.set_logger_level(
            self.model.name, logging.get_logging_severity_from_string(logging_level)
        )
        self.init_timeout = self.model.init_timeout
        self.inference_timeout = inference_timeout

    def check_connection(self) -> None:
        """initialize.
        :rtype: None
        """
        self._check_connection()

    def initialize(self) -> None:
        """initialize.
        :rtype: None
        """
        if self.init_on_activation:
            self._initialize()

    def inference(self, inference_input: dict[str, Any]) -> Optional[dict]:
        """inference.
        :param inference_input:
        :type inference_input: dict[str, Any]
        :rtype: dict | None
        """
        return self._inference(inference_input)

    def deinitialize(self):
        """deinitialize."""
        # TODO: Add check for model initialization by keeping model
        # state in client
        if self.init_on_activation:
            self._deinitialize()

    @abstractmethod
    def _check_connection(self) -> None:
        """check_connection.
        :rtype: None
        """
        raise NotImplementedError(
            "This method needs to be implemented in a child class"
        )

    @abstractmethod
    def _initialize(self) -> None:
        """initialize.
        :rtype: None
        """
        raise NotImplementedError(
            "This method needs to be implemented in a child class"
        )

    @abstractmethod
    def _inference(self, inference_input: dict[str, Any]) -> Optional[dict]:
        """inference.
        :param inference_input:
        :type inference_input: dict[str, Any]
        :rtype: dict | None
        """
        raise NotImplementedError(
            "This method needs to be implemented in a child class"
        )

    @abstractmethod
    def _deinitialize(self):
        """deinitialize."""
        raise NotImplementedError(
            "This method needs to be implemented in a child class"
        )
