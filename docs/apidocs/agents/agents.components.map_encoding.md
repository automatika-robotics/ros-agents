---
orphan: true
---

# {py:mod}`agents.components.map_encoding`

```{py:module} agents.components.map_encoding
```

```{autodoc2-docstring} agents.components.map_encoding
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MapEncoding <agents.components.map_encoding.MapEncoding>`
  - ```{autodoc2-docstring} agents.components.map_encoding.MapEncoding
    :summary:
    ```
````

### API

````{py:class} MapEncoding(*, layers: list[agents.ros.MapLayer], position: agents.ros.Topic, map_meta_data: agents.ros.Topic, config: agents.config.MapConfig, db_client: agents.clients.db_base.DBClient, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float] = 10.0, callback_group=None, **kwargs)
:canonical: agents.components.map_encoding.MapEncoding

Bases: {py:obj}`agents.components.component_base.Component`

```{autodoc2-docstring} agents.components.map_encoding.MapEncoding
```

````
