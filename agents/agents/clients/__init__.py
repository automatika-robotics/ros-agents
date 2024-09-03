"""
Clients are standard interfaces for components to interact with ML models or vector DBs served by various platforms. Currently ROS Agents provides the following clients.

```{list-table}
:widths: 20 20 60
:header-rows: 1
* - Platform
  - Client
  - Description

* - **RoboML**
  - [HTTPModelClient](agents.clients.roboml.HTTPModelClient)
  - An HTTP client for interaction with ML models served on RoboML.

* - **RoboML**
  - [HTTPDBClient](agents.clients.roboml.HTTPDBClient)
  - An HTTP client for interaction with vector DBs served on RoboML.

* - **RoboML**
  - [RESPModelClient](agents.clients.roboml.RESPModelClient)
  - A Redis Serialization Protocol (RESP) based client for interaction with ML models served on RoboML

* - **RoboML**
  - [RESPDBClient](agents.clients.roboml.RESPDBClient)
  - A Redis Serialization Protocol (RESP) based client for interaction with vector DBs served on RoboML

* - **Ollama**
  - [OllamaClient](agents.clients.ollama.OllamaClient)
  - An HTTP client for interaction with ML models served on Ollama.

"""

from .ollama import OllamaClient
from .roboml import HTTPDBClient, HTTPModelClient, RESPDBClient, RESPModelClient


__all__ = [
    "OllamaClient",
    "HTTPDBClient",
    "HTTPModelClient",
    "RESPDBClient",
    "RESPModelClient",
]
