# :crayon: Structural Design Deliberation

>>> [!note] :bulb: To define development decisions on current and future behaviour of the software
This template should be used to discuss and validate high-level design decisions. These decisions shall be persisted in repository files for latter implementation.

:ok: **Types of changes to be proposed with this template:** application behaviour specification,{% if cookiecutter.use_bdd %} BDD scenarios,{% endif %} previously undetected test cases, feature flags

:no_good: **What this type of proposal does not stand for:**

- Feature implementation;
- Public API changes;
- Documentation updates;
- Changes related to developer tools.
>>>

## What is the context behind this discussion?

<!--
  Describe WHAT your proposal refers to, with as much detail as possible
  Why should this be discussed in more detail with other members?
  What is your vision regarding this design? Defend the reasons why it should be validated and implemented
  Which benefits are you trying to reap by later implementing this design?
  Which risks is your design proposal trying to mitigate?
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
  - [ ] I am confident this should be discussed in a larger forum [before being addressed][3]
- [ ] I have added the proper [labels][4] to start this discussion;
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
- [ ] I have associated the proposal with the adequate [epic][5];
{%- else %}
- [ ] I have associated the proposal with the adequate [development milestone][5];
{%- endif %}
- [ ] I have followed the [commit customs][6] for the project;
- [ ] I have explained the [reasoning][7] behind my design choices through the commit descriptions;
- [ ] I have added the proper [Git trailers][8] to my commits;
- [ ] I have followed the [Styling Guide][9] for code and Markdown files.
>>>

>>> [!important] :petri_dish: Design control

- [ ] I am confident I have sufficiently described the design choices being validated;
- [ ] I have covered all the possible edge cases I could identify;
- [ ] I have indicated all relevant [test marks][10] for this design.
>>>

>>> [!tip] :reminder_ribbon: Contribution control

- [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][11] or the Related Issues section;
- [ ] This is my first contribution, I have included my information in the `authors` section of `pyproject.toml` and `CITATION.cff`.
>>>

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#book-our-philosophy
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#operate-with-a-bias-for-action
[4]: {{ cookiecutter.__scm_link_url }}/labels
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[5]: {{ cookiecutter.__gitlab_org }}/epics
{%- else %}
[5]: {{ cookiecutter.__scm_link_url }}/milestones
{%- endif %}
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commit-customs
[7]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#say-why-not-just-what
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#git-trailers
[9]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#styling
{%- if cookiecutter.use_bdd %}
[10]: https://pytest-bdd.readthedocs.io/en/latest/#organizing-your-scenarios
{%- else %}
[10]: https://docs.pytest.org/en/stable/reference/reference.html#custom-marks
{%- endif %}
[11]: https://docs.gitlab.com/user/project/issues/managing_issues/#closing-issues-automatically

## Maintainer Checklist

>>> [!warning] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][12]:

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

- [ ] We have discussed our opinions on the proposed design;
- [ ] We have explored possible alternative ideas;
- [ ] We have found [opportunities][13] for future development and have created work items to take action on later.
>>>

[12]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[13]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
