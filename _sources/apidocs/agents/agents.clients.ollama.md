---
orphan: true
---

# {py:mod}`agents.clients.ollama`

```{py:module} agents.clients.ollama
```

```{autodoc2-docstring} agents.clients.ollama
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`OllamaClient <agents.clients.ollama.OllamaClient>`
  - ```{autodoc2-docstring} agents.clients.ollama.OllamaClient
    :summary:
    ```
````

### API

````{py:class} OllamaClient(model: typing.Union[agents.models.LLM, typing.Dict], host: str = '127.0.0.1', port: int = 11434, inference_timeout: int = 30, init_on_activation: bool = True, logging_level: str = 'info', **kwargs)
:canonical: agents.clients.ollama.OllamaClient

Bases: {py:obj}`agents.clients.model_base.ModelClient`

```{autodoc2-docstring} agents.clients.ollama.OllamaClient
```

````
