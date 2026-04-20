{% raw -%}
---
tags:
  - Section Intros
  - User Guides
  - Configuration
---

{% endraw -%}
# {{ cookiecutter.project_name }} Configuration

{{ cookiecutter.project_name }} uses [Orbittings][1]
as the tool for managing its configuration files.
The configuration file location is placed in
`$XDG_CONFIG_HOME/.config/{{ cookiecutter.repo_name }}`
and is separated between a `settings.toml`
and `secrets.toml` files.

[1]: https://gitlab.com/galactipy/libraries/orbittings
