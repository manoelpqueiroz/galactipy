# :scroll: Project Policy Proposal

>>> [!note] :bulb: To modify documents and rules for {{ cookiecutter.project_name }} development
This template should be used to propose and discuss any changes that affect knowledge management of the project.

:ok: **Types of changes to be proposed with this template:** changes to project documentation and issue/MR templates, changes to project guidelines, changes to CI rules,{% if cookiecutter.scm_platform == 'GitLab Free' %} milestone creation/completion,{% endif %} roadmap updates, changes to linting, styling, testing and issue triaging rules

:no_good: **What this type of proposal does not stand for:**

- Changes that modify tool functionality;
- Typo fixes;
- Updates to CI pipeline jobs scripts/steps;
- Developer tool additions or updates.
>>>

## What do you propose with this MR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

## Why should this policy be adopted?

<!--
  Provide arguments in favour of adopting this proposed policy in lieu of the current rules
  How well does it resonate with our philosophy?
  How is it going to help communication across the project once it is implemented?
  Why is it relevant enough to be formalised?

  Feel free to bring some of your personal experience as a {{ cookiecutter.project_name }} contributor to let us understand the circumstances that led to this proposal
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

>>> [!important] :clipboard: Proposal control

- [ ] The proposal changes policy documents;
  - [ ] I have detailed the proposal in the appropriate file;
  - [ ] I have improved content rendering by leveraging [GitLab Flavored Markdown][9];
  - [ ] I have enriched my proposal with links to point readers to further information where relevant, whether internal or external.
- [ ] The proposal changes internal configuration files:
  - [ ] I have applied the correct syntax to keep the tool functional for developers;
  - Regarding documentation changes: <!-- Pick only one -->
    - [ ] I have evaluated that this configuration change does not require updating a documentation file or comment to substantiate it;
    - [ ] I have updated the documentation highlighting this change and any relevant information.
>>>

>>> [!tip] :reminder_ribbon: Contribution control

- [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][10] or the Related Issues section;
- [ ] I have revised the [`ROADMAP.md`][11] and updated the information on development status;
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
[9]: https://docs.gitlab.com/user/markdown/
[10]: https://docs.gitlab.com/user/project/issues/managing_issues/#closing-issues-automatically
[11]: {{ cookiecutter.__scm_link_url }}/blob/master/ROADMAP.md

## Maintainer Checklist

>>> [!warning] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][12]:

- [ ] The proposal does not change non-policy files;
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

- [ ] We have discussed our opinions on the proposed policy;
- [ ] We have explored possible alternative ideas;
- [ ] We have found [opportunities][13] for future development and have created work items to take action on later.
>>>

[12]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[13]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
