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

````{py:class} TextToSpeech(*, inputs: list[agents.ros.Topic], outputs: typing.Optional[list[agents.ros.Topic]] = None, model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.TextToSpeechConfig] = None, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float], callback_group=None, component_name: str = 'texttospeech_component', **kwargs)
:canonical: agents.components.texttospeech.TextToSpeech

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.texttospeech.TextToSpeech
```

````
