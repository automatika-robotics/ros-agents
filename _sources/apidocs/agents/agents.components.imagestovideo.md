---
orphan: true
---

# {py:mod}`agents.components.imagestovideo`

```{py:module} agents.components.imagestovideo
```

```{autodoc2-docstring} agents.components.imagestovideo
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`VideoMessageMaker <agents.components.imagestovideo.VideoMessageMaker>`
  - ```{autodoc2-docstring} agents.components.imagestovideo.VideoMessageMaker
    :summary:
    ```
````

### API

````{py:class} VideoMessageMaker(*, inputs: list[agents.ros.Topic], outputs: list[agents.ros.Topic], config: typing.Optional[agents.config.VideoMessageMakerConfig] = None, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic]], callback_group=None, component_name: str = 'video_maker_component', **kwargs)
:canonical: agents.components.imagestovideo.VideoMessageMaker

Bases: {py:obj}`agents.components.component_base.Component`

```{autodoc2-docstring} agents.components.imagestovideo.VideoMessageMaker
```

````
