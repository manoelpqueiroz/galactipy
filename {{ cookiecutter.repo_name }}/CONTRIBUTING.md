{% set roadmap_mapping = {
  'GitLab Premium/Ultimate': 'epic',
  'GitLab Free': 'milestone',
  'GitHub': 'project'
} -%}
{% set licence_mapping = {
  'MIT': 'MIT Licence',
  'BSD-3-Clause': '3-Clause BSD',
  'GPL-3.0-or-later': 'GNU GPL v3.0',
  'AGPL-3.0-or-later': 'GNU AGPL v3.0',
  'LGPL-3.0-or-later': 'GNU LGPL v3.0',
  'MPL-2.0': 'Mozilla Public License 2.0',
  'Apache-2.0': 'Apache Software License 2.0',
  'nos': 'Non-OSS'
} -%}
{% set docstring_mapping = {
  'numpy': 'numpydoc',
  'google': 'Google Python Style',
  'sphinx': 'Sphinx Style',
  'other': 'custom'
} -%}
{% set roadmap_item = roadmap_mapping[cookiecutter.scm_platform] -%}
{% set licence_name = licence_mapping[cookiecutter.licence] -%}
{% set docstring_name = docstring_mapping[cookiecutter.docstring_style] -%}
{% set roadmap_item_undefined = 'an' ~ roadmap_item if roadmap_item == 'epic' else 'a' ~ roadmap_item -%}
{% set task_item = 'task' if cookiecutter.__scm_platform_lc == 'gitlab' else 'sub-issue' -%}
# How to Contribute

{{ cookiecutter.project_description }}.

We would like to encourage you
to contribute to this project
and we strive to make it
as easy as possible.
This guide is aimed at
facilitating onboarding
for new collaborators
and serving as the single source of truth
for the project's rules
and modus operandi.

Contributions to {{ cookiecutter.project_name }} include
file manipulation code,
tests,
tool configuration and updates,
development automation
via CI/CD,
answering user questions,
as well as
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
managing the backlog of [issues][intro1]
and [{{ cookiecutter.__mr_term }}s][intro2]
through open discussions.
{%- else %}
managing the backlog of [issues][intro1],
[{{ cookiecutter.__mr_term }}s][intro2]
and [open discussions][intro3].
{%- endif %}

{% if cookiecutter.licence != 'nos' -%}
We welcome all contributors
willing to work in good faith
with other contributors
and the community.
No contribution is too small
and all contributions are valued.

Whether you intend
to become a [developer][proposals]
for {{ cookiecutter.project_name }}
{%- if cookiecutter.app_type != 'bare_repo' %}
or you are a [user][contributions] of the application,
{%- else %}
or you are a [user][contributions] of the library,
{%- endif %}
following these guidelines
helps to communicate
that you respect the time
of the developers
managing and developing
this open source project.
In return,
they should reciprocate
that respect
in addressing your issue
or assessing patches and features.

{% endif -%}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[[_TOC_]]

{% endif -%}
## :runner: TL;DR

Preconditions for
contributing as a developer:

- Creating {{ cookiecutter.__mr_term }}s
  requires a {{ cookiecutter.__scm_platform_base }} account;
- {{ cookiecutter.__mr_term }}s should
  adhere to the [{{ cookiecutter.project_name }} Philosophy][philosophy];
{%- if cookiecutter.use_bdd %}
- Follow [Behaviour-Driven Development][bdd]
  principles during contributions;
{%- endif %}
- Commits should
  adhere to our [commit customs][committing];
- The project's [codestyle][codestyle] should
  be followed strictly;
- Work item management should
  be done following [our specific practices][practices].

### Development Setup

To start contributing to {{ cookiecutter.project_name }},
you should start
by [forking][setup1] the upstream repository
to your own {{ cookiecutter.__scm_platform_base }} [group][setup2].
We manage contributions
{%- if cookiecutter.licence != 'nos' %}
from the community
{%- endif %}
through the [fork][setup3] system,
which helps us
monitor and appreciate continuous input
from individuals and organisations.
{%- if cookiecutter.licence != 'nos' %}
Contributors who can
demonstrate their competence
in further developing {{ cookiecutter.project_name }}
may be [promoted][promotion]
to upstream Developers or Maintainers.
{%- endif %}

After forking the upstream repository,
cloning it to your local environment
and accessing the root dir
via your IDE or the terminal:

1. Make sure
   you have Poetry [installed][setup4];
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
for a [first contribution][workflow].

## :shrug: Not Sure Where to Start?

If you don't feel
ready to start contributing,
the following steps
should help:

- The project [`README`][readme] details
  how to use {{ cookiecutter.project_name }},
  provides a high-level overview
  of its features;
- To effectively contribute to {{ cookiecutter.project_name }},
  you should probably get knowledgeable
  about a few topics:
{%- if cookiecutter.app_type != 'bare_repo' %}
{%- if cookiecutter.app_type != 'cli' %}
  - Understand how [Typer][apptopic1] and [Textual][apptopic1a] work
    under the hood
    and how they interact
    with each other
    to enable a TUI application
    on the command-line;
{%- else %}
  - Understand how [Typer][apptopic1] works
    under the hood
    to create CLI applications;
{%- endif %}
  - Study [Orbittings][apptopic2] and
    its upstream library, [Dynaconf][apptopic3],
    which manage the configuration files
    for {{ cookiecutter.project_name }};
  - Do the same with [Nebulog][apptopic4] and [Loguru][apptopic5],
    which empower the logging functionality
    of the application;
{%- if cookiecutter.use_bdd %}
  - Check the [`features/`][apptopic5a] directory,
    containing the files
    describing the functional behaviour of {{ cookiecutter.project_name }}
    with the BDD paradigm;
  - The [`tests/`][apptopic6] directory
    contains all unit tests
    validating the scenarios
    described in `features/`;
{%- else %}
  - Check the [`tests/`][apptopic6] directory,
    which validate all code
    for the application;
{%- endif %}
{%- else %}
<!-- DEFINE the basic dependencies your project contributors should be familiar with -->
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  - Review the [`.gitlab-ci.yml`][topic1] file
    containing {{ cookiecutter.project_name }}'s [CI jobs][cicd],
    which outlines
    the steps
    for automating project development;
{%- else %}
  - Review the [`workflows/`][topic1] directory
    containing {{ cookiecutter.project_name }}'s [GitHub Actions][cicd]
    defined for the project;
{%- endif %}
- Take a look at
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
  the organisation's [{{ roadmap_item.capitalize() }}s][topic2] page
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
  the project's [{{ roadmap_item.capitalize() }}s][topic2] page
{%- else %}
  our [{{ roadmap_item.capitalize() }}s][topic2] page
{%- endif %}
  to get familiar
  with the team's plans
  for future releases;
- When you feel ready
  to jump into {{ cookiecutter.project_name }} development,
  a good place to start
  is to look for issues
{%- if cookiecutter.__scm_platform_lc == 'github' %}
  and discussions
{%- endif %}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
  labelled with [`seeking-contributors`][query6]
{%- else %}
  labelled with [`seeking-builders`][query6]
{%- endif %}
  or [`starter-assignment`][query5];
- After familiarising yourself
  with the project's [labels][topic3] and [stages][tracking],
  you can contribute
  by participating in discussions on issues
  at any of the **Needs** statuses,
{% if cookiecutter.licence != 'nos' -%}
  especially those in the [**Needs Triage**][query3] stage;
  we are always looking for people
  who help refine issues,
  spot duplicates,
  guide issue authors toward better clarification
  and promote project activity
  through constructive discussions.

If the steps above seem daunting,
we can relate!
Contributing to an open source project,
whether you are a seasoned developer
or perhaps a newcomer
aiming to improve your software skills,
[can be scary][topic4]
due to a plethora of reasons.
As maintainers,
we are committed
to building an environment
where every new contributor can thrive,
improve their skills
and feel recognised
for their contributions.

Should you still feel lost
at how to start,
these tips might
make you more comfortable
with your first steps here:

- **Join the community:**
  each open source project operates
  on different principles
  and practices.
  Coming for the first time
  is sometimes frightening
  as you might not be
  familiar with our ways.
  We approach our development
  as a continuous [debate][swmr],
  and we are always open
  to discussing
  with different minds
  in a constructive way.
  You can reach out to us
  in our [{{ cookiecutter.__mr_term }}s][intro2]
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  and [Issue Tracker][intro1]
{%- else %}
  and [Discussions Page][intro3]
{%- endif %}
  and comment on current developments
  with questions,
  doubts
  and suggestions.
  If still unsure,
  reach us by [e-mail][topic5]
  to introduce yourself,
  we will help you
  with further orientation;
- **Lurk first:**
  there is no need
  to rush things in open source,
  take your time
  by simply observing repo activity
  (you can set the option
  to [watch][topic6] the repository),
  reading the archives
  and documentation
  to soak up the culture
  before contributing.
  The more time
  you spend reading
  and listening,
  the more likely it is
  that your contribution
  will be well received;
- **Understand the governance:**
  read the documentation
  before contributing.
  By doing so
  you will know
  how we make decisions
  and how these decisions are made
  for each type of contribution.
  _Reading documentation isn't optional_
  when contributing to open source;
- **Start small:**
  as mentioned above,
  tackle simple bug
  or documentation fixes
  to start.
  It will be easier
  to learn the process
  and correct mistakes
  on a small contribution
  that isn't critical
  to the project.
  Make your mistakes
  on small and less significant contributions
  as you work up
  to the more complex contributions
  that {{ cookiecutter.project_name }} needs.
  Check [starter assignment][query5] issues,
  or [find your own][gfi]
  that deserves your time and effort.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!tip]
Having all that said,
aside from actions
and tasks
you can take
to feel more comfortable contributing,
we believe
there are three fundamental _behaviours_
that, if followed,
will help you become
an even more robust contributor:

1. **Communication makes all the difference:**
   open source projects often
   have contributors
   from all over the world,
   so clear communication
   is key.
   It's completely okay
   to ask questions
   when you're stuck
   and being clear
   when submitting a {{ cookiecutter.__mr_term }}
   helps everyone involved.
   Jumping into discussions
   don't just improve your contributions;
   it also helps you
   learn much more
   from those with more experience
   and improve
   your problem-solving skills;
2. **Patience is part of the process:**
   waiting for feedback on {{ cookiecutter.__mr_term }}s,
   learning new tools
   and figuring things out
   all take time.
   There might be times
   where frustration kicks in
   and everything feels like
   taking you nowhere,
   but if you stick to the process
   and leverage collaboration
   with other contributors
   you will thrive.
   _Contributing to open source is a marathon, not a sprint_;
3. **The learning never stops:**
   contributing to open source
   is a rewarding experience,
   it will push you
   to learn new things,
   show you different perspectives
   and help you
   become a better communicator.
   And there's always
   more to learn,
   getting a chance to grow
   with every issue,
   every interaction
   and every feedback.
>>>
{%- else -%}
> [!TIP]
> Having all that said,
> aside from actions
> and tasks
> you can take
> to feel more comfortable contributing,
> we believe
> there are three fundamental _behaviours_
> that, if followed,
> will help you become
> an even more robust contributor:
>
> 1. **Communication makes all the difference:**
>    open source projects often
>    have contributors
>    from all over the world,
>    so clear communication
>    is key.
>    It's completely okay
>    to ask questions
>    when you're stuck
>    and being clear
>    when submitting a {{ cookiecutter.__mr_term }}
>    helps everyone involved.
>    Jumping into discussions
>    don't just improve your contributions;
>    it also helps you
>    learn much more
>    from those with more experience
>    and improve
>    your problem-solving skills;
> 2. **Patience is part of the process:**
>    waiting for feedback on {{ cookiecutter.__mr_term }}s,
>    learning new tools
>    and figuring things out
>    all take time.
>    There might be times
>    where frustration kicks in
>    and everything feels like
>    taking you nowhere,
>    but if you stick to the process
>    and leverage collaboration
>    with other contributors
>    you will thrive.
>    _Contributing to open source is a marathon, not a sprint_;
> 3. **The learning never stops:**
>    contributing to open source
>    is a rewarding experience,
>    it will push you
>    to learn new things,
>    show you different perspectives
>    and help you
>    become a better communicator.
>    And there's always
>    more to learn,
>    getting a chance to grow
>    with every issue,
>    every interaction
>    and every feedback.
{%- endif %}
{%- else %}
  especially those in the [**Needs Triage**][query3] stage.
{%- endif %}

## :classical_building: Fundamental Policies

### Code of Conduct

{{ cookiecutter.project_name }} has adopted the [Contributor Covenant][cc1]
as its Code of Conduct,
and we expect project participants
to adhere to it.
Please read the [full document][cc2]
to understand
how to properly communicate
with others
and know which actions
will and will not be tolerated.

### {% if cookiecutter.licence != 'nos' %}Open {% endif %}Development

All work on {{ cookiecutter.project_name }} happens
directly on [{{ cookiecutter.__scm_platform_base }}][development1],
including roadmap
and [{{ roadmap_item }}s][topic2].
Therefore,
a {{ cookiecutter.__scm_platform_base }} account is needed
to start contributing.

{% if cookiecutter.licence != 'nos' -%}
#### Contributor Promotion

Access to the upstream repository is granted
at the project owner's discretion,
with no current structured process
to evaluate and promote fork contributors.
However,
we are open
to assign roles
to the upstream {{ cookiecutter.project_name }} repository
to open source developers.
A non-exhaustive list of prerequisites
can be found below:

- Contributors will be evaluated
  by their influence on the project
  through quality,
  quantity
  and consistency
  of their changes;
- Getting owner buy-in
  through open communication
  on relevant topics for the project
  is valuable,
  whether in issue and {{ cookiecutter.__mr_acronym }} discussions
  or directly
  through [e-mail][topic5] contact;
- Follow the formal proposal process
  and be an advocate of our guidelines,
  not only safeguarding
  its integrity,
  but also pushing
  for improvements
  where deemed necessary;
- Do the work
  by effectively delivering
  the changes proposed
  for the project,
  ensuring its quality and testing
  before merging
  to the `master` branch;
- Do the **other** work, by:
  - [Showing responsibility][bias] to document
    all relevant information
    promptly,
    whether for
    internal or external use,
    to ensure maintenance
    of our [institutional knowledge][knowledge];
  - Upkeeping repository order
    through our [practices][practices];
  - Being an exemplar advocate
    for a [welcoming community][community];
- Aside from
  displaying the aforementioned conduct,
  the contributor must express
  their actual interest
  in attaining a [role][development2]
  in the upstream repository.

We also recommend interested individuals
to follow
the guide to the [_Pragmatic Open Source Contributor_][development3],
which goes
into the attitude
for candidate contributors
in more detail.

{% endif -%}
#### Roadmap Management

Medium and long-term vision for {{ cookiecutter.project_name }}
is managed through the project's roadmap,
where the general direction of development
is stored and accessible
for anyone to see and comment.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
Issues and {{ cookiecutter.__mr_term }}s should ideally
{%- else %}
Issues,
discussions
and {{ cookiecutter.__mr_term }}s
should ideally
{%- endif %}
be related to {{ roadmap_item_undefined }}
once a work item has been created.

Any contributor can propose a new distinct deliverable
to be added to the roadmap.
A [{{ cookiecutter.__mr_term }}][swmr] containing the proposal
must be opened with the [**Project Policies** template][roadmap1],
detailing nature, scope and purpose of the {{ roadmap_item }}.

The {{ cookiecutter.__mr_acronym }} must detail the proposed {{ roadmap_item }}
added to the [`ROADMAP.md` table][roadmap2]
for discussion,
containing:

- **Title:**
  the proposed title for the {{ roadmap_item }};
- **Description:**
  an overview of the development,
  in a short summary.
  Details regarding the {{ roadmap_item }}
  will be discussed in the {{ cookiecutter.__mr_acronym }} and
  later be included in the official project {{ roadmap_item }}
  if accepted;
- **Theme:**
  the theme to which
  the proposed {{ roadmap_item }} is best related to.
  The naming is open to discussion and
  the author is free to suggest it,
  along with an Emoji to
  better convey its nature,
  in a `:emoji: Theme Title` pattern;
- **Timeline:**
  a broad estimation of when this proposed {{ roadmap_item }}
  can be delivered in full.
  Should act as a starting point for
  the actual work tracking
  to be done via
  the official {{ roadmap_item }}.

Contributors and maintainers will participate in the discussion to
[refine][swnjw] the scope of the {{ roadmap_item }} and
either accept of reject the proposal via [thumbs-up/thumbs-down][roadmap3] reactions
on the author's initial comment.

Once {{ roadmap_item_undefined }} has been accepted for inclusion in the roadmap,
it will be officially created in the [{{ roadmap_item.capitalize() }}s][topic2] page.
The {{ roadmap_item }} itself should contain:

- The [Motivational Narrative][roadmap4] as a summary to the {{ roadmap_item }}'s goal;
  - We suggest using the following pattern if the actor of the deliverable is not clear:
    `**In order to** {GOAL},<br>**The project will** {ACTION}.`;
- Detailed information collected from the discussion
  regarding nature and scope,
  under the **Reasoning** section;
- A non-exhaustive list of leading developments
  that have been discussed in the {{ cookiecutter.__mr_acronym }}
  in the **Anticipated Developments** section;
- Details on potential bottleneck mappings
  in the **Caveats** section.

Once the official {{ roadmap_item }} is created,
it should be attached to the proposal {{ cookiecutter.__mr_acronym }} and
the `ROADMAP.md` table should be updated
with the actual link to the {{ roadmap_item }}
before merging to `master`.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!tip]
{{ roadmap_item.capitalize() }}s should be the entry door for new contributors
to have a general glimpse on
what the project has been prioritising and
where it wants to go,
helping newcomers get onboarded more quickly.
Therefore, contributors writing official {{ roadmap_item }}s
should approach the task with the following goals in mind:

- [_Comprehensive, yet succinct_][roadmap5];
- [_Standardised, yet conscious_][roadmap6].
>>>
{%- else -%}
> [!TIP]
> {{ roadmap_item.capitalize() }}s should be the entry door for new contributors
> to have a general glimpse on
> what the project has been prioritising and
> where it wants to go,
> helping newcomers get onboarded more quickly.
> Therefore, contributors writing official {{ roadmap_item }}s
> should approach the task with the following goals in mind:
>
> - [_Comprehensive, yet succinct_][roadmap5];
> - [_Standardised, yet conscious_][roadmap6].
{%- endif %}

After {{ roadmap_item_undefined }} has been completed,
a new {{ cookiecutter.__mr_term }} should be opened to
update the `ROADMAP.md` table in the **Timeline** field
with the following possible values:

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
- `**Delivered with <version> :airplane_departure:**`,
{% else -%}
- `**Delivered with <version> :flight_departure:**`,
{%- endif %}
  if properly associated to a [{{ cookiecutter.__scm_platform_base }} Release][roadmap7];
- `**Delivered Internally :100:**`,
  if the {{ roadmap_item }} has no impact on project releases.

Likewise,
the {{ cookiecutter.__mr_acronym }}s should be associated with
the completed {{ roadmap_item }}.

#### Work Item Tracking

[![Issues][badge1]][query1]
{%- if cookiecutter.scm_platform == 'GitLab Free' %}
[![Tasks][badge1a]][query1a]
{%- endif %}

[![Needs Contributors][badge2]][query2]
[![Needs Triage][badge3]][query3]
[![Designs][badge4]][query4]

[![Starter Assignments][badge5]][query5]
[![Needs Delivery][badge6]][query6]
[![Quick Wins][badge7]][query7]

[![Stale Issues][badge8]][query8]

[![RFCs][badge9]][query9]
[![RFIs][badge10]][query10]
[![RFSs][badge11]][query11]

{{ cookiecutter.project_name }} development is iterative
and structured preferably around [{{ cookiecutter.__mr_term }}s][swmr].
Whenever project advancements are not immediately deliverable,
progress is tracked through {{ cookiecutter.__scm_platform_base }} Issues
and {{ task_item.capitalize() }}s.
Use cases for this type of work item include:

- User requests
  (since general users are not allowed to create {{ cookiecutter.__mr_acronym }}s);
- Larger scoped developments
  which are unable to be delivered
  in a single {{ cookiecutter.__mr_acronym }};
- Ideas for future developments
  which can't be prioritised
  due to scope or team capacity.

##### Labels

{{ cookiecutter.project_name }} defines
the following labels
to mark
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
issues
{%- else %}
issues,
discussions
{%- endif %}
and {{ cookiecutter.__mr_term }}s,
contributors should be familiar
with their usage:

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
|               Label               | Usage                                                                                                             |
| :-------------------------------: | ----------------------------------------------------------------------------------------------------------------- |
|       ~"backend::external"        | Changes to modules interacting directly with external APIs.                                                       |
|      ~"backend::components"       | Changes to internal modules and utils.                                                                            |
|       ~"backend::database"        | Changes to database schema and operations.                                                                        |
|     ~"blocked-by-dependency"      | Resolution requires development on upstream dependency.                                                           |
|           ~"ci::build"            | Improves the project's deployment reliability through automated validation.                                       |
{%- if cookiecutter.create_docker %}
|           ~"ci::docker"           | Changes how {{ cookiecutter.project_name }} containers are built and provided to users.                           |
{%- endif %}
|           ~"ci::tasks"            | Structures automated tasks of different functions to run on scheduled pipelines.                                  |
{%- if cookiecutter.app_type != 'bare_repo' %}
|           ~"cli::arch"            | Changes to logic in the layer directly below the CLI, including input validation and file parsing.                |
|         ~"cli::commands"          | Changes to the CLI command structure and capabilities, including the addition of new commands.                    |
|       ~"cli::deprecations"        | Marks deprecations for future removal to CLI features.                                                            |
|          ~"cli::options"          | Changes to available options and option flag behaviour for CLI users.                                             |
|         ~"cli::removals"          | CLI feature sunsetting.                                                                                           |
{%- else %}
|          ~"deprecations"          | Marks deprecations for future removal.                                                                            |
{%- endif %}
|       ~"design::discovery"        | Debates high-level concepts for new {{ cookiecutter.project_name }} features.                                     |
|      ~"design::formulation"       | Specifies expected behaviour for {{ cookiecutter.project_name }} features under different possible circumstances. |
|      ~"design::reassessment"      | Reevaluates a previous design that did not consider all possible cases.                                           |
|         ~"docs::nudging"          | Updates formal documentation with tips and tricks for better {{ cookiecutter.project_name }} usage.               |
|          ~"docs::guides"          | Updates formal documentation with structured user guides.                                                         |
|        ~"docs::technical"         | Updates formal documentation with API reference or development guides.                                            |
|    ~"internals::configuration"    | Regulates current development toolset behaviour.                                                                  |
|  ~"internals::developer-output"   | Boosts team productivity with incremental automation and simplification.                                          |
|       ~"internals::invoke"        | Streamlines local development operations.                                                                         |
|          ~"localization"          | Updates translation files for other languages.                                                                    |
|   ~"maintenance::configuration"   | Updates current development toolset syntax and options.                                                           |
|   ~"maintenance::dependencies"    | Upgrades project dependencies.                                                                                    |
|        ~"maintenance::bot"        | Work items managed automatically by a project GitLab Bot.                                                         |
|     ~"maintenance::knowledge"     | Updates already existing information for knowledge retention and sharing.                                         |
|   ~"maintenance::test-coverage"   | Changes being enforced due to software regression.                                                                |
|      ~"maintenance::toolset"      | Updates or replaces current development tools functionality.                                                      |
|          ~"manual-check"          | Requires manual validation to certain or all acceptance criteria.                                                 |
|         ~"manual-closure"         | Items that should not be closed through commit closing patterns.                                                  |
|            ~"plugins"             | Updates logic to enable third-party extensions based on the core {{ cookiecutter.project_name }} implementation.  |
|          ~"policies::ci"          | Changes to rules triggering CI jobs.                                                                              |
|      ~"policies::guidelines"      | Changes to project guidelines in `CONTRIBUTING.md` or the formal documentation.                                   |
|       ~"policies::roadmap"        | Work items related to debates and proposals relating to the project roadmap.                                      |
|        ~"policies::rules"         | Changes to rules for development tools (e.g., Ruff/mypy rules, issue triaging etc.).                              |
|      ~"policies::templates"       | Changes to issue and {{ cookiecutter.__mr_term }} templates.                                                      |
|           ~"quick-win"            | Development requires low effort.                                                                                  |
|          ~"refactoring"           | Restructures existing source code without changing its functionality.                                             |
{%- if cookiecutter.app_type == 'bare_repo' %}
|            ~"removals"            | Feature sunsetting.                                                                                               |
{%- endif %}
|      ~"request::correction"       | For work items for when something is not working properly.                                                        |
|      ~"request::improvement"      | For work items containing suggestions for new features from the community.                                        |
|        ~"request::support"        | For issues opened by users seeking advice regarding {{ cookiecutter.project_name }}.                              |
| ~"seeking-contributors::delivery" | Proposal is polished and can be picked up if you feel inclined to.                                                |
| ~"seeking-contributors::opinion"  | In need of help to further discuss and define scope.                                                              |
|             ~"stale"              | Work items without activity that are marked for closing.                                                          |
| ~"starter-assignment::quick-win"  | Development requires low effort and is ideal for first-time contributors.                                         |
| ~"starter-assignment::supervised" | Proposal and delivery steps are clear and can be picked up by first-time contributors.                            |
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
|       ~"ui::accessibility"        | Promotes accessibility options for users in the interface.                                                        |
|            ~"ui::arch"            | Changes to rendering logic in the layer directly below the user interface.                                        |
|        ~"ui::deprecations"        | Marks deprecations for future removal to UI features.                                                             |
|          ~"ui::features"          | Introduces new functions and capabilities to the user interface.                                                  |
|           ~"ui::layout"           | Changes the disposition of elements and text in the user interface.                                               |
|          ~"ui::removals"          | User interface feature sunsetting.                                                                                |
{%- endif %}
|        ~"up-for-a-change"         | Author-based label to express interest in delivering their own request.                                           |
|          ~"ux::advanced"          | Updates features available to power users of {{ cookiecutter.project_name }}.                                     |
|       ~"ux::customization"        | Improves options available for program customisation by users.                                                    |
|           ~"ux::flags"            | Implements feature flags for {{ cookiecutter.project_name }}.                                                     |
|         ~"ux::migration"          | Offers predefined migration options to users in the case of breaking changes.                                     |
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
|         ~"ux::navigation"         | Improves user navigation in the user interface.                                                                   |
{%- endif %}
|          ~"ux::nudging"           | Helps users understand the application with more ease, like help panels, notifications etc.                       |

{% elif cookiecutter.scm_platform == 'GitLab Free' -%}
| Development Domain  |             Label             | Usage                                                                                                             |
| :-----------------: | :---------------------------: | ----------------------------------------------------------------------------------------------------------------- |
|      Back-End       |      ~"backend-external"      | Changes to modules interacting directly with external APIs.                                                       |
|      Back-End       |     ~"backend-components"     | Changes to internal modules and utils.                                                                            |
|      Back-End       |      ~"backend-database"      | Changes to database schema and operations.                                                                        |
|         N/A         |   ~"blocked-by-dependency"    | Resolution requires development on upstream dependency.                                                           |
|         CI          |          ~"ci-build"          | Improves the project's deployment reliability through automated validation.                                       |
{%- if cookiecutter.create_docker %}
|         CI          |         ~"ci-docker"          | Changes how {{ cookiecutter.project_name }} containers are built and provided to users.                           |
{%- endif %}
|         CI          |          ~"ci-tasks"          | Structures automated tasks of different functions to run on scheduled pipelines.                                  |
{%- if cookiecutter.app_type != 'bare_repo' %}
|         CLI         |          ~"cli-arch"          | Changes to logic in the layer directly below the CLI, including input validation and file parsing.                |
|         CLI         |        ~"cli-commands"        | Changes to the CLI command structure and capabilities, including the addition of new commands.                    |
|         CLI         |      ~"cli-deprecations"      | Marks deprecations for future removal to CLI features.                                                            |
|         CLI         |        ~"cli-options"         | Changes to available options and option flag behaviour for CLI users.                                             |
|         CLI         |        ~"cli-removals"        | CLI feature sunsetting.                                                                                           |
{%- else %}
|         N/A         |        ~"deprecations"        | Marks deprecations for future removal. sunsetting.                                                                |
{%- endif %}
|       Design        |      ~"design-discovery"      | Debates high-level concepts for new {{ cookiecutter.project_name }} features.                                     |
|       Design        |     ~"design-formulation"     | Specifies expected behaviour for {{ cookiecutter.project_name }} features under different possible circumstances. |
|       Design        |    ~"design-reassessment"     | Reevaluates a previous design that did not consider all possible cases.                                           |
|    Documentation    |        ~"docs-nudging"        | Updates formal documentation with tips and tricks for better {{ cookiecutter.project_name }} usage.               |
|    Documentation    |        ~"docs-guides"         | Updates formal documentation with structured user guides.                                                         |
|    Documentation    |       ~"docs-technical"       | Updates formal documentation with API reference or development guides.                                            |
| Internal Operations |  ~"internals-configuration"   | Regulates current development toolset behaviour.                                                                  |
| Internal Operations | ~"internals-developer-output" | Boosts team productivity with incremental automation and simplification.                                          |
| Internal Operations |      ~"internals-invoke"      | Streamlines local development operations.                                                                         |
|         N/A         |        ~"localization"        | Updates translation files for other languages.                                                                    |
|     Maintenance     | ~"maintenance-configuration"  | Updates current development toolset syntax and options.                                                           |
|     Maintenance     |  ~"maintenance-dependencies"  | Upgrades project dependencies.                                                                                    |
|     Maintenance     |      ~"maintenance-bot"       | Work items managed automatically by a project GitLab Bot.                                                         |
|     Maintenance     |   ~"maintenance-knowledge"    | Updates already existing information for knowledge retention and sharing.                                         |
|     Maintenance     | ~"maintenance-test-coverage"  | Changes being enforced due to software regression.                                                                |
|     Maintenance     |    ~"maintenance-toolset"     | Updates or replaces current development tools functionality.                                                      |
|         N/A         |        ~"manual-check"        | Requires manual validation to certain or all acceptance criteria.                                                 |
|         N/A         |       ~"manual-closure"       | Items that should not be closed through commit closing patterns.                                                  |
|         N/A         |          ~"plugins"           | Updates logic to enable third-party extensions based on the core {{ cookiecutter.project_name }} implementation.  |
|      Policies       |        ~"policies-ci"         | Changes to rules triggering CI jobs.                                                                              |
|      Policies       |    ~"policies-guidelines"     | Changes to project guidelines in `CONTRIBUTING.md` or the formal documentation.                                   |
|      Policies       |      ~"policies-roadmap"      | Work items related to debates and proposals relating to the project roadmap.                                      |
|      Policies       |       ~"policies-rules"       | Changes to rules for development tools (e.g., Ruff/mypy rules, issue triaging etc.).                              |
|      Policies       |     ~"policies-templates"     | Changes to issue and {{ cookiecutter.__mr_term }} templates.                                                      |
|         N/A         |         ~"quick-win"          | Development requires low effort.                                                                                  |
|         N/A         |        ~"refactoring"         | Restructures existing source code without changing its functionality.                                             |
{%- if cookiecutter.app_type == 'bare_repo' %}
|         N/A         |          ~"removals"          | Feature sunsetting.                                                                                               |
{%- endif %}
|    User Requests    |            ~"rfc"             | For work items for when something is not working properly.                                                        |
|    User Requests    |            ~"rfi"             | For work items containing suggestions for new features from the community.                                        |
|    User Requests    |            ~"rfs"             | For issues opened by users seeking advice regarding {{ cookiecutter.project_name }}.                              |
|         N/A         |    ~"seeking-contributors"    | Umbrella label to mark work items requiring contributor involvement.                                              |
|         N/A         |      ~"seeking-builders"      | Proposal is polished and can be picked up if you feel inclined to.                                                |
|         N/A         |       ~"seeking-input"        | In need of help to further discuss and define scope.                                                              |
|         N/A         |           ~"stale"            | Work items without activity that are marked for closing.                                                          |
|         N/A         |     ~"starter-assignment"     | Proposal and delivery steps are clear and can be picked up by first-time contributors.                            |
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
|   User Interface    |      ~"ui-accessibility"      | Promotes accessibility options for users in the interface.                                                        |
|   User Interface    |          ~"ui-arch"           | Changes to rendering logic in the layer directly below the user interface.                                        |
|   User Interface    |      ~"ui-deprecations"       | Marks deprecations for future removal to UI features.                                                             |
|   User Interface    |        ~"ui-features"         | Introduces new functions and capabilities to the user interface.                                                  |
|   User Interface    |         ~"ui-layout"          | Changes the disposition of elements and text in the user interface.                                               |
|   User Interface    |        ~"ui-removals"         | User interface feature sunsetting.                                                                                |
{%- endif %}
|         N/A         |      ~"up-for-a-change"       | Author-based label to express interest in delivering their own request.                                           |
|   User Experience   |        ~"ux-advanced"         | Updates features available to power users of {{ cookiecutter.project_name }}.                                     |
|   User Experience   |      ~"ux-customization"      | Improves options available for program customisation by users.                                                    |
|   User Experience   |          ~"ux-flags"          | Implements feature flags for {{ cookiecutter.project_name }}.                                                     |
|   User Experience   |        ~"ux-migration"        | Offers predefined migration options to users in the case of breaking changes.                                     |
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
|   User Experience   |       ~"ux-navigation"        | Improves user navigation in the user interface.                                                                   |
{%- endif %}
|   User Experience   |         ~"ux-nudging"         | Helps users understand the application with more ease, like help panels, notifications etc.                       |

{% else -%}
| Development Domain  |            Label             | Usage                                                                                                             |
| :-----------------: | :--------------------------: | ----------------------------------------------------------------------------------------------------------------- |
|      Back-End       |      `backend-external`      | Changes to modules interacting directly with external APIs.                                                       |
|      Back-End       |     `backend-components`     | Changes to internal modules and utils.                                                                            |
|      Back-End       |      `backend-database`      | Changes to database schema and operations.                                                                        |
|         N/A         |   `blocked-by-dependency`    | Resolution requires development on upstream dependency.                                                           |
|         CI          |          `ci-build`          | Improves the project's deployment reliability through automated validation.                                       |
{%- if cookiecutter.create_docker %}
|         CI          |         `ci-docker`          | Changes how {{ cookiecutter.project_name }} containers are built and provided to users.                           |
{%- endif %}
|         CI          |          `ci-tasks`          | Structures automated tasks of different functions to run on scheduled pipelines.                                  |
{%- if cookiecutter.app_type != 'bare_repo' %}
|         CLI         |          `cli-arch`          | Changes to logic in the layer directly below the CLI, including input validation and file parsing.                |
|         CLI         |        `cli-commands`        | Changes to the CLI command structure and capabilities, including the addition of new commands.                    |
|         CLI         |      `cli-deprecations`      | Marks deprecations for future removal to CLI features.                                                            |
|         CLI         |        `cli-options`         | Changes to available options and option flag behaviour for CLI users.                                             |
|         CLI         |        `cli-removals`        | CLI feature sunsetting.                                                                                           |
{%- else %}
|         N/A         |        `deprecations`        | Marks deprecations for future removal.                                                                            |
{%- endif %}
|       Design        |      `design-discovery`      | Debates high-level concepts for new {{ cookiecutter.project_name }} features.                                     |
|       Design        |     `design-formulation`     | Specifies expected behaviour for {{ cookiecutter.project_name }} features under different possible circumstances. |
|       Design        |    `design-reassessment`     | Reevaluates a previous design that did not consider all possible cases.                                           |
|    Documentation    |        `docs-nudging`        | Updates formal documentation with tips and tricks for better {{ cookiecutter.project_name }} usage.               |
|    Documentation    |        `docs-guides`         | Updates formal documentation with structured user guides.                                                         |
|    Documentation    |       `docs-technical`       | Updates formal documentation with API reference or development guides.                                            |
| Internal Operations |  `internals-configuration`   | Regulates current development toolset behaviour.                                                                  |
| Internal Operations | `internals-developer-output` | Boosts team productivity with incremental automation and simplification.                                          |
| Internal Operations |      `internals-invoke`      | Streamlines local development operations.                                                                         |
|         N/A         |        `localization`        | Updates translation files for other languages.                                                                    |
|     Maintenance     | `maintenance-configuration`  | Updates current development toolset syntax and options.                                                           |
|     Maintenance     |  `maintenance-dependencies`  | Upgrades project dependencies.                                                                                    |
|     Maintenance     |      `maintenance-bot`       | Work items managed automatically by a project GitLab Bot.                                                         |
|     Maintenance     |   `maintenance-knowledge`    | Updates already existing information for knowledge retention and sharing.                                         |
|     Maintenance     | `maintenance-test-coverage`  | Changes being enforced due to software regression.                                                                |
|     Maintenance     |    `maintenance-toolset`     | Updates or replaces current development tools functionality.                                                      |
|         N/A         |        `manual-check`        | Requires manual validation to certain or all acceptance criteria.                                                 |
|         N/A         |       `manual-closure`       | Items that should not be closed through commit closing patterns.                                                  |
|         N/A         |          `plugins`           | Updates logic to enable third-party extensions based on the core {{ cookiecutter.project_name }} implementation.  |
|      Policies       |        `policies-ci`         | Changes to rules triggering CI jobs.                                                                              |
|      Policies       |    `policies-guidelines`     | Changes to project guidelines in `CONTRIBUTING.md` or the formal documentation.                                   |
|      Policies       |      `policies-roadmap`      | Work items related to debates and proposals relating to the project roadmap.                                      |
|      Policies       |       `policies-rules`       | Changes to rules for development tools (e.g., Ruff/mypy rules, issue triaging etc.).                              |
|      Policies       |     `policies-templates`     | Changes to issue and {{ cookiecutter.__mr_term }} templates.                                                      |
|         N/A         |         `quick-win`          | Development requires low effort.                                                                                  |
|         N/A         |        `refactoring`         | Restructures existing source code without changing its functionality.                                             |
{%- if cookiecutter.app_type == 'bare_repo' %}
|         N/A         |          `removals`          | Feature sunsetting.                                                                                               |
{%- endif %}
|    User Requests    |            `rfc`             | For work items for when something is not working properly.                                                        |
|    User Requests    |            `rfi`             | For work items containing suggestions for new features from the community.                                        |
|    User Requests    |            `rfs`             | For issues opened by users seeking advice regarding {{ cookiecutter.project_name }}.                              |
|         N/A         |    `seeking-contributors`    | Umbrella label to mark work items requiring contributor involvement.                                              |
|         N/A         |      `seeking-builders`      | Proposal is polished and can be picked up if you feel inclined to.                                                |
|         N/A         |       `seeking-input`        | In need of help to further discuss and define scope.                                                              |
|         N/A         |           `stale`            | Work items without activity that are marked for closing.                                                          |
|         N/A         |     `starter-assignment`     | Proposal and delivery steps are clear and can be picked up by first-time contributors.                            |
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
|   User Interface    |      `ui-accessibility`      | Promotes accessibility options for users in the interface.                                                        |
|   User Interface    |          `ui-arch`           | Changes to rendering logic in the layer directly below the user interface.                                        |
|   User Interface    |      `ui-deprecations`       | Marks deprecations for future removal to UI features.                                                             |
|   User Interface    |        `ui-features`         | Introduces new functions and capabilities to the user interface.                                                  |
|   User Interface    |         `ui-layout`          | Changes the disposition of elements and text in the user interface.                                               |
|   User Interface    |        `ui-removals`         | User interface feature sunsetting.                                                                                |
{%- endif %}
|         N/A         |      `up-for-a-change`       | Author-based label to express interest in delivering their own request.                                           |
|   User Experience   |        `ux-advanced`         | Updates features available to power users of {{ cookiecutter.project_name }}.                                     |
|   User Experience   |      `ux-customization`      | Improves options available for program customisation by users.                                                    |
|   User Experience   |          `ux-flags`          | Implements feature flags for {{ cookiecutter.project_name }}.                                                     |
|   User Experience   |        `ux-migration`        | Offers predefined migration options to users in the case of breaking changes.                                     |
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
|   User Experience   |       `ux-navigation`        | Improves user navigation in the user interface.                                                                   |
{%- endif %}
|   User Experience   |         `ux-nudging`         | Helps users understand the application with more ease, like help panels, notifications etc.                       |

> [!IMPORTANT]
> The project labels are also used
> to define Changelog categories
> in [Release Drafter][labels1].

{% endif -%}
##### Work Item Lifecycle

To effectively manage
issue and {{ task_item }} lifecycles,
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
we use [GitLab Statuses][status1].
Our approach to this feature
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
we use specific labels
to mark issues.
Our approach
{%- else %}
we use specific labels
to mark issues
and discussions.
Our approach
{%- endif %}
relies on
keeping few options for
in-progress and completed items
and providing different options
for other stages of the lifecycle.
This allows project members to
better relay [context][swnjw]
surrounding those items,
instead of only stating
their condition.

By combining effective
status and label assignments,
both users and the development team
can locate discussions
more easily,
streamlining communication
and making development more agile.

The following statuses
have been implemented for the project,
with contributors expected to
understand
each use case and
when to move from one stage to another:

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
| Status                                               | Status Category | Description                                                                                                                                                                                                                                                                                                                                                               |
| :--------------------------------------------------- | :-------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Triage icon][icon1] **Needs Triage**               |     Triage      | Initial stage for [User requests][status2], which require a first analysis by a {{ cookiecutter.project_name }} contributor before work on its scope is either accepted or declined. It is also the default open state for new items if not overridden.                                                                                                                   |
| ![Refinement icon][icon2] **Needs Refinement**       |     Triage      | Describes more general ideas that might receive development at some point, but whose current state does not detail implementation or paths to delivery. Lacking scope, represents more of a desire than an actual proposal – which might actually prove infeasible later. Should be used to inform the need for further discussions before being cleared for development. |
| ![Criteria icon][icon3] **Needs Criteria**           |     Triage      | This describes items whose scope is set, but acceptance criteria is still pending to be added before being cleared for development. In contrast with the **Needs Refinement** status, in this stage the deliverable is known and understood, but is waiting for a contributor to detail in smaller steps.                                                                 |
| ![Steps icon][icon4] **Needs Delivery Steps**        |     Triage      | A specific type of triaging item, signaling pending work before the item can be cleared as a [starter assignment][starter] development. In contrast with the **Needs Criteria**, this stage indicates the work item will be processed with greater detail than usual so a new contributor can pick it up and develop it with little to no friction.                       |
| ![Decomposition icon][icon5] **Needs Decomposition** |     Triage      | Proposals or requests that have been deemed too large in scope to be considered a single work item and must be broken down in two or more items before proceeding.                                                                                                                                                                                                        |
| ![Greenlit icon][icon6] **Greenlit**                 |      To Do      | Items that have been cleared for development after having their scope and acceptance criteria properly defined.                                                                                                                                                                                                                                                           |
| ![Pipeline icon][icon7] **Pipeline**                 |      To Do      | Items that have scope and acceptance criteria, but that address a specific development stream which is not currently considered the most valuable for delivery. Can be picked for development, but should be left out in favour of **Greenlit** and **Priority** items.                                                                                                   |
| ![Priority icon][icon8] **Priority**                 |      To Do      | Signals items which take priority over other cleared work items. Should be used with discretion and only in cases where lack of action can lead to significant issues to security or user experience.                                                                                                                                                                     |
| ![Deferred icon][icon9] **Deferred**                 |      To Do      | Signals items that, despite having scope and acceptance criteria, are deliberately being deprioritised for development (e.g., due to an upstream block).                                                                                                                                                                                                                  |
| ![Progress icon][icon10] **In Progress**             |   In Progress   | Items currently being actively worked on.                                                                                                                                                                                                                                                                                                                                 |
| ![Done icon][icon11] **Done**                        |      Done       | Items delivered in full.                                                                                                                                                                                                                                                                                                                                                  |
| ![Canceled icon][icon12] **Out of Scope**            |    Canceled     | Items deemed out of the scope of {{ cookiecutter.project_name }}.                                                                                                                                                                                                                                                                                                         |
| ![Canceled icon][icon12] **Cannot Implement**        |    Canceled     | Items which are unable to be delivered by the development team in its original form, due to technical barriers or security risks.                                                                                                                                                                                                                                         |
| ![Canceled icon][icon12] **Not Feasible**            |    Canceled     | Items which can technically be delivered, but that have been declined for development due to any other factor outside the other **Canceled** stage items.                                                                                                                                                                                                                 |
| ![Redundant icon][icon13] **Redundant**              |    Canceled     | Items whose scope has become superfluous to the project due to design changes in other domains.                                                                                                                                                                                                                                                                           |
| ![Duplicate icon][icon14] **Duplicate**              |    Canceled     | Items marked as duplicates of previous work items.                                                                                                                                                                                                                                                                                                                        |

Task lifecycles are made simpler
to reduce overhead
on the development team,
defining only the
![Created icon][icon15] **Created**,
![Ongoing icon][icon16] **Ongoing**,
![Done icon][icon11] **Done**,
![Aborted icon][icon17] **Aborted**
and ![Duplicate icon][icon14] **Duplicate**
stages.
Developers, however,
are not obligated
to mark their tasks
as "Ongoing"
if development will be short lived.

{% else -%}
|          Status          |           Label           | Status Category | Description                                                                                                                                                                                                                                                                                                                                                               |
| :----------------------: | :-----------------------: | :-------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     **Needs Triage**     |    `sts-needs-triage`     |     Triage      | Initial stage for User Requests, which require a first analysis by a {{ cookiecutter.project_name }} contributor before work on its scope is either accepted or declined.                                                                                                                                                                                                 |
|   **Needs Refinement**   |  `sts-needs-refinement`   |     Triage      | Describes more general ideas that might receive development at some point, but whose current state does not detail implementation or paths to delivery. Lacking scope, represents more of a desire than an actual proposal – which might actually prove infeasible later. Should be used to inform the need for further discussions before being cleared for development. |
|    **Needs Criteria**    |   `sts-needs-criteria`    |     Triage      | This describes items whose scope is set, but acceptance criteria is still pending to be added before being cleared for development. In contrast with the **Needs Refinement** status, in this stage the deliverable is known and understood, but is waiting for a contributor to detail in smaller steps.                                                                 |
| **Needs Delivery Steps** |     `sts-needs-steps`     |     Triage      | A specific type of triaging item, signaling pending work before the item can be cleared as a [starter assignment][starter] development. In contrast with the **Needs Criteria**, this stage indicates the work item will be processed with greater detail than usual so a new contributor can pick it up and develop it with little to no friction.                       |
| **Needs Decomposition**  | `sts-needs-decomposition` |     Triage      | Proposals or requests that have been deemed too large in scope to be considered a single work item and must be broken down in two or more items before proceeding.                                                                                                                                                                                                        |
|       **Greenlit**       |      `sts-greenlit`       |      To Do      | Items that have been cleared for development after having their scope and acceptance criteria properly defined.                                                                                                                                                                                                                                                           |
|       **Pipeline**       |      `sts-pipeline`       |      To Do      | Items that have scope and acceptance criteria, but that address a specific development stream which is not currently considered the most valuable for delivery. Can be picked for development, but should be left out in favour of **Greenlit** and **Priority** items.                                                                                                   |
|       **Priority**       |      `sts-priority`       |      To Do      | Signals items which take priority over other cleared work items. Should be used with discretion and only in cases where lack of action can lead to significant issues to security or user experience.                                                                                                                                                                     |
|       **Deferred**       |      `sts-deferred`       |      To Do      | Signals items that, despite having scope and acceptance criteria, are deliberately being deprioritised for development (e.g., due to an upstream block).                                                                                                                                                                                                                  |
|     **In Progress**      |       `sts-ongoing`       |   In Progress   | Items currently being actively worked on.                                                                                                                                                                                                                                                                                                                                 |
|     **Out of Scope**     |         `sts-oos`         |    Canceled     | Items deemed out of the scope of {{ cookiecutter.project_name }}.                                                                                                                                                                                                                                                                                                         |
|   **Cannot Implement**   |        `sts-cant`         |    Canceled     | Items which are unable to be delivered by the development team in its original form, due to technical barriers or security risks.                                                                                                                                                                                                                                         |
|     **Not Feasible**     |      `sts-declined`       |    Canceled     | Items which can technically be delivered, but that have been declined for development due to any other factor outside the other **Canceled** stage items.                                                                                                                                                                                                                 |
|      **Redundant**       |      `sts-redundant`      |    Canceled     | Items whose scope has become superfluous to the project due to design changes in other domains.                                                                                                                                                                                                                                                                           |
|      **Duplicate**       |      `sts-duplicate`      |    Canceled     | Items marked as duplicates of previous work items.                                                                                                                                                                                                                                                                                                                        |

{{ task_item.capitalize() }}s do not require
a lifecycle label.

{% endif -%}
#### General Practices

##### Issue Titles Should be Framed in Imperative Mood

Issue titles should be clear
to allow anyone
visiting the Issue Tracker
to understand
the scope of development,
and get more detail
by opening the issue page
if one picks their interest.
Thus, issue titles
should use imperative,
just like [commits][practices1].

Using the imperative mood for issue titles
is recommended because
it clearly states
the action or goal of the issue
as a command
or instruction,
making it easier to understand
what needs to be **done**,
explicitly describing
the task to be accomplished,
rather than
just naming a topic
or describing past actions.
The title of an issue
should always summarise
the _what_ that specific issue
is trying to address.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!caution]
The only exception
to using imperative mood
in issue titles is
when it refers
to a bug or malfunction
that has been identified.
In this case,
the title should refer
to the erroneous **behaviour** of {{ cookiecutter.project_name }}.

Since when bugs first appear,
its solution is unknown,
by providing
the behaviour being observed
we can equally understand
_what_ needs to be addressed
to close the issue.
>>>
{%- else -%}
> [!CAUTION]
> The only exception
> to using imperative mood
> in issue titles is
> when it refers
> to a bug or malfunction
> that has been identified.
> In this case,
> the title should refer
> to the erroneous **behaviour** of {{ cookiecutter.project_name }}.
>
> Since when bugs first appear,
> its solution is unknown,
> by providing
> the behaviour being observed
> we can equally understand
> _what_ needs to be addressed
> to close the issue.
{%- endif %}

##### {{ task_item.capitalize() }}s Are Used as Acceptance Criteria for Issues

[{{ task_item.capitalize() }}s][practices2] are a specific type of work item
in {{ cookiecutter.__scm_platform_base }}
which can be associated
with issues as their child items.
In {{ cookiecutter.project_name }} development,
{{ cookiecutter.__mr_term }}s are
the [default][swmr] form of actionable development,
while issues are used
for compiling user requests
and development intentions
that can not be directly delivered
through an open {{ cookiecutter.__mr_term }}.

In either case,
{{ task_item }}s must be used
to complement the open issue
with their acceptance criteria
to be closed.
Their titles should follow
the same [rules][imperative] as issue titles,
while descriptions are optional
if relevant to understand implementation.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!caution]
The only label allowed on {{ task_item }}s
is `manual-closure`.
Otherwise,
there should be no labels
associated with a {{ task_item }}.
>>>
{%- else -%}
> [!CAUTION]
> The only label allowed on {{ task_item }}s
> is `manual-closure`.
> Otherwise,
> there should be no labels
> associated with a {{ task_item }}.
{%- endif %}

##### Usage of the `seeking-contributors` Labels

`seeking-contributors` is the label used
to indicate work items
whose authors need help from the community
in further advancing with development.

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
The `opinion` value label marks work items which
{% else -%}
The `seeking-input` label marks work items which
{%- endif %}
are at a [**Triage**][tracking] stage
and whose discussion has stalled.
It signals other contributors and the community
that more people are requested
to provide opinion on the matter,
as a consensus for its final scope
has not been reached yet.

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
The `delivery` value label,
{% else -%}
The `seeking-builders` label,
{%- endif %}
on the other hand,
is used to mark items
at the **To Do** stage
that can be picked up for development
if a contributor is interested
in delivering the solution.
It is similar in this manner
to the `starter-assignment` labels,
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
with the difference that `seeking-contributors::delivery` is aimed
{%- else %}
with the difference that `seeking-builders` is aimed
{%- endif %}
towards contributors
with intermediate experience in the project.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!important]
Contributors planning
on refining an issue
or {{ cookiecutter.__mr_term }}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
to mark with the `seeking-contributors::delivery` label
{%- else %}
to mark with the `seeking-builders` label
{%- endif %}
should be aware
of the **Goldilocks Priority** principle:
the item's priority
should not be so high
that a core contributor should do it,
but not too low
that it isn't useful enough
for a core contributor
to spend time reviewing it,
answering questions,
helping get it into a release
etc.
>>>
{%- else -%}
> [!IMPORTANT]
> Contributors planning
> on refining an issue
> or {{ cookiecutter.__mr_term }}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
> to mark with the `seeking-contributors::delivery` label
{%- else %}
> to mark with the `seeking-builders` label
{%- endif %}
> should be aware
> of the **Goldilocks Priority** principle:
> the item's priority
> should not be so high
> that a core contributor should do it,
> but not too low
> that it isn't useful enough
> for a core contributor
> to spend time reviewing it,
> answering questions,
> helping get it into a release
> etc.
{%- endif %}

##### Blocks Must be Set at the Same Issue Level

[Issue blocks][practices3] are not mandatory
for development,
but marking block relations
between work items
is encouraged
when they are clear
for the issue author,
but might not be
for someone else.
This helps
reinforce an orderly development
and improve the environment
for newcomers and veterans alike.

However,
block relations
must only be placed
between working items
of the same type:
issues can only block **issues**,
{{ task_item }}s can only block **{{ task_item}}s**.

{% if cookiecutter.scm_platform == 'GitLab Free' -%}
##### Tasks Should Have no Milestones

Given GitLab Tasks are used
for acceptance criteria of issues,
breaking a deliverable down to
smaller components,
we prefer to keep
only issues and {{ cookiecutter.__mr_acronym }}s
associated with milestones.
This reduces clutter
in the milestone board.

However,
given the [default behaviour][practices4] of GitLab,
tasks associated with milestones
can accumulate over time.
The association
should be removed
by [being queried][query1a]
in the Issue Tracker
and edited
through the "Bulk edit" option.

{% endif -%}
{% if cookiecutter.use_bdd -%}
### Behaviour-Driven Development

{% if cookiecutter.licence != 'nos' -%}
At {{ cookiecutter.project_name }},
we believe building software
goes beyond just coding
its implementation.
More often than not,
open source projects
face extreme hurdles
to effectively
deliver aggregated value
to their users
due to a lenient _laissez-faire_ approach
to project development.
This leaves users frustrated
when desired features
go unlaunched
and can eventually signal a project's doom,
as users migrate
to alternative solutions which,
while not perfect,
address the singular pivotal element
that guarantee their adoption:
**making the user feel like they matter**.

We have adopted a mission
to turn our project development
more structured
and better prepared
to handle scaling adequately
with the community's expectations
on the development team's capabilities.
We believe the best practice
we could embrace
towards this vision
is to leverage
[Behaviour-Driven Development][bdd1]
for our development cycle.

{% endif -%}
We expect all contributors
to understand
and adopt BDD best practices
during development,
striving to formulate unclear specifications,
engaging with other contributors
to debate different implementation choices
and safeguarding [institutional knowledge][knowledge].

We understand that
adopting BDD might seem like
an additional step
that slows down
our development process
at first glance.
However,
we are committed to BDD
because it aligns with {{ cookiecutter.project_name }}'s [core values][philosophy] of
collaboration,
transparency
and continuous improvement.

By focusing on
{%- if cookiecutter.app_type != 'bare_repo' %}
the behaviour of our application
{%- else %}
the behaviour of our library
{%- endif %}
from the end-user's perspective
through BDD,
we ensure that everyone
— developers, testers, and users —
shares a clear  understanding
of what we aim to achieve.
This approach promotes upfront clarity,
reducing misunderstandings and misalignments
down the line.
It also encourages us
to articulate requirements
in plain language,
fostering better communication
and collaboration among team members.

While there may be
an initial learning curve
for those unfamiliar
with the paradigm,
the long-term benefits are substantial.
It results in
more sustainable and maintainable code,
ultimately accelerating our development cycle
and ensuring we deliver value consistently.
{%- if cookiecutter.licence != 'nos' %}
It also reinforces
our commitment
to creating an environment
where contributions are
diverse
— involving not only the work of
software developers,
but also
product managers,
designers,
researchers
_and_ users
—
contributors are valued
and everyone feels empowered to grow and succeed.

{% endif -%}
#### References for BDD

The structured approach BDD offers
will help us maintain
the high standards we strive for,
ensuring that every contribution
aligns with our shared vision and goals.

To help contributors
to get more familiar
with BDD practices,
we provide a suggested list of references below:

- [The Cucumber documentation][bdd1],
  especially their [article on BDD][bdd2];
- The [Modern Software Engineering channel BDD playlist][bdd3],
  with special consideration to
  the following videos:
  - [_3 Reasons why BDD Is Failing You_][bdd4];
  - [_The Truth about Cucumber & BDD_][bdd5];
- The [`pytest-bdd` documentation][bdd6],
  as {{ cookiecutter.project_name }} uses this library
  to parse the feature files
  with test scenarios;
- Automation Panda's [BDD Guide][bdd7];
- [_Behaviour-Driven Development: A Data Scientist Perspective_][bdd8].

{% endif -%}
### Versioning Customs

{{ cookiecutter.project_name }}'s versioning
should be seen
as reflecting
the progression of our efforts
over time.
We choose to adhere
to [Intended Effort Versioning][versioning1]
for consistency
and improved user communication.

The following guidelines
should be taken in consideration
regarding versioning in general:

<!-- DEFINE the acceptance criteria for releasing a v1.0 for your project -->
- Version `v1.0.0` can only be set
  once all requirements specified
  in the `v1.0 Release` {{ roadmap_item }}
  are satisfied;
- Versions can only be tagged
  if altering user-facing files;
  changes to project internals only
  do not qualify for tagging;

While EffVer makes
the choice of updating versions
more human-natured
and less mechanic,
you can refer to
the following list
for common circumstances
under which a version schema
might be selected
for the next version:

- Update **MICRO** versions when:
<!-- DEFINE common developments related to micro versions -->
- Update **MESO** versions when:
<!-- DEFINE common developments related to meso versions -->
- Update **MACRO** versions when:
<!-- DEFINE common developments related to macro versions -->

### Branch Organization

We apply the [{{ cookiecutter.project_name }} Philosophy][philosophy]
for conducting new development,
which means
that all changes
revolve around open {{ cookiecutter.__mr_term }}s,
and {{ cookiecutter.__mr_term }}s are
the central space
for discussing design,
implementation
and monitoring development health
{%- if cookiecutter.__scm_platform_base == 'gitlab' %}
with [CI pipelines][cicd].
{%- else %}
with [GitHub Actions][cicd].
{%- endif %}

Creation of new branches
without subsequent attachment
to a new {{ cookiecutter.__mr_acronym }}
is strongly discouraged.
If the work is still in progress
but needs to be uploaded
to the repository,
name the branch
with the `test-`
or `wip-` prefixes
so the CI will ignore it.

#### Branch Naming Standards

While standard branch naming
is not strictly required,
we offer some suggestions
to enhance communication
during {{ cookiecutter.__mr_term }} reviews:

- Use the [imperative mood][imperative]
  with concise language
  for your branch names;
  this helps reviewers
  quickly gain insight
  into the changes
  your branch applies;
- For small changes,
  consider naming the branch
  with either the `flash-` or `fl-` prefixes
  to inform reviewers
  of their nature.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!note]
Flash branches are not the same
as `quick-win` labelled issues:

- **`quick-win` issues**
  mark planned developments
  that are easy to deliver
  and are used
  to track such initiatives;
- **Flash branches**
  indicate changes
  that are intended
  to be created
  and merged quickly,
  often representing unplanned work
  that doesn't require an associated issue
  or extensive {{ cookiecutter.__mr_term }} details.

While flash branches can sometimes
be linked to `quick-win` issues,
they primarily serve
as a signal
for short-lived changes
without the need
for prior planning
or detailed documentation.
>>>
{%- else -%}
> [!NOTE]
> Flash branches are not the same
> as `quick-win` labelled issues:
>
> - **`quick-win` issues**
>   mark planned developments
>   that are easy to deliver
>   and are used
>   to track such initiatives;
> - **Flash branches**
>   indicate changes
>   that are intended
>   to be created
>   and merged quickly,
>   often representing unplanned work
>   that doesn't require an associated issue
>   or extensive {{ cookiecutter.__mr_term }} details.
>
> While flash branches can sometimes
> be linked to `quick-win` issues,
> they primarily serve
> as a signal
> for short-lived changes
> without the need
> for prior planning
> or detailed documentation.
{%- endif %}

### Commit Customs

{% if cookiecutter.commit_convention == 'gitmoji' -%}
#### Gitmoji

{{ cookiecutter.project_name }} uses [Gitmoji][committing1]
to characterise
the nature of each commit,
you should familiarise yourself
with this method
by looking at
the list of possible Emoji
to be used.
Additionally,
looking at past commits
and which files they modified
is also a good way
to understand how Gitmoji
should be applied
to the project.

Some times a commit
can encompass more than one Gitmoji,
as changes to a file
related to a domain
can only be applied
without breaking the project
by also changing other files.
In this case,
prefer to classify the commit
through the most fundamental change
(i.e., the change
that led to subsequent file changes
from other domains).

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!warning]
The shorthand codes
specified in the Gitmoji website
use the GitHub standard.
For some of the Gitmoji,
these shorthands are different
when rendering in GitLab,
be aware of which ones:

|       Gitmoji       |     Default Shorthand     |  Shorthand in GitLab  |
| :-----------------: | :-----------------------: | :-------------------: |
|       :brick:       |        `:bricks:`         |       `:brick:`       |
| :construction_site: | `:building_construction:` | `:construction_site:` |
| :camera_with_flash: |     `:camera_flash:`      | `:camera_with_flash:` |
|     :card_box:      |     `:card_file_box:`     |     `:card_box:`      |
|       :goal:        |       `:goal_net:`        |       `:goal:`        |
|      :pencil:       |         `:memo:`          |      `:pencil:`       |
| :face_with_monocle: |     `:monocle_face:`      | `:face_with_monocle:` |
>>>

{% endif -%}
If the changes
still reflect a work in progress
that will be rebased
at a later moment,
we recommend committing
with the `:construction:` Gitmoji
so the CI will ignore it.

{% elif cookiecutter.commit_convention == 'conventional' -%}
#### Conventional Commits

{{ cookiecutter.project_name }} uses [Conventional Commits][committing1]
to characterise
the nature of each commit,
you should familiarise yourself
with this method.
We follow the [Angular Convention][committing1a]
to specify
the allowed commit types:

|    Type    | Description                                                                                             |
| :--------: | ------------------------------------------------------------------------------------------------------- |
|   `fix`    | A bug fix.                                                                                              |
|   `feat`   | A new feature.                                                                                          |
|  `build`   | Changes that affect the build system or external dependencies.                                          |
|    `ci`    | Changes to our CI configuration files and scripts.                                                      |
|   `docs`   | Documentation only changes.                                                                             |
|   `perf`   | A code change that improves performance.                                                                |
| `refactor` | A code change that neither fixes a bug nor adds a feature.                                              |
|  `style`   | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons etc.). |
|   `test`   | Adding missing tests or correcting existing tests.                                                      |

Scopes are optional
and used
at the discretion of contributors.
Breaking changes are
preferably identified
with exclamation marks (`!`)
after identifying the type.

Additionally,
looking at past commits
and which files they modified
is also a good way
to understand how the convention
should be applied
to the project.

If the changes
still reflect a work in progress
that will be rebased
at a later moment,
we recommend committing
with the `wip` type
so the CI will ignore it.

{% else -%}
#### Conventional Gitmoji

{{ cookiecutter.project_name }} uses [Conventional Gitmoji][committing1]
to characterise
the nature of each commit,
you should familiarise yourself
with this method,
based on [Conventional Commits][committing1a]
with visual cues added
via Emoji.

The list of commit types
that can be used
are listed below:

|      Type       |            Emoji            |
| :-------------: | :-------------------------: |
|      `fix`      |            :bug:            |
|     `feat`      |         :sparkles:          |
|     `docs`      |          :pencil:           |
|     `style`     |            :art:            |
|   `refactor`    |          :recycle:          |
|     `perf`      |            :zap:            |
|     `test`      |     :white_check_mark:      |
|     `build`     |    :construction_worker:    |
|      `ci`       |        :green_heart:        |
|    `revert`     |          :rewind:           |
|     `dump`      |           :fire:            |
|    `hotfix`     |         :ambulance:         |
|    `deploy`     |          :rocket:           |
|      `ui`       |         :lipstick:          |
|     `init`      |           :tada:            |
|   `security`    |           :lock:            |
|    `secret`     |   :closed_lock_with_key:    |
|     `bump`      |         :bookmark:          |
|   `fix-lint`    |      :rotating_light:       |
|      `wip`      |       :construction:        |
|   `dep-drop`    |        :arrow_down:         |
|   `dep-bump`    |         :arrow_up:          |
|      `pin`      |          :pushpin:          |
|   `analytics`   | :chart_with_upwards_trend:  |
|    `dep-add`    |      :heavy_plus_sign:      |
|    `dep-rm`     |     :heavy_minus_sign:      |
|    `config`     |          :wrench:           |
|    `script`     |          :hammer:           |
|     `lang`      |   :globe_with_meridians:    |
|     `typo`      |          :pencil2:          |
|     `poop`      |           :poop:            |
|     `merge`     | :twisted_rightwards_arrows: |
|    `package`    |          :package:          |
|   `external`    |           :alien:           |
|   `resource`    |           :truck:           |
|    `license`    |      :page_facing_up:       |
|     `boom`      |           :boom:            |
|     `asset`     |           :bento:           |
| `accessibility` |        :wheelchair:         |
|  `source-docs`  |           :bulb:            |
|     `beer`      |           :beers:           |
|     `text`      |      :speech_balloon:       |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|      `db`       |         :card_box:          |
{%- else %}
|      `db`       |       :card_file_box:       |
{%- endif %}
|   `logs-add`    |        :loud_sound:         |
|    `logs-rm`    |           :mute:            |
|    `people`     |    :busts_in_silhouette:    |
|      `ux`       |     :children_crossing:     |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `arch`      |     :construction_site:     |
{%- else %}
|     `arch`      |   :building_construction:   |
{%- endif %}
|    `design`     |          :iphone:           |
|     `mock`      |           :clown:           |
|      `egg`      |            :egg:            |
|    `ignore`     |        :see_no_evil:        |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `snap`      |     :camera_with_flash:     |
{%- else %}
|     `snap`      |       :camera_flash:        |
{%- endif %}
|  `experiment`   |          :alembic:          |
|      `seo`      |            :mag:            |
|     `types`     |           :label:           |
|     `seed`      |         :seedling:          |
|     `flag`      |  :triangular_flag_on_post:  |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `catch`     |           :goal:            |
{%- else %}
|     `catch`     |         :goal_net:          |
{%- endif %}
|   `animation`   |           :dizzy:           |
|  `deprecation`  |        :wastebasket:        |
|     `auth`      |     :passport_control:      |
|  `fix-simple`   |     :adhesive_bandage:      |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|  `exploration`  |     :face_with_monocle:     |
{%- else %}
|  `exploration`  |       :monocle_face:        |
{%- endif %}
|     `dead`      |          :coffin:           |
|   `test-fail`   |         :test_tube:         |
|     `logic`     |          :necktie:          |
|    `health`     |        :stethoscope:        |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `infra`     |           :brick:           |
{%- else %}
|     `infra`     |          :bricks:           |
{%- endif %}
|     `devxp`     |       :technologist:        |
|     `money`     |     :money_with_wings:      |
|   `threading`   |          :thread:           |
|  `validation`   |        :safety_vest:        |
|     `chore`     |           :broom:           |

Scopes are optional
and used
at the discretion of contributors.
Breaking changes are
preferably identified
with exclamation marks (`!`)
after identifying the type.

If the changes
still reflect a work in progress
that will be rebased
at a later moment,
we recommend committing
with the `wip` type
so the CI will ignore it.

{% endif -%}
#### Commit Message Structure

Commit messages should be clear
and concise,
and detailing aspects
of the commit
through its body
is strongly encouraged,
as it helps developers
to later understand implementation
and reasoning
behind changes.
The article [_How to Write a Git Commit Message_][committing2]
is a valuable resource
and reading through it
is strongly recommended
before contributing,
as developers are expected
to apply those principles
when committing.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

#### Git Trailers

Every commit should also
be identified with the respective [Git trailer][committing3]
to categorise the type of change being made.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
When a new version of {{ cookiecutter.project_name }}
is released through a tag,
a CI pipeline compiles every trailer
to automate the version's release
and update the `CHANGELOG` file
in the root directory.
{%- endif %}

The available trailers
are listed below
and defined in the [`changelog-config.yml`][committing4] file:
{%- if cookiecutter.app_type != 'bare_repo' %}
|           Category in CHANGELOG            |                                                                                                      Available Trailers                                                                                                      | Use Cases                                                                                                                                                              |
| :----------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| :satellite_orbital: Command-line Interface |                                                                            `cli`<br>`command`<br>`commands`<br>`terminal`<br>`output`<br>`shell`                                                                             | Updates to the CLI API that bridges the interface to the actual program. This encompasses available commands and how things are printed to the user's shell.           |
|            :keyboard: CLI Usage            |                                                   `flag`<br>`flags`<br>`option`<br>`options`<br>`opt`<br>`opts`<br>`argument`<br>`arguments`<br>`arg`<br>`args`<br>`usage`                                                   | Developments that change how the user interacts with the CLI, like options and arguments available for fine-tuning command control.                                    |
{%- if cookiecutter.app_type != 'cli' %}
|   :computer: User Interface Improvements   |                                             `tui`<br>`ui`<br>`layout`<br>`screen`<br>`element`<br>`elements`<br>`panel`<br>`panels`<br>`widget`<br>`widgets`<br>`accessibility`                                              | Improvements to the terminal user interface (TUI), which can be related to widgets, screens, layout, readability etc.                                                  |
|        :video_game: User Experience        |                                                                     `ux`<br>`xp`<br>`interaction`<br>`navigation`<br>`nav`<br>`shortcut`<br>`shortcuts`                                                                      | All development focused on interaction processes between the user and the terminal user interface, controlling its behaviour.                                          |
{%- endif %}
|          :peacock: Customisation           |                                                            `customization`<br>`customize`<br>`theme`<br>`themes`<br>`theming`<br>`style`<br>`styles`<br>`styling`                                                            | Customisation options for user satisfaction.                                                                                                                           |
|             :beginner: Nudging             |                                                    `nudge`<br>`nudges`<br>`nudging`<br>`tutorial`<br>`tutorials`<br>`hint`<br>`hints`<br>`help`<br>`helper`<br>`helpers`                                                     | Developments that help users navigate and use the application with more ease, like tutorials, notifications, command helpers, argument/option groups, help panels etc. |
|       :electric_plug: Extensibility        | `plugin`<br>`plugins`<br>`hook`<br>`hooks`<br>`event`<br>`events`<br>`entrypoint`<br>`entrypoints`<br>`extension`<br>`extensions`<br>`extend`<br>`scaffold`<br>`scaffolds`<br>`scaffolding`<br>`type`<br>`types`<br>`typing` | Changes related to improving {{ cookiecutter.project_name }} extensibility, like entry points, plugin enablers, improvements to type hints etc.                        |
|    :link: Compatibility & Integrations     |                   `api`<br>`rest`<br>`restful`<br>`integration`<br>`integrations`<br>`integrate`<br>`compatibility`<br>`compat`<br>`service`<br>`services`<br>`webservice`<br>`webservices`<br>`external`                    | Compatibility and integrations with external services and tools.                                                                                                       |
|       :earth_americas: Localisation        |                                                                        `localization`<br>`localize`<br>`translation`<br>`translations`<br>`translate`                                                                        | Changes related to project localisation.                                                                                                                               |
|   :puzzle_piece: Application Components    |                                              `component`<br>`components`<br>`module`<br>`modules`<br>`backend`<br>`performance`<br>`improvement`<br>`improvements`<br>`improve`                                              | Changes to components in the backend not directly affecting user experience.                                                                                           |
|       :floppy_disk: Database Changes       |                                                                                           `database`<br>`db`<br>`data`<br>`schema`                                                                                           | Database-related changes.                                                                                                                                              |
|    :city_dusk: Deprecations & Removals     |                                                              `deprecation`<br>`deprecations`<br>`deprecate`<br>`removal`<br>`removals`<br>`remove`<br>`sunset`                                                               | Changes that mark features and options as deprecated or remove them from the public API.                                                                               |
|              :toolbox: Fixes               |                                                  `bug`<br>`bugfix`<br>`fix`<br>`hotfix`<br>`security`<br>`sec`<br>`critical`<br>`leak`<br>`injection`<br>`typo`<br>`typos`                                                   | Fixes for wrongful behaviour (i.e., bugs).                                                                                                                             |
|    :factory_worker: Codebase Renovation    |                                                 `architecture`<br>`arch`<br>`refactor`<br>`refactors`<br>`refactoring`<br>`rework`<br>`reworks`<br>`reworking`<br>`plumbing`                                                 | Architectural changes, refactoring and other improvements done under the hood.                                                                                         |
|         :up: Dependencies Updates          |                                                                                              `dependencies`<br>`dep`<br>`deps`                                                                                               |                                                                                                                                                                        |
|    :comet: Build & Release Optimisation    |                             `build`<br>`building`<br>`packaging`<br>`script`<br>`scripts`<br>`ci`<br>`workflow`<br>`workflows`<br>`environment`<br>`env`<br>`infrastructure`<br>`infra`<br>`iac`                             | Improvements to how the project is set up for compilation and release.                                                                                                 |
{%- if cookiecutter.use_bdd %}
|        :repeat: Design & Validation        |                                                    `design`<br>`ideation`<br>`test`<br>`tests`<br>`testing`<br>`bdd`<br>`scenario`<br>`scenarios`<br>`story`<br>`stories`                                                    | Code integrity validations, tests and feature scenarios specification.                                                                                                 |
{%- else %}
|        :repeat: Design & Validation        |                                                                                   `design`<br>`ideation`<br>`test`<br>`tests`<br>`testing`                                                                                   | Code integrity validations and unit tests.                                                                                                                             |
{%- endif %}
| :suspension_railway: Developer Experience  |                                           `dev`<br>`devx`<br>`devdep`<br>`devdeps`<br>`pyproject`<br>`tool`<br>`tools`<br>`specification`<br>`specifications`<br>`spec`<br>`specs`                                           | Changes to internal configuration to standardise and ease development workflow.                                                                                        |
|           :books: Documentation            |                                                                                              `documentation`<br>`doc`<br>`docs`                                                                                              | Formal documentation.                                                                                                                                                  |
|         :scroll: Project Policies          |                                  `policy`<br>`policies`<br>`rule`<br>`rules`<br>`milestone`<br>`milestones`<br>`epic`<br>`epics`<br>`roadmap`<br>`template`<br>`templates`<br>`templating`                                   | Changes that altered project rules and/or project-specific documentation.                                                                                              |
|     :gem: Continuous Improvement Feats     |                        `monitor`<br>`monitoring`<br>`tracker`<br>`trackers`<br>`tracking`<br>`log`<br>`logs`<br>`logging`<br>`alert`<br>`alerts`<br>`detection`<br>`detect`<br>`diligence`<br>`rskm`                         | Internal improvements to detect and report issues, targeting CI/CD maturity.                                                                                           |
{%- else %}
|        Category in CHANGELOG        |                                                          Available Trailers                                                          |
| :---------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: |
|           :new: Additions           |                                                    `feature`<br>`add`<br>`added`                                                     |
|        :arrow_right: Changes        |                               `change`<br>`changes`<br>`changed`<br>`update`<br>`updates`<br>`updated`                               |
| :city_dusk: Deprecations & Removals |    `deprecation`<br>`deprecations`<br>`deprecate`<br>`deprecated`<br>`removal`<br>`removals`<br>`remove`<br>`removed`<br>`sunset`    |
|           :toolbox: Fixes           | `bug`<br>`bugfix`<br>`fix`<br>`fixed`<br>`hotfix`<br>`security`<br>`sec`<br>`critical`<br>`leak`<br>`injection`<br>`typo`<br>`typos` |
|      :up: Dependencies Updates      |                                                  `dependencies`<br>`dep`<br>`deps`                                                   |
|  :black_circle: Other Developments  |                                                               `other`                                                                |
{%- endif %}
{%- endif %}

### Styling

#### Codestyle

The project uses [Ruff][style1]
for formatting and codestyle.
Developers can check
both the linter
and the formatter
with the preconfigured tasks
with `invoke codestyle` and `invoke lint` commands.

To suggest changes and additions
to Ruff rules and conventions
for the project,
use a [Project Policy Proposal {{ cookiecutter.__mr_acronym }}][roadmap1].

#### Docstring Convention

{% if cookiecutter.docstring_style != 'other' -%}
We choose to write our docstrings
using the [{{ docstring_name }}][style1a] standard.
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
- Objects defined in the `tests` directory
  are not obliged
  to define docstrings.

{% else -%}
<!-- DEFINE your docstring convention details and usage guidelines -->
We choose to write our docstrings
using a custom standard.
Please be aware
to adhere to it
when making your contributions.

{% endif -%}
#### Semantic Line Breaks

When editing Markdown files,
[Semantic Line Breaks][style2] should be applied.
This increases the document's readability
by other contributors
and makes changes clearer
when using `git diff`.
This comes from Brian Kernighan
in his 1974 book _"UNIX for Beginners"_:

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!note] Hints for Preparing Documents
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
>>>
{%- else -%}
> [!NOTE]
> **Hints for Preparing Documents**
> Most documents go
> through several versions
> (always more than you expected)
> before they are finally finished.
> Accordingly,
> you should do whatever possible
> to make the job of changing them easy.
>
> First,
> when you do the purely mechanical operations of typing,
> type so subsequent editing will be easy.
> Start each sentence on a new line.
> Make lines short,
> and break lines at natural places,
> such as after commas and semicolons,
> rather than randomly.
> Since most people change documents
> by rewriting phrases
> and adding, deleting and rearranging sentences,
> these precautions simplify
> any editing you have to do later.
{%- endif %}

On a more practical level,
this [article][style3] from Derek Sivers
provides additional reasons
for adopting this style.

The only files
that should not follow this rule
are issue and {{ cookiecutter.__mr_term }} templates
inside [`.{{ cookiecutter.__scm_platform_lc }}`][style4] and [`CHANGELOG.md`][style5].

### Checks & Hooks

Developers are encouraged
to run local tests,
check codestyle and static typing
with the `invoke sweep` command
before committing.

Pre-commit hooks are configured
to block updates not following the rules:

- All files must comply to the [POSIX][hooks1] standard;
- Code files must comply with the Ruff linter.

Ensure both Invoke and Pre-Commit are [installed][setup]
in your virtual environment.

### Continuous Integration

Besides being hosted in {{ cookiecutter.__scm_platform_base }},
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
{{ cookiecutter.project_name }} uses [GitLab CI][ci1]
{%- else %}
{{ cookiecutter.project_name }} uses [GitHub Actions][ci1]
{%- endif %}
to automate the following development streams:

- Testing;
- Test coverage reporting;
{%- if cookiecutter.__coverage_lc == 'codacy' %}
- Code quality analysis;
{%- endif %}
- Releases.

{{ cookiecutter.__mr_term }}s can not be completed
unless its CI pipeline passes.
The project's CI configuration
runs under more strict rules
and no jobs are allowed to fail.
{%- if cookiecutter.__coverage_lc == 'codacy' %}
This includes the external job
provided by [Codacy][ci1a],
which is used for code quality assurance.
Take a look at the [Pull Requests][ci1b] page for {{ cookiecutter.project_name }}
for further information
on reasons
why a PR Quality Review job
might have failed.
{%- endif %}

Developers should be familiar
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
with the [GitLab CI syntax][ci2]
{%- else %}
with the [GitHub Actions syntax][ci2]
{%- endif %}
to effectively contribute
with further automation
of the development cycle.

### Licence

{% if cookiecutter.licence != 'nos' -%}
By contributing to {{ cookiecutter.project_name }},
you agree that your contributions
will be licensed under
the [{{ licence_name }}][licence1].

{% else -%}
{{ cookiecutter.project_name }} is _**not**_ open source software.
Please [contact][topic5] the maintainer
for more information
on licencing the project.

{% endif -%}
## :book: Our Philosophy

This document is
more than just a technical guide
on how to contribute;
it defines the deeper principles
we follow
to shape our approach
to {{ cookiecutter.project_name }} development.
This section outlines our _modus operandi_
and provides insight
into the mindset needed
for successful contributions.

Our project's guidelines
are strongly influenced by the [GitLab Handbook][values1],
which serves as GitLab's official company manual.
Their best practices
are transferable
to any team,
and we have adopted several
of these principles
to formalise expectations
for contributors
within our development ecosystem.

### Start with a {{ cookiecutter.__mr_term }}

> Adapted from the [Communication][values2] section of the GitLab Handbook.

When possible,
it's best practice
to start a discussion
with a {{ cookiecutter.__mr_term }} ({{ cookiecutter.__mr_acronym }})
instead of an issue.
An {{ cookiecutter.__mr_acronym }} is associated
with a specific change
that is proposed
and transparent for everyone
to review
and openly discuss.

The nature of {{ cookiecutter.__mr_acronym }}s
facilitate discussions
around a proposed solution
to a problem that is actionable.
An {{ cookiecutter.__mr_acronym }} is actionable,
while an issue
will take longer
to take action on.

1. **Always** open an {{ cookiecutter.__mr_acronym }}
   for things you are suggesting
   and/or proposing.
   Whether something is not working right
   or we are iterating
   on a new internal process,
   it is worth opening a {{ cookiecutter.__mr_term }}
   with the minimal valuable change
   instead of opening an issue
   encouraging open feedback on the problem
   without proposing any specific change directly.
   Remember,
   an {{ cookiecutter.__mr_acronym }} also invites discussion,
   but it's specific
   to the proposed change
   which facilitates focused decision;
2. Never ask someone
   to create an issue
   when they can default
   to the {{ cookiecutter.__mr_term }};
3. Not every solution
   will solve the problem at hand.
   Keep discussions focused
   by **defining the problem first**
   and **explaining your rationale**
   behind the Minimal Valuable Change (MVC)
   proposed in the {{ cookiecutter.__mr_acronym }};
4. Have a [**bias for action**][bias]
   and do not aim for consensus.
   Every {{ cookiecutter.__mr_acronym }} is as-is proposal,
   if an {{ cookiecutter.__mr_acronym }}'s author isn't responsive
   take ownership of it
   and complete it.
   Some improvement is better than none;
5. If submitting a change for a feature,
   **update the description with the final conclusions**
   – why an {{ cookiecutter.__mr_acronym }} was rejected
   or why it was approved.
   This makes it much easier
   to see the current state of an issue
   for everyone involved
   in the implementation
   and prevents confusion
   and discussion
   later on;
6. Submit the **smallest** viable and valuable thing.
   When proposing a change,
   submit the smallest reasonable commit,
   put suggestions
   for other enhancements
   in separate issues/{{ cookiecutter.__mr_acronym }}s
   and link them.
   An {{ cookiecutter.__mr_acronym }} can start off
   as only a problem description
   and `TODO` comments;
7. Do not leave {{ cookiecutter.__mr_acronym }}s open
   for a long time.
   {{ cookiecutter.__mr_acronym }}s should be **actionable**
   – maintainers should have
   a clear understanding
   of what changed
   and what they are
   ultimately approving or rejecting;
8. When submitting a MVC,
   **ask for feedback**
   from your peers.
   If they suggest changes,
   you get the opportunity
   to improve your work
   and propose an alternative solution.
   This promotes collaboration
   and advances everyone's skills;
9. Respond to comments within a **threaded discussion**.
   If there isn't a discussion thread yet,
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
   you can use the Reply to Comment button
{%- else %}
   you can use the Quote Reply button
{%- endif %}
   from the comments to create one.
   This will prevent comments
   from containing many interweaved discussions
   with responses that are hard to follow;
10. If your comment or answer
    contains separate topics,
    write separate comments for each,
    so others can address topics independently
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
    using the Reply to Comment button;
{%- else %}
    using the Quote Reply button;
{%- endif %}
11. If you have received any feedback
    or questions on your {{ cookiecutter.__mr_acronym }},
    try to acknowledge comments
    as that's how we ensure
    we create an environment of belonging
    for all team members.
    Merging your {{ cookiecutter.__mr_acronym }} as-is
    without giving an answer
    or any response
    makes the commenters feel
    their opinions are unheard.
    On the other hand,
    having a {{ cookiecutter.__mr_acronym }} with too many comments
    may risk the author falling
    into a perpetual loop of
    changing the {{ cookiecutter.__mr_acronym }} description
    or explaining too much,
    causing people to defer
    rather than working
    with a bias for action.
    This is something we want to avoid.
    When fast decisions are needed,
    we'll have to accept
    that people listened to us
    but don't owe us an explanation
    to have fast decisions
    based on everyone's input.
    The goals are to be transparent
    and collaborative
    – not to lose efficiency.
    Not everyone will agree,
    but we expect all people to
    disagree, commit, and disagree;
12. Even when something is not done,
    share it internally
    so people can comment early
    and prevent rework;
13. Create a **Draft** {{ cookiecutter.__mr_term }}
    to prevent an accidental early merge.
    Only use Draft when merging it
    would **make things worse**,
    which should rarely be the case
    when contributing to the project.
    Most {{ cookiecutter.__mr_term }}s that are in progress
    don't make things worse.
    In this case, do not use Draft;
    if someone merges it
    earlier than you expected
    just create a new {{ cookiecutter.__mr_term }}
    for additional items.
    Never ask someone
    to do a final review
    or merge something
    that still has Draft status.
    At that point
    you should be convinced
    it is good enough to go out;
14. If any follow-up actions are required
    on the issue
    after the {{ cookiecutter.__mr_term }} is merged,
    avoid auto-closing the related issue.

### _Say Why, Not Just What_

> Adapted from the [GitLab Values][values3].

Transparent changes
have the reasons for the change
laid out clearly
along with the change itself.
This leads to fewer questions later on
because people already have some understanding.
A change with no public explanation
can lead to a lot of
extra rounds of questioning,
which is less efficient.

This also helps
with institutional memory:
a year from now
when you want to know
why a decision was made,
or not,
the issue or {{ cookiecutter.__mr_acronym }} that has the decision
also shares why the decision was made.
This is related to [Chesterton's fence][values4]
– it's much easier
to suggest removing
or changing something
if you know
why it exists
in the first place.

If you use generalised terms
such as "industry standard"
or "best practices",
be sure to give context,
as without context
they can be seen
as potentially vague
or opaque.

Saying why and not just what
enables discussion around topics
that may impact
more than one front.
When decisions align
with more than a single project goal,
they are easy to discuss
and decide.
When there are multiple goals
involved for a change,
directly discussing the trade-offs
is easier
with more context.

Articulating why
also helps people understand
how something changed
when you articulate
that you changed your mind.

Saying why does not mean
justifying a decision against all other suggestions.
The maintainers are responsible
for their decision.
The maintainers are not responsible
for convincing other people,
but they should be able
to articulate their reasoning
for the change.

When a contributor comes across
{{ roadmap_item_undefined }},
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
{{ cookiecutter.__mr_term }}
{%- else %}
{{ cookiecutter.__mr_term }},
discussion
{%- endif %}
or issue
that does not provide a "why"
with sufficient context,
the team member is responsible
for getting the why
and, if needed,
working with the maintainers
to ensure that
it is adequately documented
and communicated
to give context
to other team members.
In the absence of a why,
team members may
speculate the why.
This is something
that can lead to disruption
and inefficiency.

### Operate with a Bias for Action

> Adapted from the [GitLab Values][values5].

It's important that
we keep our focus on action,
and don't fall into the trap
of analysis paralysis
or sticking to
a slow, quiet path
without risk.
Decisions should
be thoughtful,
but delivering fast results
requires the fearless acceptance
of occasionally making mistakes;
our bias for action
also allows us
to course correct quickly.
Try to get results
as fast as possible,
but without compromising
consistency,
quality
or jostling
our general practices
when working together.

### Interactions Enable Insights

At {{ cookiecutter.project_name }},
we approach every single interaction
– with other contributors,
users,
the codebase,
the configuration files
and documentation –
as a stimulant
to keep our minds acute,
allowing us
to tie elements previously unnoticed
that echo through the project.

Interact with elements of the project
with an observant spirit,
there is always an unseen factor.
Capture insights
and reflect upon their meaning
and implications
for the project
and your work.
Software development is human
at its core,
and [**human systems are inherently complex**][values6].
We should not let
all the code,
interfaces
and systems
we handle on our work
obscure the fact
that we pursue
building a template
so it can be useful
and cherished by others.

### Sharing Insights Drives Progress

By extracting the root
of those four values,
we have conceived
a fifth value of our own
to steer our development philosophy.
This principle is fundamental
to how we approach
collaboration,
documentation,
and community engagement.
It emphasises the importance of
actively sharing knowledge,
experiences,
and ideas
to foster a culture
keen to exercising **continuous improvement**.
By embracing this value,
we aim to create
an environment
where both contributors
and users
feel empowered
to learn,
cooperate
and grow together.

In practical terms,
this means that
we prioritise clear and concise documentation of knowledge,
ensuring that
relevant information
is easily accessible
to all interested parties.
This includes
maintaining up-to-date
guides,
tutorials
and reference materials
that reflect the current state of the project;
articulating thought processes,
design decisions
and problem-solving strategies
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
in issue and {{ cookiecutter.__mr_term }} discussions;
{%- else %}
in issues, discussions and {{ cookiecutter.__mr_term }}s;
{%- endif %}
providing the adequate guidance
for new contributors
to succeed in their first development;
storing ideas
generated from discussions
into work items
for future prioritisation.

By doing so,
we facilitate
a deeper understanding
of the project's internals
and evolution,
making it easier for new contributors
to get started
and for users
to understand
how to make the most
out of our project.
This also reinforces that
recognising even small efforts,
such as adding a link
to a useful resource
or explaining a complex concept
in simpler terms,
can significantly impact
the value of the project
to someone else.

{% if cookiecutter.licence != 'nos' -%}
### There Are no Good First Issues

The concept of
labelling issues in open source projects
to mark potential good contributions
for a first timer
has its origins in the [First Timers Only][values7] initiative
by Kent C. Dodds.

At {{ cookiecutter.project_name }},
we tackle the notion of Good First Issues
in a different way.
We believe that
enabling development from new contributors
is an integral part
of keeping an open source project active,
but it takes more
than a label in an issue tracker
to succeed.
The notion that
people can just browse repositories
and search for a contribution
is invalid,
most of what is labelled
needs more context
for any one new contributor
to approach it.
This is represented by our philosophy:

<div align="center">

_The best good first issues are the ones you open yourself._

</div>

- For **upstream developers**,
  this means understanding that
  not all developments mapped by you
  should be _delivered_ by you.
  If the change in question
  can be considered relevant
  for introducing a new contributor
  to the project,
  time should be dedicated
  in ensuring the change
  _can_ be delivered by them,
  through work item refinement
  and clear steps
  to conclude the demand,
  instead of being delivered
  without ever
  granting an opportunity for someone
  – and the community –
  to grow.
  This also means
  being available
  to [orient][community] contributors
  should they feel lost
  and reassure [clear communication][behaviour]
  with them;
- For **{{ cookiecutter.project_name }} users**
  who have opened a request
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  on the Issue Tracker,
{%- else %}
  on the Issue Tracker
  or GitHub Discussions,
{%- endif %}
  this means that
  the best solution to your request
  is to deliver it yourself!
  By approaching your requests
  as a gateway to contributing to the project,
  you generate growth opportunities
  to yourself and the team.
  If upon opening your request
  you feel inclined
  to come forward and help resolve it yourself,
  mark it with the appropriate label
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  by adding `/label ~"up-for-a-change"`
  to the request description
{%- else %}
  by adding the `up-for-a-change` label
  to the request being opened
{%- endif %}
  so that a developer can mentor you
  on the solution.

{% endif -%}
## :speaking_head: Proposing Changes as a Developer

{% if cookiecutter.app_type in ['tui', 'hybrid'] -%}
<!-- DEFINE the context and purposes of your library -->
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
  - [`tui/`][changes0a] contains the entire logic
    for rendering and controlling
    the terminal interface
    with [Textual][changes0b];
    this includes
    interface components
    (i.e.,
    widgets,
    screens,
    layouts
    etc.),
    styles
    and themes;
  - [`cli/`][changes1] structures
    the available commands
    to control the application
    from the command-line
    using [Typer][changes2],
    including launching the TUI;
- Backend components
  to enable fluid experience:
  - [`config/`][changes3] defines
    the API necessary
    for manipulating configuration files,
    used to store user-specific data,
    application state
    and customisation options;
  - [Logging][changes4] customisations
    to be rendered
    as the program output
    or as structured files
    for debugging purposes;
- [Tests][apptopic6]
  for validating program behaviour
  as expected;
- [Tasks][changes5] aimed at
  improving
  and speeding up
  local development
  with [Invoke][changes6].

{% elif cookiecutter.app_type == 'cli' -%}
<!-- DEFINE the context and purposes of your library -->
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
  - [`cli/`][changes1] structures
    the available commands
    to control the application
    from the command-line
    using [Typer][changes2],
    including launching the TUI;
- Backend components
  to enable fluid experience:
  - [`config/`][changes3] defines
    the API necessary
    for manipulating configuration files,
    used to store user-specific data,
    application state
    and customisation options;
  - [Logging][changes4] customisations
    to be rendered
    as the program output
    or as structured files
    for debugging purposes;
- [Tests][apptopic6]
  for validating program behaviour
  as expected;
- [Tasks][changes5] aimed at
  improving
  and speeding up
  local development
  with [Invoke][changes6].

{% else -%}
<!-- DEFINE the context surrounding your library, detailing the main modules for code maintenance and their purpose -->

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
  - The [`README`][readme] file,
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

### Preparing to Contribute

#### Choosing What to Contribute

[![Needs Triage][badge3]][query3]

Everyone benefits
if contributors focus on changes
that are useful,
clear,
easy to evaluate,
and already pass basic checks.

Sometimes,
a contributor will already have
a particular new change or fix
in mind.
If seeking ideas,
consult the list of [starter assignments][query5].

Before proceeding,
contributors should evaluate
if the proposed change
is likely to be
relevant,
new
and actionable:

- Is it clear
  that code or configuration files
  must change?
  Proposing a {{ cookiecutter.__mr_term }} is appropriate
  only when a clear problem
  or beneficial change
  has been identified.
  If simply having trouble using {{ cookiecutter.project_name }},
  go through the [`README`][readme] file and links directing
  to support content first,
  rather than consider filing an issue
  or proposing an {{ cookiecutter.__mr_acronym }}.
  When in doubt,
  email [`{{ cookiecutter.email }}`][topic5] first
  about the possible change;
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
- Search the [Issue Tracker][intro1]
{%- else %}
- Search the [Issue Tracker][intro1],
  [Discussions page][intro3]
{%- endif %}
  and [past {{ cookiecutter.__mr_term }}s][intro2]
  for related discussions.
  Often,
  the problem has been discussed before,
  with a resolution
  that doesn't require a code or configuration change,
  or recording what kinds of changes
  will not be accepted as a resolution;
- Otherwise,
  if a logically similar issue or {{ cookiecutter.__mr_acronym }} already exists,
  then contribute to the discussion first,
  instead of creating a new one;
- Is the scope of the change
  matched to the contributor's level of experience?
  Anyone is qualified
  to suggest a typo fix,
  but refactoring core scheduling logic
  requires much more understanding
  of the underlying tool/code.
  Some changes require building up experience first.

{% if cookiecutter.app_type != 'bare_repo' -%}
It's worth emphasizing that
changes to CLI commands
{%- if cookiecutter.app_type != 'cli' %}
and interface elements
{%- endif %}
available for users in {{ cookiecutter.project_name }}
are more complex to implement
as it requires
a potential overhaul of the public API.
They will be subjected
to more scrutiny,
and held to a higher standard of review
than changes
to less fundamental building blocks.

{% endif -%}
#### Opening Admissible {{ cookiecutter.__mr_term }}s

For developers and maintainers,
changes should not be approached
in a reactive way
as demands,
but as a proactive **proposals**.
If you are contributing in the {{ cookiecutter.project_name }} repository,
you are expected
to always act on
and provide proposals
to improve the state of the project.
This distinguishes developers
from {{ cookiecutter.project_name }} users who,
unfamiliar with the codebase
and project configuration,
are only able to _request_ changes
through the Issue Tracker{% if cookiecutter.__scm_platform_lc == 'github' %} and GitHub Discussions{% endif %}.

To work under
a proactive proposal mindset,
we always [start with a {{ cookiecutter.__mr_term }}][swmr].

It is best
to follow these best practices
when proposing changes:

- **Always** use one of the [{{ cookiecutter.__mr_term }} templates][prepare1],
  applying the proper type
  to the change being proposed.
  Each template contains
  a brief summary detailing
  under which circumstances
  it is best employed.
  This helps coordinate discussions
  with the rest of the team
  and facilitates the reviewer's work;
- If the change is non-trivial,
  we encourage you
  to start a discussion
  with a maintainer
  or another member of the team.
  You can do this
  by tagging them in an {{ cookiecutter.__mr_acronym }}
  before submitting the code for review.
  Talking to team members
  can be helpful
  when making design decisions.
  Communicating the [intent][swnjw] behind your changes
  can also help expedite {{ cookiecutter.__mr_term }} reviews;
- Follow our [commit customs][committing],
  as consistent commit messages
  that follow these guidelines
  make the history more readable.

Also equally important
is the notion to
**keep {{ cookiecutter.__mr_acronym }}s simple**,
with the amount of changes in a single {{ cookiecutter.__mr_acronym }}
as small as possible.
If you want
to contribute a large feature,
think carefully about
what the minimum valuable change is.
Can you split the functionality
into two smaller {{ cookiecutter.__mr_acronym }}s?
Can you submit
only a fraction of the code?
Can you start
with a minimal proof-of-concept?
Can you do
just a part of the refactor?

<div align="center">

_Live by smaller iterations._

</div>

Small {{ cookiecutter.__mr_acronym }}s
which are more easily reviewed
lead to higher code quality,
which is more important to {{ cookiecutter.project_name }}
than having a minimal commit log.
The smaller an {{ cookiecutter.__mr_acronym }} is,
the more likely it will be merged quickly.
After that
you can send more {{ cookiecutter.__mr_acronym }}s
to enhance and expand the feature.
The [_How to Get Faster PR Reviews_][prepare2] guide
from the Kubernetes team
also has some great points regarding this.

#### Review Criteria

Before considering how to contribute,
it's useful to understand
how contributions are reviewed,
and why changes may be rejected.
See the detailed [guide][prepare3] for code reviewers
from Google's Engineering Practices documentation.
Simply put,
changes that have many or large positives,
and few negative effects or risks,
are much more likely
to be merged,
and merged quickly.
Risky and less valuable changes
are unlikely to be merged,
and may be rejected outright
rather than receive iterations of review.

Below is a non-exhaustive list
of traits
a contribution might have
that either enhances or hinders
its probability of being merged:

- **Positives:**
  - Fixes the root cause of a bug
    in existing functionality;
  - Adds functionality
    or fixes a problem
    needed by a large number of users;
  - Simple,
    targeted;
  - Maintains or improves
    template consistency;
  - Easily tested;
    has tests;
  - Reduces complexity,
    lines of code
    and configuration;
  - Change has already been discussed
    and is known
    to committers;
- **Negatives, risks:**
  - Band-aids
    a symptom of a bug only
    without addressing its root cause;
  - Introduces complex new functionality,
    especially an API
    that needs to be supported;
  - Adds complexity
    that only helps
    a niche use case;
  - Changes a public API
    or semantics
    (rarely allowed);
  - Adds large dependencies;
  - Changes versions
    of existing dependencies
    without proper testing;
  - Adds a large amount of code;
  - Makes lots of modifications
    in one "big bang" change.

### Development Workflow

After cloning {{ cookiecutter.project_name }}
and following the [development setup][setup],
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

As a developer,
please be conscious
of crucial steps to validate
before submitting your changes.
A non-exhaustive list of steps to consider:

- Did you add
  or modify unit tests
  if development involved
  changes to the API?
- Did you
  flag the tests
  with the appropriate
  Pytest marks?
- Have you covered
  possible edge cases
  which might not be clear
  on first thought?
- Are all checks passing
  with `invoke sweep`?
{%- if cookiecutter.__coverage_lc == 'codacy' %}
- Did you address
  all issues raised by Codacy
  for the {{ cookiecutter.__mr_term }} branch in question?
{%- endif %}
{%- if cookiecutter.app_type != 'bare_repo' %}
- Have any changes been made
  to how the default configuration
  file is structured?
  Can pre-existing user configuration
  still be used
  after these changes
  without crashing the application?
- Do changes secure
  user data integrity,
  without any data losses?
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
- Have changes been made
  to the frontend components?
  Did you check
  that these changes do not
  degrade,
  corrupt
  or crash
  the user interface?
{%- endif %}
{%- else %}
<!-- DEFINE common checks developers should make related specifically to your project's public API -->
{%- endif %}

#### Test Markers

When writing tests,
we strongly encourage developers
{%- if cookiecutter.use_bdd %}
to leverage [feature file tags][workflow1]
{%- else %}
to leverage [custom Pytest markers][workflow1]
{%- endif %}
to improve test collection
and organisation.
This allows the team
to get more context
if tests start to fail
after introducing a change.

The following markers are specified
in [`pyproject.toml`][workflow2]:

|     Marker      | Specification                                                                                                                   |
| :-------------: | ------------------------------------------------------------------------------------------------------------------------------- |
|    `backend`    | Tests validating the behaviour of back end components.                                                                          |
|   `frontend`    | Tests validating the behaviour of the user-facing components.                                                                   |
{%- if cookiecutter.app_type != 'bare_repo' %}
|      `cli`      | Tests validating command-line interface behaviour.                                                                              |
{%- endif %}
|   `standard`    | Tests defining behaviour for program operations considered the standard procedure.                                              |
|  `validation`   | Tests related to data input validation and handling.                                                                            |
|     `edge`      | Tests defining the expected behaviour of the program in edge cases.                                                             |
|   `security`    | Tests validating security aspects of the program.                                                                               |
|  `performance`  | Tests aimed at certifying expected performance from program operations, usually against benchmarks.                             |
|  `persistence`  | Tests which certify that data is consistently and correctly persisted.                                                          |
|    `config`     | Tests related to modifications in user configuration for the program.                                                           |
| `customization` | Tests related to customization options.                                                                                         |
| `compatibility` | Tests validating compatibility of {{ cookiecutter.project_name }} across its different versions.                                |
|     `async`     | Tests validating asynchronous code.                                                                                             |
|  `integration`  | Tests certifying integration with external services, libraries and platforms.                                                   |
|   `database`    | Tests specifically aimed at validating database operations.                                                                     |
|      `api`      | Tests validating integration with external API schemas.                                                                         |
|   `identity`    | Tests related to user identity verification and validation.                                                                     |
|  `networking`   | Tests validating expected connection standards and quality to other services, whether internal or external.                     |
|  `monitoring`   | Tests certifying that program healthchecks provide the necessary information to external systems and files in case of failures. |

To propose changes
to the marker options,
do so through a [Project Policy Proposal][roadmap1].

#### Feature Flags

<!-- DEFINE the guidelines on how to implement and handle feature flags -->

### {{ cookiecutter.__mr_term }} Review Process

After [starting with a {{ cookiecutter.__mr_term }}][swmr],
ensuring you have opened an [admissible {{ cookiecutter.__mr_acronym }}][admission]
and have finished contributing with changes,
the review process can start.

#### Contribution Acceptance Criteria

To make sure that
your {{ cookiecutter.__mr_term }} can be approved,
ensure that
it meets the contribution acceptance criteria below:

1. The change is
   as small as possible;
2. If the {{ cookiecutter.__mr_term }} contains
   more than 500 changes:
   - Explain the reason;
   - Mention a maintainer;
3. Mention any major breaking changes;
4. Include proper tests
   and make all tests pass
   (unless it contains a test
   exposing a bug in existing code);
   - If a failing CI build
     seems to be
     unrelated to your contribution,
     you can try restarting the failing CI job,
     rebasing on top of the target branch
     to bring in updates
     that may resolve the failure,
     or if it has not been fixed yet,
     ask a developer
     to help you fix the test;
5. The {{ cookiecutter.__mr_acronym }} contains
   a few logically organised commits,
{%- if cookiecutter.commit_convention == 'gitmoji' %}
   using [Gitmoji][convention].
{%- elif cookiecutter.commit_convention == 'conventional' %}
   using [Conventional Commits][convention].
{%- else %}
   using [Conventional Gitmoji][convention].
{%- endif %}
   We do not apply the squash method
   for merging changes;
6. The changes can merge
   without problems.
   If not,
   you should rebase
   if you're the only one working
   on your feature branch,
   otherwise merge the default branch
   into the {{ cookiecutter.__mr_acronym }} branch;
7. Only one specific issue is fixed
   or one specific feature is implemented.
   Do not combine things;
   send separate {{ cookiecutter.__mr_term }}s
   for each issue or feature;
8. Contains functionality
   that other users will benefit from;
9. Changes do not degrade performance;
10. If the {{ cookiecutter.__mr_term }} adds
    any new dependencies,
    they should conform
    to our existing licence;
    also,
    make the reviewer aware
    of the new library
    and explain
    why you need it.

#### Getting Reviewed

As soon as you have changes to review,
have the changes reviewed
by a reviewer.
The reviewer can:

- Give you a second opinion
  on the chosen solution
  and implementation;
- Help look for
  bugs,
  logic problems,
  or uncovered edge cases.

If the {{ cookiecutter.__mr_term }}
is small and straightforward
to review,
you can skip the reviewer step
and directly ask a maintainer.

What constitutes "small and straightforward"
is a gray area.
Here are some examples
of small and straightforward changes:

- Fixing a typo
  or making small copy changes;
- A tiny refactor
  that doesn't change
  any behaviour
  or data;
- Removing unused functions,
  classes
  and methods;
- A well-understood logic change
  that requires changes
  to 5 lines of code
  or less.

Otherwise,
a {{ cookiecutter.__mr_term }} should be first
reviewed by a reviewer
in each domain
(e.g., CI,
backend,
frontend
etc.)
the {{ cookiecutter.__mr_acronym }} touches,
as maintainers may
not have the relevant domain knowledge.
This also helps
to spread the workload.

Depending on the areas
your {{ cookiecutter.__mr_term }} touches,
it must be approved
by one or more maintainers.

Getting your {{ cookiecutter.__mr_term }} merged
also requires a maintainer.
If it requires more than one approval,
the last maintainer
to review and approve merges it.

### Roles and Attributions

#### The Responsibility of the {{ cookiecutter.__mr_term }} Author

The responsibility to
find the best solution
and implement it
lies with the {{ cookiecutter.__mr_term }} author.
The author stays assigned
to the {{ cookiecutter.__mr_term }}
as the assignee
throughout the code review lifecycle.
If you are unable
to set yourself as an assignee,
ask a reviewer
to do this for you.

Before requesting
a review from a maintainer
to approve and merge,
they should be confident that:

- It actually solves the problem
  it was meant to solve;
- It does so
  in the most appropriate way;
- It satisfies all requirements;
- There are no remaining
  bugs,
  logical problems,
  uncovered edge cases,
  or known vulnerabilities.

The best way to do this,
and to avoid
unnecessary back-and-forth
with reviewers,
is to perform a self-review
of your own {{ cookiecutter.__mr_term }},
following the [Code Review][review] guidelines.
During this self-review,
try to include
comments in the {{ cookiecutter.__mr_acronym }} on lines
where decisions or trade-offs were made,
or where a contextual explanation
might aid the reviewer
in more easily
understanding the code.

To reach
the required level of confidence
in their solution,
an author is expected
to involve other people
in the investigation
and implementation processes
as appropriate,
with the goal of:

- Discussing different solutions
  or getting an implementation reviewed;
- Getting an in-depth review
  of the solution;
- Clearing up confusion
  or verify that
  the end result matches
  what the team
  had in mind.

If you know
you'll need many {{ cookiecutter.__mr_term }}s
to deliver a feature
– for example,
you created a proof of concept
and it is clear the feature
will consist of 10+ {{ cookiecutter.__mr_term }}s –,
consider identifying reviewers and maintainers
who possess the necessary understanding
of the feature
(you share the context with them).
Then direct all {{ cookiecutter.__mr_term }}s
to these reviewers.
Having stable reviewer counterparts
for multiple {{ cookiecutter.__mr_term }}s with the same context
improves efficiency.

Before the review,
the author is requested
to submit comments
on the {{ cookiecutter.__mr_term }} diff
alerting the reviewer
to anything important
as well as for anything
that demands further explanation
or attention.
Examples of content
that may warrant a comment
could be:

- The addition of a linting rule;
- The addition of a dependency;
- Where not obvious,
  a link to
  the parent class
  or method;
- Any benchmarking performed
  to complement the change;
- Potentially insecure code.

If there are any
projects,
snippets,
or other assets
that are required for a reviewer
to validate the solution,
ensure they have access
to those assets
before requesting review.

When assigning reviewers,
it can be helpful
to add a comment indicating
which _type_ of review
you are looking for that reviewer.
Explicitness around {{ cookiecutter.__mr_acronym }} review types
is efficient for the {{ cookiecutter.__mr_acronym }} author
because they receive the type of review
that they are looking for
and it is efficient for the {{ cookiecutter.__mr_acronym }} reviewers
because they immediately know
which type of review to provide.

Avoid:

- Adding `TODO` comments
  directly to the source code
  unless the reviewer requires you
  to do so.
  If `TODO` comments are added
  due to an actionable task,
  include a link
  to the relevant issue;
- Adding comments
  which only explain
  what the code is doing.
  If non-`TODO` comments are added,
  they should explain [why, not what][swnjw];
- Requesting maintainer reviews
  of {{ cookiecutter.__mr_term }}s with failed tests.
  If the tests are failing
  and you have to
  request a review,
  ensure you leave a comment
  with an explanation.

This saves reviewers time
and helps authors catch mistakes earlier.

##### Recommendations to Get Your Changes Merged Faster

1. Make sure
   to follow best practices:
   - Write
     efficient instructions,
     add screenshots,
     steps to validate
     etc.;
   - Follow the acceptance checklist
     for the {{ cookiecutter.__mr_acronym }} template;
2. Follow the {{ cookiecutter.project_name }} patterns,
   even if you think there's a better way.
   Discussions often delay merging code.
   If a discussion is getting too long,
   consider following
   the documented approach
   or the maintainer's suggestion,
   then open a separate {{ cookiecutter.__mr_acronym }}
   to implement your approach
   as part of our best practices
   and have the discussions there;
3. Consider splitting big {{ cookiecutter.__mr_acronym }}s
   into smaller ones.
   Around 200 lines is a good threshold:
   - Smaller {{ cookiecutter.__mr_acronym }}s reduce cognitive load
     for authors and reviewers;
   - Reviewers tend
     to pick up smaller {{ cookiecutter.__mr_acronym }}s
     to review first
     (a large number of files
     can be scary);
   - Discussions on one particular part of the code
     will not block
     other parts of the code
     from being merged;
   - Smaller {{ cookiecutter.__mr_acronym }}s are often simpler,
     and you can consider
     skipping the first review
     and sending directly
     to the maintainer,
     or skipping one of the suggested domains
     (e.g.,
     CI,
     backend,
     frontend
     etc.);
   - :warning: Split {{ cookiecutter.__mr_acronym }}s with caution:
     {{ cookiecutter.__mr_acronym }}s that are too small
     increase the number of total reviews,
     which can cause the opposite effect;
4. Minimise the number of reviewers
   in a single {{ cookiecutter.__mr_acronym }}.

##### Recommendations for Facilitating Reviews

Keep in mind that
code review is a process
that can take multiple iterations,
and reviewers may spot things
later that they may not have seen
the first time.

- The first reviewer of your code is you.
  Before you perform that first push
  of your shiny new branch,
  read through the entire diff.
  Does it make sense?
  Did you include something
  unrelated to the overall purpose
  of the changes?
  Did you forget to
  remove any debugging code?
- Write a detailed description
  as outlined in the [{{ cookiecutter.__mr_term }} guidelines][admission].
  Some reviewers may not be familiar
  with the product feature
  or area of the codebase.
  Thorough descriptions help all reviewers
  understand your request
  and test effectively;
- If you know your change depends
  on another being merged first,
  note it in the description
  and set a {{ cookiecutter.__mr_term }} dependency;
- Be grateful
  for the reviewer's suggestions
  ("Good call. I'll make that change.");
- Don't take it personally.
  The review is of the code,
  not of you;
- Explain [why][swnjw] the code exists
  ("It's like that because of these reasons.
  Would it be more clear
  if I rename this class/file/method/variable?");
- Extract unrelated changes
  and refactoring tasks
  into future {{ cookiecutter.__mr_acronym }}s/issues;
- Seek to understand
  the reviewer's perspective;
- Try to respond to every comment;
- The {{ cookiecutter.__mr_term }} author
  resolves only the threads
  they have fully addressed.
  If there's
  an open reply,
  an open thread,
  a suggestion,
  a question,
  or anything else,
  the thread should
  be left to be resolved
  by the reviewer;
- It should not be assumed
  that all feedback requires their recommended changes
  to be incorporated into the {{ cookiecutter.__mr_acronym }}
  before it is merged.
  It is a judgment call
  by the {{ cookiecutter.__mr_acronym }} author
  and the reviewer
  as to if this is required,
  or if a follow-up issue
  should be created
  to address the feedback
  in the future
  after the {{ cookiecutter.__mr_acronym }} in question is merged;
- Request a new review
  from the reviewer
  once you are ready
  for another round of review.
  If you do not have
  the ability to request a review,
  `@` mention the reviewer instead.

#### The Responsibility of the Reviewer

All {{ cookiecutter.project_name }} contributors
who choose to review
and provide feedback on {{ cookiecutter.__mr_term }}s
have a responsibility to
both the project
and the individual making the contribution.
Reviews and feedback must be
helpful,
insightful,
and geared towards
improving the contribution
as opposed to
simply blocking it.
Do not expect
to be able to block a {{ cookiecutter.__mr_term }}
from advancing simply
because you say "No" without [giving an explanation][swnjw].
Be open to having your mind changed.
Be open to working with the contributor
to make the {{ cookiecutter.__mr_term }} better.

Reviews that are
dismissive
or disrespectful
of the contributor
or any other reviewers
are strictly counter
to the [Code of Conduct][cc2].

When reviewing a {{ cookiecutter.__mr_term }},
the primary goals are
for the codebase to improve
and for the person submitting the request to succeed.
Even if a {{ cookiecutter.__mr_term }} does not land,
the submitters should come away from the experience
feeling like their effort
was not wasted
or unappreciated.
Every {{ cookiecutter.__mr_term }} from a new contributor
is an opportunity to grow the community.

Review a bit at a time,
do not overwhelm new contributors.
It is tempting to micro-optimise
and make everything about
relative performance,
perfect grammar,
or exact style matches.
Do not succumb to that temptation.

Focus first
on the most significant aspects of the change:

- Does this change make sense for {{ cookiecutter.project_name }}?
- Does this change make {{ cookiecutter.project_name }} better,
  even if only incrementally?
- Are there clear bugs
  or larger scale issues
  that need attending to?
- Are the commit messages
  readable and correct?
- If it contains a breaking change,
  is it clear enough?

Understand why the change is necessary
(fixes a bug,
improves the user experience,
refactors the existing code).
Then:

- Try to be thorough in your reviews
  to reduce the number of iterations;
- Communicate
  which ideas you feel strongly about
  and those you don't;
- Identify ways
  to simplify the code
  while still solving the problem;
- Offer alternative implementations,
  but assume the author
  already considered them
  ("What do you think about using a custom validator here?");
- Seek to understand
  the author's perspective;
- Check out the branch,
  and test the changes locally.
  You can decide how much manual testing
  you want to perform.
  Your testing might result
  in opportunities
  to add automated tests;
- If you don't understand a piece of code,
  _say so_.
  There's a good chance someone else
  would be confused by it
  as well;
- Ensure the submitter is clear on
  what is required from them
  to address/resolve the suggestion;
- Ensure there are no open dependencies.
  Check linked issues for blockers.
  Clarify with the submitters if necessary.
  If blocked by one or more open {{ cookiecutter.__mr_acronym }}s,
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
  set an [{{ cookiecutter.__mr_acronym }} dependency][reviewing0];
{%- else %}
  mention the blocking {{ cookiecutter.__mr_acronym }}
  in the discussion;
{%- endif %}
- After a round of line notes,
  it can be helpful
  to post a summary note
  such as "Looks good to me",
  or "Just a couple things to address";
- Let the submitter know
  if changes are required following your review.

When changes are necessary,
**request** them,
do not _demand_ them,
and do not assume
that the submitter already knows
how to add a test
or run a benchmark.

Specific
performance optimization techniques,
coding styles,
and conventions
change over time.
**The first impression you give to a new contributor never does.**

[Nits][reviewing1]
(requests for small changes
that are not essential)
are fine,
but try to avoid
stalling the {{ cookiecutter.__mr_term }}.
Most nits can typically be fixed by the reviewer
but they can also be
an opportunity for the contributor
to learn a bit more about the project.

It is always good to
clearly indicate nits
when you comment
(e.g.,
`Nit: change foo() to bar(). But this is not blocking.`).

**Be aware of the person behind the change:**
_how_ you communicate requests and reviews in your feedback
can have a significant impact
on the success of the {{ cookiecutter.__mr_term }}.
Yes,
we may land a particular change
that makes {{ cookiecutter.project_name }} better,
but the individual might just not want
to have anything to do with {{ cookiecutter.project_name }}
ever again.
The goal is not just
having good code,
you should guide the author
towards succeeding
with their contributions,
whether the {{ cookiecutter.__mr_acronym }} is approved or not
in the end.

Lastly,
**accept that there are different opinions about what belongs in {{ cookiecutter.project_name }}.**
It is not uncommon for contributors
to suggest new features they feel
would make {{ cookiecutter.project_name }} better.
These may or may not make sense to add,
but as with all changes,
be courteous in
how you communicate your stance on these.
Comments that make the contributor feel
like they should have "known better"
or ridiculed for even trying
run counter to the [Code of Conduct][cc2].

##### The Right Balance

One of the most difficult things
during code review
is finding the right balance
in how deep the reviewer
can interfere with the code
created by a submitter.

- Learning how to find the right balance takes time;
  that is why we have reviewers
  that become maintainers
  after some time spent
  on reviewing {{ cookiecutter.__mr_term }}s;
- Finding bugs is important,
  but thinking about good design
  is important as well.
  Building abstractions and good design
  is what makes it possible
  to hide complexity
  and makes future changes easier;
- Enforcing and improving [codestyle][codestyle]
  should be primarily done
  through automation
  instead of review comments;
- Asking the submitter
  to change the design
  sometimes means
  the complete rewrite
  of the contributed code.
  It's usually a good idea
  to ask another maintainer or reviewer
  before doing it,
  but have the courage to do it
  when you believe it is important;
- In the interest of iteration,
  if your review suggestions are
  non-blocking changes,
  or personal preference
  – not a documented or agreed requirement –,
  consider approving the {{ cookiecutter.__mr_term }}
  before passing it back
  to the submitter.
  This allows them
  to implement your suggestions
  if they agree,
  or allows them to pass it
  onto the maintainer for review
  straight away.
  This can help
  reduce our overall time-to-merge;
- There is a difference
  in doing things right
  and doing things _right now_.
  Ideally,
  we should do the former,
  but in the real world
  we need the latter as well.
  A good example
  is a security fix
  which should be released
  as soon as possible.
  Asking the submitter
  to do a major refactoring
  in a {{ cookiecutter.__mr_term }} that is an urgent fix
  should be avoided;
- Doing things well today is usually better
  than doing something perfectly tomorrow.
  Shipping a kludge today is usually worse
  than doing something well tomorrow.
  When you are not able
  to find the right balance,
  ask other people
  about their opinion
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
  and use the [`seeking-contributors::opinion`][query2] label.
{%- else %}
  and use the [`seeking-input`][query2] label.
{%- endif %}

#### The Responsibility of the Maintainers

Maintainers are responsible for
the overall health,
quality,
and consistency
of the {{ cookiecutter.project_name }} codebase.

Consequently,
their reviews focus primarily
on things like
overall architecture,
code organization,
separation of concerns,
tests,
DRYness,
consistency,
and readability.

Because a maintainer's job only depends
on their knowledge of the overall {{ cookiecutter.project_name }} codebase,
and not that of any specific domain,
they can review,
approve,
and merge {{ cookiecutter.__mr_acronym }}s
from any type of changes.

Maintainers are the responsible individuals
of assuring that the acceptance criteria of a {{ cookiecutter.__mr_term }}
are reasonably met.
In general,
quality is everyone's responsibility,
but maintainers are held responsible
for ensuring that an {{ cookiecutter.__mr_acronym }}
meets those general quality standards.
This includes
avoiding the creation of technical debt
in follow-up issues.

Maintainers do their best
to also review the specifics
of the chosen solution
before merging,
but as they are not necessarily domain experts,
they may be poorly placed to do so
without an unreasonable investment of time.
In those cases,
they defer to the judgment
of the submitter and earlier reviewers,
in favour of focusing
on their primary responsibilities.

If a developer who happens to also be a maintainer
was involved in a {{ cookiecutter.__mr_term }} as a reviewer,
it is recommended that
they are not also picked
as the maintainer to
ultimately approve and merge it.

Maintainers should check before merging
if the {{ cookiecutter.__mr_term }} is approved
by the required approvers.
If still awaiting further approvals from others,
`@` mention the submitter
and explain why in a comment.

{% if cookiecutter.licence != 'nos' -%}
### How to Behave among Other Contributors

{{ cookiecutter.__mr_term }}s,
when worked under the concept of [proposals][admission],
turn into
live and open discussions.
Whenever contributing to these discussions,
please remind of the following
to write your comments:

- Be kind;
- Accept that
  many programming decisions are opinions.
  Discuss trade-offs,
  which you prefer,
  and reach a resolution quickly;
- Ask questions;
  don't make demands
  ("What do you think about naming this `user_id`?");
- Ask for clarification
  ("I didn't understand. Can you clarify?");
- Avoid selective ownership of code
  ("mine",
  "not mine",
  "yours");
- Avoid using terms
  that could be seen as
  referring to personal traits
  ("dumb",
  "stupid").
  Assume everyone is intelligent
  and well-meaning;
- Be explicit.
  Remember people don't always
  understand your intentions online;
- Be humble
  ("I'm not sure, let's look it up.");
- Don't use hyperbole
  ("always",
  "never",
  "endlessly",
  "nothing");
- Be careful about the use of sarcasm.
  Everything we do is public;
  what seems like good-natured ribbing
  to you and a long-time colleague
  might come off as mean and unwelcoming
  to a person new to the project;
- If you ask a question
  to a specific person,
  always start the comment
  by mentioning them;
  this ensures they see it
  if their notification level
  is set to "mentioned"
  and other people understand
  they don't have to respond.

### Fostering an Inviting Community

As a {{ cookiecutter.project_name }} contributor, your responsibilities
are not supposed to be restricted to
code,
commits
and work items only.
Software development is an act of collaboration,
and collaboration is inherently human in nature.
Our desire is
to build an outstanding product,
but it will be even more successful
if it can be built
with an ever growing community of contributors.

However,
the hard part of
getting into open source for the first time
isn't the implementation of a feature,
but **figuring out how to actually contribute with changes**.
That's why
ensuring new contributors can get started
is as important as contributing itself.
Open source projects live and die
by their communities,
if we as contributors are not doing our job
of fostering communal interactions,
maintaining the project might prove much harder
in the future.

There are two separate areas of action
in which actions can be taken
to achieve this goal:

1. Preserve an orderly environment:
   - Keep the `CONTRIBUTING` file up to date
     and always reflective of
     the project's current policies and guidelines.
     Successful projects that reach larger audiences
     are able to do so
     through ease of access
     to knowledge surrounding them;
   - Make a conscious attempt
     to keep code and configuration [organised][community1],
     with relevant implementation reasoning
     [documented][swnjw] via the commit description;
   - Maintain and update Git hooks
     to check and enforce any project standards
     so people don't have the frustration
     of going back and forth on the {{ cookiecutter.__mr_term }};
   - Maintain and update CI jobs
     to automate further development tasks
     and allow contributors to focus
     on delivering new features;
   - Be conscious of the [energy vampires][community2] perturbing development
     and either propose [actions][bias]
     for eliminating them
     or seek discussion and feedback
     via an [**Internal Improvement**][community3] {{ cookiecutter.__mr_acronym }};
   - Keep the {{ cookiecutter.__scm_platform_base }} repository efficient
     by properly labelling work items
     and associating them
     with the relevant project milestone;
2. Become an advocate for new contributors:
   - Be overly conscious of [how to behave][behaviour]
     when interacting with a user
     publishing their first request.
     The guidelines for [reviewers][reviewer] also apply
     when communicating with {{ cookiecutter.project_name }} users
     in their requests;
   - Before jumping
     to resolve a request opened by a user,
     the best thing you can do
     is to open a sea of opportunities:
     **invite the author to solve the request together**
     and in the process
     grant them their first contribution
     to the project.
     You already know the drill,
     use the space
     to guide them
     on our ways and standards,
     empower them to understand how the project operates.
     You have [started small][community4],
     so why not help someone else
     take this small first step?
   - Likewise,
     there are developments
     you could complete in less than 10 minutes.
     Why not turn them into [starter assignments][starter]?

#### About Starter Assignments

We refer to our "Good First Issue" work items
as **starter assignments**,
a term we believe better aligns
with our goal
of fostering a vibrant community
around {{ cookiecutter.project_name }}.
The term "good first issue"
often feels generic
and commoditised,
offering little incentive for newcomers
to engage deeply with the project.
In contrast,
"starter assignments" emphasise action
and significance,
providing value
for both new contributors
and developers
who create these opportunities.

Through stater assignments,
we aim to:

1. Offer a compelling resource
   that encourages developers
   to begin contributing to {{ cookiecutter.project_name }};
2. Enhance contributor onboarding
   by providing an alternative
   to simply pointing to documentation;
3. Encourage existing contributors
   to refine skills in
   technical writing,
   requirements specification,
   contextualisation
   and problem-solving organisation;
4. Elevate discussions
   around future developments
   by helping newcomers understand
   the project’s vision
   and enabling veterans
   to articulate ideas more clearly
   – ultimately leading to...
5. A broader pool of perspectives
   and proposals
   to amplify developments
   and help {{ cookiecutter.project_name }} thrive.

To achieve these goals,
it is essential
for current contributors
to identify opportunities
to turn ongoing work
into practical assignments
that new contributors can tackle
with ease.
Remember:
**designing starter assignments**
**is just as important**
**as developing new features**
– treat them
with the same care and dedication.

A few tips
to create high quality
starter assignments:

- Make them purpose-driven
  and connect them
  to greater goals of the project;
  good first issues exist
  solely for leaving a breadcrumb
  for the new contributor;
- Provide a clear path
  to the solution
  so someone else can implement it;
  you can leverage {{ cookiecutter.__scm_platform_base }}'s
  feed-like functionality
  and work item hierarchy
  to slice the solution
  in smaller chunks;
- Make it as easy as possible;
  say exactly where changes need to go,
  recommend a good approach
  and tie it in
  to project's goals
  and development standards.

For new contributors
who have picked up a starter assignment,
your mentor most likely
has made their best effort
to ensure the delivery steps
are as clear as possible.
However, if you ever feel stuck
or confused,
don't hesitate to seek help.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
Leverage [replies][community5]
{%- else %}
Leverage replies
{%- endif %}
and [reactions][roadmap3]
to direct your questions
and work together
with your mentor
so you can see your contribution delivered.

If you are not getting replies
from your mentor,
mention `@all`
in your starter assignment
and someone from the team
will reach out to you.

## :reminder_ribbon: Other Ways to Contribute

You can contribute to {{ cookiecutter.project_name }}
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

[![RFSs][badge11]][query11]

Inspired by [Typer's][help1] welcoming community
and their positive outlook
on the effect of [collective intelligence][help2],
we are committed to enabling an environment
in which such exponential interactions
can take place.
As such,
one of the best ways people can
contribute to {{ cookiecutter.project_name }}
is by helping others,
either users like you
who have reached the members of the project
with questions and requests
or the development team itself.

The most direct way
you can provide your help to others
is to look for open [Requests for Support][query11]
and try to answer other users' questions.
In many cases
you might already know the answer to them!

Just remember,
the most important point is:
**try to be kind**.
People come with their frustrations
and in many cases don't ask
in the best way,
but try as best as you can
to be kind.
As mentioned earlier,
we want this community
to the welcoming.

At the same time,
don't accept bullying
or disrespectful behaviour
towards others.
We have to take care of each other.
See the [Code of Conduct][cc2]
for more details
on how we deal with these cases.

#### Orientation for Effectively Helping Others

Here is a general guide
on how to help other users
with their requests:

1. Understand the request:
   - Check if you can understand
     what is the **purpose**
     and use case
     of the person asking;
   - Then check if the request is **clear**;
   - In many cases the question asked
     is about an imaginary solution
     from the user,
     but there might be a **better** one.
     If you can understand
     the problem and use case
     better,
     you might be able
     to suggest a better **alternative solution**;
   - If you can't understand the question,
     ask for more details;
2. Reproduce the problem:
   for most of the cases
   relating to issues and questions
   in general,
   most likely
   there's something
   related to the person's original code.
   In many cases
   they will only copy a fragment of the code,
   but that's not enough
   to reproduce the problem;
   - You can ask them
     to provide a [minimal, reproducible example][help3],
     that you can copy-paste
     and run locally
     to see the same error or behavior
     they are seeing,
     or to understand
     their use case better;
   - If you are feeling too generous,
     you can try
     to create an example like that
     yourself,
     just based
     on the description of the problem.
     Just have in mind that
     this might take a lot of time
     and it might be better
     to ask them
     to clarify the problem first;
3. Suggest solutions:
   - After being able to
     understand the question,
     you can give them
     a possible answer;
   - In many cases,
     it's better to understand
     their **underlying problem**
     or use case,
     because there might be a better way
     to solve it
     than what they are trying to do.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!tip] Tip: When Things are Difficult
When things are great,
everything is easier,
so that doesn't need much instructions.
When things are difficult,
here are some guidelines.

Try to find the good side.
In general,
if people are not being unfriendly,
try to thank their effort and interest,
even if you disagree
with the main subject,
just thank them
for being interested in the project,
or for having dedicated some time
to try to do something.

It's difficult to
convey emotion in text,
use emoji to help.
:wink:

In many requests
people bring their frustration
and show it without filter,
which can be displayed through
exaggerating,
complaining,
being entitled
etc.
That's really not nice,
and when it happens,
it lowers our priority
to solve their problems.
Still,
try to breathe,
and be gentle with your answers.

Try to avoid
using bitter sarcasm
or potentially passive-aggressive comments.
If something is wrong,
it's better to be direct
(try to be gentle)
than sarcastic.

Try to be
as specific and objective
as possible,
avoid generalisations.
>>>

{% else -%}
> [!TIP]
> **When Things are Difficult**
>
> When things are great,
> everything is easier,
> so that doesn't need much instructions.
> But when things are difficult,
> here are some guidelines.
>
> Try to find the good side.
> In general,
> if people are not being unfriendly,
> try to thank their effort and interest,
> even if you disagree
> with the main subject,
> just thank them
> for being interested in the project,
> or for having dedicated some time
> to try to do something.
>
> It's difficult to
> convey emotion in text,
> use emoji to help.
> :wink:
>
> In many requests
> people bring their frustration
> and show it without filter,
> which can be displayed through
> exaggerating,
> complaining,
> being entitled
> etc.
> That's really not nice,
> and when it happens,
> it lowers our priority
> to solve their problems.
> But still,
> try to breathe,
> and be gentle with your answers.
>
> Try to avoid
> using bitter sarcasm
> or potentially passive-aggressive comments.
> If something is wrong,
> it's better to be direct
> (try to be gentle)
> than sarcastic.
>
> Try to be
> as specific and objective
> as possible,
> avoid generalisations.

{% endif -%}
#### Commitment to Help

What consumes
most of the time of the development team
is actually answering questions
and solving problems.
We end up not being able
to add new features,
fix bugs
and review {{ cookiecutter.__mr_term }}s
as fast as we wanted
because too much of the time
is spent handling user requests.

Also, this is
on top of all the help
provided by several community members
that dedicate a lot of their time
to come here
and aid others.

If more {{ cookiecutter.project_name }} users
came to help others like them
just a little bit more,
it would be much less effort for them.

That's why our templates for requests
include a section
calling authors to action
with improving the {{ cookiecutter.project_name }} ecosystem
the best way they can.
For all purposes,
we believe that
contributions should be done by the person's own accord,
demonstrating a [bias for action][bias]
and fitting for
their perceived capacity
for helping.

Therefore,
we have implemented a **Commitment to Help** modus operandi,
kindly asking issue authors
to engage further
and help lessen demand overall.
If for every new request that comes
there is extra action from its author
to help with another project demand,
we strengthen our community
and improve,
bit by bit,
every aspect of {{ cookiecutter.project_name }}:
communication,
agility,
organization,
aggregated value
and more!

If you have opened
or are about to open
a Request for Support
or a Request for Improvement,
we would be extremely grateful
if you could pick one of the options
from the list provided in the template
to commit with additional help
for the project.

We thank you in advance
for your kindness and dedication!

### Contributing through User Requests

If you are simply
having trouble using {{ cookiecutter.project_name }},
go through the [`README`][readme] file and links
directing to support content first,
rather than filing a request.

{{ cookiecutter.project_name }} implements
three types of requests for users
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
through [Issue Templates][request1]:
{%- else %}
through [Issue][request1]
and [Discussion][request1a] templates:
{%- endif %}

- **Requests for Correction**;
- **Requests for Improvement**;
- **Requests for Support**.

All three templates
provide a brief summary
explaining their purpose,
as well as a handy information
on where to best use them.
They contain structured sections
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
with HTML comments
{%- endif %}
to guide you further
with opening your request correctly,
please follow them
as closely as possible.
If any instruction is not clear,
please raise your concern
so we can help
and improve them
if applicable.

{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
>>> [!note]
Two additional templates,
**Internal Work Item**
and **Starter Assignment Treatment**,
are available to contributors
for specific cases
regarding project development.
These should not be used
if you do not have Developer status.
>>>
{%- else %}
> [!NOTE]
> Two additional issue templates,
> **Internal Work Item**
> and **Starter Assignment Treatment**,
> are available to contributors
> for specific cases
> regarding project development.
> These should not be used
> if you do not have Developer status.
{%- endif %}

**Always use one of the templates for opening requests!**
By taking a single look
at its type
and the structured sections
filled by the author,
we can provide faster feedback
on your request.
We will kindly ask you
to edit the work item
with the appropriate template
if one is not used
or used incorrectly.

Here are a few general tips
when opening any kind of request
to enhance your chances
of a quick response:

- Follow the template sections
  so team members can view
  your structured line of thought
  and actions leading up
  to your request;
- Provide **context**:
  explaining the conditions
  which led you to open your request
  facilitates our comprehension
  of your perspective
  and helps creating empathy
  with your case;
- **Avoid duplication**
  by making a real effort to determine
  whether your request
  has not been already made by another user
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  before using the [Search][request2] feature
  for all items in the Issue Tracker;
{%- else %}
  before using the Search feature
  for all items in the [Issue Tracker][request2]
  and the [Discussions Page][request2a];
{%- endif %}
- It is also important
  to avoid requests
  that describe too much.
  Each should be documented
  in its own request.
  It's often unavoidable
  that requests can be complex,
  especially with big feature requests.
  Adding a lot of detail to a request
  is great,
  but when a complex one
  can be separated into multiple requests,
  that makes them easier to resolve.
  **One request per request**;
- **Titles are important!**
  Keep your titles
  short and descriptive.
  Don't try to
  cram every bit of information
  in the title.
  More importantly,
  titles should also be **compelling**.
  When someone reads your request,
  they should want to work on it.
  The title sells the request.
  Don't sacrifice allure for brevity;
  - A good rule of thumb
    is that a title should be
    descriptive enough
    that someone looking back at it later
    will understand
    what the purpose of the issue was
    and how it fits
    into the larger context;
  - To make your request more descriptive,
    avoid vague titles like
    "update files" or "fix issue."
    Instead, specify
    what the request comprises;
- Properly format your messages.
  Help the reader focus on what matters
  and understand the structure of your message.
  [{{ cookiecutter.__scm_platform_base }} Flavoured Markdown][request3] has a simple
  but effective syntax,
  consider taking a look
  before writing your request;
- **Good requests are also professional development.**
  Many companies have a remote-first style
  where most discussions happen asynchronously.
  We truly believe that
  approaching your request with this mindset
  can also help you
  further become a better developer
  down the line.

#### Specific Guidelines for Requests for Support

If {{ cookiecutter.project_name }} is not working correctly for you,
most likely it is a simple configuration issue.
Try running {{ cookiecutter.project_name }} again
paying attention to the parameters
{%- if cookiecutter.app_type != 'bare_repo' %}
you have provided,
or use a vanilla configuration
alternatively.
{%- else %}
you have provided.
{%- endif %}

If you are still having difficulty
generating your project as desired,
open an [RFS][request4],
{%- if cookiecutter.app_type != 'bare_repo' %}
providing your `settings.toml`
and `report.log` files
{%- else %}
and provide your
configuration and log files
{%- endif %}
if applicable.

Only open a Request for Correction
if you have clearly identified
an unexpected behaviour
that needs to be addressed.
Otherwise,
if details are not clear,
prefer sticking to the Request for Support
as the means to reach the team.

#### Specific Guidelines for Requests for Improvement

Requests for Improvement are used
when users feel a need for development
related to features provided by {{ cookiecutter.project_name }},
either existent
or yet-to-be-implemented.
They are much welcome,
as they help us engage with the community
on a more proactive level
and work to deliver a solution
of aggregated value
to our users.

Nevertheless,
before opening an [RFI][request5],
take a moment to find out
whether your idea fits with the scope
and [aims][topic2] of the project.
It's up to _you_
to make a strong case
to convince the project's developers
of the merits of this feature.
Please provide
as much detail and context
as possible.

If you are requesting
an entirely new feature
to be added to the {{ cookiecutter.project_name }} toolset,
please consider answering
the following prospective questions
to make your case stronger:

- Is the feature or service
  majorly beneficial
  to user experience
  in general terms,
  as opposed to
  only addressing
  a niche use case?
- Could your desired feature
  be delivered by
  one of the components
  already provided by {{ cookiecutter.project_name }}?
- Is this feature clear enough
  to be adopted by users
  unfamiliar with its purpose?
- Is this feature
  easy to use
  once it is implemented?
- Does this feature require
  just additional configuration
  for {{ cookiecutter.project_name }}?
  Or does it require
  writing additional code?
  The less API changes needed
  for the feature to work
  the more chances it will have
  to be eventually added;
- What is the level of maintenance
  that will be needed
  once this feature is integrated
  into {{ cookiecutter.project_name }}?

Also,
why not take this opportunity
to [become a contributor][bias]?
After all,
the most effective way
to make a contribution
is to make one [that comes from yourself][gfi].

#### Specific Guidelines for Requests for Correction

[![RFCs][badge9]][query9]

Requests for Correction are used
to track unexpected behaviour
from template generation,
namely bugs.

A bug is a **demonstrable** problem
that is caused by
the code in the repository.

Guidelines for [RFCs][request6]:

- Use the [issue search][query9]
  to check if a request
  has already been reported;
- Check if the issue has been fixed
  by trying to reproduce it
  using the latest version of {{ cookiecutter.project_name }};
- **Isolate the problem:**
  create a test case
  to demonstrate your issue.
  Provide either
  a repository,
  [gist][request7]/[snippet][request8]
  or code sample
  to demonstrate you problem.

We kindly ask applicants
to be available for follow-up questions
to clarify their reports
if more information is needed.
A good RFC should include
sufficient information
to help developers identify
the issue's underlying cause.
While the nature of errors
can be diverse
and thus challenging for users to report
with full context,
providing the information below
is much valuable
to accelerate the process:

- What is your environment?
  - What OS are you using?
  - Which version of {{ cookiecutter.project_name }} are you using?
- What steps will reproduce the issue?
  - What are the parameters used
    during application runtime
    that reproduce the bug?
{%- if cookiecutter.app_type != 'bare_repo' %}
    You can provide those
    through the `settings.toml` file;
{%- endif %}
  - At which point specifically
    did your error occur
    during your journey?
- Can you provide
  error logs or tracebacks
  to further detail the issue?
{%- if cookiecutter.app_type != 'bare_repo' %}
  {{ cookiecutter.project_name }} provides
  a `report.log` file
  containing only the last executed run of the program
  to facilitate bug reporting;
  additionally,
  tools like [`reprexpy`][request9]
{%- else %}
  Tools like [`reprexpy`][request9]
{%- endif %}
  can assist you
  in providing more technical detail
  if you are not able to;
- Do you have
  any visual evidence
  to share for further investigation?

These details
will help people
to fix any potential issues.
It is important to note
that **all** reports are valuable,
even if they are not perfectly detailed.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
>>> [!warning]
**Avoid overloading with extraneous details.**
RFCs are the type of request
that most need attention
and careful examination
by the development team,
since a bug can turn {{ cookiecutter.project_name }}
entirely unusable.
Focus on objective facts
directly related to the bug
and kindly perform your due diligence
as much as possible
before bringing it to us,
contextualising your research and findings
to avoid rework
by the development team.
>>>

{% else -%}
> [!WARNING]
> **Avoid overloading with extraneous details.**
> RFCs are the type of request
> that most need attention
> and careful examination
> by the development team,
> since a bug can turn {{ cookiecutter.project_name }}
> entirely unusable.
> Focus on objective facts
> directly related to the bug
> and kindly perform your due diligence
> as much as possible
> before bringing it to us,
> contextualising your research and findings
> to avoid rework
> by the development team.

{% endif -%}
### Contributing by Reviewing Changes

Changes to {{ cookiecutter.project_name }} source code are
proposed,
reviewed
and committed
via [{{ cookiecutter.__scm_platform_base }} {{ cookiecutter.__mr_term }}s][intro2].
Anyone can view and comment
on active changes here.
Participating in code reviews
helps you understand our processes
and explore different domains of the project.
Contribute by reviewing proposed changes
and identifying potential improvements
– as simple as typos
or styling inconsistencies.

As a reviewer,
your job is not
to make sure that
the code is what you would have written
– **because it will not be**.
Your job as a reviewer of a change
is to make sure that
the change as written by its submitter
is correct.

Try to think of edge cases
when testing or evaluating the code,
double check the test coverage.
However,
do not frown
if you merged the {{ cookiecutter.__mr_term }}
and something broke after all.
This is the learning path
to avoiding this mistake
on the next attempt.
Not doing a review
in the first place
will not move you forward either.

To get you quickstarted
on reviewing {{ cookiecutter.__mr_acronym }}s for {{ cookiecutter.project_name }},
here are a few tips
that may help
overcoming the paralysis
of [taking action][bias]:

- Verify that
  the appropriate tests
  have been added.
  When testing a feature or change,
  check out the code tests
  at least the happy paths
  according to the specification
  of the {{ cookiecutter.__mr_acronym }};
- See if documentation has been added
  for the change in question.
  Smaller documentation changes
  should be added
  along with the core changes
  of the proposal;
- Changes should be **readable**,
  that is,
  you as a reviewer
  should be able
  to understand the nature of the changes
  without additional explanations
  outside the changes;
  however,
  if something is not clear,
  we encourage you
  to ask for clarification
  as it might indicate
  the need for further changes
  for full compliance
  before a maintainer
  can complete the {{ cookiecutter.__mr_acronym }};
- You should not rush
  through a code review,
  but also,
  you need to do it promptly.
  Your colleagues are waiting for you.

We strongly encourage you
to take further readings on
the [Review Process][review],
the [Responsibilities of the Reviewer][reviewer]
and [general communication guidelines][behaviour]
to get more detail
on how to make
the most out of your contributions
as a reviewer.
We appreciate your commitment beforehand!

### Contributing with Documentation Changes

Currently,
the documentation surrounding {{ cookiecutter.project_name }}, including
features,
how to use,
options
and reference material
are found directly
in the project [`README`][readme] file.

You can propose changes and additions
to the documentation
by editing the `README` file
and [opening a {{ cookiecutter.__mr_term }}][swmr]
to integrate your changes to the project.

### Contributing to Roadmap Maintenance

[![Issues][badge1]][query1]
{%- if cookiecutter.scm_platform == 'GitLab Free' %}
[![Tasks][badge1a]][query1a]
{%- endif %}

The project roadmap is maintained
through [{{ cookiecutter.__scm_platform_base }} {{ roadmap_item.capitalize() }}s][topic2].
It provides an overview
of the medium and long-term priorities of {{ cookiecutter.project_name }}
as a project,
whether they impact end-users or not.

Contributors and maintainers
are responsible for managing the roadmap.
However,
anyone can support the project
by ensuring alignment with this roadmap,
identifying opportunities
that influence
the project's most impactful deliverables
and communicating them
to the development team:

- Getting familiar
  with our milestones
  and associated items,
  and then
  opening additional [**Requests for Improvement**][request5]
  that pertain to existing {{ roadmap_item }}s;
- Commenting on [issues without associated {{ roadmap_item }}s][query1]
  and suggesting what relevant developments
  could they be associated with
  for the development team to evaluate;
- Linking issues and {{ cookiecutter.__mr_term }}s
  that provide combined effort
  towards a single goal of the project.
  If two or more development streams
  can be delivered with the same solution,
  we can generate increased aggregated value;
- Becoming a [contributor][proposals]
  to act on existing {{ roadmap_item }}s,
  propose new developments not yet mapped
  or recommend [changes to the roadmap itself][roadmap].

### Contributing by Promoting {{ cookiecutter.project_name }}

Promoting {{ cookiecutter.project_name }}
helps us reach a larger audience
and receive more feedback
to continuously improve the project,
your endorsement and recommendation
of our project
is of a **huge** value to us!
Thank you in advance for your interest
and use of {{ cookiecutter.project_name }},
we are really proud of this project
and we couldn't keep advancing with it
without your support!

Here's how you can promote {{ cookiecutter.project_name }}:

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
- Set the [Notification level][promote0] to **"Watch"**
  on the [{{ cookiecutter.scm_namespace.capitalize() }} organisation][promote1]
{% else -%}
- Set the [Notification level][topic6] to **"Watch"**
  on the [{{ cookiecutter.project_name }} repository][development1]
{%- endif %}
  and receive updates
  on most of our activity;
- Star the project;
- Share the project with your colleagues;
- Write a short article
  on how you are using {{ cookiecutter.project_name }}
  in your day-to-day life;
- Share your
  best practices
  and workflows
  for leveraging {{ cookiecutter.project_name }} usefulness
  with us,
  we love getting inspired
  to add new functionality
  and value to our application!

Thank you
for your interest
in {{ cookiecutter.project_name }}!
Your engagement
and contributions
reassure us that
what we are doing matters!
:beers:

{% endif -%}
<!-- Anchors -->

[readme]: {{ cookiecutter.__scm_link_url }}/blob/master/README.md
[swmr]: #start-with-a-{{ cookiecutter.__mr_term_slug }}
[swnjw]: #say-why-not-just-what
[starter]: #about-starter-assignments
[philosophy]: #book-our-philosophy
[committing]: #commit-customs
[codestyle]: #codestyle
[practices]: #general-practices
[workflow]: #development-workflow
[cicd]: #continuous-integration
[tracking]: #work-item-tracking
[bias]: #operate-with-a-bias-for-action
[imperative]: #issue-titles-should-be-framed-in-imperative-mood
[setup]: #development-setup
[admission]: #opening-admissible-merge-requests
{%- if cookiecutter.use_bdd %}
[bdd]: #behaviour-driven-development
{%- endif %}
{%- if cookiecutter.commit_convention == 'gitmoji' %}
[convention]: #gitmoji
{%- elif cookiecutter.commit_convention == 'conventional' %}
[convention]: #conventional-commits
{%- else %}
[convention]: #conventional-gitmoji
{%- endif %}
[review]: #merge-request-review-process
[reviewer]: #the-responsibility-of-the-reviewer
[roadmap]: #roadmap-management
{%- if cookiecutter.licence != 'nos' %}
[proposals]: #speaking_head-proposing-changes-as-a-developer
[contributions]: #reminder_ribbon-other-ways-to-contribute
[promotion]: #contributor-promotion
[gfi]: #there-are-no-good-first-issues
[community]: #fostering-an-inviting-community
[behaviour]: #how-to-behave-among-other-contributors
{%- endif %}

[badge1]: https://img.shields.io/badge/issues_without_{{ roadmap_item }}-006272?style=for-the-badge
{%- if cookiecutter.scm_platform == 'GitLab Free' %}
[badge1a]: https://img.shields.io/badge/{{ task_item }}s_with_{{ roadmap_item }}-08b1ab?style=for-the-badge
{%- endif %}
[badge2]: https://img.shields.io/badge/seeking_input-69ad6b?style=for-the-badge
[badge3]: https://img.shields.io/badge/needs_triage-4285f4?style=for-the-badge
[badge4]: https://img.shields.io/badge/designs_under_discussion-ff2f82?style=for-the-badge
[badge5]: https://img.shields.io/badge/starter_assignments-66aa9c?style=for-the-badge
[badge6]: https://img.shields.io/badge/seeking_contributors-9ccfcd?style=for-the-badge
[badge7]: https://img.shields.io/badge/quick_wins-5ebc8b?style=for-the-badge
[badge8]: https://img.shields.io/badge/stale_issues-9400d3?style=for-the-badge
[badge9]: https://img.shields.io/badge/requests_for_correction-dc143c?style=for-the-badge
[badge10]: https://img.shields.io/badge/requests_for_improvement-0055ff?style=for-the-badge
[badge11]: https://img.shields.io/badge/requests_for_support-ed9121?style=for-the-badge

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
[query1]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&type%5B%5D=issue&parent_id=None
[query2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors%3A%3Aopinion&type%5B%5D=issue
[query3]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&status=Needs%20Triage&type%5B%5D=issue
[query4]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=design%3A%3A%2A&type%5B%5D=issue
[query5]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=starter-assignment%3A%3A%2A&type%5B%5D=issue
[query6]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors%3A%3Adelivery&type%5B%5D=issue
[query7]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&or%5Blabel_name%5D%5B%5D=quick-win&or%5Blabel_name%5D%5B%5D=starter-assignment%3A%3Aquick-win
[query8]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=stale&type%5B%5D=issue
[query9]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=request%3A%3Acorrection&type%5B%5D=issue
[query10]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=request%3A%3Aimprovement&type%5B%5D=issue
[query11]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=request%3A%3Asupport&type%5B%5D=issue

{% elif cookiecutter.scm_platform == 'GitLab Free' -%}
[query1]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&type%5B%5D=issue&milestone_title=None
[query1a]: {{ cookiecutter.__scm_link_url }}/issues?state=all&type%5B%5D=task&milestone_title=Any
[query2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors&label_name%5B%5D=seeking-input&type%5B%5D=issue
[query3]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=sts-needs-triage&type%5B%5D=issue
[query4]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5D%5B%5D=design-discovery&or%5Blabel_name%5D%5B%5D=design-formulation&or%5Blabel_name%5D%5B%5D=design-reassessment&type%5B%5D=issue
[query5]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=starter-assignment&type%5B%5D=issue
[query6]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors&label_name%5B%5D=seeking-builders&type%5B%5D=issue
[query7]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=quick-win&type%5B%5D=issue
[query8]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=stale&type%5B%5D=issue
[query9]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=rfc&type%5B%5D=issue
[query10]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=rfc&type%5B%5D=issue
[query11]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=rfs&type%5B%5D=issue

{% else -%}
[query1]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20no%3Aproject
[query2]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Aseeking-contributors%20label%3Aseeking-input
[query3]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Asts-needs-triage
[query4]: {{ cookiecutter.__scm_link_url }}/issues?q=label%3Adesign-discovery%20OR%20label%3Adesign-formulation%20OR%20label%3Adesign-reassessment
[query5]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Astarter-assignment
[query6]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Aseeking-contributors%20label%3Aseeking-builders
[query7]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Aquick-win
[query8]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Astale
[query9]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Arfc
[query10]: {{ cookiecutter.__scm_link_url }}/discussions/categories/requests-for-improvement
[query11]: {{ cookiecutter.__scm_link_url }}/discussions/categories/requests-for-support

{% endif -%}
{% if cookiecutter.licence != 'nos' or cookiecutter.use_bdd -%}
[knowledge]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge

{% endif -%}
[intro1]: {{ cookiecutter.__scm_link_url }}/issues
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[intro2]: {{ cookiecutter.__scm_link_url }}/merge_requests
{%- else %}
[intro2]: {{ cookiecutter.__scm_link_url }}/pulls
[intro3]: {{ cookiecutter.__scm_link_url }}/discussions
{%- endif %}

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[setup1]: {{ cookiecutter.__scm_link_url }}/forks/new
[setup2]: https://docs.gitlab.com/user/group/
[setup3]: https://docs.gitlab.com/user/project/repository/forking_workflow/
{% else -%}
[setup1]: {{ cookiecutter.__scm_link_url }}/fork
[setup2]: https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations
[setup3]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
{% endif -%}
[setup4]: https://python-poetry.org/docs/#installation
{%- if cookiecutter.app_type != 'bare_repo' %}

[apptopic1]: https://typer.tiangolo.com/tutorial/
{%- if cookiecutter.app_type != 'cli' %}
[apptopic1a]: https://textual.textualize.io/guide/
{%- endif %}
[apptopic2]: https://gitlab.com/galactipy/orbittings
[apptopic3]: https://www.dynaconf.com/
[apptopic4]: https://gitlab.com/galactipy/nebulog
[apptopic5]: https://loguru.readthedocs.io/en/stable/
{%- if cookiecutter.use_bdd %}
[apptopic5a]: {{ cookiecutter.__scm_link_url }}/tree/master/tests/features
{%- endif %}
[apptopic6]: {{ cookiecutter.__scm_link_url }}/tree/master/tests
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[topic1]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab-ci.yml
{%- else %}

[topic1]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/workflows
{%- endif %}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[topic2]: {{ cookiecutter.__gitlab_org }}/epics
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[topic2]: {{ cookiecutter.__scm_link_url }}/milestones
{%- else %}
[topic2]: {{ cookiecutter.__scm_link_url }}/projects
{%- endif %}
[topic3]: {{ cookiecutter.__scm_link_url }}/labels
{%- if cookiecutter.licence != 'nos' %}
[topic4]: https://goauthentik.io/blog/2024-03-07-why-contributing-to-open-source-is-scary/
[topic5]: mailto:{{ cookiecutter.email }}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[topic6]: https://gitlab.com/gitlab-org/gitlab-foss/-/issues/234#note_17497758
{%- else %}
[topic6]: https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications#about-participating-and-watching-notifications
{%- endif %}
{%- endif %}

[cc1]: https://www.contributor-covenant.org/
[cc2]: {{ cookiecutter.__scm_link_url }}/blob/master/CODE_OF_CONDUCT.md

[development1]: {{ cookiecutter.__scm_base_url }}
{%- if cookiecutter.licence != 'nos' %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[development2]: https://docs.gitlab.com/user/permissions/
{%- else %}
[development2]: https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization
{%- endif %}
[development3]: https://diurnal.st/2025/03/02/the-pragmatic-open-source-contributor.html
{%- endif %}

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[roadmap1]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Project%2520Policies
{% else -%}
[roadmap1]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=project_policies.md
{% endif -%}
[roadmap2]: {{ cookiecutter.__scm_link_url }}/blob/master/ROADMAP.md#roadmap-history
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[roadmap3]: https://docs.gitlab.com/user/emoji_reactions/
{%- else %}
[roadmap3]: https://github.blog/news-insights/product-news/add-reactions-to-pull-requests-issues-and-comments/
{%- endif %}
[roadmap4]: https://blog.crisp.se/2014/09/25/david-evans/as-a-i-want-so-that-considered-harmful
[roadmap5]: https://www.reforge.com/blog/user-stories-misuse
[roadmap6]: https://www.mountaingoatsoftware.com/blog/critiquing-one-of-my-own-real-user-stories
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[roadmap7]: https://docs.gitlab.com/user/project/releases/
{%- else %}
[roadmap7]: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
{%- endif %}

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
[status1]: https://docs.gitlab.com/user/work_items/status/
[status2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&type%5B%5D=issue&label_name%5B%5D=request%3A%3A%2A

[icon1]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/triage.png
[icon2]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/refinement.png
[icon3]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/criteria.png
[icon4]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/steps.png
[icon5]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/decomposition.png
[icon6]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/greenlit.png
[icon7]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/pipeline.png
[icon8]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/priority.png
[icon9]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/deferred.png
[icon10]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/progress.png
[icon11]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/done.png
[icon12]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/canceled.png
[icon13]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/redundant.png
[icon14]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/duplicate.png
[icon15]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/created.png
[icon16]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/ongoing.png
[icon17]: https://gitlab.com/galactipy/galactipy/-/raw/master/assets/png/aborted.png

{% elif cookiecutter.scm_platform == 'GitHub' -%}
[labels1]: {{ cookiecutter.__scm_link_url }}/.github/release-drafter.yml

{% endif -%}
[practices1]: https://cbea.ms/git-commit/#imperative
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[practices2]: https://docs.gitlab.com/user/tasks/
{% else -%}
[practices2]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues
{% endif -%}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[practices3]: https://docs.gitlab.com/user/project/issues/related_issues/#blocking-issues
{%- if cookiecutter.scm_platform == 'GitLab Free' %}
[practices4]: https://docs.gitlab.com/user/tasks/#add-a-task-to-a-milestone
{%- endif %}

{% else -%}
[practices3]: https://github.blog/changelog/2025-08-21-dependencies-on-issues/

{% endif -%}
{% if cookiecutter.use_bdd -%}
[bdd1]: https://cucumber.io/docs/
[bdd2]: https://cucumber.io/docs/bdd/
[bdd3]: https://youtube.com/playlist?list=PLwLLcwQlnXByKR1Fo7UnE6gQAbx-JfYJZ
[bdd4]: https://youtu.be/LuCqnxGxIPE
[bdd5]: https://youtu.be/YUkk2lGLxjA
[bdd6]: https://pytest-bdd.readthedocs.io/en/latest/
[bdd7]: https://automationpanda.com/bdd/
[bdd8]: https://data-ai.theodo.com/en/technical-blog/behavior-driven-development-data-scientist-perspective

{% endif -%}
[versioning1]: https://jacobtomlinson.dev/effver/

{% if cookiecutter.commit_convention == 'gitmoji' -%}
[committing1]: https://gitmoji.dev/
{% elif cookiecutter.commit_convention == 'conventional' -%}
[committing1]: https://www.conventionalcommits.org/en/v1.0.0/
[committing1a]: https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md
{% else -%}
[committing1]: https://github.com/ljnsn/cz-conventional-gitmoji
[committing1a]: https://www.conventionalcommits.org/en/v1.0.0/
{% endif -%}
[committing2]: https://cbea.ms/git-commit/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[committing3]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
[committing4]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/changelog_config.yml
{%- endif %}

[style1]: https://docs.astral.sh/ruff/
{%- if cookiecutter.docstring_style == 'numpy' %}
[style1a]: https://numpydoc.readthedocs.io/en/latest/format.html
{%- elif cookiecutter.docstring_style == 'google' %}
[style1a]: https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings
{%- elif cookiecutter.docstring_style == 'sphinx' %}
[style1a]: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
{%- endif %}
[style2]: https://sembr.org/
[style3]: https://sive.rs/1s <!-- codespell:ignore -->
[style4]: {{ cookiecutter.__scm_link_url }}/tree/master/.{{ cookiecutter.__scm_platform_lc }}
[style5]: {{ cookiecutter.__scm_link_url }}/blob/master/CHANGELOG.md

[hooks1]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[ci1]: https://docs.gitlab.com/topics/build_your_application/
{%- else -%}
[ci1]: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments
{%- endif %}
{%- if cookiecutter.__coverage_lc == 'codacy' %}
[ci1a]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
[ci1b]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/pull-requests/open
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[ci2]: https://docs.gitlab.com/ci/yaml/
{%- else %}
[ci2]: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow
{%- endif %}

{% if cookiecutter.licence != 'nos' -%}
[licence1]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE

{% endif -%}
[values1]: https://handbook.gitlab.com/
[values2]: https://handbook.gitlab.com/handbook/communication/#start-with-a-merge-request
[values3]: https://handbook.gitlab.com/handbook/values/#say-why-not-just-what
[values4]: https://theknowledge.io/chestertons-fence-explained/
[values5]: https://handbook.gitlab.com/handbook/values/#operate-with-a-bias-for-action
[values6]: https://conversational-leadership.net/we-human-beings-are-complex/
{%- if cookiecutter.licence != 'nos' %}
[values7]: https://kentcdodds.com/blog/first-timers-only
{%- endif %}

{% if cookiecutter.app_type in ['tui', 'hybrid'] -%}
[changes0a]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/tui
[changes0b]: https://textual.textualize.io/
{% endif -%}
{% if cookiecutter.app_type != 'bare_repo' -%}
[changes1]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/cli
[changes2]: https://typer.tiangolo.com/
[changes3]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/config
[changes4]: {{ cookiecutter.__scm_link_url }}/tree/master/{{ cookiecutter.package_name }}/logging
[changes5]: {{ cookiecutter.__scm_link_url }}/blob/master/tasks.py
[changes6]: https://www.pyinvoke.org/

{% endif -%}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[prepare1]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/merge_request_templates
{% else -%}
[prepare1]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/MERGE_REQUEST_TEMPLATE
{% endif -%}
[prepare2]: https://github.com/kubernetes/kubernetes/blob/release-1.5/docs/devel/faster_reviews.md
[prepare3]: https://google.github.io/eng-practices/review/

{% if cookiecutter.use_bdd -%}
[workflow1]: https://pytest-bdd.readthedocs.io/en/latest/#organizing-your-scenarios
{% else -%}
[workflow1]: https://docs.pytest.org/en/stable/example/markers.html#mark-examples
{% endif -%}
[workflow2]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
[reviewing0]: https://docs.gitlab.com/user/project/merge_requests/dependencies/
{% endif -%}
[reviewing1]: https://josipmisko.com/posts/code-review-nit
{%- if cookiecutter.licence != 'nos' %}

[community1]: https://gregorybeamer.wordpress.com/2020/11/12/why-code-organization-is-so-important-in-software/
[community2]: https://simonsinek.com/stories/the-right-way-to-stand-up-for-yourself-at-work/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[community3]: {{ cookiecutter.__scm_link_url }}/merge_requests/new?issuable_template=Internal%2520Improvements
{%- else %}
[community3]: {{ cookiecutter.__scm_link_url }}/pulls/compare?template=internal_improvements.md
{%- endif %}
[community4]: https://firstpr.me/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[community5]: https://docs.gitlab.com/user/discussions/
{%- endif %}

[help1]: https://typer.tiangolo.com/help-typer/#help-others-with-questions-in-github
[help2]: https://www.blockchain-council.org/ai/collective-intelligence-framework/
[help3]: https://stackoverflow.com/help/minimal-reproducible-example

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[request1]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/issue_templates
[request2]: {{ cookiecutter.__scm_link_url }}/issues?state=all&type%5B%5D=issue
[request3]: https://docs.gitlab.com/user/markdown/
[request4]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Support
[request5]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
[request6]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Correction
{% else -%}
[request1]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/ISSUE_TEMPLATE
[request1a]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/DISCUSSION_TEMPLATE
[request2]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue
[request2a]: {{ cookiecutter.__scm_link_url }}/discussions?discussions_q=
[request3]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
[request4]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-support
[request5]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
[request6]: {{ cookiecutter.__scm_link_url }}/issues/new?template=request_for_correction.yml
{% endif -%}
[request7]: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists
[request8]: https://docs.gitlab.com/user/snippets/
[request9]: https://reprexpy.readthedocs.io/en/latest/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[promote0]: https://docs.gitlab.com/user/profile/notifications/#notification-levels
[promote1]: https://{{ cookiecutter.__scm_platform_lc }}.com/{{ cookiecutter.scm_namespace }}
{%- endif %}
{%- endif %}
