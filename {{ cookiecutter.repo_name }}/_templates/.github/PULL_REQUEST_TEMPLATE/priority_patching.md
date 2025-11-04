# :fire_extinguisher: Priority Patching Request

> [!NOTE]
> :bulb: **Emergency developments that must be prioritised**
>
> This template should be used to propose changes resolving a major issue with the project.
>
> :exclamation: **Use this template on any of the following conditions (this is a non-exhausting list):**
>
> - Security issues;
> - Reverting/addressing changes that crash the application;
> - Reverting/addressing changes that make the application unusable;
> - Pipeline failures.

## What piece of the project requires attention?

<!-- Describe WHAT the request raises attention about, with as much detail as possible -->

> **Proposed Version:** <!-- What is your proposed version following the EffVer scheme? -->

## Why is this issue critical?

<!--
  How seriously does this affect {{ cookiecutter.project_name }} users?
  What security risks does this pose?
-->

## Submitter Checklist

<!--
  Mark complying items as they are delivered with `[x]`
  Single out unnecessary or unworkable items with `[~]`
-->

> [!CAUTION]
> :scroll: **Policy compliance**
>
> - [ ] I have read the [`CONTRIBUTING`][1] guide for proposing changes;
> - [ ] I have read the [`SECURITY`][2] guide to correctly address issue confidentiality;
> - [ ] I provided a concise and clear title for this discussion;
> - [ ] I have presented my case following the [{{ cookiecutter.project_name }} philosophy][3];
> - [ ] I have added the proper [labels][4] to start this discussion.

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/SECURITY.md
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#book-our-philosophy
[4]: {{ cookiecutter.__scm_link_url }}/labels

## Assignee Checklist

> [!CAUTION]
> :scroll: **Policy compliance**
>
> - [ ] I have followed the [commit customs][5] for the project;
> - [ ] I have explained the [reasoning][6] behind my design choices through the commit descriptions;
> - [ ] I have added the proper [Git trailers][7] to my commits;
> - [ ] I have followed the [Styling Guide][8] for code and Markdown files.

> [!IMPORTANT]
> :technologist: **Development control**
>
> - [ ] I have assembled the minimal configuration to resolve the root cause of the issue;
> - [ ] I have tested my implementation to confirm the issue is resolved.

> [!TIP]
> :reminder_ribbon: **Contribution control**
>
> - [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][9] or the Related Issues section.

[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commit-customs
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#say-why-not-just-what
[7]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#git-trailers
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#styling
[9]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue

## Reviewer Checklist

> [!WARNING]
> :passport_control: **MANDATORY**
>
> I attest that the proposed change meets the [Contribution Acceptance Criteria][10]:
>
> - [ ] The change is as small as possible;
> - [ ] The root cause of the issue is addressed without workarounds;
> - The change: <!-- Pick only one -->
>   - [ ] Does not require any addition or modification to unit tests;
>   - [ ] Modifies internal code logic, with proper tests being added or updated;
> - [ ] The commit history is logical;
{%- if cookiecutter.commit_convention == 'gitmoji' %}
> - [ ] The commit history applies the proper Gitmoji;
{%- else %}
> - [ ] The commit history applies the proper conventional types;
{%- endif %}
> - [ ] The commit titles apply the imperative mood;
> - [ ] The commit descriptions sufficiently explain design choices;
> - [ ] Issues marked for automatic closing are accurate;
> - [ ] Issues requiring manual check have been addressed;
> - [ ] The proposed {{ cookiecutter.project_name }} version adheres to our view on [EffVer][11].

> [!TIP]
> :fountain_pen: **Discretionary**
>
> I attest that during the course of this development, the following interactions have taken place:
>
> - [ ] We have discussed our opinions on the chosen solution and implementation;
> - [ ] We have explored possible alternative solutions;
> - [ ] We have worked to simplify the implementation;
> - [ ] We have covered all the edge cases we could come up with;
> - [ ] We have found [opportunities][12] for future development and have created work items to take action on later.

[10]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[11]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#versioning-customs
[12]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
