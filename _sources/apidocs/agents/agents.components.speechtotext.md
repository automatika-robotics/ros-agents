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

`````{py:class} SpeechToText(*, inputs: typing.List[agents.ros.Topic], outputs: typing.List[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.SpeechToTextConfig] = None, trigger: typing.Union[agents.ros.Topic, typing.List[agents.ros.Topic]], component_name: str, callback_group=None, **kwargs)
:canonical: agents.components.speechtotext.SpeechToText

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.speechtotext.SpeechToText
```

````{py:method} custom_on_activate()
:canonical: agents.components.speechtotext.SpeechToText.custom_on_activate

```{autodoc2-docstring} agents.components.speechtotext.SpeechToText.custom_on_activate
```

````

`````
