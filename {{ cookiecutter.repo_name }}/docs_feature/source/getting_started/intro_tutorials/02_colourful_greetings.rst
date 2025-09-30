{%- set page_title = 'Using ' ~ cookiecutter.project_name ~ ' to Make Things More Colourful' -%}
{{ '=' * (page_title | length) }}
{{ page_title }}
{{ '=' * (page_title | length) }}

Using the Terminal to Get Coloured Output
=========================================

.. code-block:: shell

    {{ cookiecutter.repo_name }} --name Manoel

To use the command-line tool, you need to call the ``{{ cookiecutter.repo_name }}``
executable and inform a name to greet. **Always** provide a name, otherwise the program
will fail.

By calling the ``{{ cookiecutter.repo_name }}`` executable from your command line, a
random colour will be chosen to render the greeting.

I Want to Choose Myself a Colour for My Greeting
================================================

.. code-block:: shell

    {{ cookiecutter.repo_name }} --name Manoel --colour red

The ``{{ cookiecutter.repo_name }}`` command-line tool provides a ``--colour`` option to
force the output in the desired colour.

.. note::

    The available colours follow the basic 8-bit terminal colours:

    - Black;
    - Red;
    - Green;
    - Yellow;
    - Blue;
    - Magenta;
    - Cyan;
    - White.

.. tip::

    You can simplify your command by shortcoding the ``--colour`` option to the ``-c``
    alias.

Wrapping Up
===========

.. hint::
    Remember:

    - Call the ``{{ cookiecutter.repo_name }}`` command-line tool with
      ``{{ cookiecutter.repo_name }} --name TEXT``;
    - The ``--name`` option must always be provided for the CLI to work;
    - You can specifiy a desired colour with the ``--colour`` option.
