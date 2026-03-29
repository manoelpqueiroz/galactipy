# Meet the Community

{{ cookiecutter.project_name }} is
a community-driven open source project
developed and supported
by a group of contributors.
The project maintainers have made a strong commitment
to creating
an open,
inclusive
and positive community.
Please read our [behaviour tips][1]
for guidance on how to interact with others
in a way that makes the community thrive.

We offer several communication channels
to share knowledge
and allow people to connect
with the {{ cookiecutter.project_name }} community.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
## {{ cookiecutter.__scm_platform_base }} Issue Tracker

Our main place of interaction
is in the [Issue Tracker][2].
{% else -%}
## {{ cookiecutter.__scm_platform_base }} Issue Tracker and Discussions Page

Our main places of interaction
is in the [Issue Tracker][2]
and the [Discussions page][2a].
{% endif -%}
Anyone can participate
by opening new items
to address your questions,
such as:

- "I noticed the this {% if cookiecutter != 'bare_repo' %}feature{% else %}function{% endif %}
  is not working as expected"
  (i.e., bug reports);
- "I would like this error message
  to be more readable"
  (i.e., feature requests);
- "I found this documentation section unclear"
  (i.e., request quality-of-life improvements).

Check our section on [contributing][3]
for more information.

<!-- RECORD other forms to reach the community, like meetings, event calendar, mailing list, Discord etc. -->

<!-- Anchors -->

[1]: ./for_developers/behave.md
[2]: {{ cookiecutter.__scm_link_url }}/issues
{%- if cookiecutter.__scm_platform_lc == 'github' %}
[2a]: {{ cookiecutter.__scm_link_url }}/discussions
{%- endif %}
[3]: ./for_others/index.md
