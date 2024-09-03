# Configuration file for the Sphinx documentation builder.
import os
import sys
import subprocess
from datetime import date

sys.path.insert(0, os.path.abspath(".."))
version = (
    subprocess.run(
        ["ros2", "pkg", "xml", "agents", "--tag", "version"], stdout=subprocess.PIPE
    )
    .stdout.decode("utf-8")
    .strip()
)

project = "ROS Agents"
copyright = f"{date.today().year}, Automatika Robotics"
author = "Automatika Robotics"
release = version

extensions = [
    "sphinx.ext.viewcode",
    "sphinx.ext.doctest",
    "sphinx_copybutton",  # install with `pip install sphinx-copybutton`
    "autodoc2",  # install with `pip install sphinx-autodoc2`
    "myst_parser",  # install with `pip install myst-parser`
]

autodoc2_packages = [
    {
        "module": "agents",
        "path": "../agents/agents",
        "exclude_dirs": ["__pycache__", "utils"],
        "exclude_files": [
            "callbacks.py",
            "publisher.py",
            "component_base.py",
            "model_component.py",
            "model_base.py",
            "db_base.py",
        ],
    },
]

autodoc2_docstrings = "all"
autodoc2_class_docstring = "both"  # bug in autodoc2, should be `merge`
autodoc2_render_plugin = "myst"
autodoc2_hidden_objects = ["private", "dunder", "undoc"]
autodoc2_module_all_regexes = [
    r"agents.models",
    r"agents.vectordbs",
    r"agents.ros",
    r"agents.clients\.[^\.]+",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


html_theme = "sphinx_book_theme"  # install with `pip install sphinx-book-theme`
html_static_path = ["_static"]
html_theme_options = {
    "logo": {
        "image_light": "_static/ROS_AGENTS_DARK.png",
        "image_dark": "_static/ROS_AGENTS.png",
    }
}