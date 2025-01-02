---
orphan: true
---

# {py:mod}`agents.components.mllm`

```{py:module} agents.components.mllm
```

```{autodoc2-docstring} agents.components.mllm
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MLLM <agents.components.mllm.MLLM>`
  - ```{autodoc2-docstring} agents.components.mllm.MLLM
    :summary:
    ```
````

### API

`````{py:class} MLLM(*, inputs: typing.List[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], outputs: typing.List[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.MLLMConfig] = None, db_client: typing.Optional[agents.clients.db_base.DBClient] = None, trigger: typing.Union[agents.ros.Topic, typing.List[agents.ros.Topic], float] = 1.0, callback_group=None, component_name: str = 'mllm_component', **kwargs)
:canonical: agents.components.mllm.MLLM

Bases: {py:obj}`agents.components.llm.LLM`

```{autodoc2-docstring} agents.components.mllm.MLLM
```

````{py:method} add_documents(ids: typing.List[str], metadatas: typing.List[typing.Dict], documents: typing.List[str]) -> None
:canonical: agents.components.mllm.MLLM.add_documents

```{autodoc2-docstring} agents.components.mllm.MLLM.add_documents
```

````

````{py:method} set_topic_prompt(input_topic: agents.ros.Topic, template: typing.Union[str, pathlib.Path]) -> None
:canonical: agents.components.mllm.MLLM.set_topic_prompt

```{autodoc2-docstring} agents.components.mllm.MLLM.set_topic_prompt
```

````

````{py:method} set_component_prompt(template: typing.Union[str, pathlib.Path]) -> None
:canonical: agents.components.mllm.MLLM.set_component_prompt

```{autodoc2-docstring} agents.components.mllm.MLLM.set_component_prompt
```

````

````{py:method} register_tool(tool: typing.Callable, tool_description: typing.Dict, send_tool_response_to_model: bool = False) -> None
:canonical: agents.components.mllm.MLLM.register_tool

```{autodoc2-docstring} agents.components.mllm.MLLM.register_tool
```

````

`````
