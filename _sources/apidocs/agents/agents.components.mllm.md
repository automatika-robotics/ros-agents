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

````{py:class} MLLM(*, inputs: typing.List[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], outputs: typing.List[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.MLLMConfig] = None, db_client: typing.Optional[agents.clients.db_base.DBClient] = None, trigger: typing.Union[agents.ros.Topic, typing.List[agents.ros.Topic], float] = 1.0, component_name: str, callback_group=None, **kwargs)
:canonical: agents.components.mllm.MLLM

Bases: {py:obj}`agents.components.llm.LLM`

```{autodoc2-docstring} agents.components.mllm.MLLM
```

````
