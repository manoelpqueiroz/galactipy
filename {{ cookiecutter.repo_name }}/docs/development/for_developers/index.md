{% raw -%}
---
tags:
  - Section Intros
  - Development Guides
---

{% endraw -%}
# Proposing Changes

{% if cookiecutter.__app_group == 'tui' -%}
<!-- RECORD the context and purposes of your library -->
{{ cookiecutter.project_name }} is a Terminal User Interface (TUI) application,
paired with a Command-line Interface (CLI)
for performing operations
entirely from your terminal.
Therefore,
the project's main consumption of time
is related to
how these interfaces behave
with the user
and their capabilities
when called upon
to perform operations.

Code maintenance within {{ cookiecutter.project_name }} itself encompasses:

- Frontend developments
  to improve and refine
  the application:
    - [`tui/`][0a] contains the entire logic
      for rendering and controlling
      the terminal interface
      with [Textual][0b];
      this includes
      interface components
      (i.e.,
      widgets,
      screens,
      layouts
      etc.),
      styles
      and themes;
    - [`cli/`][1] structures
      the available commands
      to control the application
      from the command-line
      using [Typer][2],
      including launching the TUI;
- Backend components
  to enable fluid experience:
    - [`config/`][3] defines
      the API necessary
      for manipulating configuration files,
      used to store user-specific data,
      application state
      and customisation options;
    - [Logging][4] customisations
      to be rendered
      as the program output
      or as structured files
      for debugging purposes;
- [Tests][5]
  for validating program behaviour
  as expected;
- [Tasks][6] aimed at
  improving
  and speeding up
  local development
  with [Invoke][7].

{% elif cookiecutter.__app_group == 'cli' -%}
<!-- RECORD the context and purposes of your library -->
{{ cookiecutter.project_name }} is a Command-line Interface (CLI) application
for performing operations
entirely from your terminal.
Therefore,
the project's main consumption of time
is related to
how this interface behaves
with the user
and its capabilities
when called upon
to perform operations.

Code maintenance within {{ cookiecutter.project_name }} itself encompasses:

- Frontend developments
  to improve and refine
  the application:
    - [`cli/`][1] structures
      the available commands
      to control the application
      from the command-line
      using [Typer][2],
      including launching the TUI;
- Backend components
  to enable fluid experience:
    - [`config/`][3] defines
      the API necessary
      for manipulating configuration files,
      used to store user-specific data,
      application state
      and customisation options;
    - [Logging][4] customisations
      to be rendered
      as the program output
      or as structured files
      for debugging purposes;
- [Tests][5]
  for validating program behaviour
  as expected;
- [Tasks][6] aimed at
  improving
  and speeding up
  local development
  with [Invoke][7].

{% else -%}
<!-- RECORD the context surrounding your library, detailing the main modules for code maintenance and their purpose -->

{% endif -%}
Outside this set of code contributions,
the development team's time
will involve:

- Researching,
  designing
  and implementing
  new application features
  to deliver aggregated value
  to users;
{%- if cookiecutter.use_bdd %}
  this includes
  engaging with the community and contributors
  to delineate {{ cookiecutter.project_name }} behaviour
  at the discovery and formulation stages
  of our behaviour-driven development;
{%- endif %}
- Extending {{ cookiecutter.project_name }}'s capabilities
  for other developers
  to build their own solutions
  leveraging our public API;
- Keeping development tools and integrations
  updated and working
  with constant revision
  of configuration files,
  workflows
  and behaviour;
- Keeping the documentation up to date;
  this encompasses:
{%- if cookiecutter.app_type != 'bare_repo' %}
    - The [`README`][8] file,
{%- else %}
    - The [`README`][1] file,
{%- endif %}
      which lists all features
      provided by {{ cookiecutter.project_name }},
      basic instructions on setup
      and usage;
    - The formal documentation, providing
      detailed instructions on installation,
      in-depth user guide
      for newcomers,
      API reference,
      a comprehensive guide for contributors
      on technical details
      for developing the application,
      as well as release notes;
    - The policies that orient
      {{ cookiecutter.project_name }} development
      and contributor interactions.

<!-- Anchors -->
{%- if cookiecutter.app_type != 'bare_repo' %}

{% if cookiecutter.__app_group == 'tui' -%}
[0a]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/tui
[0b]: https://textual.textualize.io/
{% endif -%}
[1]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/cli
[2]: https://typer.tiangolo.com/
[3]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/config
[4]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/logging
[5]: {{ cookiecutter.__scm_link_url }}/tree/master/tests
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/tasks.py
[7]: https://www.pyinvoke.org/
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/README.md
{%- else %}

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/README.md
{%- endif %}
