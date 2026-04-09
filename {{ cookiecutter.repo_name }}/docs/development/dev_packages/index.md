# Development Packages Reference
{%- if cookiecutter.app_type != 'bare_repo' %}

The following packages are used
for development of front-end features
and interface elements,
and thus are not documented
in the same section
as the public API:

- **`{{ cookiecutter.package_name }}.cli`**;
- **`{{ cookiecutter.package_name }}.tui`**.

The objects in these packages
are referenced in detail
in this section
to better onboard developers
on the inner workings
of {{ cookiecutter.project_name }}.

Additionally,
this section also collects
the custom code created
to run the test suite
and non-public objects
which are part
of the [public packages][1].
{%- else %}

The following packages are used
for feature development,
and thus are not documented
in the same section
as the public API:

<!-- RECORD the packages that are not part of the public API -->

The objects in these packages
are referenced in detail
in this section
to better onboard developers
on the inner workings
of {{ cookiecutter.project_name }}.

Additionally,
this section also collects
the custom code created
to run the test suite
and non-public objects
which are part
of the [public packages][1].
{%- endif %}

<!-- Anchors -->

[1]: ../../reference/index.md
