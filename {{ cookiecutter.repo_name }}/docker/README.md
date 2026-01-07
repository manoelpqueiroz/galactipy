{%- set docker_repo = 'registry.gitlab.com/' ~ cookiecutter.scm_namespace ~ '/' ~ cookiecutter.repo_name if cookiecutter.__scm_platform_lc == 'gitlab' else cookiecutter.scm_namespace ~ '/' ~ cookiecutter.repo_name -%}
# Docker for {{ cookiecutter.project_name }}

## Published Images

{{ cookiecutter.project_name }} provides official Docker images
to run the application on a container.
Published images are available
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
via [GitLab Container Registries][1].
{%- else %}
via [Docker Hub][1].
{%- endif %}
You can search
through the available tags
[here][2].

### Usage

To run {{ cookiecutter.project_name }} inside a Docker container,
use the following command:

```bash
docker run -it --rm {{ docker_repo }}:latest
```

## Local Building

Developers can build and test
their work in progress
with local images
using Invoke commands.

### Installation

To create a Docker image
you can run:

```bash
invoke container
```

This will create a default image `{{ cookiecutter.repo_name }}:wip-local`.

You may provide
multiple tags for the image,
and you can also override
the default `{{ docker_repo }}` repository:

```bash
invoke container -t sometag
invoke container -t latest -t sometag -r someuser/somerepo
```

## How to clean up

To uninstall the default Docker image
run:

```bash
invoke prune
```

Again,
you may also remove multiple tags:

```bash
invoke prune -t latest -t sometag
```

<!-- Anchors -->
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[1]: https://docs.gitlab.com/user/packages/container_registry/
[2]: {{ cookiecutter.__scm_base_url }}/container_registry
{%- else %}

[1]: https://hub.docker.com/
[2]: https://hub.docker.com/r/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
{%- endif %}
