# :tools: Request for Correction

>>> [!important]
:bulb: **Expose errors with {{ cookiecutter.project_name }} for the development team to address.**

Please run through all items under the **`Applicant Checklist`** section and be as much detailed as you can to speed up diagnostic and solution.

---

:ok: **Use this template for:**

- Bugs and crashes;
{%- if cookiecutter.app_type == 'cli' %}
- Application freezes/hangs;
{%- else %}
- Application freezes/lagging;
- Faulty widgets and screen elements;
- Unresponsive shortcuts;
{%- endif %}
- Silent failures;
- Command interpretation flaws;
- Inexistent commands;
- Malformed outputs;
- Reading/writing issues;
- Permission issues;
- Deconfiguration.

:no_good: **Refrain from using this template if:**

- You do not feel capable of providing details and some initial direction for the development team :right_arrow: open a **`Request for Support`** first.
>>>

## Applicant Checklist

<!-- Please check all items with an `x` (like `[x]`) before proceeding -->

- [ ] I am using the latest version of {{ cookiecutter.project_name }};
- [ ] I am using a valid configuration file for {{ cookiecutter.project_name }};
- [ ] I have looked at the [open Merge Requests][1] to check if my case has not been already identified by the development team;
- [ ] I have explored the [Issue Tracker][2] looking for duplicates, attempting searches with the following terms:
  <!-- List all searches you have performed -->
  - `...`
  - `...`
- [ ] I have read the [`CONTRIBUTING`][3] guide and I have understood how to improve communication between me and the development team;
- [ ] I am assured this should not be a confidential issue due to [security implications][4];
- [ ] I provided a concise and clear title for this discussion;
- [ ] I have provided the development team the context surrounding this issue as most detailed as I possibly can;
- [ ] I am confident this discussion does not fall in another category.

[1]: {{ cookiecutter.__scm_link_url }}/merge_requests
[2]: {{ cookiecutter.__scm_link_url }}/issues/?state=all&type%5B%5D=issue
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#contributing-through-user-requests
[4]: {{ cookiecutter.__scm_link_url }}/blob/master/SECURITY.md

## :thought_balloon: Context

<!--
  Provide a clear and concise description of the issue you are facing
  Also provide everything you have attempted so far to address the issue
-->

### How to Reproduce

<!--
  If applicable, list a step-by-step attempt at replicating the situation
-->

### Configuration

<!--
  Provide your configuration file contents, located at:

  ~/.config/{{ cookiecutter.repo_name }}/settings.toml (Linux/MacOS)
  C:\Users\user\AppData\Local\{{ cookiecutter.repo_name }}\settings.toml (Windows)
-->

### Log Output

<!--
  Provide the log file output generated after reproducing the situation, located at:

  ~/.local/state/log/{{ cookiecutter.repo_name }}/report.log (Linux/MacOS)
  C:\Users\user\AppData\Local\{{ cookiecutter.repo_name }}\Logs\report.log (Windows)
-->

{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
/label ~"request::correction"
{%- else %}
/label ~"rfc" ~"sts-needs-triage"
{%- endif %}
