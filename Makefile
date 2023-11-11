#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://install.python-poetry.org | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://install.python-poetry.org | $(PYTHON) - --uninstall

.PHONY: poetry-plugins
poetry-plugins:
	poetry self add poetry-plugin-up


#* Installation
.PHONY: install
install:
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n
	-poetry run mypy --install-types --non-interactive hooks tests

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install


#* Formatters
.PHONY: codestyle
codestyle:
	poetry run pyupgrade --exit-zero-even-if-changed --py38-plus **/*.py
	poetry run isort --settings-path pyproject.toml hooks tests
	poetry run black --config pyproject.toml hooks tests

.PHONY: formatting
formatting: codestyle


#* Linting
.PHONY: test
test:
	PYTHONPATH=$(PYTHONPATH) poetry run pytest -c pyproject.toml --cov=hooks tests/

.PHONY: check-codestyle
check-codestyle:
	poetry run isort --diff --check-only --settings-path pyproject.toml hooks tests
	poetry run black --diff --check --config pyproject.toml hooks tests

.PHONE: check-formatting
check-formatting: check-codestyle

.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml hooks tests

.PHONY: check-safety
check-safety:
	poetry check
	poetry run safety check --full-report
	poetry run bandit -ll --recursive hooks

.PHONE: lint
lint:
	poetry run flake8 --count --config=.flake8 hooks tests
	poetry run pydocstyle --count --config=pyproject.toml hooks tests
	poetry run pydoclint --config=pyproject.toml hooks tests

.PHONY: lint-all
lint: test check-codestyle lint mypy check-safety

.PHONY: update-dev-deps
update-dev-deps:
	poetry up --only=dev-dependencies --latest

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: ipynbcheckpoints-remove
ipynbcheckpoints-remove:
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove
