# {py:mod}`agents.ros`

```{py:module} agents.ros
```

```{autodoc2-docstring} agents.ros
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Topic <agents.ros.Topic>`
  - ```{autodoc2-docstring} agents.ros.Topic
    :summary:
    ```
* - {py:obj}`FixedInput <agents.ros.FixedInput>`
  - ```{autodoc2-docstring} agents.ros.FixedInput
    :summary:
    ```
* - {py:obj}`MapLayer <agents.ros.MapLayer>`
  - ```{autodoc2-docstring} agents.ros.MapLayer
    :summary:
    ```
* - {py:obj}`Route <agents.ros.Route>`
  - ```{autodoc2-docstring} agents.ros.Route
    :summary:
    ```
````

### API

`````{py:class} Topic
:canonical: agents.ros.Topic

Bases: {py:obj}`auto_ros.topic.BaseTopic`

```{autodoc2-docstring} agents.ros.Topic
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.ros.Topic.asdict

```{autodoc2-docstring} agents.ros.Topic.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.ros.Topic.from_dict

```{autodoc2-docstring} agents.ros.Topic.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.ros.Topic.from_yaml

```{autodoc2-docstring} agents.ros.Topic.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.ros.Topic.to_json

```{autodoc2-docstring} agents.ros.Topic.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.ros.Topic.from_json

```{autodoc2-docstring} agents.ros.Topic.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.ros.Topic.has_attribute

```{autodoc2-docstring} agents.ros.Topic.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.ros.Topic.get_attribute_type

```{autodoc2-docstring} agents.ros.Topic.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.ros.Topic.update_value

```{autodoc2-docstring} agents.ros.Topic.update_value
```

````

`````

`````{py:class} FixedInput
:canonical: agents.ros.FixedInput

Bases: {py:obj}`ros_sugar.base_attrs.BaseAttrs`

```{autodoc2-docstring} agents.ros.FixedInput
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.ros.FixedInput.asdict

```{autodoc2-docstring} agents.ros.FixedInput.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.ros.FixedInput.from_dict

```{autodoc2-docstring} agents.ros.FixedInput.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.ros.FixedInput.from_yaml

```{autodoc2-docstring} agents.ros.FixedInput.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.ros.FixedInput.to_json

```{autodoc2-docstring} agents.ros.FixedInput.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.ros.FixedInput.from_json

```{autodoc2-docstring} agents.ros.FixedInput.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.ros.FixedInput.has_attribute

```{autodoc2-docstring} agents.ros.FixedInput.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.ros.FixedInput.get_attribute_type

```{autodoc2-docstring} agents.ros.FixedInput.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.ros.FixedInput.update_value

```{autodoc2-docstring} agents.ros.FixedInput.update_value
```

````

`````

`````{py:class} MapLayer
:canonical: agents.ros.MapLayer

Bases: {py:obj}`ros_sugar.base_attrs.BaseAttrs`

```{autodoc2-docstring} agents.ros.MapLayer
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.ros.MapLayer.asdict

```{autodoc2-docstring} agents.ros.MapLayer.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.ros.MapLayer.from_dict

```{autodoc2-docstring} agents.ros.MapLayer.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.ros.MapLayer.from_yaml

```{autodoc2-docstring} agents.ros.MapLayer.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.ros.MapLayer.to_json

```{autodoc2-docstring} agents.ros.MapLayer.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.ros.MapLayer.from_json

```{autodoc2-docstring} agents.ros.MapLayer.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.ros.MapLayer.has_attribute

```{autodoc2-docstring} agents.ros.MapLayer.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.ros.MapLayer.get_attribute_type

```{autodoc2-docstring} agents.ros.MapLayer.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.ros.MapLayer.update_value

```{autodoc2-docstring} agents.ros.MapLayer.update_value
```

````

`````

`````{py:class} Route
:canonical: agents.ros.Route

Bases: {py:obj}`ros_sugar.base_attrs.BaseAttrs`

```{autodoc2-docstring} agents.ros.Route
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.ros.Route.asdict

```{autodoc2-docstring} agents.ros.Route.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.ros.Route.from_dict

```{autodoc2-docstring} agents.ros.Route.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.ros.Route.from_yaml

```{autodoc2-docstring} agents.ros.Route.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.ros.Route.to_json

```{autodoc2-docstring} agents.ros.Route.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.ros.Route.from_json

```{autodoc2-docstring} agents.ros.Route.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.ros.Route.has_attribute

```{autodoc2-docstring} agents.ros.Route.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.ros.Route.get_attribute_type

```{autodoc2-docstring} agents.ros.Route.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.ros.Route.update_value

```{autodoc2-docstring} agents.ros.Route.update_value
```

````

`````
