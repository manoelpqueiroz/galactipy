# :rocket: Tool Expansion Proposal

>>> [!note] :bulb: To provide additional tools for Galactipy-generated projects
This template should be used to propose and discuss the inclusion of new tools and integrated solutions to the pool of features provided by Galactipy templates to user projects.

:ok: **Types of changes to be proposed with this template:** cutting-edge tools, service integrations, non-existing features, either as a complete or an incremental development

:no_good: **What this type of proposal does not stand for:**

- Updates to existing tools;
- Proposals to replace existing tools with alternatives;
- Tools for development of Galactipy itself.
>>>

## What new feature do you propose with this MR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

## Why should we consider this new feature for the project?

<!--
  Defend the reasons why this improvement is important moving forward
  What problem does it solve?
  What benefits does it bring and to whom?
  Is the tool/service in question widely known, used and accepted?
  What would be considered a successful outcome for this development from your perspective?
  How much developer support for this feature should be expected?

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
- [ ] I have associated the proposal with the adequate [development milestone][4];
- [ ] I have followed the [commit customs][5] for the project;
- [ ] I have explained the [reasoning][6] behind my design choices through the commit descriptions;
- [ ] I have added the proper [Git trailers][7] to my commits;
- [ ] I have followed the [Styling Guide][8] for code and Markdown files.
>>>

>>> [!important] :technologist: Development control

- [ ] I have assembled the minimal configuration to make the proposed tool/service functional for users;
- [ ] I have provided links to repository and configuration reference of the proposed tool/service as inline comments;
- [ ] I have updated the documentation promoting the tool/service as a feature, along with any additional references that might be useful for users;
- [ ] I have included the relevant `TODO` and `UPDATEME` comments to orient users on next steps after generating projects with Galactipy;
- [ ] I have bumped the Galactipy [version][9] appropriately as my final commit for this change.
>>>

>>> [!tip] :reminder_ribbon: Contribution control

- [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][10] or the Related Issues section;
- [ ] This is my first contribution, I have included my information in the `authors` section of `pyproject.toml` and `CITATION.cff`.
>>>

[1]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[2]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#book-our-philosophy
[3]: https://gitlab.com/galactipy/galactipy/-/labels
[4]: https://gitlab.com/galactipy/galactipy/-/milestones
[5]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#commit-customs
[6]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#say-why-not-just-what
[7]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#git-trailers
[8]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#styling
[9]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#versioning-customs
[10]: https://docs.gitlab.com/user/project/issues/managing_issues/#closing-issues-automatically

## Reviewer Checklist

>>> [!warning] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][11]:

- [ ] The change is as small as possible;
- [ ] Only one specific feature is implemented and does not combine things;
- [ ] Proper documentation was added, promoting and preserving [institutional knowledge][12];
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
- [ ] We have covered all the edge cases we could come up with;
- [ ] We have found [opportunities][13] for future development and have created work items to take action on later.
>>>

[11]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[12]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[13]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress

/label ~"enhancement::tool-expansion"
