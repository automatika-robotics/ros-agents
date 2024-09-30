---
orphan: true
---

# {py:mod}`agents.components.speechtotext`

```{py:module} agents.components.speechtotext
```

```{autodoc2-docstring} agents.components.speechtotext
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SpeechToText <agents.components.speechtotext.SpeechToText>`
  - ```{autodoc2-docstring} agents.components.speechtotext.SpeechToText
    :summary:
    ```
````

### API

````{py:class} SpeechToText(*, inputs: list[agents.ros.Topic], outputs: list[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.SpeechToTextConfig] = None, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float], callback_group=None, component_name: str = 'speechtotext_component', **kwargs)
:canonical: agents.components.speechtotext.SpeechToText

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.speechtotext.SpeechToText
```

````
