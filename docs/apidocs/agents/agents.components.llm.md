---
orphan: true
---

# {py:mod}`agents.components.llm`

```{py:module} agents.components.llm
```

```{autodoc2-docstring} agents.components.llm
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LLM <agents.components.llm.LLM>`
  - ```{autodoc2-docstring} agents.components.llm.LLM
    :summary:
    ```
````

### API

`````{py:class} LLM(*, inputs: list[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], outputs: list[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.LLMConfig] = None, db_client: typing.Optional[agents.clients.db_base.DBClient] = None, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float] = 1, callback_group=None, component_name: str = 'llm_component', **kwargs)
:canonical: agents.components.llm.LLM

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.llm.LLM
```

````{py:method} add_documents(ids: list[str], metadatas: list[dict], documents: list[str]) -> None
:canonical: agents.components.llm.LLM.add_documents

```{autodoc2-docstring} agents.components.llm.LLM.add_documents
```

````

````{py:method} set_topic_prompt(input_topic: agents.ros.Topic, template: typing.Union[str, pathlib.Path]) -> None
:canonical: agents.components.llm.LLM.set_topic_prompt

```{autodoc2-docstring} agents.components.llm.LLM.set_topic_prompt
```

````

````{py:method} set_component_prompt(template: typing.Union[str, pathlib.Path]) -> None
:canonical: agents.components.llm.LLM.set_component_prompt

```{autodoc2-docstring} agents.components.llm.LLM.set_component_prompt
```

````

`````
