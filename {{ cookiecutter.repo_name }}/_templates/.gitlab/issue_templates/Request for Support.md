# :wave: Request for Support

>>> [!important]
:bulb: **Seek help from the development team for {{ cookiecutter.project_name }} usage.**

Please run through all items under the **`Applicant Checklist`** section and provide details on the reasons that brought you to open this discussion.

---

:ok: **Use this template for:** general questions on how to use {{ cookiecutter.project_name }}, when you are experiencing issues but are unsure why, questions for the developers regarding design decisions.

:no_good: **Refrain from using this template if:**

- You have a clear request for a new feature or an update to an existing feature :right_arrow: use the **`Request for Improvement`** template instead;
- Your templates are experiencing an unexpected behaviour which you have identified :right_arrow: a **`Request for Correction`** is more suitable.
>>>

## Applicant Checklist

<!-- Please check all that apply with an `x` (like `[x]`); checking is not mandatory -->

- [ ] I am using the latest version of {{ cookiecutter.project_name }};
- [ ] I have explored the [Issue Tracker][1] for similar cases, attempting searches with the following terms:
  <!-- List all searches you have performed -->
  - `...`
  - `...`
{%- if cookiecutter.create_docs %}
- [ ] I have looked at {{ cookiecutter.project_name }}'s [documentation][2] for information on my topic of interest;
{%- else %}
- [ ] I have looked at {{ cookiecutter.project_name }}'s [`README`][2] for information on my topic of interest;
{%- endif %}
- [ ] I have read the [Contributing Guide][3] and I have understood how to improve communication between me and the development team;
- [ ] I provided a concise and clear title for this discussion;
- [ ] I am confident this discussion does not fall in another category.

[1]: {{ cookiecutter.__scm_repo_latch }}/issues/?state=all&type%5B%5D=issue
{%- if cookiecutter.create_docs %}
[2]: {{ cookiecutter.__pages_url }}/user_guide
[3]: {{ cookiecutter.__pages_url }}/development/for_others/user_requests
{%- else %}
[2]: {{ cookiecutter.__scm_repo_latch }}/blob/master/README.md
[3]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#contributing-through-user-requests
{%- endif %}

### Commitment to Project Support

After reading the [Commitment to Help][4] section of the Contributing Guide and submitting this request, I commit to one of:

- [ ] Read [open discussions][5] until I find **2** where I can help someone and add a comment to help there;
- [ ] Hit the ["Watch"][6] button in this repository to receive notifications about the project and help **2** people that ask questions in the future;
- [ ] Review **1** Merge Request by cloning the project and following the [review process][7].

{% if cookiecutter.create_docs -%}
[4]: {{ cookiecutter.__pages_url }}/development/for_others/help_others
{% else -%}
[4]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#commitment-to-help
{% endif -%}
[5]: {{ cookiecutter.__scm_repo_latch }}/issues/?type%5B%5D=issue
[6]: https://gitlab.com/gitlab-org/gitlab-foss/-/issues/234#note_17497758
{%- if cookiecutter.create_docs %}
[7]: {{ cookiecutter.__pages_url }}/development/for_others/review_changes
{%- else %}
[7]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#contributing-by-reviewing-changes
{%- endif %}

## :speech_balloon: Context

<!-- Add the details for your request here -->

{% if cookiecutter.__scm_platform_group == 'glab-paid' -%}
/label ~"request::support"
{%- else -%}
/label ~"rfs" ~"sts-needs-triage"
{%- endif %}
