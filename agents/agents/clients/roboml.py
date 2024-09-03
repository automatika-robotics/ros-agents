import base64
import time
from enum import Enum
from typing import Any, Optional

import httpx
import msgpack
import msgpack_numpy as m_pack
from redis import Redis
from redis.exceptions import ConnectionError, ModuleError

from ..models import Model, OllamaModel
from ..utils import encode_arr_base64
from ..vectordbs import DB
from .db_base import DBClient
from .model_base import ModelClient

# patch msgpack for numpy arrays
m_pack.patch()

__all__ = ["HTTPModelClient", "HTTPDBClient", "RESPDBClient", "RESPModelClient"]


class Status(str, Enum):
    """Model Node Status."""

    LOADED = "LOADED"
    INITIALIZING = "INITIALIZING"
    READY = "READY"
    INITIALIZATION_ERROR = "INITIALIZATION_ERROR"


class RoboMLError(Exception):
    """RoboMLError."""

    pass


class HTTPModelClient(ModelClient):
    """An HTTP client for interaction with ML models served on RoboML"""

    def __init__(
        self,
        model: Model,
        host: str = "127.0.0.1",
        port: int = 8000,
        inference_timeout: int = 30,
        logging_level: str = "info",
    ):
        if isinstance(model, OllamaModel):
            raise TypeError(
                "An ollama model cannot be passed to a RoboML client. Please use the OllamaClient"
            )
        super().__init__(model, host, port, inference_timeout, logging_level)
        self.url = f"http://{self.host}:{self.port}"
        self._check_connection()

    def _check_connection(self) -> None:
        """Check if the platfrom is being served on specified IP and port"""
        # Ping remote server to check connection
        self.logger.info("Checking connection with remote RoboML")
        try:
            # port specific to ollama
            httpx.get(f"{self.url}/").raise_for_status()
        except Exception as e:
            self.__handle_exceptions(e)
            raise

    def _initialize(self) -> None:
        """
        Initialize the model on platform using the paramters provided in the model specification class
        """
        # Create a model node on RoboML
        self.logger.info("Creating model node on remote")
        start_params = {"node_name": self.model.name, "node_type": self.model_type}
        try:
            httpx.post(
                f"{self.url}/add_node", params=start_params, timeout=self.init_timeout
            ).raise_for_status()
            self.logger.info(f"Initializing {self.model.name} on RoboML remote")
            # get initialization params and initiale model
            model_dict = self.model._get_init_params()
            if hasattr(self.model, "system_prompt") and (
                sys_prompt := self.model.system_prompt  # type: ignore
            ):
                model_dict["system_prompt"] = sys_prompt
            httpx.post(
                f"{self.url}/{self.model.name}/initialize",
                params=model_dict,
                timeout=self.init_timeout,
            ).raise_for_status()
        except Exception as e:
            return self.__handle_exceptions(e)
        self.logger.info(f"{self.model.name} initialized on remote")

    def _inference(self, inference_input: dict[str, Any]) -> Optional[dict]:
        """Call inference on the model using data and inference parameters from the component"""
        try:
            # encode any byte or numpy array data
            if inference_input.get("query") and isinstance(
                inference_input["query"], bytes
            ):
                inference_input["query"] = base64.b64encode(
                    inference_input["query"]
                ).decode("utf-8")
            if images := inference_input.get("images"):
                inference_input["images"] = [encode_arr_base64(img) for img in images]
            # call inference method
            r = httpx.post(
                f"{self.url}/{self.model.name}/inference",
                json=inference_input,
                timeout=self.inference_timeout,
            ).raise_for_status()
            result = r.json()
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        # replace np images back in inference input
        if images:
            inference_input["images"] = images

        # make input query part of the result
        result.update(inference_input)
        return result

    def _deinitialize(self) -> None:
        """Deinitialize the model on the platform"""

        self.logger.error(f"Deinitializing {self.model.name} model on RoboML remote")
        stop_params = {"node_name": self.model.name}
        try:
            httpx.post(f"{self.url}/remove_node", params=stop_params).raise_for_status()
        except Exception as e:
            self.__handle_exceptions(e)

    def __handle_exceptions(self, excep: Exception) -> None:
        """__handle_exceptions.

        :param excep:
        :type excep: Exception
        :rtype: None
        """
        if isinstance(excep, httpx.RequestError):
            self.logger.error(
                f"{excep} RoboML server inaccessible. Might not be running. Make sure remote is correctly configured."
            )
        elif isinstance(excep, httpx.HTTPStatusError):
            try:
                excep_json = excep.response.json()
                self.logger.error(
                    f"RoboML server returned an invalid status code. Error: {excep_json}"
                )
            except Exception:
                self.logger.error(
                    f"RoboML server returned an invalid status code. Error: {excep}"
                )
        else:
            self.logger.error(str(excep))


class HTTPDBClient(DBClient):
    """An HTTP client for interaction with vector DBs served on RoboML"""

    def __init__(
        self,
        db: DB,
        host: str = "127.0.0.1",
        port: int = 8000,
        response_timeout: int = 30,
        logging_level: str = "info",
    ):
        super().__init__(db, host, port, logging_level)
        self.url = f"http://{self.host}:{self.port}"
        self.response_timeout = response_timeout
        self._check_connection()

    def _check_connection(self):
        """Check if the platfrom is being served on specified IP and port"""
        # Ping remote server to check connection
        self.logger.info("Checking connection with remote RoboML")
        try:
            # port specific to ollama
            httpx.get(f"{self.url}/").raise_for_status()
        except Exception as e:
            self.__handle_exceptions(e)
            raise

    def _initialize(self) -> None:
        """
        Initialize the vector DB on platform using the paramters provided in the DB specification class
        """
        # Create a DB node on RoboML
        self.logger.info("Creating db node on remote")
        start_params = {"node_name": self.db.name, "node_type": self.db_type}
        try:
            httpx.post(
                f"{self.url}/add_node", params=start_params, timeout=self.init_timeout
            ).raise_for_status()
            self.logger.info(f"Initializing {self.db.name} on RoboML remote")
            # get initialization params and initiale db
            db_dict = self.db._get_init_params()
            httpx.post(
                f"{self.url}/{self.db.name}/initialize",
                params=db_dict,
                timeout=self.init_timeout,
            ).raise_for_status()
        except Exception as e:
            return self.__handle_exceptions(e)
        self.logger.info(f"{self.db.name} initialized on remote")

    def _add(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Add data.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            # add to DB
            r = httpx.post(
                f"{self.url}/{self.db.name}/add",
                json=db_input,
                timeout=self.response_timeout,
            ).raise_for_status()
            result = r.json()
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _conditional_add(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Add data only if the ids dont exist. Otherwise update metadatas
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            # add to DB
            r = httpx.post(
                f"{self.url}/{self.db.name}/conditional_add",
                json=db_input,
                timeout=self.response_timeout,
            ).raise_for_status()
            result = r.json()
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _metadata_query(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Query based on given metadata.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            # query db
            r = httpx.post(
                f"{self.url}/{self.db.name}/metadata_query",
                json=db_input,
                timeout=self.response_timeout,
            ).raise_for_status()
            result = r.json()
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _query(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Query using a query string.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            # query db
            r = httpx.post(
                f"{self.url}/{self.db.name}/query",
                json=db_input,
                timeout=self.response_timeout,
            ).raise_for_status()
            result = r.json()
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _deinitialize(self) -> None:
        """Deinitialize DB on the platform"""

        self.logger.error(f"Deinitializing {self.db.name} on RoboML remote")
        stop_params = {"node_name": self.db.name}
        try:
            httpx.post(f"{self.url}/remove_node", params=stop_params).raise_for_status()
        except Exception as e:
            self.__handle_exceptions(e)

    def __handle_exceptions(self, excep: Exception) -> None:
        """__handle_exceptions.

        :param excep:
        :type excep: Exception
        :rtype: None
        """
        if isinstance(excep, httpx.RequestError):
            self.logger.error(
                f"{excep} RoboML server inaccessible. Might not be running. Make sure remote is correctly configured."
            )
        elif isinstance(excep, httpx.HTTPStatusError):
            try:
                excep_json = excep.response.json()
                self.logger.error(
                    f"RoboML server returned an invalid status code. Error: {excep_json}"
                )
            except Exception:
                self.logger.error(
                    f"RoboML server returned an invalid status code. Error: {excep}"
                )
        else:
            self.logger.error(str(excep))


class RESPModelClient(ModelClient):
    """A Redis Serialization Protocol (RESP) based client for interaction with ML models served on RoboML"""

    def __init__(
        self,
        model: Model,
        host: str = "127.0.0.1",
        port: int = 6379,
        inference_timeout: int = 30,
        logging_level: str = "info",
    ):
        if isinstance(model, OllamaModel):
            raise TypeError(
                "An ollama model cannot be passed to a RoboML client. Please use the OllamaClient"
            )
        super().__init__(model, host, port, inference_timeout, logging_level)
        # TODO: handle timeoout
        self.redis = Redis(self.host, port=self.port)
        self._check_connection()

    def _check_connection(self) -> None:
        """Check if the platfrom is being served on specified IP and port"""
        # Ping remote server to check connection
        self.logger.info("Checking connection with remote RoboML")
        try:
            self.redis.execute_command(b"PING")
        except Exception as e:
            self.__handle_exceptions(e)
            raise

    def _initialize(self) -> None:
        """
        Initialize the model on platform using the paramters provided in the model specification class
        """
        # Create a model node on RoboML
        self.logger.info("Creating model node on remote")
        start_params = {"node_name": self.model.name, "node_type": self.model_type}
        try:
            start_params_b = msgpack.packb(start_params)
            self.redis.execute_command("add_node", start_params_b)

            self.logger.info(f"Initializing {self.model.name} on RoboML remote")
            # make initialization params
            model_dict = self.model._get_init_params()
            if hasattr(self.model, "system_prompt") and (
                sys_prompt := self.model.system_prompt  # type: ignore
            ):
                model_dict["system_prompt"] = sys_prompt

            # initialize model
            init_b = msgpack.packb(model_dict)
            self.redis.execute_command(f"{self.model.name}.initialize", init_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        # check status for init completion after every second
        status = self.__check_model_status()
        counter = 0
        while status != Status.READY and counter < self.init_timeout:
            time.sleep(1)
            counter += 1
            status = self.__check_model_status()

        if status == Status.READY:
            self.logger.info(f"{self.model.name} model initialized on remote")
        elif status == Status.INITIALIZING:
            self.logger.error(f"{self.model.name} model initialization timed out.")
        elif status == Status.INITIALIZATION_ERROR:
            self.logger.error(
                f"{self.model.name} model initialization failed. Check remote for logs."
            )
        else:
            self.logger.error(
                f"Unexpected Error while initializing {self.model.name}: Check remote for logs."
            )

    def _inference(self, inference_input: dict[str, Any]) -> Optional[dict]:
        """Call inference on the model using data and inference parameters from the component"""
        try:
            data_b = msgpack.packb(inference_input)
            # call inference method
            result_b = self.redis.execute_command(
                f"{self.model.name}.inference", data_b
            )
            result = msgpack.unpackb(result_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        # make input query part of the result
        result.update(inference_input)
        return result

    def _deinitialize(self) -> None:
        """Deinitialize the model on the platform"""

        self.logger.error(f"Deinitializing {self.model.name} on RoboML remote")
        stop_params = {"node_name": self.model.name}
        try:
            stop_params_b = msgpack.packb(stop_params)
            self.redis.execute_command("remove_node", stop_params_b)
        except Exception as e:
            self.__handle_exceptions(e)

    def __check_model_status(self) -> Optional[str]:
        """Check remote model node status.
        :rtype: str | None
        """
        try:
            status_b = self.redis.execute_command(f"{self.model.name}.get_status")
            status = msgpack.unpackb(status_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        return status

    def __handle_exceptions(self, excep: Exception) -> None:
        """__handle_exceptions.

        :param excep:
        :type excep: Exception
        :rtype: None
        """
        if isinstance(excep, ConnectionError):
            self.logger.error(
                f"{excep} RoboML server inaccessible. Might not be running. Make sure remote is correctly configured."
            )
        elif isinstance(excep, ModuleError):
            self.logger.error(
                f"{self.model_type} is not a supported model type in RoboML library. Please use another model client or another model."
            )
            raise RoboMLError(
                f"{self.model_type} is not a supported model type in RoboML library. Please use another model client or another model."
            )
        else:
            self.logger.error(str(excep))


class RESPDBClient(DBClient):
    """A Redis Serialization Protocol (RESP) based client for interaction with vector DBs served on RoboML"""

    def __init__(
        self,
        db: DB,
        host: str = "127.0.0.1",
        port: int = 6379,
        logging_level: str = "info",
    ):
        super().__init__(db, host, port, logging_level)
        # TODO: handle timeout
        self.redis = Redis(self.host, port=self.port)
        self._check_connection()

    def _check_connection(self) -> None:
        """Check if the platfrom is being served on specified IP and port"""
        # Ping remote server to check connection
        self.logger.info("Checking connection with remote RoboML")
        try:
            self.redis.execute_command(b"PING")
        except Exception as e:
            self.__handle_exceptions(e)
            raise

    def _initialize(self) -> None:
        """
        Initialize the vector DB on platform using the paramters provided in the DB specification class
        """
        # Creating DB node on remote
        self.logger.info("Creating db node on remote")
        start_params = {"node_name": self.db.name, "node_type": self.db_type}

        try:
            start_params_b = msgpack.packb(start_params)
            self.redis.execute_command("add_node", start_params_b)
        except Exception as e:
            self.__handle_exceptions(e)

        self.logger.info(f"Initializing {self.db.name} on remote")
        try:
            db_dict = self.db._get_init_params()
            init_b = msgpack.packb(db_dict)
            # initialize database
            self.redis.execute_command(f"{self.db.name}.initialize", init_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        # check status for init completion after every second
        status = self.__check_db_status()
        counter = 0
        while status != Status.READY and counter < self.init_timeout:
            time.sleep(1)
            counter += 1
            status = self.__check_db_status()

        if status == Status.READY:
            self.logger.info(f"{self.db.name} db initialized on remote")
        elif status == Status.INITIALIZING:
            self.logger.error(f"{self.db.name} db initialization timed out.")
        elif status == Status.INITIALIZATION_ERROR:
            self.logger.error(
                f"{self.db.name} db initialization failed. Check remote for logs."
            )
        else:
            self.logger.error(
                f"Unexpected Error while initializing {self.db.name}: Check remote for logs."
            )

    def _add(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Add data.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            data_b = msgpack.packb(db_input)
            # add to DB
            result_b = self.redis.execute_command(f"{self.db.name}.add", data_b)
            result = msgpack.unpackb(result_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _conditional_add(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Add data only if the ids dont exist. Otherwise update metadatas
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            data_b = msgpack.packb(db_input)
            # add to DB
            result_b = self.redis.execute_command(
                f"{self.db.name}.conditional_add", data_b
            )
            result = msgpack.unpackb(result_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _metadata_query(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Query based on given metadata.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            data_b = msgpack.packb(db_input)
            # query db
            result_b = self.redis.execute_command(
                f"{self.db.name}.metadata_query", data_b
            )
            result = msgpack.unpackb(result_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _query(self, db_input: dict[str, Any]) -> Optional[dict]:
        """Query using a query string.
        :param db_input:
        :type db_input: dict[str, Any]
        :rtype: dict | None
        """
        try:
            data_b = msgpack.packb(db_input)
            # query db
            result_b = self.redis.execute_command(f"{self.db.name}.query", data_b)
            result = msgpack.unpackb(result_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        self.logger.debug(str(result))

        return result

    def _deinitialize(self) -> None:
        """Deinitialize DB on the platform"""

        self.logger.error(f"Deinitializing {self.db.name} on remote")
        stop_params = {"node_name": self.db.name}
        try:
            stop_params_b = msgpack.packb(stop_params)
            self.redis.execute_command("remove_node", stop_params_b)
        except Exception as e:
            self.__handle_exceptions(e)

    def __check_db_status(self) -> Optional[str]:
        """Check remote db node status.
        :rtype: str | None
        """
        try:
            status_b = self.redis.execute_command(f"{self.db.name}.get_status")
            status = msgpack.unpackb(status_b)
        except Exception as e:
            return self.__handle_exceptions(e)

        return status

    def __handle_exceptions(self, excep: Exception) -> None:
        """__handle_exceptions.

        :param excep:
        :type excep: Exception
        :rtype: None
        """
        if isinstance(excep, ConnectionError):
            self.logger.error(
                f"{excep} RoboML server inaccessible. Might not be running. Make sure remote is correctly configured."
            )
        elif isinstance(excep, ModuleError):
            self.logger.error(
                f"{self.db_type} is not a supported vectordb type in RoboML library. Please use another database client or another database."
            )
            raise RoboMLError(
                f"{self.db_type} is not a supported vectordb type in RoboML library. Please use another database client or another database."
            )
        else:
            self.logger.error(str(excep))
