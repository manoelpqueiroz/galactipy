==========================
Comparison with ``lolcat``
==========================

Many users can likely be familiar with the command-line formatter ``lolcat``, available
in a number of distributions. This page aims to compare both applications and their
fundamental differences.

Tool Comparison
---------------

CLI Usage
~~~~~~~~~

{{ cookiecutter.project_name }} provides a simpler setup than ``lolcat`` as it simply
needs a name for greeting:

.. code-block:: shell

    {{ cookiecutter.repo_name }} --name Manoel

This will render the greeting in a random colour on the terminal. Optionally, the user
can specify the colour with an additional argument:

.. code-block:: shell

    {{ cookiecutter.project_name }} --name Manoel -c red

``lolcat``, on the other hand, needs a file to be provided to its command in order to
format it to the output:

.. code-block:: shell

    echo "Hello Manoel" >> hello.txt
    lolcat hello.txt

Alternatively, the user can pipe the output from another command directly to ``lolcat``:

.. code-block:: shell

    echo "Hello Manoel" | lolcat

Output
~~~~~~

{{ cookiecutter.project_name }} outputs a greeting to someone in the terminal.
``lolcat`` can output any text and thus is more recommended if your aim is to provide a
colourful text display to the user.

However, there are differences between both applications in terms of how they output
colour to the terminal. {{ cookiecutter.project_name }} is locked to displaying a single
colour for the entire greeting, whereas ``lolcat`` will render the text in a rainbow
gradient, which can also be customised in terms of spread, frequency and starting tone.
``lolcat`` is also more advanced in terms of output as the user can configure the
rainbow gradient to be animated.

So in terms of colour output, ``lolcat`` does provide more options for the user. But if
you wish to simply display a greeting in a single colour tone, {{ cookiecutter.project_name }}
may be a more practical solution to your needs.
