{%- set index_title = cookiecutter.project_name ~ ' Documentation' -%}
{{ '=' * (index_title | length) }}
{{ index_title }}
{{ '=' * (index_title | length) }}

{{ cookiecutter.project_description.replace('`', '``') }}
