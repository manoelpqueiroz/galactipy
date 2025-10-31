# :pinata: Feature Proposal

>>> [!note] :bulb: To reshape user-facing parts of the {{ cookiecutter.project_name }} API
This template should be used to propose and discuss incremental or novel working application units offered to users.

:ok: **Types of changes to be proposed with this template:** user interface elements/capabilities, customization options,{% if cookiecutter.app_type != 'bare_repo' %} command structure and flags,{% endif %} accessibility options, entry points and logic for extensions, hooks and events

:no_good: **What this type of proposal does not stand for:**

- Backend developments with no direct significance to the user;
- Changes to the current user experience without additive functionality;
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
- Changes to interface architecture layers for rendering purposes;
{%- endif %}
- Data and input validation;
- File parsing;
- Feature flag implementation.
>>>

## What new feature do you propose with this MR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

> **Proposed Version:** <!-- What is your proposed version following the EffVer scheme? -->

## Why should we consider this new feature for the project?

<!--
  Defend the reasons why this improvement is important moving forward
  What problem does it solve?
  What benefits does it bring to users?
  What would be considered a successful outcome for this development from your perspective?
  How much developer support for this feature should be expected?

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

- [ ] I have verified the feature does not conflict with other existing features;
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
Regarding technical delivery:
  - [ ] I have verified the feature does not break UI elements;
  - [ ] I have verified the added/updated UI elements do not clash with pre-existing ones;
{%- endif %}
- Regarding user experience:
  - [ ] I have included elements to help the user absorb the new feature in their workflow;
  - [ ] I am confident this change does not pose security risks for the user;
- Regarding code structure:
  - [ ] I have followed best design practices to organise the source code;
  - [ ] I have added/updated the proper type annotations;
- [ ] I have updated the documentation detailing the feature, along with any additional references that might be useful for users;
- [ ] I have included the relevant logging calls for debugging;
- [ ] I have written docstrings for objects at a convenient level of detail;
- [ ] I have added the relevant test cases to validate the expected program behaviour.
>>>

>>> [!tip] :reminder_ribbon: Contribution control

- [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][9] or the Related Issues section;
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

## Reviewer Checklist

>>> [!warning] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][10]:

- [ ] The change is as small as possible;
- [ ] Only one specific feature is implemented and does not combine things;
- [ ] Proper documentation was added, promoting and preserving [institutional knowledge][11];
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
- [ ] The proposed {{ cookiecutter.project_name }} version adheres to our view on [EffVer][12].
>>>

>>> [!tip] :pen_fountain: Discretionary
I attest that during the course of this development, the following interactions have taken place:

- [ ] We have discussed our opinions on the chosen solution and implementation;
- [ ] We have explored possible alternative solutions;
- [ ] We have worked to simplify the implementation;
- [ ] We have covered all the edge cases we could come up with;
- [ ] We have found [opportunities][13] for future development and have created work items to take action on later.
>>>

[10]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[11]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[12]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#versioning-customs
[13]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
