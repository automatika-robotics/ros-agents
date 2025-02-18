---
orphan: true
---

# {py:mod}`agents.components.texttospeech`

```{py:module} agents.components.texttospeech
```

```{autodoc2-docstring} agents.components.texttospeech
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TextToSpeech <agents.components.texttospeech.TextToSpeech>`
  - ```{autodoc2-docstring} agents.components.texttospeech.TextToSpeech
    :summary:
    ```
````

### API

````{py:class} TextToSpeech(*, inputs: typing.List[agents.ros.Topic], outputs: typing.Optional[typing.List[agents.ros.Topic]] = None, model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.TextToSpeechConfig] = None, trigger: typing.Union[agents.ros.Topic, typing.List[agents.ros.Topic]], component_name: str, callback_group=None, **kwargs)
:canonical: agents.components.texttospeech.TextToSpeech

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.texttospeech.TextToSpeech
```

````
