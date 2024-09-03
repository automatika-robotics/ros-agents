---
orphan: true
---

# {py:mod}`agents.clients.roboml`

```{py:module} agents.clients.roboml
```

```{autodoc2-docstring} agents.clients.roboml
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HTTPModelClient <agents.clients.roboml.HTTPModelClient>`
  - ```{autodoc2-docstring} agents.clients.roboml.HTTPModelClient
    :summary:
    ```
* - {py:obj}`HTTPDBClient <agents.clients.roboml.HTTPDBClient>`
  - ```{autodoc2-docstring} agents.clients.roboml.HTTPDBClient
    :summary:
    ```
* - {py:obj}`RESPDBClient <agents.clients.roboml.RESPDBClient>`
  - ```{autodoc2-docstring} agents.clients.roboml.RESPDBClient
    :summary:
    ```
* - {py:obj}`RESPModelClient <agents.clients.roboml.RESPModelClient>`
  - ```{autodoc2-docstring} agents.clients.roboml.RESPModelClient
    :summary:
    ```
````

### API

````{py:class} HTTPModelClient(model: agents.models.Model, host: str = '127.0.0.1', port: int = 8000, inference_timeout: int = 30, logging_level: str = 'info')
:canonical: agents.clients.roboml.HTTPModelClient

Bases: {py:obj}`agents.clients.model_base.ModelClient`

```{autodoc2-docstring} agents.clients.roboml.HTTPModelClient
```

````

````{py:class} HTTPDBClient(db: agents.vectordbs.DB, host: str = '127.0.0.1', port: int = 8000, response_timeout: int = 30, logging_level: str = 'info')
:canonical: agents.clients.roboml.HTTPDBClient

Bases: {py:obj}`agents.clients.db_base.DBClient`

```{autodoc2-docstring} agents.clients.roboml.HTTPDBClient
```

````

````{py:class} RESPDBClient(db: agents.vectordbs.DB, host: str = '127.0.0.1', port: int = 6379, logging_level: str = 'info')
:canonical: agents.clients.roboml.RESPDBClient

Bases: {py:obj}`agents.clients.db_base.DBClient`

```{autodoc2-docstring} agents.clients.roboml.RESPDBClient
```

````

````{py:class} RESPModelClient(model: agents.models.Model, host: str = '127.0.0.1', port: int = 6379, inference_timeout: int = 30, logging_level: str = 'info')
:canonical: agents.clients.roboml.RESPModelClient

Bases: {py:obj}`agents.clients.model_base.ModelClient`

```{autodoc2-docstring} agents.clients.roboml.RESPModelClient
```

````
