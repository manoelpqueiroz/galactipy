# :card_index: Internal Work Item

>>> [!important]
:bulb: **Manage development iteration with issues and tasks.**

Please read the [`CONTRIBUTING`][1] guide for best practices when opening issues and run through the items under the **`Author Checklist`**.

---

:ok: **Use this template for:** breaking down larger developments into actionable and iterable steps, preserve ideas for future development.

:no_entry: ***DO NOT use this template if you do not have a Developer role in this project.***
>>>

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md

## :thinking: Circumstances and Context

<!-- Insert all necessary information regarding this work item, linking to other resources if applicable -->

## Author Checklist

<!-- Leaving list items unchecked is not an impediment to opening the Internal Work Item -->

- [ ] I am confident this work item is not immediately deliverable via a [Merge Request][2];
- [ ] I have provided a concise and clear title for this issue;
- [ ] I have populated this issue with as much detail as possible, including links to issues, MRs and external sources;
- [ ] I have assigned proper labels for this issue;
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
- [ ] I have set the fitting [status][3] for this issue;
- [ ] I have uploaded the relevant [Designs][4] for further discussing implementation;
- [ ] I have added the **acceptance criteria** for closing this issue as [tasks][5].
{%- else %}
- [ ] I have uploaded the relevant [Designs][3] for further discussing implementation;
- [ ] I have added the **acceptance criteria** for closing this issue as [tasks][4].
{%- endif %}

## Reviewer Checklist

{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
- [ ] I attest that the **acceptance criteria** are well-defined and encompass all expected development for this issue;
- [ ] I have flagged the work item with the appropriate [`To Do` status][6].
{%- else %}
- [ ] I attest that the **acceptance criteria** are well-defined and encompass all expected development for this issue.
{%- endif %}

[2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#start-with-a-merge-request
{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#work-item-tracking
[4]: https://docs.gitlab.com/user/project/issues/design_management/
[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#tasks-are-used-as-acceptance-criteria-for-issues
[6]: https://docs.gitlab.com/user/work_items/status/#status-categories
{%- else -%}
[3]: https://docs.gitlab.com/user/project/issues/design_management/
[4]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#tasks-are-used-as-acceptance-criteria-for-issues
{%- endif %}

/assign me
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
/label ~"seeking-contributors::opinion"
{%- else %}
/label ~"seeking-contributors" ~"seeking-input" ~"sts-needs-refinement"
{%- endif %}
