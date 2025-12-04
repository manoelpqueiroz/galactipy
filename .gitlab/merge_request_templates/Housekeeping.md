# :house_abandoned: Housekeeping

>>> [!note] :bulb: Proposals for keeping project units tidy
This template should be used to propose and discuss changes that improve project maintainability over time, generally with incremental changes.

:ok: **Types of changes to be proposed with this template:** updates to generated projects documentation, typo fixes, dependency updates to project and template, tool syntax updates, code refactoring

:no_good: **What this type of proposal does not stand for:**

- Changes that modify tool behaviour;
- Changes to documentation outside `{{ cookiecutter.repo_name }}`.
>>>

## What change do you propose with this MR?

<!-- Describe WHAT your proposal refers to -->

## Submitter Checklist

<!--
  Mark complying items as they are delivered with `[x]`
  Single out unnecessary or unworkable items with `[~]`
-->

>>> [!caution] :scroll: Policy compliance

- [ ] I have read the [`CONTRIBUTING`][1] guide for proposing changes;
- [ ] I provided a concise and clear title for this discussion;
- [ ] I have presented my proposal following [Galactipy's philosophy][2] principles;
- [ ] I have added the proper [labels][3] to start this discussion;
- [ ] I have associated the proposal with the adequate [epic][4];
- [ ] I have followed the [commit customs][5] for the project;
- [ ] I have explained the [reasoning][6] behind my design choices through the commit descriptions;
- [ ] I have added the proper [Git trailers][7] to my commits;
- [ ] I have followed the [Styling Guide][8] for code and Markdown files.
>>>

>>> [!important] :technologist: Development control

- Regarding file changes: <!-- Pick only one -->
  - [ ] I have changed configuration files, without causing incompatibility;
  - [ ] I have changed documentation files only;
- Regarding versioning: <!-- Pick only one -->
  - [ ] I have bumped the Galactipy [version][9] appropriately as my final commit for this change;
  - [ ] I have kept the Galactipy version the same, as it does not change end-user files.
>>>

>>> [!tip] :reminder_ribbon: Contribution control

- [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][10] or the Related Issues section;
- [ ] This is my first contribution, I have included my information in the `authors` section of `pyproject.toml` and `CITATION.cff`.
>>>

[1]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[2]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#book-our-philosophy
[3]: https://gitlab.com/galactipy/galactipy/-/labels
[4]: https://gitlab.com/groups/galactipy/-/epics
[5]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#commit-customs
[6]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#say-why-not-just-what
[7]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#git-trailers
[8]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#styling
[9]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#versioning-customs
[10]: https://docs.gitlab.com/user/project/issues/managing_issues/#closing-issues-automatically

## Reviewer Checklist

>>> [!warning] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][11]:

- [ ] The change is as small as possible;
- [ ] Only one specific change and does not combine things;
- The change: <!-- Pick only one -->
  - [ ] Does not require any addition or modification to unit tests;
  - [ ] Modifies Cookiecutter pre-gen and/or post-gen hooks, with proper tests being added;
- [ ] The commit history is logical;
- [ ] The commit history applies the proper Gitmoji;
- [ ] The commit titles apply the imperative mood;
- [ ] The commit descriptions sufficiently explain design choices;
- [ ] Issues marked for automatic closing are accurate;
- [ ] Issues requiring manual check have been addressed;
- [ ] The proposed Galactipy version adheres to our view on [RomVer][9].
>>>

>>> [!tip] :pen_fountain: Discretionary
I attest that during the course of this development, the following interactions have taken place:

- [ ] We have found [opportunities][12] for future development and have created work items to take action on later.
>>>

[11]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[12]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
