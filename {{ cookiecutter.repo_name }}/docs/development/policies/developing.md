{% set scope_separator = '::' if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' else '-' -%}
# {% if cookiecutter.licence != 'nos' %}Open {% endif %}Development

All work on {{ cookiecutter.project_name }} happens
directly on [{{ cookiecutter.__scm_platform_base }}][1],
including roadmap
and [{{ cookiecutter.__roadmap_item }}s][2].
Therefore,
a {{ cookiecutter.__scm_platform_base }} account is needed
to start contributing.

{% if cookiecutter.licence != 'nos' -%}
## Contributor Promotion

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
  through [e-mail][2a] contact;
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
    - [Showing responsibility][2b] to document
      all relevant information
      promptly,
      whether for
      internal or external use,
      to ensure maintenance
      of our [institutional knowledge][2c];
    - Upkeeping repository order
      through our [practices][2d];
    - Being an exemplar advocate
      for a [welcoming community][2e];
- Aside from
  displaying the aforementioned conduct,
  the contributor must express
  their actual interest
  in attaining a [role][2f]
  in the upstream repository.

We also recommend interested individuals
to follow
the guide to the [_Pragmatic Open Source Contributor_][2g],
which goes
into the attitude
for candidate contributors
in more detail.

{% endif -%}
## Work Item Tracking

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
and structured preferably around [{{ cookiecutter.__mr_term }}s][3].
Whenever project advancements are not immediately deliverable,
progress is tracked through {{ cookiecutter.__scm_platform_base }} Issues
and {{ cookiecutter.__task_item.capitalize() }}s.
Use cases for this type of work item include:

- User requests
  (since general users are not allowed to create {{ cookiecutter.__mr_acronym }}s);
- Larger scoped developments
  which are unable to be delivered
  in a single {{ cookiecutter.__mr_acronym }};
- Ideas for future developments
  which can't be prioritised
  due to scope or team capacity.

### Labels

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

| Development Domain  |                      Label                       | Usage                                                                                                             |
| :-----------------: | :----------------------------------------------: | ----------------------------------------------------------------------------------------------------------------- |
|      Back-End       |      `backend{{ scope_separator }}external`      | Changes modules interacting directly with external APIs.                                                          |
|      Back-End       |     `backend{{ scope_separator }}components`     | Changes internal modules and utils.                                                                               |
|      Back-End       |      `backend{{ scope_separator }}database`      | Changes database schema and operations.                                                                           |
|      Back-End       |    `backend{{ scope_separator }}performance`     | Improves the program's performance and reliability for users.                                                     |
|         N/A         |             `blocked-by-dependency`              | Resolution requires development on upstream dependency.                                                           |
|         CI          |          `ci{{ scope_separator }}build`          | Improves the project's deployment reliability through automated validation.                                       |
{%- if cookiecutter.create_docker %}
|         CI          |         `ci{{ scope_separator }}docker`          | Changes how {{ cookiecutter.project_name }} containers are built and provided to users.                           |
{%- endif %}
|         CI          |          `ci{{ scope_separator }}tasks`          | Structures automated tasks of different functions to run on scheduled pipelines.                                  |
{%- if cookiecutter.app_type == 'bare_repo' %}
|         N/A         |                  `deprecations`                  | Marks deprecations for future removal.                                                                            |
{%- else %}
|         CLI         |          `cli{{ scope_separator }}arch`          | Changes logic in the layer directly below the CLI, including input validation and file parsing.                   |
|         CLI         |        `cli{{ scope_separator }}commands`        | Changes the CLI command structure and capabilities, including the addition of new commands.                       |
|         CLI         |      `cli{{ scope_separator }}deprecations`      | Marks deprecations for future removal to CLI features.                                                            |
|         CLI         |        `cli{{ scope_separator }}options`         | Changes available options and option flag behaviour for CLI users.                                                |
|         CLI         |        `cli{{ scope_separator }}removals`        | CLI feature sunsetting.                                                                                           |
{%- endif %}
|       Design        |      `design{{ scope_separator }}discovery`      | Debates high-level concepts for new {{ cookiecutter.project_name }} features.                                     |
|       Design        |     `design{{ scope_separator }}formulation`     | Specifies expected behaviour for {{ cookiecutter.project_name }} features under different possible circumstances. |
|       Design        |    `design{{ scope_separator }}reassessment`     | Reevaluates a previous design that did not consider all possible cases.                                           |
|    Documentation    |        `docs{{ scope_separator }}nudging`        | Updates formal documentation with tips and tricks for better {{ cookiecutter.project_name }} usage.               |
|    Documentation    |        `docs{{ scope_separator }}guides`         | Updates formal documentation with structured user guides.                                                         |
|    Documentation    |       `docs{{ scope_separator }}technical`       | Updates formal documentation with API reference or development guides.                                            |
| Internal Operations |  `internals{{ scope_separator }}configuration`   | Regulates current development toolset behaviour.                                                                  |
| Internal Operations | `internals-developer{{ scope_separator }}output` | Boosts team productivity with incremental automation and simplification.                                          |
| Internal Operations |      `internals{{ scope_separator }}invoke`      | Streamlines local development operations.                                                                         |
| Internal Operations |     `internals{{ scope_separator }}toolset`      | Adds, updates or removes tools available for developers.                                                          |
|         N/A         |                  `localization`                  | Updates translation files for other languages.                                                                    |
|     Maintenance     | `maintenance{{ scope_separator }}configuration`  | Updates current development toolset syntax and options.                                                           |
|     Maintenance     |  `maintenance{{ scope_separator }}dependencies`  | Upgrades project dependencies.                                                                                    |
|     Maintenance     |      `maintenance{{ scope_separator }}bot`       | Work items managed automatically by a project Bot.                                                                |
|     Maintenance     |   `maintenance{{ scope_separator }}knowledge`    | Updates already existing information for knowledge retention and sharing.                                         |
|     Maintenance     |   `maintenance{{ scope_separator }}dependabot`   | Issues and Pull Requests to be automatically handled by Dependabot.                                               |
|     Maintenance     | `maintenance{{ scope_separator }}test-coverage`  | Changes being enforced due to software regression.                                                                |
|     Maintenance     |    `maintenance{{ scope_separator }}toolset`     | Updates or replaces current development tools functionality.                                                      |
|         N/A         |                  `manual-check`                  | Requires manual validation to certain or all acceptance criteria.                                                 |
|         N/A         |                 `manual-closure`                 | Items that should not be closed through commit closing patterns.                                                  |
|       Plugins       |        `plugins{{ scope_separator }}api`         | Updates logic to enable third-party extensions based on the core {{ cookiecutter.project_name }} implementation.  |
|       Plugins       |        `plugins{{ scope_separator }}arch`        | Implements undelying systems and structures for supporting plugins, including loading and discovery mechanisms.   |
|      Policies       |        `policies{{ scope_separator }}ci`         | Changes rules triggering CI jobs.                                                                                 |
|      Policies       |    `policies{{ scope_separator }}guidelines`     | Changes project guidelines in `CONTRIBUTING.md` or the formal documentation.                                      |
|      Policies       |      `policies{{ scope_separator }}roadmap`      | Work items related to debates and proposals relating to the project roadmap.                                      |
|      Policies       |       `policies{{ scope_separator }}rules`       | Changes rules for development tools (e.g., Ruff/mypy rules, issue triaging etc.).                                 |
|      Policies       |     `policies{{ scope_separator }}templates`     | Changes issue and {{ cookiecutter.__mr_term }} templates.                                                         |
|         N/A         |                   `quick-win`                    | Development requires low effort.                                                                                  |
|         N/A         |                  `refactoring`                   | Restructures existing source code without changing its functionality.                                             |
{%- if cookiecutter.app_type == 'bare_repo' %}
|         N/A         |                    `removals`                    | Feature sunsetting.                                                                                               |
{%- endif %}
|    User Requests    |                      `rfc`                       | For work items for when something is not working properly.                                                        |
|    User Requests    |                      `rfi`                       | For work items containing suggestions for new features from the community.                                        |
|    User Requests    |                      `rfs`                       | For issues opened by users seeking advice regarding {{ cookiecutter.project_name }}.                              |
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
|         N/A         |         `seeking-contributors::delivery`         | Proposal is polished and can be picked up if you feel inclined to.                                                |
|         N/A         |         `seeking-contributors::opinion`          | In need of help to further discuss and define scope.                                                              |
{%- else %}
|         N/A         |              `seeking-contributors`              | Umbrella label to mark work items requiring contributor involvement.                                              |
|         N/A         |                `seeking-builders`                | Proposal is polished and can be picked up if you feel inclined to.                                                |
|         N/A         |                 `seeking-input`                  | In need of help to further discuss and define scope.                                                              |
{%- endif %}
|         N/A         |                     `stale`                      | Work items without activity that are marked for closing.                                                          |
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
|         N/A         |         `starter-assignment::quick-win`          | Development requires low effort and is ideal for first-time contributors.                                         |
|         N/A         |         `starter-assignment::supervised`         | Proposal and delivery steps are clear and can be picked up by first-time contributors.                            |
{%- else %}
|         N/A         |               `starter-assignment`               | Proposal and delivery steps are clear and can be picked up by first-time contributors.                            |
{%- endif %}
{%- if cookiecutter.__app_group == 'tui' %}
|   User Interface    |      `ui{{ scope_separator }}accessibility`      | Promotes accessibility options for users in the interface.                                                        |
|   User Interface    |          `ui{{ scope_separator }}arch`           | Changes rendering logic in the layer directly below the user interface.                                           |
|   User Interface    |      `ui{{ scope_separator }}deprecations`       | Marks deprecations for future removal to UI features.                                                             |
|   User Interface    |        `ui{{ scope_separator }}features`         | Introduces new functions and capabilities to the user interface.                                                  |
|   User Interface    |         `ui{{ scope_separator }}layout`          | Changes the disposition of elements and text in the user interface.                                               |
|   User Interface    |        `ui{{ scope_separator }}removals`         | User interface feature sunsetting.                                                                                |
{%- endif %}
|         N/A         |                `up-for-a-change`                 | Author-based label to express interest in delivering their own request.                                           |
|   User Experience   |        `ux{{ scope_separator }}advanced`         | Updates features available to power users of {{ cookiecutter.project_name }}.                                     |
|   User Experience   |      `ux{{ scope_separator }}customization`      | Improves options available for program customisation by users.                                                    |
|   User Experience   |          `ux{{ scope_separator }}flags`          | Implements feature flags for {{ cookiecutter.project_name }}.                                                     |
|   User Experience   |        `ux{{ scope_separator }}migration`        | Offers predefined migration options to users in the case of breaking changes.                                     |
{%- if cookiecutter.__app_group == 'tui' %}
|   User Experience   |       `ux{{ scope_separator }}navigation`        | Improves user navigation in the user interface.                                                                   |
{%- endif %}
|   User Experience   |         `ux{{ scope_separator }}nudging`         | Helps users understand the application with more ease, like help panels, notifications etc.                       |

{% if cookiecutter.__scm_platform_lc == 'github' -%}
!!! note

    The project labels are also used
    to define Changelog categories
    in [Release Drafter][labels1].

{% endif -%}
### Work Item Lifecycle

To effectively manage
issue and {{ cookiecutter.__task_item }} lifecycles,
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
we use [GitLab Statuses][4].
{%- else %}
we use specific labels
{%- if cookiecutter.__scm_platform_lc == 'github' %}
to mark issues
and discussions.
{%- else %}
to mark issues.
{%- endif %}
{%- endif %}
Our approach
relies on
keeping few options for
in-progress and completed items
and providing different options
for other stages of the lifecycle.
This allows project members to
better relay [context][5]
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
| ![Triage icon][icon1] **Needs Triage**               |     Triage      | Initial stage for User requests, which require a first analysis by a Galactipy contributor before work on its scope is either accepted or declined. It is also the default open state for new items if not overriden.                                                                                                                                                     |
| ![Refinement icon][icon2] **Needs Refinement**       |     Triage      | Describes more general ideas that might receive development at some point, but whose current state does not detail implementation or paths to delivery. Lacking scope, represents more of a desire than an actual proposal – which might actually prove unfeasible later. Should be used to inform the need for further discussions before being cleared for development. |
| ![Criteria icon][icon3] **Needs Criteria**           |     Triage      | This describes items whose scope is set, but acceptance criteria is still pending to be added before being cleared for development. In contrast with the **Needs Refinement** status, in this stage the deliverable is known and understood, but is waiting for a contributor to detail in smaller steps.                                                                 |
| ![Steps icon][icon4] **Needs Delivery Steps**        |     Triage      | A specific type of triaging item, signaling pending work before the item can be cleared as a [starter assignment][6] development. In contrast with the **Needs Criteria**, this stage indicates the work item will be processed with greater detail than usual so a new contributor can pick it up and develop it with little to no friction.                             |
| ![Decomposition icon][icon5] **Needs Decomposition** |     Triage      | Proposals or requests that have been deemed too large in scope to be considered a single work item and must be broken down in two or more items before proceeding.                                                                                                                                                                                                        |
| ![Greenlit icon][icon6] **Greenlit**                 |      To Do      | Items that have been cleared for development after having their scope and acceptance criteria properly defined.                                                                                                                                                                                                                                                           |
| ![Pipeline icon][icon7] **Pipeline**                 |      To Do      | Items that have scope and acceptance criteria, but that address a specific development stream which is not currently considered the most valuable for delivery. Can be picked for development, but should be left out in favour of **Greenlit** and **Priority** items.                                                                                                   |
| ![Priority icon][icon8] **Priority**                 |      To Do      | Signals items which take priority over other cleared work items. Should be used with discretion and only in cases where lack of action can lead to significant issues to security or user experience.                                                                                                                                                                     |
| ![Deferred icon][icon9] **Deferred**                 |      To Do      | Signals items that, despite having scope and acceptance criteria, are deliberately being deprioritised for development (e.g., due to an upstream block).                                                                                                                                                                                                                  |
| ![Progress icon][icon10] **In Progress**             |   In Progress   | Items currently being actively worked on.                                                                                                                                                                                                                                                                                                                                 |
| ![Done icon][icon11] **Done**                        |      Done       | Items delivered in full.                                                                                                                                                                                                                                                                                                                                                  |
| ![Canceled icon][icon12] **Out of Scope**            |    Canceled     | Items deemed out of the scope of Galactipy.                                                                                                                                                                                                                                                                                                                               |
| ![Canceled icon][icon12] **Cannot Implement**        |    Canceled     | Items which are unable to be delivered by the development team in its original form, due to technical barriers or security risks.                                                                                                                                                                                                                                         |
| ![Canceled icon][icon12] **Not Feasible**            |    Canceled     | Items which can technically be delivered, but that have been declined for development due to any other factor outside the other **Canceled** stage items.                                                                                                                                                                                                                 |
| ![Redundant icon][icon13] **Redundant**              |    Canceled     | Items whose scope has become superfluous to a project due to design changes in other domains.                                                                                                                                                                                                                                                                             |
| ![Duplicate icon][icon14] **Duplicate**              |    Canceled     | Items marked as duplicates of previous work items.                                                                                                                                                                                                                                                                                                                        |

Task lifecycLes are made simpler
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
| **Needs Delivery Steps** |     `sts-needs-steps`     |     Triage      | A specific type of triaging item, signaling pending work before the item can be cleared as a [starter assignment][6] development. In contrast with the **Needs Criteria**, this stage indicates the work item will be processed with greater detail than usual so a new contributor can pick it up and develop it with little to no friction.                             |
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

{{ cookiecutter.__task_item.capitalize() }}s do not require
a lifecycle label.

{% endif -%}
## General Practices

### Issue Titles Should be Framed in Imperative Mood

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
just like [commits][7].

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

!!! warning

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

### {{ cookiecutter.__task_item.capitalize() }}s Are Used as Acceptance Criteria for Issues

[{{ cookiecutter.__task_item.capitalize() }}s][8] are a specific type of work item
in {{ cookiecutter.__scm_platform_base }}
which can be associated
with issues as their child items.
In {{ cookiecutter.project_name }} development,
{{ cookiecutter.__mr_term }}s are
the [default][3] form of actionable development,
while issues are used
for compiling user requests
and development intentions
that can not be directly delivered
through an open {{ cookiecutter.__mr_term }}.

In either case,
{{ cookiecutter.__task_item }}s must be used
to complement the open issue
with their acceptance criteria
to be closed.
Their titles should follow
the same [rules][9] as issue titles,
while descriptions are optional
if relevant to understand implementation.

!!! warning

    The only label allowed on {{ cookiecutter.__task_item }}s
    is `manual-closure`.
    Otherwise,
    there should be no labels
    associated with a {{ cookiecutter.__task_item }}.

### Usage of the `seeking-contributors` Labels

`seeking-contributors` is the label used
to indicate work items
whose authors need help from the community
in further advancing with development.

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
The `opinion` value label marks work items which
{% else -%}
The `seeking-input` label marks work items which
{%- endif %}
are at a [**Triage**][10] stage
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

!!! tip

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

### Blocks Must be Set at the Same Issue Level

[Issue blocks][11] are not mandatory
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
{{ cookiecutter.__task_item }}s can only block **{{ cookiecutter.__task_item}}s**.

### Tasks Should Have no Milestones

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
given the [default behaviour][12] of GitLab,
tasks associated with milestones
can accumulate over time.
The association
should be removed
by [being queried][query1a]
in the Issue Tracker
and edited
through the "Bulk edit" option.

<!-- Anchors -->

[1]: {{ cookiecutter.__scm_base_url }}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[2]: {{ cookiecutter.__gitlab_org }}/epics
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[2]: {{ cookiecutter.__scm_link_url }}/milestones
{%- else %}
[2]: {{ cookiecutter.__scm_link_url }}/projects
{%- endif %}
{%- if cookiecutter.licence != 'nos' %}
[2a]: mailto:{{ cookiecutter.email }}
[2b]: ../philosophy.md#operate-with-a-bias-for-action
[2c]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[2d]: #general-practices
[2e]: ../for_developers/foster.md
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[2f]: https://docs.gitlab.com/user/permissions/
{%- else %}
[2f]: https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization
{%- endif %}
[2g]: https://diurnal.st/2025/03/02/the-pragmatic-open-source-contributor.html
{%- endif %}
[3]: ../philosophy.md#start-with-a-{{ cookiecutter.__mr_term_slug }}
[4]: https://docs.gitlab.com/user/work_items/status/
[5]: ../philosophy.md#say-why-not-just-what
[6]: ../for_developers/foster.md#about-starter-assignments
[7]: https://cbea.ms/git-commit/#imperative
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[8]: https://docs.gitlab.com/user/tasks/
{%- else %}
[8]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues
{%- endif %}
[9]: #issue-titles-should-be-framed-in-imperative-mood
[10]: #work-item-tracking
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[11]: https://docs.gitlab.com/user/project/issues/related_issues/#blocking-issues
{%- if cookiecutter.scm_platform == 'GitLab Free' %}
[12]: https://docs.gitlab.com/user/tasks/#add-a-task-to-a-milestone
{%- endif %}
{%- else %}
[11]: https://github.blog/changelog/2025-08-21-dependencies-on-issues/
{%- endif %}

[badge1]: https://img.shields.io/badge/issues_without_{{ cookiecutter.__roadmap_item }}-006272?style=for-the-badge
{%- if cookiecutter.scm_platform == 'GitLab Free' %}
[badge1a]: https://img.shields.io/badge/{{ cookiecutter.__task_item }}s_with_{{ cookiecutter.__roadmap_item }}-08b1ab?style=for-the-badge
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
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}

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
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}

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
{%- else %}

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
{%- endif %}
