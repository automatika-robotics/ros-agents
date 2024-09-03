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

````{py:class} MLLM(*, inputs: list[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], outputs: list[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.MLLMConfig] = None, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float] = 1, callback_group=None, component_name: str = 'mllm_component', **kwargs)
:canonical: agents.components.mllm.MLLM

Bases: {py:obj}`agents.components.llm.LLM`

```{autodoc2-docstring} agents.components.mllm.MLLM
```

````
