# :bow: Request for Improvement

>>> [!important]
:bulb: **Suggest an improvement to the {{ cookiecutter.project_name }} feature set.**

Please run through all items under the **`Applicant Checklist`** section and follow the [_why, not just what_][1] directive.

---

:ok: **Use this template for:** requests for new features and updates to existing features, such as:

- Configuration options improvements;
- Upgrades to output formatting, including logs;
- Input validation enhancements;
{%- if cookiecutter.app_type != 'cli' %}
- Shortcuts and navigation;
- Screen layout and widgets;
- Search and filtering functionality;
- Accessibility options;
{%- endif %}
- Customisation;
- Clearer instructions and documentation;
- Integration with other tools, frameworks and platforms;
- Increased modularity for extending the application.

:no_good: **Refrain from using this template if:**

- Your request involves addressing unexpected behaviour :right_arrow: use a **`Request for Correction`**;
- You are unsure your request involves an actual feature :right_arrow: attempt a **`Request for Support`** first;
- You feel your request is not clear enough yet :right_arrow: a **`Request for Support`** is also recommended.
>>>

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#say-why-not-just-what

## Applicant Checklist

<!-- Please check all items with an `x` (like `[x]`) before proceeding -->

- [ ] I am using the latest version of {{ cookiecutter.project_name }};
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
- [ ] I have looked at issues and MRs associated with the current [epics][2] to check if my request is not already anticipated by the development team;
{%- else %}
- [ ] I have looked at issues and MRs associated with the current [milestones][2] to check if my request is not already anticipated by the development team;
{%- endif %}
- [ ] I have explored the [Issue Tracker][3] looking for duplicates, attempting searches with the following terms:
  <!-- List all searches you have performed -->
  - `...`
  - `...`
- [ ] I have read the [`CONTRIBUTING`][4] guide and I have understood how to improve communication between me and the development team;
- [ ] I provided a concise and clear title for this discussion;
- [ ] I have provided the development team the desired feature as most detailed as I possibly can;
- [ ] I have followed the [_why, not just what_][1] directive to open this request;
- [ ] I am confident this discussion does not fall in another category.

{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[2]: {{ cookiecutter.__gitlab_org }}/epics
{%- else %}
[2]: {{ cookiecutter.__scm_link_url }}/milestones
{%- endif %}
[3]: {{ cookiecutter.__scm_link_url }}/issues/?state=all&type%5B%5D=issue
[4]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contributing-through-user-requests

### Commitment to Project Support

After reading the [Commitment to Help][5] section of the `CONTRIBUTING` guide and submitting this request, I commit to one of:

- [ ] Read [open discussions][6] until I find **2** where I can help someone and add a comment to help there;
- [ ] Hit the ["Watch"][7] button in this repository to receive notifications about the project and help **2** people that ask questions in the future;
- [ ] Review **1** Merge Request by cloning the project and following the [review process][8].

[5]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commitment-to-help
[6]: {{ cookiecutter.__scm_link_url }}/issues/?type%5B%5D=issue
[7]: https://gitlab.com/gitlab-org/gitlab-foss/-/issues/234#note_17497758
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contributing-by-reviewing-changes

## :thought_balloon: Request Details

<!-- Please check the single most related item with an `x` (like `[x]`) -->

How would you classify this request?

{%- if cookiecutter.app_type != 'bare_repo' %}
- [ ] :keyboard: Changes to CLI behaviour;
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
- [ ] :iphone: Changes in the user interface and user experience;
{%- endif %}
- [ ] :peacock: Customisation options;
{%- else %}
- [ ] :sparkles: New features;
{%- endif %}
- [ ] :information_source: Improvements to documentation and help menus;
- [ ] :electric_plug: Proposal for package extension;
- [ ] :link: Compatibility/integration with another tool/platform;
- [ ] Something entirely different.

### What improvement do you propose?

<!-- Describe WHAT your request refers to, with as much detail as possible -->

### Why should we consider this improvement for the project?

<!--
  Defend the reasons why this improvement is important moving forward
  What problem does it solve?
  What benefits does it bring and to whom?
  What would be considered a successful outcome for this development from your perspective?

  Feel free to bring some of your personal experience as a {{ cookiecutter.project_name }} user to let us understand the circumstances that led to this request
-->

### Additional context

<!--
  Add any other information here
  Screenshots, links and any content that helps us better visualise your desired outcome are welcome!
-->

{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
/label ~"request::improvement"
{%- else %}
/label ~"rfi" ~"sts-needs-triage"
{%- endif %}
