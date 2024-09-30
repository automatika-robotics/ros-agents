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

````{py:class} Vision(*, inputs: list[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], outputs: list[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.VisionConfig] = None, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float] = 1, callback_group=None, component_name: str = 'vision_component', **kwargs)
:canonical: agents.components.vision.Vision

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.vision.Vision
```

````
