# :surfer: User Experience Enrichment

>>> [!NOTE] :bulb: Changes that reduce user friction with {{ cookiecutter.project_name }} usage
This template should be used to propose and discuss progressive revisions to user interaction, aiming to improve their satisfaction and familiarity with the application.

:ok: **Types of changes to be proposed with this template:** navigation, shortcuts and power user features, user help and tutorials, output formatting, public extensions, type annotation improvements, user-facing logging, accessibility features

:no_good: **What this type of proposal does not stand for:**

- Backend developments;
- Incremental functionality implementation;
- Changes to interface architecture layers for rendering purposes;
- Data and input validation;
- Code refactors;
- File parsing.
>>>

## What improvement do you propose with this PR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

> **Proposed Version:** <!-- What is your proposed version following the EffVer scheme? -->

## Why should we consider this change for the project?

<!--
  Defend the reasons why this improvement is important moving forward
  What is the motivation for proposing the improvement in question?
  What benefits does it bring to users:
  What would be considered a successful outcome for this development from your perspective?

  Feel free to bring some of your personal experience as a {{ cookiecutter.project_name }} user to let us understand the circumstances that led to this proposal
-->

## Submitter Checklist

<!--
  Mark complying items as they are delivered with `[x]`
  Single out unnecessary or unworkable items with `[~]`
-->

>>> [!CAUTION] :scroll: Policy compliance

- [ ] I have read the [`CONTRIBUTING`][1] guide for proposing changes;
- [ ] I provided a concise and clear title for this discussion;
- [ ] I have presented my proposal following the [{{ cookiecutter.project_name }} philosophy][2];
- [ ] I have added the proper [labels][3] to start this discussion;
- [ ] I have associated the proposal with the adequate [project][4];
- [ ] I have followed the [commit customs][5] for the project;
- [ ] I have explained the [reasoning][6] behind my design choices through the commit descriptions;
- [ ] I have added the proper [Git trailers][7] to my commits;
- [ ] I have followed the [Styling Guide][8] for code and Markdown files.
>>>

>>> [!IMPORTANT] :technologist: Development control

- [ ] I am confident the implementation is clear and accessible;
- [ ] I have included elements to help the user absorb the new feature in their workflow;
- [ ] I have assured the interaction cost required to access the component is consistent with the relevance of the underlying feature;
- [ ] I have validated that the change does not degrade performance;
- [ ] I have verified the updated code does not generate unnecessary cognitive load to the user;
- [ ] I am confident this change does not pose security risks for the user;
- [ ] I have written docstrings for objects at a convenient level of detail;
- [ ] I have added the relevant test cases to validate the expected program behaviour and output;
- Regarding extensibility: <!-- Pick only one -->
  - [ ] This improvement does not change entry points for extending {{ cookiecutter.project_name }};
  - [ ] This update modifies library extensions; I have guaranteed satisfactory modularity, averting unnecessary code duplication by users.
>>>

>>> [!TIP] :reminder_ribbon: Contribution control

- [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][9] or the Related Issues section;
- [ ] This is my first contribution, I have included my information in the `authors` section of `pyproject.toml` and `CITATION.cff`.
>>>

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#book-our-philosophy
[3]: {{ cookiecutter.__scm_link_url }}/labels
[4]: {{ cookiecutter.__scm_link_url }}/projects
[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commit-customs
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#say-why-not-just-what
[7]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#git-trailers
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#styling
[9]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue

## Reviewer Checklist

>>> [!WARNING] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][10]:

- [ ] The change is as small as possible;
- [ ] Only the configuration enhancement is implemented and the change does not include other types of development;
- [ ] The change reduces complexity for users instead of increasing it;
- The change: <!-- Pick only one -->
  - [ ] Does not require updating the documentation;
  - [ ] Added the proper documentation on the topic, promoting and preserving [institutional knowledge][11];
- The change: <!-- Pick only one -->
  - [ ] Does not require any addition or modification to unit tests;
  - [ ] Modifies Cookiecutter pre-gen and/or post-gen hooks, with proper tests being added;
- [ ] The commit history is logical;
- [ ] The commit history applies the proper Gitmoji;
- [ ] The commit titles apply the imperative mood;
- [ ] The commit descriptions sufficiently explain design choices;
- [ ] Issues marked for automatic closing are accurate;
- [ ] Issues requiring manual check have been addressed;
- [ ] The proposed {{ cookiecutter.project_name }} version adheres to our view on [EffVer][12].
>>>

>>> [!TIP] :pen_fountain: Discretionary
I attest that during the course of this development, the following interactions have taken place:

- [ ] We have discussed our opinions on the chosen solution and implementation;
- [ ] We have explored possible alternative solutions;
- [ ] We have worked to simplify the implementation;
- [ ] We have found [opportunities][13] for future development and have created work items to take action on later.
>>>

[10]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[11]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[12]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#versioning-customs
[13]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
