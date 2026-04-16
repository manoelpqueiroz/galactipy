{% raw -%}
---
tags:
  - Development Guides
  - Policies & Rules
  - Workflows
---

{% endraw -%}
# Making Changes to the Documentation
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#making-changes-to-the-documentation

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#making-changes-to-the-documentation

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

!!! warning

    This section refers to guidelines
    for changing the **Formal Documentation**.

    If you wish to make changes
    to another type of file,
    refer to its respective commentary
    in the [Anatomy section][1].

Anyone is welcome
to make improvements to the documentation,
validated through a [**Project Policy Proposal** {{ cookiecutter.__mr_term }}][2].
Even if the updates are marginal,
we encourage contributors
to submit their changes
and help us get closer
to delivering flawless docs
to our community.

Be aware to observe
the following protocols
to orient your approach
at all times
during content edition:

- The target reader varies
  depending on the page;
  strive to change/add content
  so it suits its respective audience;
  do not attempt to
  accommodate multiple reader types
  to a single page;
- Leverage [Zensical's features][3] where appropriate
  to elevate knowledge transmission;
  use them strategically,
  however,
  and avoid overrelying on them
  to build a page's content;
- Keep pages
  with a maximum heading depth of **3**
  to reduce cognitive load on readers,
  and split into multiple pages
  to focus on a single unit of knowledge
  at a time.

Additionally,
some parts of the documentation
should adhere to specific conventions
to standardise content and formatting,
helping users more easily navigate
through the pages.

## API Collection
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#api-collection

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#api-collection

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The project uses [`mkdocstrings`][4]
(and, more specifically, [`mkdocstrings-python`][5])
to collect the API from {{ cookiecutter.project_name }}.
This makes the process
of providing API details to users
much more efficient,
but mkdocstrings does not make
the process completely automatic.
Thus,
contributors are required to understand
specific conventions defined here
to ensure their changes
follow a logical standard.

For the public API,
we enforce the rule of
**one page per method/attribute**.
Instead of collecting the entire class
or module
in a single page,
by having each method,
attribute
or function
be placed in its own page
we reduce clutter
and readers can focus on
those objects' implementation
without distraction.

### Classes

For classes,
this encompasses
a specific structure
with distinct `mkdocstrings` options:

1. A [navigation section][6] page
   to present the class' docstring
   and objects:

```
::: <object_path>
    options:
      members: false
      show_root_full_path: true
      show_symbol_type_heading: false
      show_signature: false
      separate_signature: false
      show_docstring_parameters: false
      show_docstring_returns: false
      show_docstring_examples: false
      show_docstring_raises: false
      show_docstring_warns: false
      show_docstring_yields: false
```

2. A page to provide the class' constructor
   and `__init__` method details,
   named `init.md`:

```
::: <object_path>
    options:
      show_docstring_attributes: false
      show_docstring_functions: false
      show_docstring_description: false
      members:
      - __init__
```

3. Additional subpages
   to document each method
   or property for the class
   (does not require
   `mkdocstrings` handler option overriding).

!!! note

    For simpler classes
    that do not require a constructor,
    such as Enums or dataclasses,
    the `init.md` file can be skipped altogether,
    using the navigation section page
    to perform its purpose:

    ```
    ::: <object_path>
        options:
          members: false
          show_root_full_path: true
    ```

### Functions

For any public functions,
only the object path
should be overridden
from `mkdocstrings` handlers:

```
::: <object_path>
    options:
      show_root_full_path: true
```

### Constants

If a constant is exposed to users
in the public API,
their collection into the docs
must also include content
manually added
to explain its purpose and usage,
as constants are object instances
and thus lack docstrings on their own.
The `mkdocstrings` configuration
for this object is the following:

```
::: <object_path>
    options:
      show_root_full_path: true
      separate_signature: false
      show_attribute_values: false
```

### Non-Exposed API

Some of the objects
are not exposed to users
in the public API.
They should be collected instead
in the [Development Packages Reference][7] section
as a reference for developers
working in {{ cookiecutter.project_name }}.
{%- if cookiecutter.app_type != 'bare_cli' %}
Their configuration is simpler:

- For objects defined
{%- if cookiecutter.__app_group == 'tui' %}
  either in the `tui` or `cli` packages,
{%- else %}
  in the `cli` package,
{%- endif %}
  they should be individually collected,
  but classes do not require multiple pages
  and can be displayed
  with all attributes and methods
  listed in a single page;
- For everything else,
  objects should be collected
  for each module
  that is not exposed publicly,
  including any auxiliary packages
  defined in `tests`.

For both cases,
the API can be collected
{%- else %}

<!-- DEFINE your rules for non-exposed API collection -->

For auxiliary packages
in the `tests` directory,
objects should be collected
at the module level
{%- endif %}
using the following `mkdocstrings` configuration:

```
::: <object_path>
    options:
      show_root_full_path: true
```

The rules for API collection
described here
should be applied
in conjunction with [docstring rules][8]
for full compliance
with documentation rules.

## Policy Mirroring
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#policy-mirroring

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#policy-mirroring

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The contents of
`CONTRIBUTING.md`,
`ROADMAP.md`
and `SECURITY.md`
should always be reflected
in the formal documentation.
Whenever you make changes
to files in the `docs/` directory
or these policy files,
always make sure to check
for changes required
in the other.

Content must not be blindly copied
from one to the other:
since features and Markdown syntax
differ between [{{ cookiecutter.__scm_platform_base }} Flavoured Markdown][9]
and [Zensical][3],
contributors should aim
to leverage each one's
leading components,
which may lead to
different layouts altogether
(cf. the Invoke command list
in [`CONTRIBUTING.md`][10]
and [the formal documentation][11]).

Whenever mirroring content,
make sure to leave comments
at Markdown headings on each file
pointing to where contributors
can find their counterpart.
While this makes
the process of updating documentation
unable to be fully automated,
this ensures team members focus
on tailoring knowledge sharing
to suit the environment
where it is presented.

## Page Tags
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#page-tags

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#page-tags

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

To facilitate navigation
for users,
we leverage [Zensical tags][12]
on our documentation pages.
Broadly speaking,
they are grouped
to more properly
categorise each page
across two purposes:

- The intended **target audience**
  for the file:
  either _general users_
  or _developers/contributors_;
- A specific **field**
  the page's contents delves into.

| Tag                      | Target Audience | Description                                                                                                                        |
| ------------------------ | :-------------: | ---------------------------------------------------------------------------------------------------------------------------------- |
| **For Your Information** |  General Users  | Descriptive content detailing a topic or concept.                                                                                  |
| **User Guides**          |  General Users  | Tutorials and step-by-step guides to enable {{ cookiecutter.project_name }} usage.                                                 |
| **Community Content**    |  General Users  | Content provided by the community at large.                                                                                        |
| **Design Definitions**   |  Contributors   | Descriptive content providing context behind the design and architecture of {{ cookiecutter.project_name }} elements.              |
| **Policies & Rules**     |  Contributors   | Descriptive content detailing rules for project development and expected behaviour from contributors.                              |
| **Development Guides**   |  Contributors   | Tutorials and guides to enable contributions from new developers.                                                                  |
| **Workflows**            |     Either      | Guides explaining how to perform operations to achieve specific outcomes.                                                          |
| **Setup**                |     Either      | Pages containing instructions to set up environments under specific configuration and enable further actions.                      |
| **Configuration**        |  General Users  | Pages related to concepts, objects and features which customise the user's installation of {{ cookiecutter.project_name }}.        |
| **CLI**                  |     Either      | Pages related to concepts, objects and features directly associated with {{ cookiecutter.project_name }}'s command-line interface. |
| **TUI**                  |     Either      | Pages related to concepts, objects and features directly associated with {{ cookiecutter.project_name }}'s user interface.         |
| **Supporting Objects**   |  General Users  | Pages related to publicly exposed API that is not directly associated with either the CLI or TUI.                                  |
| **Backend**              |  Contributors   | Pages related to non-public API objects.                                                                                           |

Besides the tags listed above,
the following tags
serve as navigation facilitator tags:

- **Navigation Sections** simply
  mark `index.md` pages
  to provide a quick reference
  in the search bar;
- **Living Docs** determine pages
  which can be updated at any time,
  making it easier for readers
  to check them periodically.

<!-- Anchors -->

[1]: ./anatomy.md
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[2]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Project%2520Policies
{%- else %}
[2]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=project_policies.md
{%- endif %}
[3]: https://zensical.org/docs/authoring/markdown/
[4]: https://mkdocstrings.github.io/
[5]: https://mkdocstrings.github.io/python/
[6]: https://zensical.org/docs/setup/navigation/#navigation-sections
[7]: ../../dev_packages/index.md
[8]: ../../policies/styling.md#docstring-convention
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[9]: https://docs.gitlab.com/user/markdown/
{%- else %}
[9]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
{%- endif %}
[10]: ../workflow/invoke.md
[11]: {{ cookiecutter.__scm_link_url }}/blob/master/docs/development/for_developers/workflow/invoke.md
[12]: https://zensical.org/docs/setup/tags/
