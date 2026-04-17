{% raw -%}
---
tags:
  - Section Intros
  - Living Docs
  - For Your Information
---

{% endraw -%}
# Security Advisories

We keep a record
of all security advisories
for vulnerabilities
in this section.

As of
**{% now 'local', '%B %Y' %}**,
no security advisories have been announced.
{%- if cookiecutter.licence != 'nos' %}
See the [Security Guide][1]
for more information
{%- else %}
The Security Guide
contains more information
{%- endif %}
on the process related
to vulnerability reports.

<!-- RECORD one subpage for each advisory -->

<!-- Anchors -->
{%- if cookiecutter.licence != 'nos' %}

[1]: ../../development/security.md
{%- endif %}
