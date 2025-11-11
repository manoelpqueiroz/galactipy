# :bullettrain_side: Internal Improvement

>>> [!note] :bulb: Improves {{ cookiecutter.project_name }} developer experience
This template should be used to propose and discuss changes to tools used to manage {{ cookiecutter.project_name }} development.

:ok: **Types of changes to be proposed with this template:** new tools to be used during development, updates to existing tools, replacement of current tools with alternatives, Invoke tasks, updates to CI pipelines, monitoring initiatives, alert automations, error tracking, environment setup, build optimisations, scripts/containers

:no_good: **What this type of proposal does not stand for:**

- Changes not related directly to developer productivity;
- Changes to tool rules in `pyproject.toml`;
- Updates to documentation files for the project;
- Project dependency updates;
- Modifications to CI job rules only;
- Mere updates to current tools syntax.
>>>

## What improvement do you propose with this MR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

## Why should we consider this change for the project?

<!--
  Defend the reasons why this improvement is important moving forward
  What is the motivation for proposing the improvement in question?
  What benefits does it bring to developers?
  What would be considered a successful outcome for this development from your perspective?

  Feel free to bring some of your personal experience as a {{ cookiecutter.project_name }} developer to let us understand the circumstances that led to this proposal
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

- [ ] I have assembled the minimal configuration to implement the proposed change without breaking functionality;
- [ ] I have provided a way for other developers to understand when and how to use the tool being added/changed/replaced;
- Regarding documentation and knowledge management: <!-- Pick only one -->
  - [ ] I have evaluated that this change does not require updating the documentation;
  - [ ] I have updated the documentation highlighting this change and any relevant information.
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
  - [ ] Added the proper documentation on the topic, promoting and preserving [institutional knowledge][12];
- [ ] The commit history is logical;
{%- if cookiecutter.commit_convention == 'gitmoji' %}
- [ ] The commit history applies the proper Gitmoji;
{%- else %}
- [ ] The commit history applies the proper conventional types;
{%- endif %}
- [ ] The commit titles apply the imperative mood;
- [ ] The commit descriptions sufficiently explain design choices;
- [ ] Issues marked for automatic closing are accurate;
- [ ] Issues requiring manual check have been addressed.
>>>

>>> [!tip] :pen_fountain: Discretionary
I attest that during this development, the following interactions have taken place:

- [ ] We have discussed our opinions on the chosen solution and implementation;
- [ ] We have explored possible alternative solutions;
- [ ] We have worked to simplify the implementation;
- [ ] We have covered all the edge cases we could come up with;
- [ ] We have found [opportunities][13] for future development and have created work items to take action on later.
>>>

[11]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[12]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[13]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
