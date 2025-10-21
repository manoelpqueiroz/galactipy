# Build stage
FROM python:{{ cookiecutter.minimal_python_version }}-alpine AS builder

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    POETRY_HOME="/opt/.poetry" \
    POETRY_VERSION=2.1.3 \
    POETRY_DYNAMIC_VERSIONING_COMMANDS="" \
    PATH="$PATH:/opt/.poetry/bin"

RUN apk add --no-cache --virtual .build-deps \
    curl=~8.14.1-r1 \
    gcc=~14.2.0-r6 \
    musl-dev=~1.2.5-r10 \
    python3-dev=~3.12.11-r0 \
    libffi-dev=~3.4.8-r0 \
# HACK sqlite-libs has a vulnerability up to 3.49.2-r0, which is installed by default
    sqlite-libs=~3.49.2-r1

# Install Poetry
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python -

# Install dependencies and project
WORKDIR /workspace
COPY pyproject.toml poetry.lock README.md ./
RUN poetry sync --without dev --no-root
COPY {{ cookiecutter.package_name }} ./{{ cookiecutter.package_name }}/
RUN poetry sync --only-root

# Create self-contained bundle
RUN poetry bundle venv /opt/{{ cookiecutter.repo_name }}-bundle --only main && \
    apk del .build-deps

# Production stage for minimal runtime
FROM python:{{ cookiecutter.minimal_python_version }}-alpine AS runtime

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
{%- if cookiecutter.app_type != 'bare_repo' %}
    PATH="/opt/{{ cookiecutter.repo_name }}-bundle/bin:$PATH" \
    TERM=xterm-256color \
{%- else %}
    PATH="/opt/{{ cookiecutter.repo_name }}-bundle/bin:$PATH"
{%- endif %}
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
    COLORTERM=truecolor \
    PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    ncurses-terminfo-base=~6.5_p20250503-r0 \
    ncurses-libs=~6.5_p20250503-r0 \
# HACK sqlite-libs has a vulnerability up to 3.49.2-r0, which is installed by default
    sqlite-libs=~3.49.2-r1
{%- elif cookiecutter.app_type == 'cli' %}
    COLORTERM=truecolor \
    PYTHONUNBUFFERED=1
{%- endif %}

# Copy the bundled application
COPY --from=builder /opt/{{ cookiecutter.repo_name }}-bundle /opt/{{ cookiecutter.repo_name }}-bundle

{% if cookiecutter.app_type == 'tui' -%}
CMD ["{{ cookiecutter.repo_name }}"]
{% elif cookiecutter.app_type == 'hybrid' -%}
CMD ["{{ cookiecutter.repo_name }}", "launch"]
{% elif cookiecutter.app_type == 'cli' -%}
ENTRYPOINT ["{{ cookiecutter.repo_name }}"]
{% else -%}
# UPDATEME with the definitive command once your app is functional
CMD ["/bin/sh", "-c", "echo '{{ cookiecutter.project_name }} does not have a Docker image implemented yet. No application is available to run.' && exit 1"]
{%- endif %}

HEALTHCHECK --interval=30s --timeout=3s \
    CMD ["/bin/sh", "-c", "pidof {{ cookiecutter.repo_name }} > /dev/null || exit 1"]
