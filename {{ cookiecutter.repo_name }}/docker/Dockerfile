FROM python:{{ cookiecutter.minimal_python_version }}-slim-bookworm

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH="${PATH}:/root/.poetry/bin"

WORKDIR /workspace

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . /workspace/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | \
    POETRY_HOME=/opt/poetry python - --version 1.8.5 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --without dev ; fi"

CMD ["/usr/bin/bash"]
