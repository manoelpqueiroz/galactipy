# How to Contribute

Galactipy is a [Cookiecutter][intro1] template
for generating boilerplate files
and creating Python software,
especially CLI applications.

We would like to encourage you
to contribute to this project
and we strive to make it
as easy as possible.
This guide is aimed at
facilitating onboarding
for new collaborators
and as a complimentary source of information
to our [main `CONTRIBUTING` guide][intro2],
which you should read
before diving into this specific guide.

[[_TOC_]]

## :runner: TL;DR

Preconditions for
contributing as a developer:

- Creating Merge Requests
  requires a GitLab account;
- Merge Requests should
  adhere to the [Galactipy Philosophy][tldr1];
- Commits should
  adhere to our [commit customs][tldr2];
- The project's [codestyle][tldr3] should
  be followed strictly;
- Work item management should
  be done following [our specific practices][tldr4].

### Development Setup

To start contributing to Galactipy,
you should start
by [forking][setup1] the upstream repository
to your own GitLab [group][setup2].

After forking the upstream repository,
cloning it to your local environment
and accessing the root dir
via your IDE or the terminal:

1. Make sure
   you have Poetry [installed][setup3];
2. Create and activate
   your virtual environment:

```sh
poetry env use 3.14 # Or replace with your Python version
eval $(poetry env activate)
```

3. Install the project's dependencies:

```sh
poetry install # Or, preferably, `invoke install` if available
invoke hooks
```

4. Run the sweeping task
   with Invoke
   and check output:

```sh
invoke sweep
```

If everything passes,
you're good to go!
Otherwise,
something is not right
and there might be an opportunity
for a [first contribution][setup4].

## :classical_building: Fundamental Policies

### Open Development

All work on Galactipy happens
directly on [GitLab][dev1],
including
roadmap and [epics][wts5]
management.
Therefore,
a GitLab account is needed
to start contributing.

A [GitHub mirror][dev2] is set up
to facilitate discovery of the template
by other users,
but this repository
should not be used
for active development.

#### Work Item Tracking

##### Labels

Besides the labels
defined for the [Galactipy group][issue1],
the Galactipy project defines
the following additional labels
to mark
issues and Merge Requests
specific to this project:

|             Label             | Usage                                                            |
| :---------------------------: | ---------------------------------------------------------------- |
| ~"template-internals::docker" | Modifies features specifically related to Docker capabilities.   |
| ~"template-internals::github" | Adds or updates features exclusive to projects hosted in GitHub. |
| ~"template-internals::gitlab" | Adds or updates features exclusive to projects hosted in GitLab. |

### Versioning Customs

As a Cookiecutter template,
users rely on Galactipy
only once
in their project's entire lifecycle:
at its creation.
From the user's perspective,
differences between Galactipy versions
are minimal
and our template remains
in a stable state throughout time.
Most of Galactipy's development
involves incremental improvements
or new features related to file generation.

Given this context,
versioning plays a greater role
in communicating changes to users
instead of focusing on abstract concepts
such as orthogonality or breaking changes.
Since Galactipy is not a traditional software library
requiring strict adherence to semantic versioning
for downstream compatibility,
we have chosen [Romantic Versioning][version1]
as our preferred scheme.

Romantic Versioning aligns well
with Galactipy's purpose
as a repository of pre-configured files and templates.
This approach ensures
that versioning serves
its primary purpose:
informing users
about meaningful changes
in an accessible manner.

We approach our versions
with the following pattern:

- Versions can only be tagged
  if altering end-user generated projects;
  changes to project internals only
  do not qualify for tagging;
- Update **MINOR** versions when:
  - Bugs that
    prevent the template
    from being properly generated
    are fixed;
  - Typos are fixed;
  - Configuration files are updated
    with the latest reference syntax
    without altering
    their behaviour;
  - Markdown files are modified;
- Update **MAJOR** versions when:
  - Project generation behaviour is modified
    without modifications
    to `cookiecutter.json` prompts
    (i.e., the variables the user inputs);
  - Configuration files behaviour is modified;
  - Code files are added,
    removed
    or updated;
- Update **PROJECT** versions when:
  - Available options
    for a step in `cookiecutter.json`
    are altered;
  - Steps are
    either added or removed
    from `cookiecutter.json`;
  - The type of a step
    is altered in `cookiecutter.json`.

### Commit Customs

#### Git Trailers

Every commit should
be identified with the respective [Git trailer][commit1]
to categorise the type of change being made.
When a new version of Galactipy
is released through a tag,
a CI pipeline compiles every trailer
to automate the version's release
and update the `CHANGELOG` file
in the root directory.

The available trailers
are listed below
and defined in the [`changelog-config.yml`][commit2] file:

|    Git trailer    |         Category in CHANGELOG          | Use Cases                                                                                                                                                                                                                                                       |
| :---------------: | :------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   `enhancement`   |         :milky_way: Components         | Updates in behaviour and functionality to existing features for end users.                                                                                                                                                                                      |
|     `feature`     |         :milky_way: Components         | Introduction of new features, tools and integrations for end users.                                                                                                                                                                                             |
|       `bug`       |      :wrench: Fixes & Refactoring      | Correction of bugs introduced in previous releases that went unnoticed.                                                                                                                                                                                         |
|   `refactoring`   |      :wrench: Fixes & Refactoring      | Modifications to the code without changing its output.                                                                                                                                                                                                          |
|     `bugfix`      |      :wrench: Fixes & Refactoring      | Correction of bugs introduced in feature branches and identified before they are merged.                                                                                                                                                                        |
|       `fix`       |      :wrench: Fixes & Refactoring      | Minor corrections that can not be characterised as bugs in and of themselves, such as typos and naming conventions.                                                                                                                                             |
|       `ci`        |     :package: Build System & CI/CD     | Changes to Galactipy's GitLab CI file.                                                                                                                                                                                                                          |
|     `testing`     |     :package: Build System & CI/CD     | Changes to tests for Galactipy.                                                                                                                                                                                                                                 |
|      `hooks`      |            :gear: Internals            | Modifications made to pre-gen and post-gen hooks.                                                                                                                                                                                                               |
| `project-config`  |            :gear: Internals            | Modifications made to configuration files for the project, excluding those specified in the `policies` trailer.                                                                                                                                                 |
|      `build`      | :construction_site: Template Internals | Modifications to CI workflows for generated projects.                                                                                                                                                                                                           |
| `template-config` | :construction_site: Template Internals | Modifications made to configuration files for generated projects, inside `{{ cookiecutter.repo_name }}`.                                                                                                                                                        |
|  `documentation`  |         :pencil: Documentation         | Changes to documentation, either in Galactipy's or the template's `README` file.                                                                                                                                                                                |
|    `policies`     |       :scroll: Project Policies        | Modifications to official project policies in `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.triage-policies.yml`, `.pre-commit-config.yaml`, files under `.gitlab` and all `tool` sections in `pyproject.toml` except for `tool.poetry`. |
|   `milestones`    |       :scroll: Project Policies        | Milestone updates in `ROADMAP.md`.                                                                                                                                                                                                                              |
|  `dependencies`   |     :arrow_up: Dependency Updates      | Dependency updates, for either Galactipy itself or the template.                                                                                                                                                                                                |

### Styling

### Checks & Hooks

Developers are encouraged
to run local tests,
check codestyle and static typing
with the `invoke sweep` command
before committing.

Pre-commit hooks are configured
to block updates not following the rules:

- All files must comply to the [POSIX][hooks1] standard;
- Pre and post-gen hook files must comply with the Ruff linter.

Ensure both Invoke and Pre-Commit are [installed][hooks2]
in your virtual environment.

### Licence

By contributing to Galactipy,
you agree that your contributions
will be licensed under
the [MIT Licence][licence1].

## :speaking_head: Proposing Changes as a Developer

Galactipy is a Cookiecutter template,
used for generating files
within a directory structure
based on the parameters
provided by the user.
Therefore,
the project's main consumption of time
is related to
how these files are configured,
as opposed to
writing additional code.

Code maintenance within Galactipy itself encompasses:

- Hooks for Cookiecutter
  (code that is executed before
  and after file generation):
  - [`pre_gen_project.py`][wts2] is used
    to validate parameter inputs
    from the user;
  - [`post_gen_project.py`][wts3] is used
    to ensure the project is generated
    with the correct files and content;
- [Tests][wts4] for the functions
  defined in pre-gen and post-gen hooks;
- [Tasks][changes1] aimed at
  improving
  and speeding up
  local development
  with [Invoke][changes2].

Outside this narrow set of contributions,
most of the development team's time
will involve:

- Ensuring projects generated with Galactipy
  and their featured tools
  can be used
  from the very beginning;
- Keeping tools and integrations
  updated and working
  with generated projects,
  with constant revision
  of configuration files,
  workflows
  and behaviour;
- Researching and implementing
  new tools
  and integrations;
- Keeping the documentation up to date;
  this encompasses:
  - The [`README`][wts1] file,
    which lists all features
    provided by Galactipy,
    basic instructions on setup
    and usage,
    as well as
    further reading recommendations
    for additional Python libraries
    and guides
    on project management best practices;
  - URLs linking to the repository
    and configuration guide
    for each tool provided
    with generated projects
    as inline comments
    for their respective
    configuration sections;
  - Comment markers
    to guide users
    on additional configuration
    that might be needed
    for proper functioning
    of generated projects;
    see [this section][changes3]
    for further information.

### Preparing to Contribute

#### Choosing What to Contribute

Everyone benefits
if contributors focus on changes
that are useful,
clear,
easy to evaluate,
and already pass basic checks.

Before proceeding,
contributors should evaluate
if the proposed change
is likely to be
relevant,
new
and actionable.

It's worth emphasizing that
changes to startup options
available for users in Galactipy
are more complex to implement
as it requires
a potential overhaul of configuration files.
They will be subjected
to more scrutiny,
and held to a higher standard of review
than changes
to less fundamental building blocks.

### Development Workflow

After cloning Galactipy
and following the [development setup][hooks2],
run `invoke test`
(an isolated Pytest task)
and if no errors are raised,
then run `invoke sweep`
(the whole set
of development checks
in a single task).
This step is crucial to ensure
you don't introduce any regressions
as you work on your change.

>>> [!note]
The project uses `pytest-cookies`
as a development dependency.
This plugin allows Pytest
to validate if the current state of the code
and configuration files
allows for a project
to be generated without errors.
While it acts as a handy tool
to ensure that critical errors
will be caught by [`test_bake_project`][changes4],
the reality is that
developers should be aware
of limitations
currently faced by the project
to implement end-to-end tests,
as its nature relates less to code
and more to behaviour
after file generation.

&5+ has been created
to address this situation
at a future moment.
Feel free to take a look at it
and discuss with the maintainers
if you wish to contribute
to this development front.
>>>

As Galactipy's purpose is
to generate functional repositories
which can be used by developers
with minimal configuration,
the nature of development involves
ensuring not only the project itself is generated,
but that generated projects are functional.

As a developer,
please be conscious
of crucial steps to validate
before submitting your changes,
and understand many of them
require manual action
outside the Galactipy repository.

A non-exhaustive list of steps to consider:

- Did you add
  or modify unit tests
  if development involved
  changes to pre and post-gen hooks?
- Are all checks passing
  with `invoke sweep`?
- Did you address
  all issues raised by Codacy
  for the Merge Request branch in question?
- Compress the Galactipy repository
  in a ZIP file
  and use it
  to generate a project.
  After installing dependencies
  and setting up its virtual environment,
  test proper behaviour
  for the following:
  - Can the project be called from the CLI
    if the `bare_repo` option used was `False`?
  - Do tests for the generated project pass
    if the `bare_repo` option used was `False`?
  - Are files rendered correctly?
    Are there any missing files?
  - Are files rendered
    without excessive blank lines
    or lack thereof
    due to Jinja [whitespace control][changes5]?
  - After setting up
    required external configuration
    identified the `UPDATEME` tags,
    does the project CI pass
    after pushing a semantic version tag
    to its temporary repo?
  - Have the changes
    for a specific configuration file being altered
    been applied
    and are behaving as expected?

#### Feature Flags

Sometimes,
a feature is too large
to be delivered in one Merge Request,
requiring progress to be done iteratively.
To prevent the need for large changes,
contributors can specify files and directories
to be removed from project generation
by appending `_feature` to their names.
They can use this configuration
to create new files and directories
or duplicate existing ones
and work in smaller steps
until the feature is ready to be shipped to users.

Additionally,
by setting the hidden Cookiecutter variable `__debug` to `true`,
developers can render projects including the `_feature` files and directories,
in case they need to check output.

## :reminder_ribbon: Other Ways to Contribute

You can contribute to Galactipy
in additional ways,
one does not need
to know the inner workings of the project
to improve it!
This section provides an overview
on how users outside the project development
can aid the development team,
as well as how to behave and communicate
to improve efficiency
among the team
and between the team and the community.

Since running an open source project
can get exceptionally busy,
any new incoming contact
from outside the development team
can require a contributor's attention
to be redirected
from ongoing work for hours or days.

For this reason,
we kindly ask users
to make a conscious effort
to evaluate the causes
for reaching the team
and focus on matters that are
useful,
clear,
easy to evaluate
and have already been refined
to be brought to attention.
This way
everyone benefits from
faster communication and resolution.

### Contributing by Helping Other People

>>> [!tip] :pushpin: Further Guidance
You can find more information
about helping other people
in our [main `CONTRIBUTING` guide][intro2],
take a look at it
whenever possible.
>>>

### Contributing through User Requests

>>> [!tip] :pushpin: Further Guidance
You can find more information
about user requests
in our [main `CONTRIBUTING` guide][intro2],
take a look at it
whenever possible.
>>>

If you are simply
having trouble using Galactipy,
go through the [`README`][wts1] file and links
directing to support content first,
rather than filing a request.

#### Specific Guidelines for Requests for Support

If Galactipy is not working correctly for you,
most likely it is a simple configuration issue.
Try running Cookiecutter again
paying attention to the parameters
you have provided.

If you are still having difficulty
generating your project as desired,
open an [RFS][request1]
and provide your `cookiecutter-config-file.yml`
if applicable.

Only open a Request for Correction
if you have clearly identified
an unexpected behaviour
with template generation
that needs to be addressed.
Otherwise,
if details are not clear,
prefer sticking to the Request for Support
as the means to reach the team.

#### Specific Guidelines for Requests for Improvement

Requests for Improvement are used
when users feel a need for development
related to features provided by Galactipy,
either existent
or yet-to-be-implemented.
Before opening an [RFI][request2],
take a moment to find out
whether your idea fits with the scope
and [aims][wts5] of the project.

If you are requesting
an entirely new feature
to be added to the Galactipy toolset,
please consider answering
the following prospective questions
to make your case stronger:

- Is the feature or service
  widely known,
  used
  and accepted?
- Could your desired feature
  be delivered by
  one of the tools
  already provided by Galactipy?
- Is this feature well documented
  to be studied by people
  unfamiliar with it
  to use?
- Is this feature
  easy to use
  once it is implemented?
- Does this feature require
  just additional files
  to be included
  in projects generated by Galactipy?
  Or does it require additional configuration,
  either in those files
  or external services?
  The less configuration needed
  for the feature to work
  on a generated project from the start
  the more chances it will have
  to be eventually added;
- How does this feature help
  speeding development and delivery
  of other projects besides yours?
- What is the level of maintenance
  that will be needed
  once this feature is integrated
  into Galactipy?

#### Specific Guidelines for Requests for Correction

Requests for Correction are used
to track unexpected behaviour
from template generation,
namely bugs.

A bug is a **demonstrable** problem
that is caused by
the code in the repository.

While the nature of errors
can be diverse
and thus challenging for users to report
with full context,
providing the information below
is much valuable
to accelerate the process:

- What is your environment?
  - What OS are you using?
  - How did you install Cookiecutter?
  - Which version of Galactipy are you using?
- What steps will reproduce the issue?
  - What are the parameters used
    during project generation?
    You can provide those
    through the `cookiecutter-config-file.yml`;
  - At which point specifically
    did your error occur
    during your journey?
    At project generation?
    Using one of the tools/services
    provided with Galactipy projects?
  - Did you address any `UPDATEME` tags
    that could be related
    to the tool/service in question?
    What did you do?
- Can you provide
  error logs or tracebacks
  to further detail the issue?
  Tools like [`reprexpy`][request3]
  can assist you
  in providing more technical detail
  if you are not able to;
- Do you have
  any visual evidence
  to share for further investigation?

These details
will help people
to fix any potential issues.

### Contributing by Reviewing Changes

>>> [!tip] :pushpin: Further Guidance
You can find more information
about reviewing changes
in our [main `CONTRIBUTING` guide][intro2],
take a look at it
whenever possible.
>>>

### Contributing with Documentation Changes

Currently,
the documentation surrounding Galactipy, including
features,
how to use,
options
and reference material
are found directly
in the project [`README`][wts1] file.

Since Galactipy is a Cookiecutter template,
there is no API being maintained
and thus there is no need
for a comprehensive and detailed documentation.
Galactipy's documentation encompasses the following topics:

- Features provided by Galactipy templates;
- Basic steps
  to get started
  with projects generated by Galactipy;
- A list of next actions to take
  for full project setup
  that require external services,
  using the following inline comments
  where appropriate:
  - `TODO` defines obligatory actions
    in order to make the user's project functional;
  - `UPDATEME` defines optional configuration
    the user might want to delve into,
    but are not necessary
    to make the project functional;
  - `DEFINE` is used
    to point users
    to sections where
    they must include
    their own content,
    such as policies
    and guidelines;
- Reference material
  for useful Python libraries,
  tips for project management
  and links to useful articles
  and guides for further reading.

You can propose changes and additions
to the documentation
by editing the `README` file
and [opening a Merge Request][wts6]
to integrate your changes to the project.

The current state of the "documentation"
stems from Galactipy's origins
as a fork of `python-package-template`.
&4+ is currently anticipated
to better structure relevant information
and reduce clutter on the `README` file.
We welcome any contributor
willing to help us
make this transition.

### Contributing to Roadmap Maintenance

>>> [!tip] :pushpin: Further Guidance
You can find more information
about roadmap maintenance
in our [main `CONTRIBUTING` guide][intro2],
take a look at it
whenever possible.
>>>

### Contributing by Promoting Galactipy

Promoting Galactipy
helps us reach a larger audience
and receive more feedback
to continuously improve the project,
your endorsement and recommendation
of our project
is of a **huge** value to us!
Thank you in advance for your interest
and use of Galactipy,
we are really proud of this project
and we couldn't keep advancing with it
without your support!

Here's how you can promote Galactipy:

- Set the [Notification level][promo1] to **"Watch"**
  on the [Galactipy organisation][promo2]
  and receive updates
  on most of our activity;
- Star the project
  on both [GitLab][dev1] and [GitHub][dev2];
- Use our [badge][promo3]
  on your projects
  generated with Galactipy;
- Share the project with your colleagues;
- Write a short article
  on how you are using Galactipy
  in your projects;
- Share your
  best practices
  and tools
  for project management
  with us,
  we love getting inspired
  to add new functionality
  and value to our template!

Thank you
for your interest
in Galactipy!
Your engagement
and contributions
reassure us that
what we are doing matters!
:beers:

[intro1]: https://cookiecutter.readthedocs.io/en/2.0.2/
[intro2]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md

[tldr1]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#book-our-philosophy
[tldr2]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#commit-customs
[tldr3]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#codestyle
[tldr4]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#general-practices

[setup1]: https://gitlab.com/galactipy/galactipy/-/forks/new
[setup2]: https://docs.gitlab.com/user/group/
[setup3]: https://python-poetry.org/docs/#installation
[setup4]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#development-workflow

[wts1]: https://gitlab.com/galactipy/galactipy/-/blob/master/README.md
[wts2]: https://gitlab.com/galactipy/galactipy/-/blob/master/hooks/pre_gen_project.py
[wts3]: https://gitlab.com/galactipy/galactipy/-/blob/master/hooks/post_gen_project.py
[wts4]: https://gitlab.com/galactipy/galactipy/-/tree/master/tests
[wts5]: https://gitlab.com/groups/galactipy/-/epics?state=opened&label_name%5B%5D=project%3A%3Agalactipy
[wts6]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#start-with-a-merge-request

[dev1]: https://gitlab.com/galactipy/galactipy
[dev2]: https://github.com/manoelpqueiroz/galactipy

[issue1]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#labels

[version1]: https://romversioning.github.io/romver/

[commit1]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
[commit2]: https://gitlab.com/galactipy/galactipy/-/blob/master/.gitlab/changelog_config.yml

[hooks1]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206
[hooks2]: #development-setup

[licence1]: https://gitlab.com/galactipy/galactipy/-/blob/master/LICENCE

[changes1]: https://gitlab.com/galactipy/galactipy/-/blob/master/tasks.py
[changes2]: https://www.pyinvoke.org/
[changes3]: #contributing-with-documentation-changes
[changes4]: https://gitlab.com/galactipy/galactipy/-/blob/master/tests/test_template.py#L1
[changes5]: https://jinja.palletsprojects.com/en/stable/templates/#whitespace-control

[request1]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Support
[request2]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Improvement
[request3]: https://reprexpy.readthedocs.io/en/latest/

[promo1]: https://docs.gitlab.com/user/profile/notifications/#notification-levels
[promo2]: https://gitlab.com/groups/galactipy
[promo3]: https://gitlab.com/galactipy/galactipy#page_with_curl-citation
