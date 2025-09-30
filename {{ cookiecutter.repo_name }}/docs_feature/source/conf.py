# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Make sure you have set up your project with `make install` before attempting to build
# documentation, as it won't be able to retrieve the project's version unless a live
# installation of {{ cookiecutter.repo_name }} is present in your virtual environment

# -- Project information ---------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.project_name }}"
copyright = "{% raw %}{% now 'local', '%Y' %}{% endraw %}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"
release = "someversion" # TODO Find a way to use metadata


# -- General configuration -------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
]

source_suffix = [".rst", ".md"]
templates_path = ["_templates"]
exclude_patterns = [
    "**.ipynb_checkpoints",
    # to ensure that include files (partial pages) aren't built, exclude them
    # https://github.com/sphinx-doc/sphinx/issues/1965#issuecomment-124732907
    "**/includes/**",
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
root_doc = "index"


# -- Options for HTML output -----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
