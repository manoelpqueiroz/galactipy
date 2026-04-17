{% raw -%}
---
tags:
  - Section Intros
  - Design Definitions
---

{% endraw -%}
# Internal Packages

{{ cookiecutter.project_name }} implements objects
that are used to streamline functionality
of the public API.
However,
since they are not supposed
to be directly called by users,
they are gathered inside `_internal` packages
and not exposed
in the public API.

Nevertheless,
they are essential
for proper {{ cookiecutter.project_name }} functioning,
and are referenced in this section
so contributors can understand
their purpose and placement
within the code structure.
