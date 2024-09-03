# {py:mod}`agents.models`

```{py:module} agents.models
```

```{autodoc2-docstring} agents.models
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Encoder <agents.models.Encoder>`
  - ```{autodoc2-docstring} agents.models.Encoder
    :summary:
    ```
* - {py:obj}`Llama3_1 <agents.models.Llama3_1>`
  - ```{autodoc2-docstring} agents.models.Llama3_1
    :summary:
    ```
* - {py:obj}`OllamaModel <agents.models.OllamaModel>`
  - ```{autodoc2-docstring} agents.models.OllamaModel
    :summary:
    ```
* - {py:obj}`Idefics <agents.models.Idefics>`
  - ```{autodoc2-docstring} agents.models.Idefics
    :summary:
    ```
* - {py:obj}`Idefics2 <agents.models.Idefics2>`
  - ```{autodoc2-docstring} agents.models.Idefics2
    :summary:
    ```
* - {py:obj}`Llava <agents.models.Llava>`
  - ```{autodoc2-docstring} agents.models.Llava
    :summary:
    ```
* - {py:obj}`Whisper <agents.models.Whisper>`
  - ```{autodoc2-docstring} agents.models.Whisper
    :summary:
    ```
* - {py:obj}`InstructBlip <agents.models.InstructBlip>`
  - ```{autodoc2-docstring} agents.models.InstructBlip
    :summary:
    ```
* - {py:obj}`SpeechT5 <agents.models.SpeechT5>`
  - ```{autodoc2-docstring} agents.models.SpeechT5
    :summary:
    ```
* - {py:obj}`Bark <agents.models.Bark>`
  - ```{autodoc2-docstring} agents.models.Bark
    :summary:
    ```
* - {py:obj}`VisionModel <agents.models.VisionModel>`
  - ```{autodoc2-docstring} agents.models.VisionModel
    :summary:
    ```
````

### API

`````{py:class} Encoder
:canonical: agents.models.Encoder

Bases: {py:obj}`agents.models.Model`

```{autodoc2-docstring} agents.models.Encoder
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.Encoder.asdict

```{autodoc2-docstring} agents.models.Encoder.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.Encoder.from_dict

```{autodoc2-docstring} agents.models.Encoder.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.Encoder.from_yaml

```{autodoc2-docstring} agents.models.Encoder.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.Encoder.to_json

```{autodoc2-docstring} agents.models.Encoder.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.Encoder.from_json

```{autodoc2-docstring} agents.models.Encoder.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.Encoder.has_attribute

```{autodoc2-docstring} agents.models.Encoder.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.Encoder.get_attribute_type

```{autodoc2-docstring} agents.models.Encoder.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.Encoder.update_value

```{autodoc2-docstring} agents.models.Encoder.update_value
```

````

`````

`````{py:class} Llama3_1
:canonical: agents.models.Llama3_1

Bases: {py:obj}`agents.models.LLM`

```{autodoc2-docstring} agents.models.Llama3_1
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.Llama3_1.asdict

```{autodoc2-docstring} agents.models.Llama3_1.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.Llama3_1.from_dict

```{autodoc2-docstring} agents.models.Llama3_1.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.Llama3_1.from_yaml

```{autodoc2-docstring} agents.models.Llama3_1.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.Llama3_1.to_json

```{autodoc2-docstring} agents.models.Llama3_1.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.Llama3_1.from_json

```{autodoc2-docstring} agents.models.Llama3_1.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.Llama3_1.has_attribute

```{autodoc2-docstring} agents.models.Llama3_1.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.Llama3_1.get_attribute_type

```{autodoc2-docstring} agents.models.Llama3_1.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.Llama3_1.update_value

```{autodoc2-docstring} agents.models.Llama3_1.update_value
```

````

`````

`````{py:class} OllamaModel
:canonical: agents.models.OllamaModel

Bases: {py:obj}`agents.models.LLM`

```{autodoc2-docstring} agents.models.OllamaModel
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.OllamaModel.asdict

```{autodoc2-docstring} agents.models.OllamaModel.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.OllamaModel.from_dict

```{autodoc2-docstring} agents.models.OllamaModel.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.OllamaModel.from_yaml

```{autodoc2-docstring} agents.models.OllamaModel.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.OllamaModel.to_json

```{autodoc2-docstring} agents.models.OllamaModel.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.OllamaModel.from_json

```{autodoc2-docstring} agents.models.OllamaModel.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.OllamaModel.has_attribute

```{autodoc2-docstring} agents.models.OllamaModel.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.OllamaModel.get_attribute_type

```{autodoc2-docstring} agents.models.OllamaModel.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.OllamaModel.update_value

```{autodoc2-docstring} agents.models.OllamaModel.update_value
```

````

`````

`````{py:class} Idefics
:canonical: agents.models.Idefics

Bases: {py:obj}`agents.models.LLM`

```{autodoc2-docstring} agents.models.Idefics
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.Idefics.asdict

```{autodoc2-docstring} agents.models.Idefics.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.Idefics.from_dict

```{autodoc2-docstring} agents.models.Idefics.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.Idefics.from_yaml

```{autodoc2-docstring} agents.models.Idefics.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.Idefics.to_json

```{autodoc2-docstring} agents.models.Idefics.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.Idefics.from_json

```{autodoc2-docstring} agents.models.Idefics.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.Idefics.has_attribute

```{autodoc2-docstring} agents.models.Idefics.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.Idefics.get_attribute_type

```{autodoc2-docstring} agents.models.Idefics.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.Idefics.update_value

```{autodoc2-docstring} agents.models.Idefics.update_value
```

````

`````

`````{py:class} Idefics2
:canonical: agents.models.Idefics2

Bases: {py:obj}`agents.models.LLM`

```{autodoc2-docstring} agents.models.Idefics2
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.Idefics2.asdict

```{autodoc2-docstring} agents.models.Idefics2.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.Idefics2.from_dict

```{autodoc2-docstring} agents.models.Idefics2.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.Idefics2.from_yaml

```{autodoc2-docstring} agents.models.Idefics2.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.Idefics2.to_json

```{autodoc2-docstring} agents.models.Idefics2.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.Idefics2.from_json

```{autodoc2-docstring} agents.models.Idefics2.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.Idefics2.has_attribute

```{autodoc2-docstring} agents.models.Idefics2.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.Idefics2.get_attribute_type

```{autodoc2-docstring} agents.models.Idefics2.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.Idefics2.update_value

```{autodoc2-docstring} agents.models.Idefics2.update_value
```

````

`````

`````{py:class} Llava
:canonical: agents.models.Llava

Bases: {py:obj}`agents.models.LLM`

```{autodoc2-docstring} agents.models.Llava
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.Llava.asdict

```{autodoc2-docstring} agents.models.Llava.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.Llava.from_dict

```{autodoc2-docstring} agents.models.Llava.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.Llava.from_yaml

```{autodoc2-docstring} agents.models.Llava.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.Llava.to_json

```{autodoc2-docstring} agents.models.Llava.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.Llava.from_json

```{autodoc2-docstring} agents.models.Llava.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.Llava.has_attribute

```{autodoc2-docstring} agents.models.Llava.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.Llava.get_attribute_type

```{autodoc2-docstring} agents.models.Llava.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.Llava.update_value

```{autodoc2-docstring} agents.models.Llava.update_value
```

````

`````

`````{py:class} Whisper
:canonical: agents.models.Whisper

Bases: {py:obj}`agents.models.Model`

```{autodoc2-docstring} agents.models.Whisper
```

````{py:method} get_init_params() -> dict
:canonical: agents.models.Whisper.get_init_params

```{autodoc2-docstring} agents.models.Whisper.get_init_params
```

````

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.Whisper.asdict

```{autodoc2-docstring} agents.models.Whisper.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.Whisper.from_dict

```{autodoc2-docstring} agents.models.Whisper.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.Whisper.from_yaml

```{autodoc2-docstring} agents.models.Whisper.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.Whisper.to_json

```{autodoc2-docstring} agents.models.Whisper.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.Whisper.from_json

```{autodoc2-docstring} agents.models.Whisper.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.Whisper.has_attribute

```{autodoc2-docstring} agents.models.Whisper.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.Whisper.get_attribute_type

```{autodoc2-docstring} agents.models.Whisper.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.Whisper.update_value

```{autodoc2-docstring} agents.models.Whisper.update_value
```

````

`````

`````{py:class} InstructBlip
:canonical: agents.models.InstructBlip

Bases: {py:obj}`agents.models.LLM`

```{autodoc2-docstring} agents.models.InstructBlip
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.InstructBlip.asdict

```{autodoc2-docstring} agents.models.InstructBlip.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.InstructBlip.from_dict

```{autodoc2-docstring} agents.models.InstructBlip.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.InstructBlip.from_yaml

```{autodoc2-docstring} agents.models.InstructBlip.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.InstructBlip.to_json

```{autodoc2-docstring} agents.models.InstructBlip.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.InstructBlip.from_json

```{autodoc2-docstring} agents.models.InstructBlip.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.InstructBlip.has_attribute

```{autodoc2-docstring} agents.models.InstructBlip.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.InstructBlip.get_attribute_type

```{autodoc2-docstring} agents.models.InstructBlip.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.InstructBlip.update_value

```{autodoc2-docstring} agents.models.InstructBlip.update_value
```

````

`````

`````{py:class} SpeechT5
:canonical: agents.models.SpeechT5

Bases: {py:obj}`agents.models.Model`

```{autodoc2-docstring} agents.models.SpeechT5
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.SpeechT5.asdict

```{autodoc2-docstring} agents.models.SpeechT5.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.SpeechT5.from_dict

```{autodoc2-docstring} agents.models.SpeechT5.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.SpeechT5.from_yaml

```{autodoc2-docstring} agents.models.SpeechT5.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.SpeechT5.to_json

```{autodoc2-docstring} agents.models.SpeechT5.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.SpeechT5.from_json

```{autodoc2-docstring} agents.models.SpeechT5.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.SpeechT5.has_attribute

```{autodoc2-docstring} agents.models.SpeechT5.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.SpeechT5.get_attribute_type

```{autodoc2-docstring} agents.models.SpeechT5.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.SpeechT5.update_value

```{autodoc2-docstring} agents.models.SpeechT5.update_value
```

````

`````

`````{py:class} Bark
:canonical: agents.models.Bark

Bases: {py:obj}`agents.models.Model`

```{autodoc2-docstring} agents.models.Bark
```

````{py:method} get_init_params() -> dict
:canonical: agents.models.Bark.get_init_params

```{autodoc2-docstring} agents.models.Bark.get_init_params
```

````

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.Bark.asdict

```{autodoc2-docstring} agents.models.Bark.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.Bark.from_dict

```{autodoc2-docstring} agents.models.Bark.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.Bark.from_yaml

```{autodoc2-docstring} agents.models.Bark.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.Bark.to_json

```{autodoc2-docstring} agents.models.Bark.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.Bark.from_json

```{autodoc2-docstring} agents.models.Bark.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.Bark.has_attribute

```{autodoc2-docstring} agents.models.Bark.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.Bark.get_attribute_type

```{autodoc2-docstring} agents.models.Bark.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.Bark.update_value

```{autodoc2-docstring} agents.models.Bark.update_value
```

````

`````

`````{py:class} VisionModel
:canonical: agents.models.VisionModel

Bases: {py:obj}`agents.models.Model`

```{autodoc2-docstring} agents.models.VisionModel
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.models.VisionModel.asdict

```{autodoc2-docstring} agents.models.VisionModel.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.models.VisionModel.from_dict

```{autodoc2-docstring} agents.models.VisionModel.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.models.VisionModel.from_yaml

```{autodoc2-docstring} agents.models.VisionModel.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.models.VisionModel.to_json

```{autodoc2-docstring} agents.models.VisionModel.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.models.VisionModel.from_json

```{autodoc2-docstring} agents.models.VisionModel.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.models.VisionModel.has_attribute

```{autodoc2-docstring} agents.models.VisionModel.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.models.VisionModel.get_attribute_type

```{autodoc2-docstring} agents.models.VisionModel.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.models.VisionModel.update_value

```{autodoc2-docstring} agents.models.VisionModel.update_value
```

````

`````
