# Noticeboard
{%- if cookiecutter.licence != 'nos' %}

Welcome to {{ cookiecutter.project_name }}'s noticeboard!
Here we compile all documents
of public interest
and relevant announcements
in a single place
for reference.
{%- else %}
This is the {{ cookiecutter.project_name }} noticeboard.
Here we compile documents of public interest
and relevant announcements
of different topics.
{%- endif %}

Here you will find:

- The release notes history
  for all publicly released
  versions of the application;
{%- if cookiecutter.licence != 'nos' %}
- Any security advisories published
  to address security issues
  (more info on the [Security Guide][1]);
{%- else %}
- The roadmap for the project,
  listing features
  on the pipeline
  for delivery;
- Content related to security
  including the security guide
  with instructions to send vulnerability reports
  and any security advisories published
  to address security issues;
{%- endif %}
- Guides for migrating your installation of {{ cookiecutter.project_name }}
  when we publish releases
  with breaking changes.

<!-- RECORD any additional custom sections to handle your specific communication needs -->

<!-- Anchors -->
{%- if cookiecutter.licence != 'nos' %}

[1]: ../development/security.md
{%- endif %}
