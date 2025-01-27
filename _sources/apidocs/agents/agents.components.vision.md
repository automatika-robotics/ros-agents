---
orphan: true
---

# {py:mod}`agents.components.vision`

```{py:module} agents.components.vision
```

```{autodoc2-docstring} agents.components.vision
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Vision <agents.components.vision.Vision>`
  - ```{autodoc2-docstring} agents.components.vision.Vision
    :summary:
    ```
````

### API

````{py:class} Vision(*, inputs: typing.List[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], outputs: typing.List[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.VisionConfig] = None, trigger: typing.Union[agents.ros.Topic, typing.List[agents.ros.Topic], float] = 1.0, component_name: str, callback_group=None, **kwargs)
:canonical: agents.components.vision.Vision

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.vision.Vision
```

````
