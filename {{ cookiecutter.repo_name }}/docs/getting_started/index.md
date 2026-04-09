# Getting Started

{% if cookiecutter.__app_group == 'tui' -%}
{{ cookiecutter.project_name }} is a terminal application
{% elif cookiecutter.__app_group == 'cli' -%}
{{ cookiecutter.project_name }} is a command-line application
{% else -%}
{{ cookiecutter.project_name }} is a Python library
{% endif -%}
aimed at <!-- RECORD the purpose of your project and what it provides to users out of the box -->.

## Installation

<div class="grid cards" markdown>

{% if cookiecutter.app_type != 'bare_repo' -%}
-   :simple-pipx:{ .lg .middle } **Do you have pipx?**

    {{ cookiecutter.project_name }} can be installed
    in an isolated environment
    via [`pipx`][1].

    ---

    ```sh
    pipx install {{ cookiecutter.repo_name }}
    ```

-   :simple-python:{ .lg .middle } **Prefer pip?**

    {{ cookiecutter.project_name }} can also be installed
    directly via `pip`
    from [PyPI][2].

    ---

    ```sh
    pip install {{ cookiecutter.repo_name }}
    ```

</div>

<div class="grid cards" markdown>

{% else -%}
-   :simple-pypi:{ .lg .middle } **Install it with pip**

    {{ cookiecutter.project_name }} can be installed
    directly via `pip`
    from [PyPI][2].

    ---

    ```sh
    pip install {{ cookiecutter.repo_name }}
    ```

{% endif -%}
-   :fontawesome-solid-bore-hole:{ .lg .middle } **In-depth instructions**

    Installing through another method
    or a specific version?
    Check the dedicated Installation page.

    ---

    [Installation page][3]{ .md-button .md-button--primary }

</div>

## Intro to {{ cookiecutter.project_name }}

<!-- RECORD one admonition for every page in `docs/getting_started/intro_tutorials`
??? example "Question that the tutorial answers&emsp;[Straight to tutorial :fontawesome-solid-arrow-right-to-bracket:][<anchor>]{ .md-button }"

    Short text mentioning what your application is able to do, preferably with an accompanying image for greater clarity.
-->

## Coming from...

<!-- RECORD buttons linking to pages in `docs/getting_started/comparison`
<div class="grid cards" markdown>

-   :star-struck:{ .lg .middle }

    Short text mentioning concepts and keywords from one alternative software that have correspondence with your application

    ---

    [Learn More][<anchor>]{ .md-button .md-button--primary }

</div>
-->

## More References

To get familiar with the basic functionality of {{ cookiecutter.project_name }},
take a look at our assisted guide
[_10 Minutes to {{ cookiecutter.project_name }}_][4].

The community also helps
with a wide variety of tutorials online.
We provide a curated list
with some of this material
in [_Community Tutorials_][5].

[1]: https://pipx.pypa.io/latest/
[2]: https://pypi.org/project/{{ cookiecutter.repo_name }}/
[3]: ./install.md
[4]: ../user_guide/10min.md
[5]: ./tutorials.md
