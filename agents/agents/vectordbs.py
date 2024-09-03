"""
The following vector DB specification classes are meant to define a comman interface for initialization of vector DBs. Currently the only supported vector DB is Chroma.
"""

from typing import Optional

from attrs import define, field
from .ros import BaseAttrs
from .models import Encoder

__all__ = ["ChromaDB"]


@define(kw_only=True)
class DB(BaseAttrs):
    """This class describes a database initialization configuration."""

    name: str
    db_location: str = field(default="./data")
    username: Optional[str] = field(default=None)
    password: Optional[str] = field(default=None)
    encoder: Optional[Encoder] = field(default=None)
    init_timeout: int = field(default=600)  # 10 minutes
    host: str = field(default="127.0.0.1")
    port: Optional[int] = field(default=None)

    def _get_init_params(self) -> dict:
        params = {
            "username": self.username,
            "password": self.password,
            "db_location": self.db_location,
        }
        if self.encoder:
            params["encoder"] = self.encoder.get_init_params()
        return params


@define(kw_only=True)
class ChromaDB(DB):
    """[Chroma](https://www.trychroma.com/) is the open-source AI application database. It provides embeddings, vector search, document storage, full-text search, metadata filtering, and multi-modal retreival support.

    :param name: An arbitrary name given to the database.
    :type name: str
    :param db_location: The on-disk location where the database will be initialized. Defaults to "./data".
    :type db_location: str, optional
    :param username: The username for authentication. Defaults to None.
    :type username: Optional[str], optional
    :param password: The password for authentication. Defaults to None.
    :type password: Optional[str], optional
    :param encoder: An optional encoder model to use for text encoding. Defaults to None.
    :type encoder: Optional[Encoder], optional
    :param init_timeout: The timeout in seconds for the initialization process. Defaults to 10 minutes (600 seconds).
    :type init_timeout: int, optional
    :param host: The hostname or IP address of the database server. Defaults to "127.0.0.1".
    :type host: str, optional
    :param port: The port number to connect to the database server. Defaults to None.
    :type port: Optional[int], optional

    Example usage:
    ```python
    from agents.models import Encoder
    db_config = DB(name='my_database', username='user123', password='pass123')
    db_config.db_location = '/path/to/new/location'
    db_config.encoder = Encoder(checkpoint="BAAI/bge-small-en")
    ```
    """

    pass
