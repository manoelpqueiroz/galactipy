# CLI Guide

{{ cookiecutter.project_name }} provides a command-line interface
for direct interaction with the application's capabilities.
This section provides a guide
on available commands
and how to use them.

!!! abstract "How to read the legend"

    This section uses visual icons
    to denote different characteristics
    of the arguments that can or must be provided
    to each command:

    - :fontawesome-solid-font: String input;
    - :fontawesome-solid-hashtag: Number input;
    - :fontawesome-solid-sitemap: Array input (dict, list, dict of lists etc.);
    - :fontawesome-solid-folder-tree: Valid filepath;
    - :fontawesome-solid-toggle-off: Binary flag
      (by definition an optional argument).

    Additionally,
    :fontawesome-solid-border-none: denotes
    an optional argument
    for non-binary inputs.

## Calling the Program

{% if cookiecutter.app_type == 'tui' -%}
You can simply
launch {{ cookiecutter.project_name }}
by calling `{{ cookiecutter.repo_name }}`
directly in your terminal.
This will launch
the terminal user interface (TUI),
from which you will be able
to further interact
with the application.

The top-level command
is also callable
with other options
for fine-grained
control of the application:

??? success "`{{ cookiecutter.repo_name }} [--version | -v] [(--config | -c) <file>]`"

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--version` / `-v`**
    >
    > Print
    > the current version of the program
    > and exit.

    ---

    > :fontawesome-solid-border-none:{ .middle }
    > :fontawesome-solid-folder-tree:{ .middle }
    > **`--config` / `-c`**
    >
    > Specify a custom configuration file
    > to launch the application.

{% elif cookiecutter.app_type == 'hybrid' -%}
The top-level command
is the entry point
for additional
operations:

??? info "`{{ cookiecutter.repo_name }} [--version | -v]`"

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--version` / `-v`**
    >
    > Print
    > the current version of the program
    > and exit.

Launch the terminal user interface (TUI)
with the `{{ cookiecutter.repo_name }} launch` command:

??? success "`{{ cookiecutter.repo_name }} launch [(--config | -c) <file>]`"

    > :fontawesome-solid-border-none:{ .middle }
    > :fontawesome-solid-folder-tree:{ .middle }
    > **`--config` / `-c`**
    >
    > Specify a custom configuration file
    > to launch the application.
{%- else %}
The top-level command
is the entry point
for additional
operations:

??? info "`{{ cookiecutter.repo_name }} [--version | -v]`"

    > :fontawesome-solid-toggle-off:{ .middle }
    > **`--version` / `-v`**
    >
    > Print
    > the current version of the program
    > and exit.
{%- endif %}

<!-- RECORD additional subpages, grouping the different operations available in the CLI -->
