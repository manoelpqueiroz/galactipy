{% raw -%}
---
tags:
  - Development Guides
  - Policies & Rules
  - Workflows
---

{% endraw -%}
# Styling
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#styling

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#styling

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

## Codestyle
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#codestyle

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#codestyle

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The project uses [Ruff][1]
for formatting and codestyle.
Developers can check
both the linter
and the formatter
with the preconfigured tasks
with `invoke codestyle` and `invoke lint` commands.

To suggest changes and additions
to Ruff rules and conventions
for the project,
use a [Project Policy Proposal {{ cookiecutter.__mr_acronym }}][2].

## Docstring Convention
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#docstring-convention

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#docstring-convention

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{% if cookiecutter.docstring_style != 'other' -%}
We choose to write our docstrings
using the [{{ cookiecutter.__docstring_name }}][1a] standard.
Please be aware
to adhere to it
when making your contributions.

We enforce the following rules
for docstrings:

- Public functions, classes and methods
  must always contain
  the short summary
  and parameter sections;
  if return types
  and/or exceptions
  are defined,
  they must also be included
  in the docstring;
  extended summaries
  are left to the contributor's discretion;
- Private functions, classes and methods
  must define only the short summary;
  other sections
  are left to the contributor's discretion;
- For classes:
    - If a class does not define attributes
      – or only does so using properties –,
      the class docstring does not need
      to describe the "Attributes" section;
      otherwise,
      all attributes and properties
      must be listed
      in this section;
    - The parameters for the `__init__` method
      should be declared in the class docstring,
      with the method's docstring itself containing
      only the short summary
      for the purpose to pass codestyle rules;
- If a module expose public constants
  to users,
  its docstring must contain
  the "Attributes" section
  listing all constants.

{% else -%}
<!-- RECORD your docstring convention details and usage guidelines -->
We choose to write our docstrings
using a custom standard.
Please be aware
to adhere to it
when making your contributions.

{% endif -%}
## Semantic Line Breaks
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#semantic-line-breaks

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#semantic-line-breaks

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

When editing Markdown files,
[Semantic Line Breaks][3] should be applied.
This increases the document's readability
by other contributors
and makes changes clearer
when using `git diff`.
This comes from Brian Kernighan
in his 1974 book _"UNIX for Beginners"_:

!!! tip "Hints for Preparing Documents"

    Most documents go
    through several versions
    (always more than you expected)
    before they are finally finished.
    Accordingly,
    you should do whatever possible
    to make the job of changing them easy.

    First,
    when you do the purely mechanical operations of typing,
    type so subsequent editing will be easy.
    Start each sentence on a new line.
    Make lines short,
    and break lines at natural places,
    such as after commas and semicolons,
    rather than randomly.
    Since most people change documents
    by rewriting phrases
    and adding, deleting and rearranging sentences,
    these precautions simplify
    any editing you have to do later.

On a more practical level,
this [article][4] from Derek Sivers
provides additional reasons
for adopting this style.

The only files
that should not follow this rule
are issue and {{ cookiecutter.__mr_term }} templates
inside [`.{{ cookiecutter.__scm_platform_lc }}`][5] and [`CHANGELOG.md`][6].

<!-- Anchors -->

[1]: https://docs.astral.sh/ruff/
{%- if cookiecutter.docstring_style == 'numpy' %}
[1a]: https://numpydoc.readthedocs.io/en/latest/format.html
{%- elif cookiecutter.docstring_style == 'google' %}
[1a]: https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings
{%- elif cookiecutter.docstring_style == 'sphinx' %}
[1a]: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[2]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Project%2520Policies
{%- else %}
[2]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=project_policies.md
{%- endif %}
[3]: https://sembr.org/
[4]: https://sive.rs/1s
[5]: {{ cookiecutter.__scm_link_url }}/tree/master/.{{ cookiecutter.__scm_platform_lc }}
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/CHANGELOG.md
