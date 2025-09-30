============
Installation
============

It's so easy to install {{ cookiecutter.project_name }}! You can get it via ``pip``:

.. code-block:: shell

    pip install {{ cookiecutter.repo_name }}

Python Version Support
======================

{%- set list_python_version = cookiecutter.minimal_python_version.split('.') | map('int') | list %}
Officially {{ cookiecutter.project_name }} supports Python {{
    (
        cookiecutter._all_python_version
        | selectattr(0, '==', list_python_version.0)
        | selectattr(1, '>=', list_python_version.1) | list
        + cookiecutter._all_python_version | selectattr(0, '>', list_python_version.0) | list
    ) | map('join', '.') | join(', ')
}}.

Installing from PyPI
====================

{{ cookiecutter.project_name }} can be installed via pip from
`PyPI <https://pypi.org/project/{{ cookiecutter.repo_name }}>`_.

.. code-block:: shell

    pip install {{ cookiecutter.repo_name }}

.. note::

    It is recommended to install and run {{ cookiecutter.project_name }} from a virtual
    environment. You can use the Python Standard Library's `venv
    <https://docs.python.org/3/library/venv.html>`_.

    For better management with other projects, we recommend tools such as
    `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/stable/>`_ and
    `pipenv <https://pipenv.pypa.io/en/latest/index.html>`_.

Installing from Source
======================

See the :ref:`contributing guide <contributing>` for complete instructions on building
from the git source tree. Further, see :ref:`creating a development environment
<contributing_environment>` if you wish to create a {{ cookiecutter.project_name }}
development environment.

Dependencies
============

Required Dependencies
=====================

{%- if cookiecutter.app_type != 'bare_repo' %}
{{ cookiecutter.project_name }} requires the following dependencies:

================================================ =========================
Package                                          Minimum supported version
================================================ =========================
`typer <https://typer.tiangolo.com/>`_           0.7.0
`rich <https://rich.readthedocs.io/en/stable/>`_ 12.6.0
================================================ =========================
{%- else -%}
.. error::
    {{ cookiecutter.project_name }} is missing dependencies right now! Come back when
    you've decided what to do with it. and add them within a `simple table
    <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables>`_.
{%- endif %}

Optional Dependencies
=====================

.. warning::
    {{ cookiecutter.project_name }} has no optional dependencies right now! If the
    project does not need to implement them, simply remove this section. Otherwise, come
    back when you've added them to a `optional group
    <https://python-poetry.org/docs/master/managing-dependencies/#optional-groups>`_ in
    ``pyproject.toml`` and add them within a `simple table
    <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables>`_.
