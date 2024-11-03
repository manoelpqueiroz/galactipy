# Docker for {{ cookiecutter.project_name }}

## Installation

To create a Docker image you can run:

```bash
invoke docker-build
```

This will create a default image `{{ cookiecutter.package_name }}:latest`.

You may provide name and version for the image, as well as multiple tags:

```bash
invoke docker-build -i {{ cookiecutter.package_name }}:{{ cookiecutter.version }}
invoke docker-build -i {{ cookiecutter.package_name }}:latest -i {{ cookiecutter.package_name }}:{{ cookiecutter.version }}
```

## Usage

```bash
docker run -it --rm \
   -v $(pwd):/workspace \
   {{ cookiecutter.package_name }} bash
```

## How to clean up

To uninstall the default Docker image run:

```bash
invoke docker-remove
```

Again, you may also remove multiple images:

```bash
invoke docker-remove -i {{ cookiecutter.package_name }}:latest -i {{ cookiecutter.package_name }}:{{ cookiecutter.version }}
```

If you want to clean all, including `build` and `pycache` run `invoke cleanup`.
