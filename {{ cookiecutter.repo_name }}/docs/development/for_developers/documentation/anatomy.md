# Anatomy

As a contributor,
be aware that
whenever the term "documentation" is mentioned,
it can refer to any one
of the following distinct domains
where knowledge is collected
and presented to different audiences.

## The `README` File

The [`README`][1] file
is the one that users will first interact with
when they decide to check {{ cookiecutter.project_name }}
– be it in the project repository
or the PyPI package listing.
Its main purpose is
to provide the essential information
to get people started with
the project.

Thus,
the content should be targeted
towards people who are not familiar with the project,
strictly aiming for brevity and clarity
in its contents.

It should aptly fulfill
the following functions:

1. Present the purpose of the project;
2. Show how {{ cookiecutter.project_name }}
   can help people solve
   their problem at hand;
3. Provide information
   on common use cases
   for {{ cookiecutter.project_name }};
4. Swiftly detail the installation process;
5. Tell how anyone
   could contribute to {{ cookiecutter.project_name }}.

Should any of these topics
not be made explicit
from the perspective of a new user,
then changes in these files are warranted.

## Hard Policy Files

These are files
that delineate the core principles
guiding the work at {{ cookiecutter.project_name }}.
Collectively,
they form what we could call
the "statute" of the project,
and are geared towards
contributors of all levels
of familiriaty
and activity
in the project.

Their main purpose
is to place all contributors
under a single understanding
of how the work should be done in {{ cookiecutter.project_name }},
and act as a paramount resource
to address contesting visions
for implementing something
when discussions arise.

The hard policy files are:

- The [`CONTRIBUTING`][2] guide;
  - Shows how people can get started
    setting up a development environment
    for {{ cookiecutter.project_name }};
  - Lists the main tools
    used for managing development of the project
    and how contributors
    should approach them;
  - Contains all sets of rules regulating
    what contributors are expected to do,
    how they should behave
    – individually and on interactions –
    and how flexibly or not
    these rules should be followed;
- The [`ROADMAP`][3] file:
  - Delves relatively deeper than the `README`
    on the purpose of the project;
  - States the mission of the project,
    a visionary declaration
    of what the contributors see
    as the endgame of development;
  - Lays out the different stages of development
    and what is expected to be achieved
    at each one of them;
  - Provides anyone
    with a quick reference table
    of the history of major milestones
    that have been either
    discussed,
    already delivered,
    currently developed
    or planned for the future,
    aiming to more easily situate newcomers
    and people interest in contributing;
- The [`SECURITY`][4] file:
  - Presents the threat model for the project;
  - Provides guidance to people
    on how to report a security vulnerability
    (and what is **not** considered one);
  - Clarifies how we respond to
    and disclose a security report
    once it is send;
  - Informs of any current vulnerabilities and advisories;
- The [Code of Conduct][5],
  for which more specific information
  can be found in [its respective section][6].

These files are not immutable,
and can be submitted for changes and updates
by any contributor
via a [**Project Policy Proposal** {{ cookiecutter.__mr_acronym }}][7].

## Issue and {{ cookiecutter.__mr_term }} Templates

Templates used for
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
issues
{%- else %}
issues,
discussions
{%- endif %}
and {{ cookiecutter.__mr_term }}s
are also part of {{ cookiecutter.project_name }} policies,
as they regulate,
for specific themes:

- When to use a template;
- What information to provide
  to start discussions;
- How to frame
  the work item's structure
  for submission.

But since they are more flexible
in their presentation,
they are considered "soft" policy files instead.

To effectively provide value to the project,
these files must be arranged
as high-level instructions
to facilitate their filling out
in an orderly and complete manner,
and should be updated
whenever they are increasingly misused
by submitters,
be they contributors
or community members.
This includes
creating new types of templates
when the project's circumstances
call for.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

!!! tip

    Checklists can be leveraged
    for submitters and reviewers
    to follow more easily
    in regards to relevant actions
    related to the item.

    For the sake of clarity,
    whenever an action
    might take the form
    of binary choices,
    prefer splitting them
    in separate nested items
    and orient users
    to leverage
    [complete/inapplicable tasks][7].
>>>
{%- endif %}

Moreover,
our view is that
**work items are also part of documentation**.
Contributors,
especially those
who have an active role
in {{ cookiecutter.project_name }},
should always be aware
to treat posts and interactions
in work item discussions
anticipating how their input
can be useful in the future,
following our [guiding principles][9].

!!! warning

    Special attention should be given
    when participating in a **Structural Design** discussion.
    Those {{ cookiecutter.__mr_acronym }}s are more delicate
    as their purpose is
    to signal other project members
    the formation of a validation board
    which will ratify future feature implementation
    or reevaluate previous implementation flaws
    that went undetected.

    Those {{ cookiecutter.__mr_acronym }}s
    are functionally the same
    as [enhancement proposals][9],
    collecting feedback
    on a design
    and producing a historical record
    on the rationale
    behind our design decisions.
    Every contributor is welcome to participate
    and provide input to the discussions,
    but we kindly ask you
    to refrain from adding trivial comments
    in these occasions
    and actively focus
    on discussion points.

Improvements to the structure of these files,
as well as proposing new template types,
should be done via a [**Project Policy Proposal** {{ cookiecutter.__mr_acronym }}][7].

## The Formal Documentation

Apart from individual files
spread across the repository,
the [`docs/`][11] directory stores
what we call the "formal" documentation
for {{ cookiecutter.project_name }}.
These are the docs
that are exposed to the public
via a static website.

We use Zensical
as the backbone of our documentation,
which is configured
in the [`zensical.toml`][12] file.
Contributors are instructed
to read [Zensical's][13] documentation
before proposing changes to ours.

The formal docs
have their own structure,
split across four major branches of knowledge:

- The **Reference Guide**,
  a technical document
  which collects the public API
  for technical reference;
  it presents:
  - All the functions and methods
    publicly available in the software;
  - How they work;
  - What inputs and outputs
    users should expect,
    along with side effects;
  - Examples of implementation
    and use contexts;
- Instruction guides,
  with varying levels of detail;
  those are tutorial-like documents
  that take the user "by the hand"
  and loop through the features
  of {{ cookiecutter.project_name }},
  which include:
  - The installation guide,
    with full instructions
    on all different methods
    of installation;
  - An overview of the package,
    illustrating purpose,
    main features
    and core aspects;
  - Manuals on
    how to use {{ cookiecutter.project_name }}
{%- if cookiecutter.app_type != 'bare_repo' %}
    on an elementary level,
    guidance on caveats
    users should be aware of
    and the complete catalog
    of CLI commands and options;
{%- else %}
    on an elementary level
    and guidance on caveats
    users should be aware of;
{%- endif %}
- Cookbook-style content,
  containing recipes
  for how to use the library
  to accomplish specific tasks:
  - 1-minute tutorials
    to quickly showcase
    practical usage of {{ cookiecutter.project_name }},
    one feature at a time;
  - Dedicated guides
    comparing {{ cookiecutter.project_name }} to alternatives,
    providing their users
    with relevant content
    to easily translate concepts
    from those alternatives
    into {{ cookiecutter.project_name }}
    and more easily migrate from them;
  - Sections dedicated to power users
    who aim to take the most
    out of the library's functionalities;
  - A collection of community-generated guides
    and FAQs to address the most common issues
    faced by {{ cookiecutter.project_name }} users;
- The **Development Guide**,
  aimed at existing and potential contributors
  to serve as the reference
  for how development of {{ cookiecutter.project_name }} takes place,
  which encompasses:
  - The transcription
    of all hard policy files
    defining the rules
    for development;
  - The reference
    for non-public API objects
    present in the {{ cookiecutter.project_name }} codebase
    (i.e., those that are not exposed to users);
  - Information on how to contact the team
    for different purposes;
  - The collection of all previous releases
    and their release notes
    for reference.

Changes to any part of the formal documentation
are also done via [**Project Policy Proposal** {{ cookiecutter.__mr_acronym }}s][7],
with more detailed guidelines
presented in its [specific section][14].

<!-- Anchors -->

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/README.md
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md
[3]: ../../roadmap.md
[4]: {{ cookiecutter.__scm_link_url }}/blob/master/SECURITY.md
[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CODE_OF_CONDUCT.md
[6]: #code-of-conduct
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[7]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Project%2520Policies
{%- else %}
[7]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=project_policies.md
{%- endif %}
[8]: https://docs.gitlab.com/user/markdown/#task-lists
[9]: ../../philosophy.md#say-why-not-just-what
[10]: https://pydevtools.com/handbook/explanation/pep/
[11]: {{ cookiecutter.__scm_link_url }}/tree/master/docs
[12]: {{ cookiecutter.__scm_link_url }}/blob/master/zensical.toml
[13]: https://zensical.org/
[14]: ../../for_others/documentation_changes.md
