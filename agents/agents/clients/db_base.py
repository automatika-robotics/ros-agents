from abc import ABC, abstractmethod
from typing import Any, Optional

from rclpy import logging

from ..vectordbs import DB
from ..utils import validate_func_args


class DBClient(ABC):
    """DBClient."""

    @validate_func_args
    def __init__(
        self,
        db: DB,
        host: Optional[str] = None,
        port: Optional[int] = None,
        logging_level: str = "info",
    ):
        """__init__.
        :param db:
        :type db: DB
        :param host:
        :type host: Optional[str]
        :param port:
        :type port: Optional[int]
        :param logging_level:
        :type logging_level: str
        """
        self.db = db
        self.db_type = db.__class__.__name__
        self.host = host
        self.port = port
        self.logger = logging.get_logger(self.db.name)
        logging.set_logger_level(
            self.db.name, logging.get_logging_severity_from_string(logging_level)
        )
        self.init_timeout = self.db.init_timeout

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
    def _add(self, db_input: dict[str, Any]) -> Optional[dict]:
        """add data.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        raise NotImplementedError(
            "This method needs to be implemented in a child class"
        )

    @abstractmethod
    def _conditional_add(self, db_input: dict[str, Any]) -> Optional[dict]:
        """add data if given ids dont exist. Update metadatas of the ids that exist
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        raise NotImplementedError(
            "This method needs to be implemented in a child class"
        )

    @abstractmethod
    def _metadata_query(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Query based on given metadata.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        raise NotImplementedError(
            "This method needs to be implemented in a child class"
        )

    @abstractmethod
    def _query(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Query based on query string.
        :param db_input:
        :type db_input: dict[str, Any]
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
