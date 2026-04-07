# Installation

{{ cookiecutter.copyright }} officially distributes {{ cookiecutter.project_name }}
via the following methods:

- Packaged wheels
  via [PyPI][1],
  for use with pipx
  (or pip);
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
- Packaged wheels
  via the [GitLab Package Registry][1a]
  for use with pipx/pip
  (including development builds);
{%- endif %}
- Codebase hosted at [{{ cookiecutter.__scm_platform_base }}][2]
{%- if cookiecutter.create_docker %}
  for installation from source;
- Docker images
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  via the [GitLab Container Registry][2a]
{%- else %}
  via [Docker Hub][2a]
{%- endif %}
  for use as a container.
{%- else %}
  for installation from source.
{%- endif %}

!!! warning

    {{ cookiecutter.project_name }} may be installable
    from other sources
    besides the ones listed above,
    but please be advised
    that they are **not** managed by {{ cookiecutter.copyright }}.

    Verify the integrity
    of those sources
    before opting to install from them.

## Python version support

{{ cookiecutter.project_name }} supports all active Python versions
starting from **`{{ cookiecutter.minimal_python_version }}`**.
<!-- RECORD how will the process of adding support for new versions be handled -->
Support for the `{{ cookiecutter.minimal_python_version }}`
will be dropped
once it reaches [end-of-life][3].

## Installing {{ cookiecutter.project_name }}

### Installing with pipx or pip

Users can install {{ cookiecutter.project_name }}
with [pipx][4]:

```sh
pipx install {{ cookiecutter.repo_name }}
```

pipx is preferred over pip
as it automatically handles environment isolation
to enable command-line usage
for the end-user
with minimal input.

If you are installing {{ cookiecutter.project_name }}
using pip instead,
make sure to do so
and run the application
from a virtual environment,
using tools like
[pipenv][5],
[Poetry][6],
[PDM][7]
or [uv][8].

<!-- RECORD this section if your package has optional dependencies
{{ cookiecutter.project_name }} can also be installed
with sets of optional dependencies
to enable specific functionality.

For example,
to install with the dependencies
that enable <!-- RECORD an optional functionality of your library

```sh
pipx install "{{ cookiecutter.repo_name }}[<extra_group>]"
```

The full list of extras
that can be installed
are listed in the [Dependencies][opt-deps] section.
-->

{% if cookiecutter.create_docker -%}
### Installing using Docker

You can run {{ cookiecutter.project_name }}
inside a Docker container.
If you have Docker installed,
run:

```sh
docker run -it --rm {{ cookiecutter.__docker_registry }}:latest
```

{% endif -%}
### Installing from source

For complete instructions
to build the project
from the Git source,
check the [Development Setup guide][dev-setup],
which outlines prerequisites
and tools needed
to create a development environment.

### Installing development versions

Installing the development version
is a good way to:

- Try a new feature
  before it is officially released;
- Check whether
  a bug you encountered
  has been fixed
  since the last official release.

The development version is available
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
from the [GitLab Package Registry][1a]
and can be installed with:

```sh
pipx install --pre --index-url https://gitlab.com/api/v4/projects/{{ cookiecutter.repo_name }}/packages/pypi/simple {{ cookiecutter.repo_name }}
```

{% if cookiecutter.create_docker -%}
You can also use the nightly Docker image
to run a development version of {{ cookiecutter.project_name }}:

```sh
docker run -it --rm {{ cookiecutter.__docker_registry }}:latest-nightly
```

{% endif -%}
{% else -%}
on the [TestPyPI repository][8a]
and can be installed with:

```sh
pipx install --pre --index-url https://test.pypi.org/simple {{ cookiecutter.repo_name }}
```

{% endif -%}
## Dependencies

### Required dependencies

{{ cookiecutter.project_name }} requires
the following dependencies
to run effectively:

| Package            | Minimum supported version |
| ------------------ | ------------------------- |
| [`Textual`][9]    | 6.5.0                     |
| [`Typer`][10]      | 0.20.0                    |
| [`Rich`][11]       | 14.2.0                    |
| [`Orbittings`][12] | 0.2.0                     |
| [`Nebulog`][13]    | 0.1.0                     |

<!-- RECORD this section if your package has optional dependencies
### Optional dependencies

{{ cookiecutter.project_name }} has some optional dependencies
which are used for specific methods and features.
For instance,
<!-- RECORD an example of a method/function which require an optional dependency and why
If the optional dependency is not installed,
{{ cookiecutter.project_name }} will raise an `ImportError`
when the method or feature requiring that dependency
is called.

#### <extra group category>

Installable with `pipx install "{{ cookiecutter.repo_name }}[<extra_group>]"`:

| Dependency | Minimum version | Extra group | Purpose |
|------------|-----------------|-------------|---------|
-->

<!-- Anchors -->

[opt-deps]: #optional-dependencies
[dev-setup]: ../development/development_setup.md

[1]: https://pypi.org/project/{{ cookiecutter.repo_name }}/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[1a]: {{ cookiecutter.__scm_link_url }}/packages?type=PyPI
{%- endif %}
[2]: {{ cookiecutter.__scm_base_url }}
{%- if cookiecutter.create_docker %}
[2a]: {{ cookiecutter.__docker_repo }}
{%- endif %}
[3]: https://devguide.python.org/versions/
[4]: https://pipx.pypa.io/
[5]: https://pipenv.pypa.io
[6]: https://python-poetry.org/
[7]: https://pdm-project.org/en/latest/
[8]: https://docs.astral.sh/uv/
{%- if cookiecutter.__scm_platform_lc == 'github' %}
[8a]: https://test.pypi.org/
{%- endif %}
[9]: https://textual.textualize.io/
[10]: https://typer.tiangolo.com/
[11]: https://rich.readthedocs.io/en/stable/introduction.html
[12]: https://gitlab.com/galactipy/libraries/orbittings
[13]: https://gitlab.com/galactipy/libraries/nebulog
