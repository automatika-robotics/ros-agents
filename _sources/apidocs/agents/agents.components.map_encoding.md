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

`````{py:class} MapEncoding(*, layers: typing.List[agents.ros.MapLayer], position: agents.ros.Topic, map_topic: agents.ros.Topic, config: agents.config.MapConfig, db_client: agents.clients.db_base.DBClient, trigger: typing.Union[agents.ros.Topic, typing.List[agents.ros.Topic], float] = 10.0, component_name: str, callback_group=None, **kwargs)
:canonical: agents.components.map_encoding.MapEncoding

Bases: {py:obj}`agents.components.component_base.Component`

```{autodoc2-docstring} agents.components.map_encoding.MapEncoding
```

````{py:method} custom_on_configure()
:canonical: agents.components.map_encoding.MapEncoding.custom_on_configure

```{autodoc2-docstring} agents.components.map_encoding.MapEncoding.custom_on_configure
```

````

````{py:method} custom_on_deactivate()
:canonical: agents.components.map_encoding.MapEncoding.custom_on_deactivate

```{autodoc2-docstring} agents.components.map_encoding.MapEncoding.custom_on_deactivate
```

````

````{py:method} add_point(layer: agents.ros.MapLayer, point: typing.Tuple[numpy.ndarray, str]) -> None
:canonical: agents.components.map_encoding.MapEncoding.add_point

```{autodoc2-docstring} agents.components.map_encoding.MapEncoding.add_point
```

````

`````
