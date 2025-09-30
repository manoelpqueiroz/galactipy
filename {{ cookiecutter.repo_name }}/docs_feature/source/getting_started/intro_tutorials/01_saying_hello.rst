{%- set page_title = 'How Can I Say "Hello" with ' ~ cookiecutter.project_name ~ '?' -%}
{{ '=' * (page_title | length) }}
{{ page_title }}
{{ '=' * (page_title | length) }}

{% set section_1_title = 'I Want to Start Using ' ~ cookiecutter.project_name %}
{{ section_1_title }}
{{ '=' * (section_1_title | length) }}

.. ipython:: python

    from {{ cookiecutter.package_name }} import hello

To load the ``hello`` function provided by the package, import it to make it available
to work with.

I Want to Greet Someone
=======================

.. ipython:: python

    greet = hello("Manoel")
    greet

To output a greeting on the REPL, simply call the ``hello`` function with a single
argument, the name of the person who you want to greet.

.. note::
    The ``hello`` function will store the greeting in a string. You can either call it
    after storing it, call it directly without storing in a variable or use the
    ``print`` function to output it to the REPL.

Wrapping Up
===========

.. hint::
    Remember:

    - Import the ``hello`` function with ``from {{ cookiecutter.package_name }} import hello``;
    - Use the ``hello`` function with a single argument to store the greeting in a
      string;
    - You can either store the greeting in a variable and print it later or return the
      string directly.
