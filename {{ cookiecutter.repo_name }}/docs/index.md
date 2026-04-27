# {{ cookiecutter.project_name }} Documentation

{{ cookiecutter.project_description }}.

<!-- RECORD what your software aims to do in one sentence -->

{{ cookiecutter.project_name }} in three points:

<!-- RECORD what your software does in three sentences
1.
2.
3.
-->

{% if cookiecutter.version_schema != 'trunkver' -%}
<!-- RECORD the first release version and date -->
{% endif -%}
!!! info
{%- if cookiecutter.__schema_group == 'semver-like' %}

    Current Version: **`0.1.0`**
{%- elif cookiecutter.version_schema == 'calver-auto' %}

    Current Version: **`1{% now 'local', '%Y.%U' %}`**
{%- elif cookiecutter.version_schema == 'calver-explicit' %}

    Current Version: **`1{% now 'local', '%Y.%m' %}`**
{%- elif cookiecutter.version_schema == 'solover' %}

    Current Version: **`1`**
{%- endif %}
{%- if cookiecutter.version_schema == 'trunkver' %}

    {{ cookiecutter.project_name }} follows the [TrunkVer][0a] versioning schema.
    You can check the latest available version
    directly on [PyPI][0b].
    Refer to the [Release Notes][0c]
    to see the changes
    between each version.
{%- else %}
    <br>
    Released on **{% now 'local', '%B %d, %Y' %}**
{%- endif %}

<div class="grid" markdown>

:material-weather-moonset:{ .lg .middle } **Just getting started?**
<br><br>
If you are new to {{ cookiecutter.project_name }},
check out the absolute Beginner's Guide.
It contains an introduction
to {{ cookiecutter.project_name }}'s main concepts
and links to additional tutorials.
{ .card }

:material-diving-scuba:{ .lg .middle } **In-depth User Guide**
<br><br>
The User Guide provides detailed information
on the key concepts of {{ cookiecutter.project_name }} with
useful background information,
clear-cut explanations
and helpful visual guides.
{ .card }

[:fontawesome-solid-circle-chevron-right:&emsp;Go to this Section][1]{ .md-button .md-button--primary }

[:fontawesome-solid-circle-chevron-right:&emsp;Go to this Section][2]{ .md-button .md-button--primary }

</div>
<div class="grid" markdown>

:material-code-block-braces:{ .lg .middle } **API Reference**
<br><br>
The Reference Guide compiles
all modules, classes and functions
provided by {{ cookiecutter.project_name }}.
<br><br>
The reference describes
how methods work
and which parameters can be used.
It assumes you have sufficient understanding
of the key concepts.
{ .card }

:material-developer-board:{ .lg .middle } **All things development**
<br><br>
Curious about where we're heading?
Want to contribute to the source code?
Why not help with documentation
or ideas for {{ cookiecutter.project_name }}?
<br><br>
The Development Guide will navigate you
through the process of improving {{ cookiecutter.project_name }}.
{ .card }

[:fontawesome-solid-circle-chevron-right:&emsp;Go to this Section][3]{ .md-button .md-button--primary }

[:fontawesome-solid-circle-chevron-right:&emsp;Go to this Section][4]{ .md-button .md-button--primary }

</div>

<!-- Anchors -->

{% if cookiecutter.version_schema == 'trunkver' -%}
[0a]: https://trunkver.org/
[0b]: {{ cookiecutter.__pypi_url }}/#history
[0c]: ./noticeboard/release_notes/index.md
{% endif -%}
[1]: ./getting_started/index.md
[2]: ./user_guide/index.md
[3]: ./reference/index.md
[4]: ./development/index.md
