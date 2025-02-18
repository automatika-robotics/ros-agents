---
orphan: true
---

# {py:mod}`agents.components.semantic_router`

```{py:module} agents.components.semantic_router
```

```{autodoc2-docstring} agents.components.semantic_router
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SemanticRouter <agents.components.semantic_router.SemanticRouter>`
  - ```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter
    :summary:
    ```
````

### API

````{py:class} SemanticRouter(*, inputs: typing.List[agents.ros.Topic], routes: typing.List[agents.ros.Route], config: agents.config.SemanticRouterConfig, db_client: agents.clients.db_base.DBClient, default_route: typing.Optional[agents.ros.Route] = None, component_name: str, callback_group=None, **kwargs)
:canonical: agents.components.semantic_router.SemanticRouter

Bases: {py:obj}`agents.components.component_base.Component`

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter
```

````
