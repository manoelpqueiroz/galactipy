# API Reference

This section provides detailed information
on all public {{ cookiecutter.project_name }}
objects, functions and methods.

Navigation follows a natural arrangement of available objects
to make searching and consulting easier for general users.
{%- if cookiecutter.app_type != 'bare_repo' %}

## Public Packages

The following packages are public:

{% if cookiecutter.app_type != 'bare_cli' -%}
- **`{{ cookiecutter.package_name }}.config`:**
  functions and classes
  to manage {{ cookiecutter.project_name }} configuration
  and operations related to configuration;
{% endif -%}
- **`{{ cookiecutter.package_name }}.logging`:**
  functions and classes
  to handle the custom logging interface
  used by {{ cookiecutter.project_name }}.

APIs not present in these packages
are not guaranteed to be stable.
{%- else %}

<!-- RECORD the packages exposed in the public API
## Public Packages

The following packages are public:

APIs not present in these packages
are not guaranteed to be stable.
-->
{%- endif %}
