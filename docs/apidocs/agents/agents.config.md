---
orphan: true
---

# {py:mod}`agents.config`

```{py:module} agents.config
```

```{autodoc2-docstring} agents.config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LLMConfig <agents.config.LLMConfig>`
  - ```{autodoc2-docstring} agents.config.LLMConfig
    :summary:
    ```
* - {py:obj}`MLLMConfig <agents.config.MLLMConfig>`
  - ```{autodoc2-docstring} agents.config.MLLMConfig
    :summary:
    ```
* - {py:obj}`VisionConfig <agents.config.VisionConfig>`
  - ```{autodoc2-docstring} agents.config.VisionConfig
    :summary:
    ```
* - {py:obj}`TextToSpeechConfig <agents.config.TextToSpeechConfig>`
  - ```{autodoc2-docstring} agents.config.TextToSpeechConfig
    :summary:
    ```
* - {py:obj}`SpeechToTextConfig <agents.config.SpeechToTextConfig>`
  - ```{autodoc2-docstring} agents.config.SpeechToTextConfig
    :summary:
    ```
* - {py:obj}`MapConfig <agents.config.MapConfig>`
  - ```{autodoc2-docstring} agents.config.MapConfig
    :summary:
    ```
* - {py:obj}`SemanticRouterConfig <agents.config.SemanticRouterConfig>`
  - ```{autodoc2-docstring} agents.config.SemanticRouterConfig
    :summary:
    ```
* - {py:obj}`VideoMessageMakerConfig <agents.config.VideoMessageMakerConfig>`
  - ```{autodoc2-docstring} agents.config.VideoMessageMakerConfig
    :summary:
    ```
````

### API

`````{py:class} LLMConfig
:canonical: agents.config.LLMConfig

Bases: {py:obj}`agents.ros.BaseComponentConfig`

```{autodoc2-docstring} agents.config.LLMConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.LLMConfig.asdict

```{autodoc2-docstring} agents.config.LLMConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.LLMConfig.from_dict

```{autodoc2-docstring} agents.config.LLMConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.LLMConfig.from_yaml

```{autodoc2-docstring} agents.config.LLMConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.LLMConfig.to_json

```{autodoc2-docstring} agents.config.LLMConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.LLMConfig.from_json

```{autodoc2-docstring} agents.config.LLMConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.LLMConfig.has_attribute

```{autodoc2-docstring} agents.config.LLMConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.LLMConfig.get_attribute_type

```{autodoc2-docstring} agents.config.LLMConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.LLMConfig.update_value

```{autodoc2-docstring} agents.config.LLMConfig.update_value
```

````

`````

`````{py:class} MLLMConfig
:canonical: agents.config.MLLMConfig

Bases: {py:obj}`agents.config.LLMConfig`

```{autodoc2-docstring} agents.config.MLLMConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.MLLMConfig.asdict

```{autodoc2-docstring} agents.config.MLLMConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.MLLMConfig.from_dict

```{autodoc2-docstring} agents.config.MLLMConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.MLLMConfig.from_yaml

```{autodoc2-docstring} agents.config.MLLMConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.MLLMConfig.to_json

```{autodoc2-docstring} agents.config.MLLMConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.MLLMConfig.from_json

```{autodoc2-docstring} agents.config.MLLMConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.MLLMConfig.has_attribute

```{autodoc2-docstring} agents.config.MLLMConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.MLLMConfig.get_attribute_type

```{autodoc2-docstring} agents.config.MLLMConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.MLLMConfig.update_value

```{autodoc2-docstring} agents.config.MLLMConfig.update_value
```

````

`````

`````{py:class} VisionConfig
:canonical: agents.config.VisionConfig

Bases: {py:obj}`agents.ros.BaseComponentConfig`

```{autodoc2-docstring} agents.config.VisionConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.VisionConfig.asdict

```{autodoc2-docstring} agents.config.VisionConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.VisionConfig.from_dict

```{autodoc2-docstring} agents.config.VisionConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.VisionConfig.from_yaml

```{autodoc2-docstring} agents.config.VisionConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.VisionConfig.to_json

```{autodoc2-docstring} agents.config.VisionConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.VisionConfig.from_json

```{autodoc2-docstring} agents.config.VisionConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.VisionConfig.has_attribute

```{autodoc2-docstring} agents.config.VisionConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.VisionConfig.get_attribute_type

```{autodoc2-docstring} agents.config.VisionConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.VisionConfig.update_value

```{autodoc2-docstring} agents.config.VisionConfig.update_value
```

````

`````

`````{py:class} TextToSpeechConfig
:canonical: agents.config.TextToSpeechConfig

Bases: {py:obj}`agents.ros.BaseComponentConfig`

```{autodoc2-docstring} agents.config.TextToSpeechConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.TextToSpeechConfig.asdict

```{autodoc2-docstring} agents.config.TextToSpeechConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.TextToSpeechConfig.from_dict

```{autodoc2-docstring} agents.config.TextToSpeechConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.TextToSpeechConfig.from_yaml

```{autodoc2-docstring} agents.config.TextToSpeechConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.TextToSpeechConfig.to_json

```{autodoc2-docstring} agents.config.TextToSpeechConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.TextToSpeechConfig.from_json

```{autodoc2-docstring} agents.config.TextToSpeechConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.TextToSpeechConfig.has_attribute

```{autodoc2-docstring} agents.config.TextToSpeechConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.TextToSpeechConfig.get_attribute_type

```{autodoc2-docstring} agents.config.TextToSpeechConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.TextToSpeechConfig.update_value

```{autodoc2-docstring} agents.config.TextToSpeechConfig.update_value
```

````

`````

`````{py:class} SpeechToTextConfig
:canonical: agents.config.SpeechToTextConfig

Bases: {py:obj}`agents.ros.BaseComponentConfig`

```{autodoc2-docstring} agents.config.SpeechToTextConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.SpeechToTextConfig.asdict

```{autodoc2-docstring} agents.config.SpeechToTextConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.SpeechToTextConfig.from_dict

```{autodoc2-docstring} agents.config.SpeechToTextConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.SpeechToTextConfig.from_yaml

```{autodoc2-docstring} agents.config.SpeechToTextConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.SpeechToTextConfig.to_json

```{autodoc2-docstring} agents.config.SpeechToTextConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.SpeechToTextConfig.from_json

```{autodoc2-docstring} agents.config.SpeechToTextConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.SpeechToTextConfig.has_attribute

```{autodoc2-docstring} agents.config.SpeechToTextConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.SpeechToTextConfig.get_attribute_type

```{autodoc2-docstring} agents.config.SpeechToTextConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.SpeechToTextConfig.update_value

```{autodoc2-docstring} agents.config.SpeechToTextConfig.update_value
```

````

`````

`````{py:class} MapConfig
:canonical: agents.config.MapConfig

Bases: {py:obj}`agents.ros.BaseComponentConfig`

```{autodoc2-docstring} agents.config.MapConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.MapConfig.asdict

```{autodoc2-docstring} agents.config.MapConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.MapConfig.from_dict

```{autodoc2-docstring} agents.config.MapConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.MapConfig.from_yaml

```{autodoc2-docstring} agents.config.MapConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.MapConfig.to_json

```{autodoc2-docstring} agents.config.MapConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.MapConfig.from_json

```{autodoc2-docstring} agents.config.MapConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.MapConfig.has_attribute

```{autodoc2-docstring} agents.config.MapConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.MapConfig.get_attribute_type

```{autodoc2-docstring} agents.config.MapConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.MapConfig.update_value

```{autodoc2-docstring} agents.config.MapConfig.update_value
```

````

`````

`````{py:class} SemanticRouterConfig
:canonical: agents.config.SemanticRouterConfig

Bases: {py:obj}`agents.ros.BaseComponentConfig`

```{autodoc2-docstring} agents.config.SemanticRouterConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.SemanticRouterConfig.asdict

```{autodoc2-docstring} agents.config.SemanticRouterConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.SemanticRouterConfig.from_dict

```{autodoc2-docstring} agents.config.SemanticRouterConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.SemanticRouterConfig.from_yaml

```{autodoc2-docstring} agents.config.SemanticRouterConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.SemanticRouterConfig.to_json

```{autodoc2-docstring} agents.config.SemanticRouterConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.SemanticRouterConfig.from_json

```{autodoc2-docstring} agents.config.SemanticRouterConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.SemanticRouterConfig.has_attribute

```{autodoc2-docstring} agents.config.SemanticRouterConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.SemanticRouterConfig.get_attribute_type

```{autodoc2-docstring} agents.config.SemanticRouterConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.SemanticRouterConfig.update_value

```{autodoc2-docstring} agents.config.SemanticRouterConfig.update_value
```

````

`````

`````{py:class} VideoMessageMakerConfig
:canonical: agents.config.VideoMessageMakerConfig

Bases: {py:obj}`agents.ros.BaseComponentConfig`

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.config.VideoMessageMakerConfig.asdict

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.config.VideoMessageMakerConfig.from_dict

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.config.VideoMessageMakerConfig.from_yaml

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.config.VideoMessageMakerConfig.to_json

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.config.VideoMessageMakerConfig.from_json

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.config.VideoMessageMakerConfig.has_attribute

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.config.VideoMessageMakerConfig.get_attribute_type

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.config.VideoMessageMakerConfig.update_value

```{autodoc2-docstring} agents.config.VideoMessageMakerConfig.update_value
```

````

`````
