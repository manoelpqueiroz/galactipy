==========================
Comparison with ``cowsay``
==========================

Since {{ cookiecutter.project_name }} has as its main function the simple output of a
greeting, it can sometimes be compared to the popular terminal application ``cowsay``.
This page provides a more detailed look at how both tools work differently and when
to choose one over the other.

{%- if cookiecutter.app_type != 'bare_repo' -%}
Quick Reference
---------------

Let's start with a quick runthrough of the available options between {{ cookiecutter.project_name }}
and ``cowsay`` on the command line:

.. TODO: generate dynamic spacing based on string - project_name length

{{ '=' * (cookiecutter.project_name | length) }} ========== ==============
{{ cookiecutter.project_name }} ``cowsay`` Basic function
{{ '=' * (cookiecutter.project_name | length) }} ========== ==============
``--name`` ``[message]`` Output the desired value by the user.
``--colour`` None Display the output in a specific colour.
None ``-e`` Eye string.
None ``-T`` Tongue string.
None ``-W`` Column.
None ``-f`` Cowfile.

As one can see, {{ cookiecutter.project_name }} has less options than ``cowsay``, as its
main purpose is to simply display a greeting to someone in the terminal.

In this sense, ``cowsay`` is more versatile, as it allows the user to display any
message they want on the screen, so if you need your application to generate messages of
various natures, ``cowsay`` is more recommended. However, if your intent is to display a
greeting to someone, {{ cookiecutter.project_name }} will be a better option as it
only needs the name of the recipient of said greeting instead.

Also, ``cowsay`` can be better customised to the user's needs, with the possibility of
overwriting the cow's eyes, tongue and line wrap length, as well as be provided with a
specific cowfile for changing the cow itself (pre-built into the system or created by
the user). On the other hand, {{ cookiecutter.project_name }} provides a colour output
customisation out-of-the-box, whereas with ``cowsay`` you will need an additional tool
to reach a similar behaviour.

Overall, both tools have very different purposes, but achieve similar goals: outputting
messages on the terminal. Below is an example on how to use both tools to display the
same message:

.. code-block:: shell

    {{ cookiecutter.repo_name }} --name Manoel
    cowsay Hello Manoel!
{%- else %}
Tool Comparison
---------------

{{ cookiecutter.project_name }} is a Python package to be used to generate a simple
string with a greeting:

.. ipython:: python

    from {{ cookiecutter.package_name }} import hello
    hello("Manoel")

On the other hand, ``cowsay`` is a command-line tool to display messages on the
terminal, and provides a large range of options to display them, which include read from
the STDOUT, customise the cow's look and also pair it with other tools to make it
flashier.

Both tools serve very different purposes. If your goal is to have a package to easily
provide greeting strings to your code, {{ cookiecutter.project_name }} is the way to go.
However, if you wish to display messages on the CLI, then you will be better served by
``cowsay``.
{%- endif %}
