# :race_car: Tool Update/Maintenance

>>> [!note] :bulb: To keep existing tools for Galactipy-generated projects functional
This template should be used to propose and discuss the maintenance of existing tools and integrations provided by Galactipy to reflect their latest state and ensure security, functionality and futureproofing.

:ok: **Types of changes to be proposed with this template:** updates to existing tools (either adding incremental behaviour or updating current syntax), replacement of current tools with alternatives, updates to CI and template files

:no_good: **What this type of proposal does not stand for:**

- Proposals for new tools and services;
- Changes modifying only documentation files for the template;
- Template dependency updates;
- Modifications to tools and files outside `{{ cookiecutter.repo_name }}`.
>>>

## What change do you propose with this MR?

<!-- Describe WHAT your proposal refers to, with as much detail as possible -->

## Why should we consider this new feature for the project?

<!--
  Defend the reasons why this improvement is important moving forward
  What is the motivation for updating the existing tool in question?
  What benefits does it bring and to whom?
  What would be considered a successful outcome for this development from your perspective?

  Feel free to bring some of your personal experience as a Galactipy user to let us understand the circumstances that led to this proposal
-->

## Submitter Checklist

<!-- Mark complying items as they are delivered -->

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

- [ ] I have assembled the minimal configuration to implement the proposed change without breaking functionality;
- [ ] I have either:
  - Evaluated that this change does not require updating links to tool/service configuration;
  - Updated links to repository and configuration reference of the tool/service as inline comments where appropriate;
- [ ] I have either:
  - Evaluated that this change does not require updating the documentation;
  - Updated the documentation highlighting this change and any relevant information;
- [ ] I have either:
  - Evaluated that this change does not require specifying or changing `TODO`/`UPDATEME` comments;
  - Included or removed the relevant `TODO` and `UPDATEME` comments to orient users on next steps after generating projects with Galactipy;
- [ ] I have bumped the Galactipy [version][9] appropriately as my final commit for this change.
>>>

>>> [!tip] :reminder_ribbon: Contribution control

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

## Reviewer Checklist

>>> [!warning] :passport_control: MANDATORY
I attest that the proposed change meets the [Contribution Acceptance Criteria][10]:

- [ ] The change is as small as possible;
- [ ] Only one specific feature is implemented and does not combine things;
- [ ] The change either:
  - Does not require updating the documentation;
  - Proper documentation was added, promoting and preserving [institutional knowledge][11];
- [ ] The change either:
  - Does not require any addition or modification to unit tests;
  - Modifies Cookiecutter pre-gen and/or post-gen hooks, with proper tests being added;
- [ ] The commit history is logical;
- [ ] The commit history applies the proper Gitmoji;
- [ ] The commit title applies imperative mood;
- [ ] The commit descriptions sufficiently explains design choices;
- [ ] The proposed Galactipy version adheres to our view on [EffVer][9].
>>>

>>> [!tip] :pen_fountain: Discretionary
I attest that during the course of this development, the following interactions have taken place:

- [ ] We have discussed our opinions on the chosen solution and implementation;
- [ ] We have explored possible alternative solutions;
- [ ] We have worked to simplify the implementation;
- [ ] We have covered all the edge cases we could come up with;
- [ ] We have found [opportunities][12] for future development and have created work items to take action on later.
>>>

[10]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[11]: https://www.teachfloor.com/elearning-glossary/institutional-knowledge
[12]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress

## Related Issues
<!-- DO NOT ADD CONTENT BELOW THIS LINE -->
