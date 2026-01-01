# :school_satchel: Zero-Config Enhancement

>>> [!note] :bulb: Improves initial file configuration and reduces user friction
This template should be used to propose and discuss changes to the default configuration provided by Galactipy for users.

:ok: **Types of changes to be proposed with this template:** file disposition, pre-configuration of values in existing tools, Invoke tasks for automating project setup, tool maintenance which directly reduces setup time for users

:no_good: **What this type of proposal does not stand for:**

- Updates to existing tools which do not affect user experience at the project startup;
- Proposals for new tools and services;
- Modifications to configuration outside `{{ cookiecutter.repo_name }}`.
>>>

## What configuration enhancement are you proposing with this MR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

## Why this change should be considered for release?

<!--
  Defend the reasons why this change is important moving forward
  Why should the configuration change?
  Does it remove the need to act on a TODO comment specified in the generated template?
  Does it make features clearer and more accessible for usage?
  What benefits does it bring to users?
  What would be considered a successful outcome for this development from your perspective?

  Feel free to bring some of your personal experience as a Galactipy user to let us understand the circumstances that led to this proposal
-->

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

- [ ] I have modified files to sufficiently improve user experience without causing incompatibility in project generation;
- [ ] I have assured the configuration improvement works as expected;
- Regarding documentation and knowledge management: <!-- Pick only one -->
  - [ ] I have evaluated that this change does not require updating the documentation;
  - [ ] I have updated the documentation highlighting this change and any relevant information.
- Regarding user nugding:
  - [ ] I have evaluated that this change does not require specifying or changing `TODO`/`UPDATEME` comments;
  - [ ] I have included or removed the relevant `TODO` and `UPDATEME` comments to orient users on next steps after generating projects with Galactipy;
- [ ] I have bumped the Galactipy [version][9] appropriately as my final commit for this change.
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
- [ ] Only the configuration enhancement is implemented and the change does not include other types of development;
- [ ] The change reduces complexity for users instead of increasing it;
- The change: <!-- Pick only one -->
  - [ ] Does not require updating the documentation;
  - [ ] Added the proper documentation on the topic, promoting and preserving [institutional knowledge][12];
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

- [ ] We have discussed our opinions on the chosen solution and implementation;
- [ ] We have explored possible alternative solutions;
- [ ] We have worked to simplify the implementation;
- [ ] We have found [opportunities][13] for future development and have created work items to take action on later.
>>>

[11]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[12]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[13]: https://gitlab.com/galactipy/templates/-/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress

/label ~"enhancement::zero-config"
