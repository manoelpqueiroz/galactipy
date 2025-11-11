# :earth_americas: Localisation Initiative

> [!NOTE]
> This template should be used to validate localisation advancements.

## Summary

<!-- Provide a summary of the changes being made with this PR -->

> **Proposed Version:** `MICRO` <!-- Provide next expected micro version -->

## Submitter Checklist

<!--
  Mark complying items as they are delivered with `[x]`
  Single out unnecessary or unworkable items with `[~]`
-->

> [!CAUTION]
> :scroll: **Policy compliance**
>
> - [ ] I have read the [`CONTRIBUTING`][1] guide for proposing changes;
> - [ ] I provided a concise and clear title for this discussion;
> - [ ] I have presented my proposal following the [{{ cookiecutter.project_name }} philosophy][2];
> - [ ] I have added the proper [labels][3] to start this discussion;
> - [ ] I have associated the proposal with the adequate [project][4];
> - [ ] I have followed the [commit customs][5] for the project;
> - [ ] I have explained the [reasoning][6] behind my design choices through the commit descriptions;
> - [ ] I have added the proper [Git trailers][7] to my commits;
> - [ ] I have followed the [Styling Guide][8] for code and Markdown files.

> [!IMPORTANT]
> :technologist: **Development control**
>
> - Regarding the user interface:
{%- if cookiecutter.app_type != 'cli' %}
>   - [ ] Localised text fits and is readable, do not overlap with other elements;
{%- endif %}
>   - [ ] Symbol encoding and accented characters render correctly;
>   - [ ] Date formats and units correctly follow the locale;
>   - [ ] Numbers and currency have the correct separators and symbols;
> - [ ] I have attested the change does not erase persisted user data;
> - [ ] I have followed best design practices to organise the changes.

> [!TIP]
> :reminder_ribbon: **Contribution control**
>
> - [ ] I have marked issues to be resolved with this proposal either in [commit descriptions][9] or the Related Issues section;
> - [ ] I have revised the [`ROADMAP.md`][10] and updated the information on development status;
> - [ ] This is my first contribution, I have included my information in the `authors` section of `pyproject.toml` and `CITATION.cff`.

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#speaking_head-proposing-changes-as-a-developer
[2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#book-our-philosophy
[3]: {{ cookiecutter.__scm_link_url }}/labels
[4]: {{ cookiecutter.__scm_link_url }}/projects
[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commit-customs
[6]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#say-why-not-just-what
[7]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#git-trailers
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#styling
[9]: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
[10]: {{ cookiecutter.__scm_link_url }}/blob/master/ROADMAP.md

## Reviewer Checklist

> [!WARNING]
> :passport_control: **MANDATORY**
>
> I attest that the proposed change meets the [Contribution Acceptance Criteria][11]:
>
> - [ ] The change is as small as possible;
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
> - [ ] The proposed {{ cookiecutter.project_name }} version adheres to our view on [EffVer][12].

> [!TIP]
> :fountain_pen: **Discretionary**
>
> I attest that during this development, the following interactions have taken place:
>
> - [ ] We have covered all the edge cases we could come up with;
> - [ ] We have found [opportunities][13] for future development and have created work items to take action on later.

[11]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contribution-acceptance-criteria
[12]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#versioning-customs
[13]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#sharing-insights-drives-progress
