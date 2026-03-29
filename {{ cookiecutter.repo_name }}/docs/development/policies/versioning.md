# Versioning Customs

At {{ cookiecutter.project_name }},
we chose to adhere
to [{{ cookiecutter.__schema_name }}][1]
for consistency
and improved communication
of our releases.

We find that,
by adopting {{ cookiecutter.__schema_cipher}},
{%- if cookiecutter.__version_schema_base == 'effver' %}
users and developers are better served
with appropriate information to migrate
to new versions.

Our versions communicate _intentions_
instead of technical scope of changes,
making the process of updating
more human-based.
Thus, expect that
**all releases** will impact users,
and our version numbers should provide
the necessary information for them
to assess how grater or lesser work
will be required to update.
{%- elif cookiecutter.__version_schema_base == 'semver' %}
we adhere to an ubiquous standard
for software versioning
that steers development and release
towards best practices
for downstream dependency management.

Additionally,
it can be easily recognised
and followed by new contributors,
making it ideal to be adopted
by the project.
{%- elif cookiecutter.__version_schema_base == 'romver' %}
we can focus on better communicating
major advancements
and features
more adequately.

Instead of focusing solely
on technical scope of changes,
our **PROJECT** versions help users and developers
pick up the importance of their changes.
{%- elif cookiecutter.__version_schema_base == 'solover' %}
we eliminate unnecessary discussions
on software semantics,
instead focusing our efforts to deliver
frequent and incremental releases.
{%- elif cookiecutter.__version_schema_base == 'calver' %}
we help users and downstream developers
be better secured against exploits,
making it easy to identify
usage of software kept stale
for long periods of time.

{%- if cookiecutter.version_schema == 'calver-auto' %}
Our versions dismiss
lengthy discussions
on software semantics
and focus on security safeguards.
Thus,
expect that
**any release** may introduce breaking changes,
{%- else %}
Our versions follow
the **5Y.0M.MICRO** scheme variation
of CalVer.
Thus,
any **MAJOR**
(i.e., yearly)
or **MINOR**
(i.e., monthly)
releases
may introduce breaking changes,
{%- endif %}
requiring potential user action to update
to the latest version.
{%- elif cookiecutter.__version_schema_base == 'trunkver' %}
we can focus solely on
delivering our software
**on time in full**
to our users,
no matter which features
are in mid-development.
{%- endif %}

The following guidelines
should be taken in consideration
regarding versioning in general:

{% if cookiecutter.__schema_group == 'semver-like' -%}
<!-- RECORD the acceptance criteria for releasing a v1.0 for your project -->
- Version `v1.0.0` can only be set
  once all requirements specified
  in the `v1.0 Release` {{ cookiecutter.__roadmap_item }}
  are satisfied;
{% endif -%}
- Versions can only be {% if cookiecutter.version_schema == 'trunkver' %}published{% else %}tagged{% endif %}
  if altering user-facing files;
  changes to project internals only
  do not qualify for {% if cookiecutter.version_schema == 'trunkver' %}publishing{% else %}tagging{% endif %}.

{% if cookiecutter.__schema_type == 'segmented' and cookiecutter.version_schema != 'calver-auto' -%}
## Tips for Defining New Versions

Contributors can refer to
the following list
for common circumstances
under which a version segment
might be selected
for the next version:

{% if cookiecutter.version_schema != 'calver-explicit' -%}
- Update **{{ cookiecutter.__version_s1 }}** versions when:
<!-- RECORD common developments related to {{ cookiecutter.__version_s1.lower() }} versions -->
- Update **{{ cookiecutter.__version_s2 }}** versions when:
<!-- RECORD common developments related to {{ cookiecutter.__version_s2.lower() }} versions -->
{% endif -%}
- Update **{{ cookiecutter.__version_s3 }}** versions when:
<!-- RECORD common developments related to {{ cookiecutter.__version_s3.lower() }} versions -->

!!! note

    This is **not** an exhaustive list,
    nor a rigid set of rules
    defining how to choose next versions.

    Each version update
    should be properly discussed
    through their related {{ cookiecutter.__mr_acronym }}.

{% endif -%}
<!-- Anchors -->
{%- if cookiecutter.__version_schema_base == 'effver' %}

[1]: https://jacobtomlinson.dev/effver/
{%- elif cookiecutter.__version_schema_base == 'semver' %}

[1]: https://semver.org/
{%- elif cookiecutter.__version_schema_base == 'calver' %}

[1]: https://calver.org/
{%- elif cookiecutter.__version_schema_base == 'romver' %}

[1]: https://github.com/romversioning/romver
{%- elif cookiecutter.__version_schema_base == 'solover' %}

[1]: https://beza1e1.tuxen.de/SoloVer
{%- elif cookiecutter.__version_schema_base == 'trunkver' %}

[1]: https://trunkver.org/
{%- endif %}
