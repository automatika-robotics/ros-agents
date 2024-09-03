# {py:mod}`agents.vectordbs`

```{py:module} agents.vectordbs
```

```{autodoc2-docstring} agents.vectordbs
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ChromaDB <agents.vectordbs.ChromaDB>`
  - ```{autodoc2-docstring} agents.vectordbs.ChromaDB
    :summary:
    ```
````

### API

`````{py:class} ChromaDB
:canonical: agents.vectordbs.ChromaDB

Bases: {py:obj}`agents.vectordbs.DB`

```{autodoc2-docstring} agents.vectordbs.ChromaDB
```

````{py:method} asdict(filter: typing.Optional[typing.Callable] = None) -> dict
:canonical: agents.vectordbs.ChromaDB.asdict

```{autodoc2-docstring} agents.vectordbs.ChromaDB.asdict
```

````

````{py:method} from_dict(dict_obj: typing.Dict) -> None
:canonical: agents.vectordbs.ChromaDB.from_dict

```{autodoc2-docstring} agents.vectordbs.ChromaDB.from_dict
```

````

````{py:method} from_yaml(file_path: str, nested_root_name: str | None = None, get_common: bool = False) -> None
:canonical: agents.vectordbs.ChromaDB.from_yaml

```{autodoc2-docstring} agents.vectordbs.ChromaDB.from_yaml
```

````

````{py:method} to_json() -> typing.Union[str, bytes, bytearray]
:canonical: agents.vectordbs.ChromaDB.to_json

```{autodoc2-docstring} agents.vectordbs.ChromaDB.to_json
```

````

````{py:method} from_json(json_obj: typing.Union[str, bytes, bytearray]) -> None
:canonical: agents.vectordbs.ChromaDB.from_json

```{autodoc2-docstring} agents.vectordbs.ChromaDB.from_json
```

````

````{py:method} has_attribute(attr_name: str) -> bool
:canonical: agents.vectordbs.ChromaDB.has_attribute

```{autodoc2-docstring} agents.vectordbs.ChromaDB.has_attribute
```

````

````{py:method} get_attribute_type(attr_name: str) -> typing.Optional[type]
:canonical: agents.vectordbs.ChromaDB.get_attribute_type

```{autodoc2-docstring} agents.vectordbs.ChromaDB.get_attribute_type
```

````

````{py:method} update_value(attr_name: str, attr_value: typing.Any) -> bool
:canonical: agents.vectordbs.ChromaDB.update_value

```{autodoc2-docstring} agents.vectordbs.ChromaDB.update_value
```

````

`````
