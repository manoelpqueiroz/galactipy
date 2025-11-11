{%- set docker_repo = 'registry.gitlab.com/' ~ cookiecutter.scm_namespace ~ '/' ~ cookiecutter.repo_name if cookiecutter.__scm_platform_lc == 'gitlab' else cookiecutter.scm_namespace ~ '/' ~ cookiecutter.repo_name -%}
# Docker for {{ cookiecutter.project_name }}

## Installation

To create a Docker image
you can run:

```bash
invoke container
```

This will create a default image `{{ cookiecutter.repo_name }}:latest`.

You may provide
multiple tags for the image,
and you can also override
the default `{{ docker_repo }}` repository:

```bash
invoke container -t sometag
invoke container -t latest -t sometag -r someuser/somerepo
```

## Usage

```bash
docker run -it --rm {{ docker_repo }}:latest
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
