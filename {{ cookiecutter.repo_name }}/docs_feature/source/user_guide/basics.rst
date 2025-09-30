=============================
Essential Basic Functionality
=============================

In this article we discuss the essential functionality provided by {{ cookiecutter.project_name }}.
To begin, let's import the ``hello`` function:

.. ipython:: python

    from {{ cookiecutter.package_name }} import hello

Calling a Greeting
==================

The ``hello`` function receives a single string argument, which represents whom we want
to direct the greeting to:

.. ipython:: python

    hello("Manoel")
    hello("Margareth")
    hello("Romain")
