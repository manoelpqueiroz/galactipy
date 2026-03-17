==============================
Comparison with "Hello World!"
==============================

For many newcomers to the programming world, usually the first example used to build a
program is the "Hello World!" string. This page aims to provide a comparison between
this example and {{ cookiecutter.project_name }}. Our main concerns when comparing them
are:

- **Functionality / flexibility:** what can and what can not be done with each tool;
- **Ease-of-use:** in which aspects each tool is easier or harder to use;
- **Purpose of application:** what are the main purposes for using each tool.

Basic Usage
-----------

The "Hello World!" is mostly used by creating a script file containing a simple code,
usually using the ``print`` function to output the desired message on the terminal once
the script is run:

.. ipython:: python

    print("Hello World!")

{{ cookiecutter.project_name }} was designed so users can break away from the convention
and relate themselves more to the concept of talking to a machine that replicates
commands given to them. However, in order to achieve this, the user must be familiar
with external libraries and imports in Python:

.. ipython:: python

    from {{ cookiecutter.package_name }} import hello
    hello("Manoel")

.. note::

    Of course, one can emulate the same output from "Hello World!" if they so wish:

    .. ipython:: python

        hello("World")

"Hello World!" is a more basic approach to programming and is faster to set up. However,
in some cases, paradoxically it might be more difficult of an example to transmit, since
it is usually just given as an exercise or shown for the user to replicate.
{{ cookiecutter.project_name }}, although more complex in setting up (which include
also explaining the Python Standard Library vs. external libraries, ``pip`` and package
installation and package imports), can better provide a glimpse of how programming is
used in practice from the start.

{%- if cookiecutter.app_type != 'bare_repo' -%}
CLI Interface
-------------

The "Hello World!" program is always confined to the script in which it was written.
Therefore, the output will only be displayed when said script is run:

.. code-block:: shell

    echo 'print("Hello World!")' >> hello_script.py
    python hello_script.py

.. important::
    Usually for programs with this level of sophistication, mainly provided at the very
    basic of a programming course, execution will most likely be through a graphical
    user interface (GUI) of an integrated development environment (IDE). Your mileage
    may vary.

In contrast, {{ cookiecutter.project_name }}, while able to be integrated within a
script just like "Hello World!", was designed to be better enjoyed through the CLI
directly:

.. code-block:: shell

    {{ cookiecutter.repo_name }} --name Manoel

This can be viewed as a broader approach to explain programming concepts. At the highest
level of complexity and scale, programming is used to power whole applications,
platforms and systems around the world. However, by using {{ cookiecutter.project_name }}
as an example, one can more easily grasp the nature of building applications, as a CLI
interface is the simplest form of interaction with an application.
{%- endif -%}
