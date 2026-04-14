{% raw -%}
---
tags:
  - Development Guides
  - Workflows
---

{% endraw -%}
# {{ cookiecutter.__mr_term }} Review Process

After [starting with a {{ cookiecutter.__mr_term }}][1],
ensuring you have opened an [admissible {{ cookiecutter.__mr_acronym }}][2]
and have finished contributing with changes,
the review process can start.

## Contribution Acceptance Criteria

To make sure that
your {{ cookiecutter.__mr_term }} can be approved,
ensure that
it meets the contribution acceptance criteria below:

1. The change is
   as small as possible;
2. If the {{ cookiecutter.__mr_term }} contains
   more than 500 changes:
   - Explain the reason;
   - Mention a maintainer;
3. Mention any major breaking changes;
4. Include proper tests
   and make all tests pass
   (unless it contains a test
   exposing a bug in existing code);
   - If a failing CI build
     seems to be
     unrelated to your contribution,
     you can try restarting the failing CI job,
     rebasing on top of the target branch
     to bring in updates
     that may resolve the failure,
     or if it has not been fixed yet,
     ask a developer
     to help you fix the test;
5. The {{ cookiecutter.__mr_acronym }} contains
   a few logically organised commits,
{%- if cookiecutter.commit_convention == 'gitmoji' %}
   using [Gitmoji][3].
{%- elif cookiecutter.commit_convention == 'conventional' %}
   using [Conventional Commits][3].
{%- else %}
   using [Conventional Gitmoji][3].
{%- endif %}
   We do not apply the squash method
   for merging changes;
6. The changes can merge
   without problems.
   If not,
   you should rebase
   if you're the only one working
   on your feature branch,
   otherwise merge the default branch
   into the {{ cookiecutter.__mr_acronym }} branch;
7. Only one specific issue is fixed
   or one specific feature is implemented.
   Do not combine things;
   send separate {{ cookiecutter.__mr_term }}s
   for each issue or feature;
8. Contains functionality
   that other users will benefit from;
9. Changes do not degrade performance;
10. If the {{ cookiecutter.__mr_term }} adds
    any new dependencies,
    they should conform
    to our existing licence;
    also,
    make the reviewer aware
    of the new library
    and explain
    why you need it.

## Getting Reviewed

As soon as you have changes to review,
have the changes reviewed
by a reviewer.
The reviewer can:

- Give you a second opinion
  on the chosen solution
  and implementation;
- Help look for
  bugs,
  logic problems,
  or uncovered edge cases.

If the {{ cookiecutter.__mr_term }}
is small and straightforward
to review,
you can skip the reviewer step
and directly ask a maintainer.

What constitutes "small and straightforward"
is a gray area.
Here are some examples
of small and straightforward changes:

- Fixing a typo
  or making small copy changes;
- A tiny refactor
  that doesn't change
  any behaviour
  or data;
- Removing unused functions,
  classes
  and methods;
- A well-understood logic change
  that requires changes
  to 5 lines of code
  or less.

Otherwise,
a {{ cookiecutter.__mr_term }} should be first
reviewed by a reviewer
in each domain
(e.g., CI,
backend,
frontend
etc.)
the {{ cookiecutter.__mr_acronym }} touches,
as maintainers may
not have the relevant domain knowledge.
This also helps
to spread the workload.

Depending on the areas
your {{ cookiecutter.__mr_term }} touches,
it must be approved
by one or more maintainers.

Getting your {{ cookiecutter.__mr_term }} merged
also requires a maintainer.
If it requires more than one approval,
the last maintainer
to review and approve merges it.

<!-- Anchors -->

[1]: ../philosophy.md#start-with-a-{{ cookiecutter.__mr_term_slug }}
[2]: ./prepare.md#opening-admissible-{{ cookiecutter.__mr_term_slug }}s
{%- if cookiecutter.commit_convention == 'gitmoji' %}
[3]: ../policies/committing.md#gitmoji
{%- elif cookiecutter.commit_convention == 'conventional' %}
[3]: ../policies/committing.md#conventional-commits
{%- else %}
[3]: ../policies/committing.md#conventional-gitmoji
{%- endif %}
