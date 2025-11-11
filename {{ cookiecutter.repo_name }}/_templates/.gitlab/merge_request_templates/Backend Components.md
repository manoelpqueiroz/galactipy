# :puzzle_piece: Backend Components Update

>>> [!note] :bulb: Changes to non-user-facing parts of the {{ cookiecutter.project_name }} API
This template should be used to propose and discuss improvements to backend elements of the application that assist its fluid usage by users.

:ok: **Types of changes to be proposed with this template:** public and private modules API, core logic implementation, utility functions, performance improvements, database-related changes, data storage/management, background processing, API integrations

:no_good: **What this type of proposal does not stand for:**

{% if cookiecutter.app_type != 'bare_repo' -%}
- Direct changes to the CLI behaviour and functionality;
{% endif -%}
{% if cookiecutter.app_type in ['tui', 'hybrid'] -%}
- Direct changes to the TUI behaviour and functionality;
{% endif -%}
- Bug fixes;
- {{ cookiecutter.project_name }} plugin/extension logic.
>>>

## What change do you propose with this MR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

> **Proposed Version:** <!-- What is your proposed version following the EffVer scheme? -->

## Why this change should be considered for release?

<!--
  Defend the reasons why this improvement is important moving forward
  What problem does it solve?
  What benefits does it bring to users?
{%- if cookiecutter.app_type != 'bare_repo' %}
  Does it make front-end interfaces clearer and more accessible for usage?
{%- endif %}
  What would be considered a successful outcome for this development from your perspective?
  How much developer support for this implementation should be expected?

  Feel free to bring some of your personal experience as a {{ cookiecutter.project_name }} user to let us understand the circumstances that led to this proposal
-->

## Submitter Checklist

<!--
  Mark complying items as they are delivered with `[x]`
  Single out unnecessary or unworkable items with `[~]`
-->

>>> [!caution] :scroll: Policy compliance

- [ ] I have read the [`CONTRIBUTING`][1] guide for proposing changes;
- [ ] I provided a concise and clear title for this discussion;
- [ ] I have presented my proposal following the [{{ cookiecutter.project_name }} philosophy][2];
- [ ] I have added the proper [labels][3] to start this discussion;
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
- [ ] I have associated the proposal with the adequate [epic][4];
{%- else %}
- [ ] I have associated the proposal with the adequate [development milestone][4];
{%- endif %}
- [ ] I have followed the [commit customs][5] for the project;
- [ ] I have explained the [reasoning][6] behind my design choices through the commit descriptions;
- [ ] I have added the proper [Git trailers][7] to my commits;
- [ ] I have followed the [Styling Guide][8] for code and Markdown files.
>>>

>>> [!important] :technologist: Development control

- Regarding user impact: <!-- Pick only one -->
  - [ ] I have verified the change does not break the user experience with the application;
  - [ ] This update generates breaking changes; I have offered migration options for users;
- Regarding user experience:
  - [ ] I have validated that the change does not degrade performance;
  - [ ] I have attested the change does not erase persisted user data;
  - [ ] I have verified the updated code does not generate unnecessary output to the user;
  - [ ] I am confident this change does not pose security risks for the user;
- Regarding code structure:
  - [ ] I have followed best design practices to organise the source code;
  - [ ] I have added/updated the proper type annotations;
- [ ] I have included the relevant logging calls for debugging;
- [ ] I have written docstrings for objects at a convenient level of detail;
- [ ] I have added the relevant test cases to validate the expected program behaviour.
>>>

>>> [!tip] :reminder_ribbon: Contribution control

- [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][9] or the Related Issues section;
- [ ] I have revised the [`ROADMAP.md`][10] and updated the information on development status;
- [ ] This is my first contribution, I have included my information in the `authors` section of `pyproject.toml` and `CITATION.cff`.
>>>

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#book-our-philosophy
[3]: {{ cookiecutter.__scm_link_url }}/labels
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[4]: {{ cookiecutter.__gitlab_org }}/epics
{%- else %}
[4]: {{ cookiecutter.__scm_link_url }}/milestones
{%- endif %}
[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commit-customs
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#say-why-not-just-what
[7]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#git-trailers
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#styling
[9]: https://docs.gitlab.com/user/project/issues/managing_issues/#closing-issues-automatically
[10]: {{ cookiecutter.__scm_link_url }}/blob/master/ROADMAP.md

## Reviewer Checklist

>>> [!warning] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][11]:

- [ ] The change is as small as possible;
- [ ] Only one specific feature is implemented and does not combine things;
- The change: <!-- Pick only one -->
  - [ ] Does not require updating the documentation;
  - [ ] Added the proper documentation on the component, promoting and preserving [institutional knowledge][12];
- The change: <!-- Pick only one -->
  - [ ] Does not require any addition or modification to unit tests;
  - [ ] Modifies the public API, with proper tests being added;
- [ ] The commit history is logical;
{%- if cookiecutter.commit_convention == 'gitmoji' %}
- [ ] The commit history applies the proper Gitmoji;
{%- else %}
- [ ] The commit history applies the proper conventional types;
{%- endif %}
- [ ] The commit titles apply the imperative mood;
- [ ] The commit descriptions sufficiently explain design choices;
- [ ] Issues marked for automatic closing are accurate;
- [ ] Issues requiring manual check have been addressed;
- [ ] The proposed {{ cookiecutter.project_name }} version adheres to our view on [EffVer][13].
>>>

>>> [!tip] :pen_fountain: Discretionary
I attest that during this development, the following interactions have taken place:

- [ ] We have discussed our opinions on the chosen solution and implementation;
- [ ] We have explored possible alternative solutions;
- [ ] We have worked to simplify the implementation;
- [ ] We have covered all the edge cases we could come up with;
- [ ] We have found [opportunities][14] for future development and have created work items to take action on later.
>>>

[11]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[12]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[13]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#versioning-customs
[14]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
