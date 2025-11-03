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
and serving as the single source of truth
for the project's rules
and modus operandi.

Contributions to Galactipy include
file manipulation code,
tests,
tool configuration and updates,
development automation
via CI/CD,
answering user questions,
as well as
managing the backlog of [issues][intro2]
and [Merge Requests][intro3]
through open discussions.

We welcome all contributors
willing to work in good faith
with other contributors
and the community.
No contribution is too small
and all contributions are valued.

Whether you intend
to become a [developer][intro4]
for Galactipy
or you are a [user][intro5] of the template,
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

[[_TOC_]]

## :runner: TL;DR

Preconditions for
contributing as a developer:

- Creating Merge Requests
  requires a GitLab account;
- Merge Requests should
  adhere to [GitLab Philosophy][tldr1];
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
We manage contributions
from the community
through the [fork][setup3] system,
which helps us
monitor and appreciate continuous input
from individuals and organisations.
Contributors who can
demonstrate their competence
in further developing Galactipy
may be [promoted][setup4]
to upstream Developers or Maintainers.

After forking the upstream repository,
cloning it to your local environment
and accessing the root dir
via your IDE or the terminal:

1. Make sure
   you have Poetry [installed][setup5];
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
for a [first contribution][setup6].

## :shrug: Not Sure Where to Start?

If you don't feel
ready to start contributing,
the following steps
should help:

- The project [`README`][wts1] details
  how to use Galactipy,
  provides a high-level overview
  of its features
  and additional references
  for project management,
  many of which
  are applied to our development;
- To effectively contribute to Galactipy,
  you should probably get knowledgeable
  about a few topics:
  - Understand how Cookiecutter works
    under the hood
    for generating projects,
    especially its [advanced usage][wts2] features;
  - Learn how to use
    the [Jinja syntax][wts3]
    as Cookiecutter uses it
    to refine control
    over generated template contents;
  - Check the [`pre_gen_project.py`][wts4]
    and [`post_gen_project.py`][wts5]
    Cookiecutter hook files
    controlling project generation behaviour;
  - Check the [`tests/`][wts6] directory,
    which validate all code
    for pre-gen and post-gen hooks;
  - Review the [`.gitlab-ci.yml`][wts7] file
    containing Galactipy's [CI jobs][wts8],
    which outlines
    the steps
    for automating project development;
- Take a look at
  the project's [Milestones][wts9] page
  to get familiar
  with the team's plans
  for future releases;
- When you feel ready
  to jump into Galactipy development,
  a good place to start
  is to look for issues
  labelled with [`seeking-contributors`][wst10]
  or [`starter-assignment`][wts11];
- After familiarising yourself
  with the project's [labels][wts12] and [stages][wts13],
  you can contribute
  by participating in discussions on issues
  at any of the **Needs** statuses,
  especially those in the [**Needs Triage**][wts14] stage;
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
[can be scary][wts15]
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
  as a continuous [debate][wts16],
  and we are always open
  to discussing
  with different minds
  in a constructive way.
  You can reach out to us
  in our [Merge Requests][intro3]
  and [Issue Tracker][intro2]
  and comment on current developments
  with questions,
  doubts
  and suggestions.
  If still unsure,
  reach us by [e-mail][wts17]
  to introduce yourself,
  we will help you
  with further orientation;
- **Lurk first:**
  there is no need
  to rush things in open source,
  take your time
  by simply observing repo activity
  (you can set the option
  to [watch][wts18] the repository),
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
  that Galactipy needs.
  Check [starter assignment][wts11] issues,
  or [find your own][wts19]
  that deserves your time and effort.

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
   when submitting a Merge Request
   helps everyone involved.
   Jumping into discussions
   don't just improve your contributions;
   it also helps you
   learn much more
   from those with more experience
   and improve
   your problem-solving skills;
2. **Patience is part of the process:**
   waiting for feedback on Merge Requests,
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

## :classical_building: Fundamental Policies

### Code of Conduct

Galactipy has adopted the [Contributor Covenant][cc1]
as its Code of Conduct,
and we expect project participants
to adhere to it.
Please read the [full document][cc2]
to understand
how to properly communicate
with others
and know which actions
will and will not be tolerated.

### Open Development

All work on Galactipy happens
directly on [GitLab][dev1],
with roadmap
and [milestones][wts9]
being managed
via the project's repository.
Therefore,
a GitLab account is needed
to start contributing.

A [GitHub mirror][dev2] is set up
to facilitate discovery of the template
by other users,
but this repository
should not be used
for active development.

#### Contributor Promotion

Access to the upstream repository is granted
at the project owner's discretion,
with no current structured process
to evaluate and promote fork contributors.
However,
we are open
to assign roles
to the upstream Galactipy repository
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
  whether in issue and MR discussions
  or directly
  through [e-mail][wts17] contact;
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
  - [Showing responsibility][dev3] to document
    all relevant information
    promptly,
    whether for
    internal or external use,
    to ensure maintenance
    of our [institutional knowledge][dev4];
  - Upkeeping repository order
    through our [practices][tldr4];
  - Being an exemplar advocate
    for a [welcoming community][dev5];
- Aside from
  displaying the aforementioned conduct,
  the contributor must express
  their actual interest
  in attaining a [role][dev6]
  in the upstream repository.

We also recommend interested individuals
to follow
the guide to the [_Pragmatic Open Source Contributor_][dev7],
which goes
into the attitude
for candidate contributors
in more detail.

#### Roadmap Management

Medium and long-term vision for Galactipy
is managed through the project's roadmap,
where the general direction of development
is stored and accessible
for anyone to see and comment.
Issues and Merge Requests should ideally
be related to a milestone
once a work item has been created.

Any contributor can propose a new distinct deliverable
to be added to the roadmap.
A [Merge Request][wts16] containing the proposal
must be opened with the [**Project Policies** template][road1],
detailing nature, scope and purpose of the milestone.

The MR must detail the proposed milestone
added to the [`ROADMAP.md` table][road2]
for discussion,
containing:

- **Title:**
  the proposed title for the milestone;
- **Description:**
  an overview of the development,
  in a short summary.
  Details regarding the milestone
  will be discussed in the MR and
  later be included in the official project milestone
  if accepted;
- **Theme:**
  the theme to which
  the proposed milestone is best related to.
  The naming is open to discussion and
  the author is free to suggest it,
  along with an Emoji to
  better convey its nature,
  in a `:emoji: Theme Title` pattern;
- **Timeline:**
  a broad estimation of when this proposed milestone
  can be delivered in full.
  Should act as a starting point for
  the actual work tracking
  to be done via
  the official milestone.

Contributors and maintainers will participate in the discussion to
[refine][road3] the scope of the milestone and
either accept of reject the proposal via [thumbs-up/thumbs-down][road4] reactions
on the author's initial comment.

Once a milestone has been accepted for inclusion in the roadmap,
it will be officially created in the [Milestones][wts9] page.
The milestone itself should contain:

- The [Motivational Narrative][road5] as a summary to the milestone's goal;
  - We suggest using the following pattern if the actor of the deliverable is not clear:
    `**In order to** {GOAL},<br>**The project will** {ACTION}.`;
- Detailed information collected from the discussion
  regarding nature and scope,
  under the **Reasoning** section;
- A non-exhaustive list of leading developments
  that have been discussed in the MR
  in the **Anticipated Developments** section;
- Details on potential bottleneck mappings
  in the **Caveats** section.

Once the official milestone is created,
it should be attached to the proposal MR and
the `ROADMAP.md` table should be updated
with the actual link to the milestone
before merging to `master`.

>>> [!tip]
Milestones should be the entry door for new contributors
to have a general glimpse on
what the project has been prioritising and
where it wants to go,
helping newcomers get onboarded more quickly.
Therefore, contributors writing official milestones
should approach the task with the following goals in mind:

- [_Comprehensive, yet succinct_][road6];
- [_Standardised, yet conscious_][road7].
>>>

After a milestone has been completed,
a new Merge Request should be opened to
update the `ROADMAP.md` table in the **Timeline** field
with the following possible values:

- `**Delivered with <version> :airplane_departure:**`,
  if properly associated to a [GitLab Release][road8];
- `**Delivered Internally :100:**`,
  if the milestone has no impact on project releases.

Likewise,
the MRs should be associated with
the completed milestone.

#### Work Item Tracking

Galactipy development is iterative
and structured preferably around [Merge Requests][wts16].
Whenever project advancements are not immediately deliverable,
progress is tracked through GitLab Issues and Tasks.
Use cases for this type of work item include:

- User requests
  (since general users are not allowed to create MRs);
- Larger scoped developments
  which are unable to be delivered
  in a single MR;
- Ideas for future developments
  which can't be prioritised
  due to scope or team capacity.

To effectively manage
issue and task lifecycles,
we use [GitLab Statuses][issue1].
Our approach to this feature
relies on
keeping few options for
in-progress and completed items
and providing different options
for other stages of the lifecycle.
This allows project members to
better relay [context][road3]
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

| Status                                                | Status Category | Description                                                                                                                                                                                                                                                                                                                                                               |
| :---------------------------------------------------- | :-------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Triage icon][issue2] **Needs Triage**               |     Triage      | Initial stage for [User requests][issue3], which require a first analysis by a Galactipy contributor before work on its scope is either accepted or declined. It is also the default open state for new items if not overriden.                                                                                                                                           |
| ![Refinement icon][issue4] **Needs Refinement**       |     Triage      | Describes more general ideas that might receive development at some point, but whose current state does not detail implementation or paths to delivery. Lacking scope, represents more of a desire than an actual proposal – which might actually prove unfeasible later. Should be used to inform the need for further discussions before being cleared for development. |
| ![Criteria icon][issue5] **Needs Criteria**           |     Triage      | This describes items whose scope is set, but acceptance criteria is still pending to be added before being cleared for development. In contrast with the **Needs Refinement** status, in this stage the deliverable is known and understood, but is waiting for a contributor to detail in smaller steps.                                                                 |
| ![Steps icon][issue6] **Needs Delivery Steps**        |     Triage      | A specific type of triaging item, signaling pending work before the item can be cleared as a [starter assignment][issue7] development. In contrast with the **Needs Criteria**, this stage indicates the work item will be processed with greater detail than usual so a new contributor can pick it up and develop it with little to no friction.                        |
| ![Decomposition icon][issue8] **Needs Decomposition** |     Triage      | Proposals or requests that have been deemed too large in scope to be considered a single work item and must be broken down in two or more items before proceeding.                                                                                                                                                                                                        |
| ![Greenlit icon][issue9] **Greenlit**                 |      To Do      | Items that have been cleared for development after having their scope and acceptance criteria properly defined.                                                                                                                                                                                                                                                           |
| ![Pipeline icon][issue10] **Pipeline**                |      To Do      | Items that have scope and acceptance criteria, but that address a specific development stream which is not currently considered the most valuable for delivery. Can be picked for development, but should be left out in favour of **Greenlit** and **Priority** items.                                                                                                   |
| ![Priority icon][issue11] **Priority**                |      To Do      | Signals items which take priority over other cleared work items. Should be used with discretion and only in cases where lack of action can lead to significant issues to security or user experience.                                                                                                                                                                     |
| ![Progress icon][issue12] **In Progress**             |   In Progress   | Items currently being actively worked on.                                                                                                                                                                                                                                                                                                                                 |
| ![Done icon][issue13] **Done**                        |      Done       | Items delivered in full.                                                                                                                                                                                                                                                                                                                                                  |
| ![Canceled icon][issue14] **Out of Scope**            |    Canceled     | Items deemed out of the scope of Galactipy.                                                                                                                                                                                                                                                                                                                               |
| ![Canceled icon][issue14] **Cannot Implement**        |    Canceled     | Items which are unable to be delivered by the development team in its original form, due to technical barriers or security risks.                                                                                                                                                                                                                                         |
| ![Canceled icon][issue14] **Not Feasible**            |    Canceled     | Items which can technically be delivered, but that have been declined for development due to any other factor outside the other **Canceled** stage items.                                                                                                                                                                                                                 |
| ![Duplicate icon][issue15] **Duplicate**              |    Canceled     | Items marked as duplicates of previous work items.                                                                                                                                                                                                                                                                                                                        |

#### GitLab Practices

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

>>> [!caution]
The only exception
to using imperative mood
in issue titles is
when it refers
to a bug or malfunction
that has been identified.
In this case,
the title should refer
to the erroneous **behaviour** of Galactipy.

Since when bugs first appear,
its solution is unknown,
by providing
the behaviour being observed
we can equally understand
_what_ needs to be addressed
to close the issue.
>>>

##### Tasks Are Used as Acceptance Criteria for Issues

[Tasks][practices2] are a specific type of work item
in GitLab
which can be associated
with issues as their child items.
In Galactipy development,
Merge Requests are
the [default][wts16] form of actionable development,
while issues are used
for compiling user requests
and development intentions
that can not be directly delivered
through an open Merge Request.

In either case,
Tasks must be used
to complement the open issue
with their acceptance criteria
to be closed.
Their titles should follow
the same [rules][practices3] as issue titles,
while descriptions are optional
if relevant to understand implementation.

>>> [!caution]
The only label allowed on tasks
is `manual-closure`.
Otherwise,
there should be no labels
associated with a task.
>>>

##### Usage of the `seeking-contributors` Labels

`seeking-contributors` is the label used
to indicate work items
whose authors need help from the community
in further advancing with development.

The `opinion` label marks work items which
are at a [**Triage**][wts13] stage
and whose discussion has stalled.
It signals other contributors and the community
that more people are requested
to provide opinion on the matter,
as a consensus for its final scope
has not been reached yet.

The `delivery` label,
on the other hand,
is used to mark items
at the **To Do** stage
that can be picked up for development
if a contributor is interested
in delivering the solution.
It is similar in this manner
to the `starter-assignment` labels,
with the difference that `seeking-contributors::delivery` is aimed
towards contributors
with intermediate experience in the project.

>>> [!important]
Contributors planning
on refining an issue
or Merge Request
to mark with the `seeking-contributors::delivery` label
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

##### Blocks Must be Set at the Same Issue Level

[Issue blocks][practices4] are not mandatory
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
tasks can only block **tasks**.

##### Tasks Should Have no Milestones

Given GitLab Tasks are used
for acceptance criteria of issues,
breaking a deliverable down to
smaller components,
we prefer to keep
only issues and MRs
associated with milestones.
This reduces clutter
in the milestone board.

However,
given the [default behaviour][practices5] of GitLab,
tasks associated with milestones
can accumulate over time.
The association
should be removed
by [being queried][practices6]
in the Issue Tracker
and edited
through the "Bulk edit" option.

### Versioning Customs

As a Cookiecutter template,
users rely on Galactipy
only once
in their project's entire lifecycle:
at its creation.
From the user's perspective,
differences between Galactipy versions
are only minor
and the project itself
is always in a stable configuration.

From this view,
Galactipy is not a dynamic library
that demands continuous maintenance
to prevent downstream application issues
but rather a pre-configured package
providing essential files
and configurations
for rapid project initiation.

Galactipy's versioning
should be seen
as reflecting
the progression of our efforts
over time.
Given the absence
of breaking changes,
we choose to adhere
to [Intended Effort Versioning][version1]
for consistency.

We approach our versions
with the following pattern:

- Version `v1.0.0` can only be set
  once all requirements specified
  in the %7 milestone
  are satisfied;
- Versions can only be tagged
  if altering end-user generated projects;
  changes to project internals only
  do not qualify for tagging;
- Update **MICRO** versions when:
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
- Update **MESO** versions when:
  - Project generation behaviour is modified
    without modifications
    to `cookiecutter.json` prompt;
  - Configuration files behaviour is modified;
  - Code files are added,
    removed
    or updated;
- Update **MACRO** versions when:
  - Available options
    for a step in `cookiecutter.json`
    are altered;
  - Steps are
    either added or removed
    from `cookiecutter.json`;
  - The type of a step
    is altered in `cookiecutter.json`.

### Branch Organization

We apply the [GitLab Philosophy][tldr1]
for conducting new development,
which means
that all changes
revolve around open Merge Requests,
and Merge Requests are
the central space
for discussing design,
implementation
and monitoring development health
with [CI pipelines][branch1].

Creation of new branches
without subsequent attachment
to a new MR
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
during Merge Request reviews:

- Use the [imperative mood][practices3]
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
  or extensive Merge Request details.

While flash branches can sometimes
be linked to `quick-win` issues,
they primarily serve
as a signal
for short-lived changes
without the need
for prior planning
or detailed documentation.
>>>

### Commit Customs

#### Gitmoji

Galactipy uses [Gitmoji][commit1]
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

>>> [!warning]
The shorthand codes
specified in the Gitmoji website
use the GitHub standard.
For some of the Gitmoji,
these shorthands are different
when rendering in GitLab,
be aware of which ones:

| Gitmoji | Default Shorthand | Shorthand in GitLab |
|:-------:|:-----------------:|:-----------------------:|
| :brick: | `:bricks:` | `:brick:` |
| :construction_site: | `:building_construction:` | `:construction_site:` |
| :camera_with_flash: | `:camera_flash:` | `:camera_with_flash:` |
| :card_box: | `:card_file_box:` | `:card_box:` |
| :goal: | `:goal_net:` | `:goal:` |
| :pencil: | `:memo:` | `:pencil:` |
| :face_with_monocle: | `:monocle_face:` | `:face_with_monocle:` |
>>>

If the changes
still reflect a work in progress
that will be rebased
at a later moment,
we recommend committing
with the `:construction:` Gitmoji
so the CI will ignore it.

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
The article [_How to Write a Git Commit Message_][commit2]
is a valuable resource
and reading through it
is strongly recommended
before contributing,
as developers are expected
to apply those principles
when committing.

#### Git Trailers

Every commit should also
be identified with the respective [Git trailer][commit3]
to categorise the type of change being made.
When a new version of Galactipy
is released through a tag,
a CI pipeline compiles every trailer
to automate the version's release
and update the `CHANGELOG` file
in the root directory.

The available trailers
are listed below
and defined in the [`changelog-config.yml`][commit4] file:

|  Git trailer  |       Category in CHANGELOG        | Use Cases |
| :---------------: | :------------------------------------: |----|
| `enhancement`        |           :milky_way: Components            | Updates in behaviour and functionality to existing features for end users. |
| `feature`        |           :milky_way: Components            | Introduction of new features, tools and integrations for end users. |
| `bug` |      :wrench: Fixes & Refactoring      | Correction of bugs introduced in previous releases that went unnoticed. |
| `refactoring` |      :wrench: Fixes & Refactoring      | Modifications to the code without changing its output. |
| `bugfix` |      :wrench: Fixes & Refactoring      | Correction of bugs introduced in feature branches and identified before they are merged. |
| `fix` |      :wrench: Fixes & Refactoring      | Minor corrections that can not be characterised as bugs in and of themselves, such as typos and naming conventions. |
| `ci` |     :package: Build System & CI/CD     | Changes to Galactipy's GitLab CI file. |
| `testing`        |     :package: Build System & CI/CD     | Changes to tests for Galactipy. |
|      `hooks`      |            :gear: Internals            | Modifications made to pre-gen and post-gen hooks. |
| `project-config`  |            :gear: Internals            | Modifications made to configuration files for the project, excluding those specified in the `policies` trailer. |
| `build`        |     :construction_site: Template Internals     | Modifications to CI workflows for generated projects. |
| `template-config` | :construction_site: Template Internals | Modifications made to configuration files for generated projects, inside `{{ cookiecutter.repo_name }}`. |
|  `documentation`  |          :pencil: Documentation          | Changes to documentation, either in Galactipy's or the template's `README` file. |
|  `policies`  |          :scroll: Project Policies          | Modifications to official project policies in `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.triage-policies.yml`, `.pre-commit-config.yaml`, files under `.gitlab` and all `tool` sections in `pyproject.toml` except for `tool.poetry`. |
|  `milestones`  |          :scroll: Project Policies          | Milestone updates in `ROADMAP.md`. |
|  `dependencies`   |    :arrow_up: Dependency Updates     | Dependency updates, for either Galactipy itself or the template. |

### Styling

#### Codestyle

The project uses [Ruff][style1]
for formatting and codestyle.
Developers can check
both the linter
and the formatter
with the preconfigured tasks
with `invoke codestyle` and `invoke lint` commands.

Given the boilerplate code
used by Cookiecutter,
the formatter ignores all files under the `{{ cookiecutter.repo_name }}` directory,
as running Ruff otherwise
will cause it to crash.
When modifying code
within this directory,
developers are expected
to validate their codestyle
in line with Ruff
by manually generating projects
before submitting changes
for approval
through the Merge Request.

#### Semantic Line Breaks

When editing Markdown files,
[Semantic Line Breaks][style2] should be applied.
This increases the document's readability
by other contributors
and makes changes clearer
when using `git diff`.
This comes from Brian Kernighan
in his 1974 book _"UNIX for Beginners"_:

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

On a more practical level,
this [article][style3] from Derek Sivers
provides additional reasons
for adopting this style.

The only files
that should not follow this rule
are issue and Merge Request templates
inside [`.gitlab`][style4] and [`CHANGELOG.md`][style5].

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

### Continuous Integration

Besides being hosted in GitLab,
Galactipy uses [GitLab CI][ci1]
to automate the following development streams:

- Testing;
- Test coverage reporting;
- Code quality analysis;
- Releases;
- GitHub mirror branch updates.

For releases
and mirror branch updates,
a [bot user][ci2] is used
for authoring changes
through the CI/CD group variable `$GALACTIPY_BOT_API_TOKEN`.

Merge Requests can not be completed
unless its CI pipeline passes.
The project's CI configuration
runs under more strict rules
and no jobs are allowed to fail.
This includes the external job
provided by [Codacy][ci3],
which is used for code quality assurance.
Take a look at the [Pull Requests][ci4] page for Galactipy
for further information
on reasons
why a PR Quality Review job
might have failed.

Developers should be familiar
with the [GitLab CI syntax][ci5]
to effectively contribute
with further automation
of the development cycle.

### Licence

By contributing to Galactipy,
you agree that your contributions
will be licensed under
the [MIT Licence][licence1].

## :book: Our Philosophy

This document is
more than just a technical guide
on how to contribute;
it defines the deeper principles
we follow
to shape our approach
to Galactipy development.
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

### Start with a Merge Request

> Adapted from the [Communication][values2] section of the GitLab Handbook.

When possible,
it's best practice
to start a discussion
with a Merge Request (MR)
instead of an issue.
An MR is associated
with a specific change
that is proposed
and transparent for everyone
to review
and openly discuss.

The nature of MRs
facilitate discussions
around a proposed solution
to a problem that is actionable.
An MR is actionable,
while an issue
will take longer
to take action on.

1. **Always** open an MR
   for things you are suggesting
   and/or proposing.
   Whether something is not working right
   or we are iterating
   on a new internal process,
   it is worth opening a Merge Request
   with the minimal valuable change
   instead of opening an issue
   encouraging open feedback on the problem
   without proposing any specific change directly.
   Remember,
   an MR also invites discussion,
   but it's specific
   to the proposed change
   which facilitates focused decision;
2. Never ask someone
   to create an issue
   when they can default
   to the Merge Request;
3. Not every solution
   will solve the problem at hand.
   Keep discussions focused
   by **defining the problem first**
   and **explaining your rationale**
   behind the Minimal Valuable Change (MVC)
   proposed in the MR;
4. Have a [**bias for action**][dev3]
   and do not aim for consensus.
   Every MR is as-is proposal,
   if an MR's author isn't responsive
   take ownership of it
   and complete it.
   Some improvement is better than none;
5. If submitting a change for a feature,
   **update the description with the final conclusions**
   – why an MR was rejected
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
   in separate issues/MRs
   and link them.
   An MR can start off
   as only a problem description
   and `TODO` comments;
7. Do not leave MRs open
   for a long time.
   MRs should be **actionable** –
   maintainers should have
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
   you can use the Reply to Comment button
   from the comments to create one.
   This will prevent comments
   from containing many interweaved discussions
   with responses that are hard to follow;
10. If your comment or answer
    contains separate topics,
    write separate comments for each,
    so others can address topics independently
    using the Reply to comment button;
11. If you have received any feedback
    or questions on your MR,
    try to acknowledge comments
    as that's how we ensure
    we create an environment of belonging
    for all team members.
    Merging your MR as-is
    without giving an answer
    or any response
    makes the commenters feel
    their opinions are unheard.
    On the other hand,
    having a MR with too many comments
    may risk the author falling
    into a perpetual loop of
    changing the MR description
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
    and collaborative –
    not to lose efficiency.
    Not everyone will agree,
    but we expect all people to
    disagree, commit, and disagree;
12. Even when something is not done,
    share it internally
    so people can comment early
    and prevent rework;
13. Create a **Draft** Merge Request
    to prevent an accidental early merge.
    Only use Draft when merging it
    would **make things worse**,
    which should rarely be the case
    when contributing to the project.
    Most Merge Requests that are in progress
    don't make things worse.
    In this case, do not use Draft;
    if someone merges it
    earlier than you expected
    just create a new Merge Request
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
    after the Merge Request is merged,
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
the issue or MR that has the decision
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
a milestone,
MR
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

At Galactipy,
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
in issue and Merge Request discussions;
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

### There Are no Good First Issues

The concept of
labelling issues in open source projects
to mark potential good contributions
for a first timer
has its origins in the [First Timers Only][values7] initiative
by Kent C. Dodds.

At Galactipy,
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
  to [orient][dev5] contributors
  should they feel lost
  and reassure [clear communication][values8]
  with them;
- For **Galactipy users**
  who have opened a request
  on the Issue Tracker,
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
  by adding `/label ~"up-for-a-change"`
  to the request description
  so that a developer can mentor you
  on the solution.

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
  - [`pre_gen_project.py`][wts4] is used
    to validate parameter inputs
    from the user;
  - [`post_gen_project.py`][wts5] is used
    to ensure the project is generated
    with the correct files and content;
- [Tests][wts6] for the functions
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

Sometimes,
a contributor will already have
a particular new change or fix
in mind.
If seeking ideas,
consult the list of [starter assignments][wts11].

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
  Proposing a Merge Request is appropriate
  only when a clear problem
  or beneficial change
  has been identified.
  If simply having trouble using Galactipy,
  go through the [`README`][wts1] file and links directing
  to support content first,
  rather than consider filing an issue
  or proposing an MR.
  When in doubt,
  email [`mpq.dev@pm.me`][wts17] first
  about the possible change;
- Search the [Issue Tracker][intro2]
  and [past Merge Requests][intro3]
  for related discussions.
  Often,
  the problem has been discussed before,
  with a resolution
  that doesn't require a code or configuration change,
  or recording what kinds of changes
  will not be accepted as a resolution;
- Otherwise,
  if a logically similar issue or MR already exists,
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

#### Opening Admissible Merge Requests

For developers and maintainers,
changes should not be approached
in a reactive way
as demands,
but as a proactive **proposals**.
If you are contributing in the Galactipy repository,
you are expected
to always act on
and provide proposals
to improve the state of the project.
This distinguishes developers
from Galactipy users who,
unfamiliar with the codebase
and project configuration,
are only able to _request_ changes
through the Issue Tracker.

To work under
a proactive proposal mindset,
we always [start with a Merge Request][wts16].

It is best
to follow these best practices
when proposing changes:

- **Always** use one of the [Merge Request templates][changes4],
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
  by tagging them in an MR
  before submitting the code for review.
  Talking to team members
  can be helpful
  when making design decisions.
  Communicating the [intent][road3] behind your changes
  can also help expedite Merge Request reviews;
- Follow our [commit customs][tldr2],
  as consistent commit messages
  that follow these guidelines
  make the history more readable.

Also equally important
is the notion to
**keep MRs simple**,
with the amount of changes in a single MR
as small as possible.
If you want
to contribute a large feature,
think very carefully about
what the minimum valuable change is.
Can you split the functionality
into two smaller MRs?
Can you submit
only a fraction of the code?
Can you start
with a very simple proof-of-concept?
Can you do
just a part of the refactor?

<div align="center">

_Live by smaller iterations._

</div>

Small MRs
which are more easily reviewed
lead to higher code quality,
which is more important to Galactipy
than having a minimal commit log.
The smaller an MR is,
the more likely it will be merged quickly.
After that
you can send more MRs
to enhance and expand the feature.
The [_How to Get Faster PR Reviews_][changes5] guide
from the Kubernetes team
also has some great points regarding this.

#### Review Criteria

Before considering how to contribute,
it's useful to understand
how contributions are reviewed,
and why changes may be rejected.
See the detailed [guide][changes6] for code reviewers
from Google's Engineering Practices documentation.
Simply put,
changes that have many or large positives,
and few negative effects or risks,
are much more likely
to be merged,
and merged quickly.
Risky and less valuable changes
are very unlikely to be merged,
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
will be caught by [`test_bake_project`][changes7],
the reality is that
developers should be aware
of limitations
currently faced by the project
to implement end-to-end tests,
as its nature relates less to code
and more to behaviour
after file generation.

The %1 milestone has been created
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
    due to Jinja [whitespace control][changes8]?
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

### Merge Request Review Process

After [starting with a Merge Request][wts16],
ensuring you have opened an [admissible MR][mr1]
and have finished contributing with changes,
the review process can start.

#### Contribution Acceptance Criteria

To make sure that
your Merge Request can be approved,
ensure that
it meets the contribution acceptance criteria below:

1. The change is
   as small as possible;
2. If the Merge Request contains
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
5. The MR contains
   a few logically organised commits,
   using [Gitmoji][mr2].
   We do not apply the squash method
   for merging changes;
6. The changes can merge
   without problems.
   If not,
   you should rebase
   if you're the only one working
   on your feature branch,
   otherwise merge the default branch
   into the MR branch;
7. Only one specific issue is fixed
   or one specific feature is implemented.
   Do not combine things;
   send separate Merge Requests
   for each issue or feature;
8. Contains functionality
   that other users will benefit from;
9. Changes do not degrade performance;
10. If the Merge Request adds
    any new libraries,
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

If the Merge Request
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
a Merge Request should be first
reviewed by a reviewer
in each domain
(e.g., CI,
GitHub features,
GitLab features
etc.)
the MR touches,
as maintainers may
not have the relevant domain knowledge.
This also helps
to spread the workload.

Depending on the areas
your Merge Request touches,
it must be approved
by one or more maintainers.

Getting your Merge Request merged
also requires a maintainer.
If it requires more than one approval,
the last maintainer
to review and approve merges it.

### Roles and Attributions

#### The Responsibility of the Merge Request Author

The responsibility to
find the best solution
and implement it
lies with the Merge Request author.
The author stays assigned
to the Merge Request
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
of your own Merge Request,
following the [Code Review][mr3] guidelines.
During this self-review,
try to include
comments in the MR on lines
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
you'll need many Merge Requests
to deliver a feature
– for example,
you created a proof of concept
and it is clear the feature
will consist of 10+ Merge Requests –,
consider identifying reviewers and maintainers
who possess the necessary understanding
of the feature
(you share the context with them).
Then direct all Merge Requests
to these reviewers.
Having stable reviewer counterparts
for multiple Merge Requests with the same context
improves efficiency.

Before the review,
the author is requested
to submit comments
on the Merge Request diff
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
Explicitness around MR review types
is efficient for the MR author
because they receive the type of review
that they are looking for
and it is efficient for the MR reviewers
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
  they should explain [why, not what][road3];
- Requesting maintainer reviews
  of Merge Requests with failed tests.
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
     for the MR template;
2. Follow the Galactipy patterns,
   even if you think there's a better way.
   Discussions often delay merging code.
   If a discussion is getting too long,
   consider following
   the documented approach
   or the maintainer's suggestion,
   then open a separate MR
   to implement your approach
   as part of our best practices
   and have the discussions there;
3. Consider splitting big MRs
   into smaller ones.
   Around 200 lines is a good threshold:
   - Smaller MRs reduce cognitive load
     for authors and reviewers;
   - Reviewers tend
     to pick up smaller MRs
     to review first
     (a large number of files
     can be scary);
   - Discussions on one particular part of the code
     will not block
     other parts of the code
     from being merged;
   - Smaller MRs are often simpler,
     and you can consider
     skipping the first review
     and sending directly
     to the maintainer,
     or skipping one of the suggested domains
     (e.g.,
     CI,
     GitHub features,
     GitLab features
     etc.);
   - :warning: Split MRs with caution:
     MRs that are too small
     increase the number of total reviews,
     which can cause the opposite effect;
4. Minimise the number of reviewers
   in a single MR.

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
  as outlined in the [Merge Request guidelines][mr1].
  Some reviewers may not be familiar
  with the product feature
  or area of the codebase.
  Thorough descriptions help all reviewers
  understand your request
  and test effectively;
- If you know your change depends
  on another being merged first,
  note it in the description
  and set a Merge Request dependency;
- Be grateful
  for the reviewer's suggestions
  ("Good call. I'll make that change.");
- Don't take it personally.
  The review is of the code,
  not of you;
- Explain [why][road3] the code exists
  ("It's like that because of these reasons.
  Would it be more clear
  if I rename this class/file/method/variable?");
- Extract unrelated changes
  and refactoring tasks
  into future MRs/issues;
- Seek to understand
  the reviewer's perspective;
- Try to respond to every comment;
- The Merge Request author
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
  to be incorporated into the MR
  before it is merged.
  It is a judgment call
  by the MR author
  and the reviewer
  as to if this is required,
  or if a follow-up issue
  should be created
  to address the feedback
  in the future
  after the MR in question is merged;
- Request a new review
  from the reviewer
  once you are ready
  for another round of review.
  If you do not have
  the ability to request a review,
  `@` mention the reviewer instead.

#### The Responsibility of the Reviewer

All Galactipy contributors
who choose to review
and provide feedback on Merge Requests
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
to be able to block a Merge Request
from advancing simply
because you say "No" without [giving an explanation][road3].
Be open to having your mind changed.
Be open to working with the contributor
to make the Merge Request better.

Reviews that are
dismissive
or disrespectful
of the contributor
or any other reviewers
are strictly counter
to the [Code of Conduct][cc2].

When reviewing a Merge Request,
the primary goals are
for the codebase to improve
and for the person submitting the request to succeed.
Even if a Merge Request does not land,
the submitters should come away from the experience
feeling like their effort
was not wasted
or unappreciated.
Every Merge Request from a new contributor
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

- Does this change make sense for Galactipy?
- Does this change make Galactipy better,
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
  If blocked by one or more open MRs,
  set an [MR dependency][mr4];
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

[Nits][mr5]
(requests for small changes
that are not essential)
are fine,
but try to avoid
stalling the Merge Request.
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
on the success of the Merge Request.
Yes,
we may land a particular change
that makes Galactipy better,
but the individual might just not want
to have anything to do with Galactipy
ever again.
The goal is not just
having good code,
you should guide the author
towards succeeding
with their contributions,
whether the MR is approved or not
in the end.

Lastly,
**accept that there are different opinions about what belongs in Galactipy.**
It is not uncommon for contributors
to suggest new features they feel
would make Galactipy better.
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
  on reviewing Merge Requests;
- Finding bugs is important,
  but thinking about good design
  is important as well.
  Building abstractions and good design
  is what makes it possible
  to hide complexity
  and makes future changes easier;
- Enforcing and improving [codestyle][tldr3]
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
  consider approving the Merge Request
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
  in a Merge Request that is an urgent fix
  should be avoided;
- Doing things well today is usually better
  than doing something perfectly tomorrow.
  Shipping a kludge today is usually worse
  than doing something well tomorrow.
  When you are not able
  to find the right balance,
  ask other people
  about their opinion
  and use the [`seeking-contributors::opinion`][mr6] label.

#### The Responsibility of the Maintainers

Maintainers are responsible for
the overall health,
quality,
and consistency
of the Galactipy codebase.

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
on their knowledge of the overall Galactipy codebase,
and not that of any specific domain,
they can review,
approve,
and merge MRs
from any type of changes.

Maintainers are the responsible individuals
of assuring that the acceptance criteria of a Merge Request
are reasonably met.
In general,
quality is everyone's responsibility,
but maintainers are held responsible
for ensuring that an MR
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
was involved in a Merge Request as a reviewer,
it is recommended that
they are not also picked
as the maintainer to
ultimately approve and merge it.

Maintainers should check before merging
if the Merge Request is approved
by the required approvers.
If still awaiting further approvals from others,
`@` mention the submitter
and explain why in a comment.

### How to Behave among Other Contributors

Merge Requests,
when worked under the concept of [proposals][mr1],
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

As a Galactipy contributor, your responsibilities
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
     [documented][road3] via the commit description;
   - Maintain and update Git hooks
     to check and enforce any project standards
     so people don't have the frustration
     of going back and forth on the Merge Request;
   - Maintain and update CI jobs
     to automate further development tasks
     and allow contributors to focus
     on delivering new features;
   - Be conscious of the [energy vampires][community2] perturbing development
     and either propose [actions][dev3]
     for eliminating them
     or seek discussion and feedback
     via an [**Internal Improvement**][community3] MR;
   - Keep the GitLab repository efficient
     by properly labelling work items
     and associating them
     with the relevant project milestone;
2. Become an advocate for new contributors:
   - Be overly conscious of [how to behave][values8]
     when interacting with a user
     publishing their first request.
     The guidelines for [reviewers][community4] also apply
     when communicating with Galactipy users
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
     You have [started small][community5],
     so why not help someone else
     take this small first step?
   - Likewise,
     there are developments
     you could complete in less than 10 minutes.
     Why not turn them into [starter assignments][issue7]?

#### About Starter Assignments

We refer to our "Good First Issue" work items
as **starter assignments**,
a term we believe better aligns
with our goal
of fostering a vibrant community
around Galactipy.
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
   to begin contributing to Galactipy;
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
   and help Galactipy thrive.

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
  you can leverage GitLab's
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
Leverage [replies][community6]
and [reactions][road4]
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

Inspired by [Typer's][help1] welcoming community
and their positive outlook
on the effect of [collective intelligence][help2],
we are committed to enabling an environment
in which such exponential interactions
can take place.
As such,
one of the best ways people can
contribute to Galactipy
is by helping others,
either users like you
who have reached the members of the project
with questions and requests
or the development team itself.

The most direct way
you can provide your help to others
is to look for open [Requests for Support][help3]
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
     to provide a [minimal, reproducible example][help4],
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

>>> [!tip] Tip: When Things are Difficult
When things are great,
everything is easier,
so that doesn't need much instructions.
But when things are difficult,
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
But still,
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

#### Commitment to Help

What consumes
most of the time of the development team
is actually answering questions
and solving problems.
We end up not being able
to add new features,
fix bugs
and review Merge Requests
as fast as we wanted
because too much of the time
is spent handling user requests.

Also, this is
on top of all the help
provided by several community members
that dedicate a lot of their time
to come here
and aid others.

If more Galactipy users
came to help others like them
just a little bit more,
it would be much less effort for them.

That's why our templates for requests
include a section
calling authors to action
with improving the Galactipy ecosystem
the best way they can.
For all purposes,
we believe that
contributions should be done by the person's own accord,
demonstrating a [bias for action][dev3]
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
every aspect of Galactipy:
communication,
agility,
organization,
aggregated value
and more!

If you have opened
or are about to open a Request for Support,
we would be extremely grateful
if you could pick one of the options
from the list provided in the template
to commit with additional help
for the project.

We thank you in advance
for your kindness and dedication!

### Contributing through User Requests

If you are simply
having trouble using Galactipy,
go through the [`README`][wts1] file and links
directing to support content first,
rather than filing a request.

Galactipy implements
three types of requests for users
through [Issue Templates][request1]:

- **Requests for Correction**;
- **Requests for Improvement**;
- **Requests for Support**.

All three templates
provide a brief summary
explaining their purpose,
as well as a handy information
on where to best use them.
They contain structured sections
with HTML comments
to guide you further
with opening your request correctly,
please follow them
as closely as possible.
If any instruction is not clear,
please raise your concern
so we can help
and improve them
if applicable.

>>> [!note]
A fourth template,
**Internal Work Item**,
is available to contributors
for specific cases
regarding project development.
This should not be used
if you do not have Developer status.
>>>

**Always use one of the templates for opening requests!**
By taking a single look
at its type
and the structured sections
filled by the author,
we can provide faster feedback
on your request.
We will kindly ask you
to edit the issue
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
  before using the [Search][request2] feature
  for all items in the Issue Tracker;
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
    what the request comprises of;
- Properly format your messages.
  Help the reader focus on what matters
  and understand the structure of your message.
  [GitLab Flavoured Markdown][request3] has a simple
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

If Galactipy is not working correctly for you,
most likely it is a simple configuration issue.
Try running Cookiecutter again
paying attention to the parameters
you have provided.

If you are still having difficulty
generating your project as desired,
open an [RFS][request4]
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
They are very welcome,
as they help us engage with the community
on a more proactive level
and work to deliver a solution
of aggregated value
to our users.

But before opening an [RFI][request5],
take a moment to find out
whether your idea fits with the scope
and [aims][wts9] of the project.
It's up to _you_
to make a strong case
to convince the project's developers
of the merits of this feature.
Please provide
as much detail and context
as possible.

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

Also,
why not take this opportunity
to [become a contributor][dev3]?
After all,
the most effective way
to make a contribution
is to make one [that comes from yourself][wts19].

#### Specific Guidelines for Requests for Correction

Requests for Correction are used
to track unexpected behaviour
from template generation,
namely bugs.

A bug is a **demonstrable** problem
that is caused by
the code in the repository.

Guidelines for [RFCs][resquest6]:

- Use the [issue search][request7]
  to check if a request
  has already been reported;
- Check if the issue has been fixed
  by trying to reproduce it
  using the latest version of Galactipy;
- **Isolate the problem:**
  create a test case
  to demonstrate your issue.
  Provide either
  a repository,
  [gist][request8]/[snippet][request9]
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
  Tools like [`reprexpy`][request10]
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

>>> [!warning]
**Avoid overloading with extraneous details.**
RFCs are the type of request
that most need attention
and careful examination
by the development team,
since a bug can turn Galactipy
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

### Contributing by Reviewing Changes

Changes to Galactipy source code are
proposed,
reviewed
and committed
via [GitLab Merge Requests][intro3].
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
But do not frown
if you merged the Merge Request
and something broke after all.
This is the learning path
to avoiding this mistake
on the next attempt.
Not doing a review
in the first place
will not move you forward either.

To get you quickstarted
on reviewing MRs for Galactipy,
here are a few tips
that may help
overcoming the paralysis
of [taking action][dev3]:

- Verify that
  the appropriate tests
  have been added.
  When testing a feature or change,
  check out the code tests
  at least the happy paths
  according to the specification
  of the MR;
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
  can complete the MR;
- You should not rush
  through a code review,
  but also,
  you need to do it promptly.
  Your colleagues are waiting for you.

We strongly encourage you
to take further readings on
the [Review Process][review1],
the [Responsibilities of the Reviewer][community4]
and [general communication guidelines][values8]
to get more detail
on how to make
the most out of your contributions
as a reviewer.
We appreciate your commitment beforehand!

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
  that require external services;
- Reference material
  for useful Python libraries,
  tips for project management
  and links to useful articles
  and guides for further reading.

You can propose changes and additions
to the documentation
by editing the `README` file
and [opening a Merge Request][wts16]
to integrate your changes to the project.

The current state of the "documentation"
stems from Galactipy's origins
as a fork of `python-package-template`.
The %10 milestone is currently anticipated
to better structure relevant information
and reduce clutter on the `README` file.
We welcome any contributor
willing to help us
make this transition.

### Contributing to Roadmap Maintenance

The project roadmap is maintained
through [GitLab Milestones][wts9].
It provides an overview
of the medium and long-term priorities of Galactipy
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
  that pertain to existing milestones;
- Commenting on [issues without associated milestones][maintenance1]
  and suggesting what relevant developments
  could they be associated with
  for the development team to evaluate;
- Linking issues and Merge Requests
  that provide combined effort
  towards a single goal of the project.
  If two or more development streams
  can be delivered with the same solution,
  we can generate increased aggregated value;
- Becoming a [contributor][intro4]
  to act on existing milestones,
  propose new developments not yet mapped
  or recommend [changes to the roadmap itself][maintenance2].

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
  on the [Galactipy organization][promo2]
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
[intro2]: https://gitlab.com/galactipy/galactipy/-/issues
[intro3]: https://gitlab.com/galactipy/galactipy/-/merge_requests
[intro4]: #speaking_head-proposing-changes-as-a-developer
[intro5]: #reminder_ribbon-other-ways-to-contribute

[tldr1]: #book-our-philosophy
[tldr2]: #commit-customs
[tldr3]: #codestyle
[tldr4]: #gitlab-practices

[setup1]: https://gitlab.com/galactipy/galactipy/-/forks/new
[setup2]: https://docs.gitlab.com/user/group/
[setup3]: https://docs.gitlab.com/user/project/repository/forking_workflow/
[setup4]: #contributor-promotion
[setup5]: https://python-poetry.org/docs/#installation
[setup6]: #development-workflow

[wts1]: https://gitlab.com/galactipy/galactipy/-/blob/master/README.md
[wts2]: https://cookiecutter.readthedocs.io/en/2.0.2/advanced/index.html
[wts3]: https://jinja.palletsprojects.com/en/stable/templates/
[wts4]: https://gitlab.com/galactipy/galactipy/-/blob/master/hooks/pre_gen_project.py
[wts5]: https://gitlab.com/galactipy/galactipy/-/blob/master/hooks/post_gen_project.py
[wts6]: https://gitlab.com/galactipy/galactipy/-/tree/master/tests
[wts7]: https://gitlab.com/galactipy/galactipy/-/blob/master/.gitlab-ci.yml
[wts8]: #continuous-integration
[wts9]: https://gitlab.com/galactipy/galactipy/-/milestones
[wst10]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&label_name%5B%5D=seeking-contributors%3A%3A%2A&type%5B%5D=issue
[wts11]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&label_name%5B%5D=starter-assignment%3A%3A%2A&type%5B%5D=issue
[wts12]: https://gitlab.com/galactipy/galactipy/-/labels
[wts13]: #work-item-tracking
[wts14]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&status=Needs%20Triage&type%5B%5D=issue
[wts15]: https://goauthentik.io/blog/2024-03-07-why-contributing-to-open-source-is-scary/
[wts16]: #start-with-a-merge-request
[wts17]: mailto:mpq.dev@pm.me
[wts18]: https://gitlab.com/gitlab-org/gitlab-foss/-/issues/234#note_17497758
[wts19]: #there-are-no-good-first-issues

[cc1]: https://www.contributor-covenant.org/
[cc2]: https://gitlab.com/galactipy/galactipy/-/blob/master/CODE_OF_CONDUCT.md

[dev1]: https://gitlab.com/galactipy/galactipy
[dev2]: https://github.com/manoelpqueiroz/galactipy
[dev3]: #operate-with-a-bias-for-action
[dev4]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[dev5]: #fostering-an-inviting-community
[dev6]: https://docs.gitlab.com/user/permissions/
[dev7]: https://diurnal.st/2025/03/02/the-pragmatic-open-source-contributor.html

[road1]: https://gitlab.com/galactipy/galactipy/-/merge_requests/new?issuable_template=Project%20Policies
[road2]: https://gitlab.com/galactipy/galactipy/-/blob/master/ROADMAP.md#roadmap-history
[road3]: #say-why-not-just-what
[road4]: https://docs.gitlab.com/user/emoji_reactions/
[road5]: https://blog.crisp.se/2014/09/25/david-evans/as-a-i-want-so-that-considered-harmful
[road6]: https://www.reforge.com/blog/user-stories-misuse
[road7]: https://www.mountaingoatsoftware.com/blog/critiquing-one-of-my-own-real-user-stories
[road8]: https://docs.gitlab.com/user/project/releases/

[issue1]: https://docs.gitlab.com/user/work_items/status/
[issue2]: https://i.imgur.com/TvihyBU.png
[issue3]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&type%5B%5D=issue&label_name%5B%5D=request%3A%3A%2A
[issue4]: https://i.imgur.com/w3ooBe3.png
[issue5]: https://i.imgur.com/vh3wx6m.png
[issue6]: https://i.imgur.com/1qKaXvT.png
[issue7]: #about-starter-assignments
[issue8]: https://i.imgur.com/jJqAFTw.png
[issue9]: https://i.imgur.com/EUrGcQx.png
[issue10]: https://i.imgur.com/t1PyyRu.png
[issue11]: https://i.imgur.com/XImhPUk.png
[issue12]: https://i.imgur.com/Arfse0s.png
[issue13]: https://i.imgur.com/EgINyEc.png
[issue14]: https://i.imgur.com/LTYh3mB.png
[issue15]: https://i.imgur.com/Z82JtFn.png

[practices1]: https://cbea.ms/git-commit/#imperative
[practices2]: https://docs.gitlab.com/user/tasks/
[practices3]: #issue-titles-should-be-framed-in-imperative-mood
[practices4]: https://docs.gitlab.com/user/project/issues/related_issues/#blocking-issues
[practices5]: https://docs.gitlab.com/user/tasks/#add-a-task-to-a-milestone
[practices6]: https://gitlab.com/galactipy/galactipy/-/issues/?state=all&type%5B%5D=task&milestone_title=Any

[version1]: https://jacobtomlinson.dev/effver/

[branch1]: #continuous-integration

[commit1]: https://gitmoji.dev/
[commit2]: https://cbea.ms/git-commit/
[commit3]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
[commit4]: https://gitlab.com/galactipy/galactipy/-/blob/master/.gitlab/changelog_config.yml

[style1]: https://docs.astral.sh/ruff/
[style2]: https://sembr.org/
[style3]: https://sive.rs/1s
[style4]: https://gitlab.com/galactipy/galactipy/-/tree/master/.gitlab
[style5]: https://gitlab.com/galactipy/galactipy/-/blob/master/CHANGELOG.md

[hooks1]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206
[hooks2]: #development-setup

[ci1]: https://docs.gitlab.com/topics/build_your_application/
[ci2]: https://docs.gitlab.com/user/group/settings/group_access_tokens/#bot-users-for-groups
[ci3]: https://app.codacy.com/gl/galactipy/galactipy/
[ci4]: https://app.codacy.com/gl/galactipy/galactipy/pull-requests/open
[ci5]: https://docs.gitlab.com/ci/yaml/

[licence1]: https://gitlab.com/galactipy/galactipy/-/blob/master/LICENCE

[values1]: https://handbook.gitlab.com/
[values2]: https://handbook.gitlab.com/handbook/communication/#start-with-a-merge-request
[values3]: https://handbook.gitlab.com/handbook/values/#say-why-not-just-what
[values4]: https://theknowledge.io/chestertons-fence-explained/
[values5]: https://handbook.gitlab.com/handbook/values/#operate-with-a-bias-for-action
[values6]: https://conversational-leadership.net/we-human-beings-are-complex/
[values7]: https://kentcdodds.com/blog/first-timers-only
[values8]: #how-to-behave-among-other-contributors

[changes1]: https://gitlab.com/galactipy/galactipy/-/blob/master/tasks.py
[changes2]: https://www.pyinvoke.org/
[changes3]: #contributing-with-documentation-changes
[changes4]: https://gitlab.com/galactipy/galactipy/-/tree/master/.gitlab/merge_request_templates
[changes5]: https://github.com/kubernetes/kubernetes/blob/release-1.5/docs/devel/faster_reviews.md
[changes6]: https://google.github.io/eng-practices/review/
[changes7]: https://gitlab.com/galactipy/galactipy/-/blob/master/tests/test_template.py#L1
[changes8]: https://jinja.palletsprojects.com/en/stable/templates/#whitespace-control

[mr1]: #opening-admissible-merge-requests
[mr2]: #gitmoji
[mr3]: #merge-request-review-process
[mr4]: https://docs.gitlab.com/user/project/merge_requests/dependencies/
[mr5]: https://josipmisko.com/posts/code-review-nit
[mr6]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&label_name%5B%5D=seeking-contributors%3A%3Aopinion&type%5B%5D=issue

[community1]: https://gregorybeamer.wordpress.com/2020/11/12/why-code-organization-is-so-important-in-software/
[community2]: https://simonsinek.com/stories/the-right-way-to-stand-up-for-yourself-at-work/
[community3]: https://gitlab.com/galactipy/galactipy/-/merge_requests/new?issuable_template=Internal%20Improvements
[community4]: #the-responsibility-of-the-reviewer
[community5]: https://firstpr.me/
[community6]: https://docs.gitlab.com/user/discussions/

[help1]: https://typer.tiangolo.com/help-typer/#help-others-with-questions-in-github
[help2]: https://www.blockchain-council.org/ai/collective-intelligence-framework/
[help3]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&label_name%5B%5D=request%3A%3Asupport&type%5B%5D=issue
[help4]: https://stackoverflow.com/help/minimal-reproducible-example

[request1]: https://gitlab.com/galactipy/galactipy/-/tree/master/.gitlab/issue_templates
[request2]: https://gitlab.com/galactipy/galactipy/-/issues/?state=all&type%5B%5D=issue
[request3]: https://docs.gitlab.com/user/markdown/
[request4]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Support
[request5]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Improvement
[resquest6]: https://gitlab.com/galactipy/galactipy/-/issues/new?description_template=Request%20for%20Correction
[request7]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&label_name%5B%5D=request%3A%3Acorrection&type%5B%5D=issue
[request8]: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists
[request9]: https://docs.gitlab.com/user/snippets/
[request10]: https://reprexpy.readthedocs.io/en/latest/

[review1]: #merge-request-review-process

[maintenance1]: https://gitlab.com/galactipy/galactipy/-/issues/?state=opened&type%5B%5D=issue&milestone_title=None
[maintenance2]: #roadmap-management

[promo1]: https://docs.gitlab.com/user/profile/notifications/#notification-levels
[promo2]: https://gitlab.com/galactipy
[promo3]: https://gitlab.com/galactipy/galactipy#page_with_curl-citation
