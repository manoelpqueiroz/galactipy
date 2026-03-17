{%- set page_title = '10 Minutes to ' ~ cookiecutter.project_name -%}
{{ '=' * (page_title | length) }}
{{ page_title }}
{{ '=' * (page_title | length) }}

This is a short introduction to {{ cookiecutter.project_name }}, to help new users get
up and running with the basics of the library very quickly.

First of all, we usual import statement is:

.. ipython:: python

    from {{ cookiecutter.package_name }} import hello

{%- set page_title = 'Basic Elements in ' ~ cookiecutter.project_name -%}
{{ '=' * (page_title | length) }}
{{ page_title }}
{{ '=' * (page_title | length) }}

{{ cookiecutter.project_name }} provides a single function for use:

1. ``hello``: a function to output a standardised message given a name to greet.

Greeting Someone
================

Generate a greeting by calling the ``hello`` function with a single argument, the name
of whoever is being greeted:

.. ipython:: python

    hello("Manoel")

Further Reading
===============

See the Essential Basic Functionality and Advanced Features for more information on the
use of {{ cookiecutter.project_name }}.
