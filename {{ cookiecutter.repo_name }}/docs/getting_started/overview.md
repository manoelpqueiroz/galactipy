{% raw -%}
---
tags:
  - For Your Information
---

{% endraw -%}
# Package Overview

<!-- RECORD a paragraph detailing what your application provides and what it aims to be -->

<!-- RECORD the benefits of using this application
{{ cookiecutter.project_name }} is well suited for:

- ...
- ...
- ...
-->

<!-- RECORD what specific features your application excel at
Here are just a few things
that {{ cookiecutter.project_name }} does well:

- ...
- ...
- ...

These features were adopted
as fundamental principles
for {{ cookiecutter.project_name }}
to address...

<!-- RECORD additional points outside of technical implementation to pitch your application to users
!!! note

    - ...
    - ...
    - ...
-->

<!-- RECORD the one most fundamental technical aspect users must understand to be able to use {{ cookiecutter.project_name }}

## <name of the core aspect>

<!-- RECORD a layman explanation of the core aspect, making parallels with real-world concepts or comparing with tools used everyday
-->

<!-- RECORD the one most fundamental design choice users must be aware when using {{ cookiecutter.project_name }}

## <name of the core principle>

<!-- RECORD an brief explanation as to why this design principle was chosen during development (in favour or alternative options)
-->

## Getting Support

If you are unable
to resolve your question
by searching through this documentation,
we advise you to open a [Request for Support][1]
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
at our [Issue Tracker][2].
{%- else %}
in our [Discussions page][2].
{%- endif %}
The team will do their best
to address your questions.

## Licence
{%- if cookiecutter.licence != 'nos' %}

[![Licence][3]][4]

{{ cookiecutter.project_name }} is licenced
under the terms of the **{{ cookiecutter.__licence_extended }}**.
See [LICENCE][4] for more details.
{%- else %}

{{ cookiecutter.project_name }} is _**not**_ open source software.
Please contact the maintainers
for more information
on licencing the project.
{%- endif %}

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Support
[2]: {{ cookiecutter.__scm_link_url }}/issues
{%- else %}

[1]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-support
[2]: {{ cookiecutter.__scm_link_url }}/discussions
{%- endif %}
{%- if cookiecutter.licence != 'nos' %}
[3]: https://img.shields.io/{{ cookiecutter.__scm_platform_lc }}/license/{{ cookiecutter.scm_namespace}}/{{ cookiecutter.repo_name }}?style=for-the-badge
[4]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE
{%- endif %}
