# Development

We would like to encourage you
to contribute to this project
and we strive to make it
as easy as possible.
This guide is aimed at
facilitating onboarding
for new collaborators
{% if cookiecutter.scm_platform != 'GitLab Premium/Ultimate' -%}
and serving as the single source of truth
for the project's rules
and modus operandi.
{% else -%}
and as a complimentary source of information
to our [main `CONTRIBUTING` guide][0],
which you should read
before diving into this specific guide.
{% endif -%}

Contributions to {{ cookiecutter.project_name }} include
file manipulation code,
tests,
tool configuration and updates,
development automation
via CI/CD,
answering user questions,
as well as
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
managing the backlog of [issues][1]
and [{{ cookiecutter.__mr_term }}s][2]
through open discussions.
{%- else %}
managing the backlog of [issues][1],
[{{ cookiecutter.__mr_term }}s][2]
and [open discussions][2x].
{%- endif %}

We welcome all contributors
willing to work in good faith
with other contributors
and the community.
No contribution is too small
and all contributions are valued.

Whether you intend
to become a [developer][2a]
for {{ cookiecutter.project_name }}
{%- if cookiecutter.app_type == 'bare_repo' %}
or you are a [user][2b] of the library,
{%- else %}
or you are a [user][2b] of the application,
{%- endif %}
following these guidelines
helps to communicate
that you respect the time
of the developers
managing and developing
this open source project.
In return,
they should reciprocate
that respect
in addressing your issue
or assessing patches and features.

## Not Sure Where to Start?

If you don't feel
ready to start contributing,
the following steps
should help:

- The project [`README`][3] details
  how to use {{ cookiecutter.project_name }},
  provides a high-level overview
  of its features;
- To effectively contribute to {{ cookiecutter.project_name }},
  you should probably get knowledgeable
  about a few topics:
{%- if cookiecutter.app_type == 'bare_repo' %}
<!-- RECORD the basic dependencies your project contributors should be familiar with -->
{%- else %}
{%- if cookiecutter.__app_group == 'tui' %}
    - Understand how [Typer][4] and [Textual][4a] work
      under the hood
      and how they interact
      with each other
      to enable a TUI application
      on the command-line;
{%- else %}
    - Understand how [Typer][4] works
      under the hood
      to create CLI applications;
{%- endif %}
{%- if cookiecutter.app_type == 'bare_cli' %}
    - Study [Nebulog][5] and
      its upstream library, [Loguru][6],
  {%- else %}
    - Study [Orbittings][4b] and
      its upstream library, [Dynaconf][4c],
      which manage the configuration files
      for {{ cookiecutter.project_name }};
    - Do the same with [Nebulog][5] and [Loguru][6],
{%- endif %}
      which empower the logging functionality
      of the application;
{%- if cookiecutter.use_bdd %}
    - Check the [`features/`][6a] directory,
      containing the files
      describing the functional behaviour of {{ cookiecutter.project_name }}
      with the BDD paradigm;
    - The [`tests/`][7] directory
      contains all unit tests
      validating the scenarios
      described in `features/`;
{%- else %}
    - Check the [`tests/`][7] directory,
      which validate all code
      for the application;
{%- endif %}
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
    - Review the [`.gitlab-ci.yml`][8] file
      containing {{ cookiecutter.project_name }}'s [CI jobs][9],
      which outlines
      the steps
      for automating project development;
{%- else %}
    - Review the [`workflows/`][8] directory
      containing {{ cookiecutter.project_name }}'s [GitHub Actions][9]
      defined for the project;
{%- endif %}
- Take a look at
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
  the organisation's [{{ cookiecutter.__roadmap_item.capitalize() }}s][10] page
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
  the project's [{{ cookiecutter.__roadmap_item.capitalize() }}s][10] page
{%- else %}
  our [{{ cookiecutter.__roadmap_item.capitalize() }}s][10] page
{%- endif %}
  to get familiar
  with the team's plans
  for future releases;
- When you feel ready
  to jump into {{ cookiecutter.project_name }} development,
  a good place to start
  is to look for issues
{%- if cookiecutter.__scm_platform_lc == 'github' %}
  and discussions
{%- endif %}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
  labelled with [`seeking-contributors`][11]
{%- else %}
  labelled with [`seeking-builders`][11]
{%- endif %}
  or [`starter-assignment`][12];
- After familiarising yourself
  with the project's [labels][13] and [stages][14],
  you can contribute
  by participating in discussions on issues
  at any of the **Needs** statuses,
  especially those in the [**Needs Triage**][15] stage;
  we are always looking for people
  who help refine issues,
  spot duplicates,
  guide issue authors toward better clarification
  and promote project activity
  through constructive discussions.

If the steps above seem daunting,
we can relate!
Contributing to an open source project,
whether you are a seasoned developer
or perhaps a newcomer
aiming to improve your software skills,
[can be scary][16]
due to a plethora of reasons.
As maintainers,
we are committed
to building an environment
where every new contributor can thrive,
improve their skills
and feel recognised
for their contributions.

Should you still feel lost
at how to start,
these tips might
make you more comfortable
with your first steps here:

- **Join the community:**
  each open source project operates
  on different principles
  and practices.
  Coming for the first time
  is sometimes frightening
  as you might not be
  familiar with our ways.
  We approach our development
  as a continuous [debate][17],
  and we are always open
  to discussing
  with different minds
  in a constructive way.
  You can reach out to us
  in our [{{ cookiecutter.__mr_term }}s][2]
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
  and [Issue Tracker][1]
{%- else %}
  and [Discussions Page][2x]
{%- endif %}
  and comment on current developments
  with questions,
  doubts
  and suggestions.
  If still unsure,
  reach us by [e-mail][18]
  to introduce yourself,
  we will help you
  with further orientation;
- **Lurk first:**
  there is no need
  to rush things in open source,
  take your time
  by simply observing repo activity
  (you can set the option
  to [watch][19] the repository),
  reading the archives
  and documentation
  to soak up the culture
  before contributing.
  The more time
  you spend reading
  and listening,
  the more likely it is
  that your contribution
  will be well received;
- **Understand the governance:**
  read the documentation
  before contributing.
  By doing so
  you will know
  how we make decisions
  and how these decisions are made
  for each type of contribution.
  _Reading documentation isn't optional_
  when contributing to open source;
- **Start small:**
  as mentioned above,
  tackle simple bug
  or documentation fixes
  to start.
  It will be easier
  to learn the process
  and correct mistakes
  on a small contribution
  that isn't critical
  to the project.
  Make your mistakes
  on small and less significant contributions
  as you work up
  to the more complex contributions
  that {{ cookiecutter.project_name }} needs.
  Check [starter assignment][12] issues,
  or [find your own][20]
  that deserves your time and effort.

!!! tip

    Having all that said,
    aside from actions
    and tasks
    you can take
    to feel more comfortable contributing,
    we believe
    there are three fundamental _behaviours_
    that, if followed,
    will help you become
    an even more robust contributor:

    1. **Communication makes all the difference:**
       open source projects often
       have contributors
       from all over the world,
       so clear communication
       is key.
       It's completely okay
       to ask questions
       when you're stuck
       and being clear
       when submitting a {{ cookiecutter.__mr_term }}
       helps everyone involved.
       Jumping into discussions
       don't just improve your contributions;
       it also helps you
       learn much more
       from those with more experience
       and improve
       your problem-solving skills;
    2. **Patience is part of the process:**
       waiting for feedback on {{ cookiecutter.__mr_term }}s,
       learning new tools
       and figuring things out
       all take time.
       There might be times
       where frustration kicks in
       and everything feels like
       taking you nowhere,
       but if you stick to the process
       and leverage collaboration
       with other contributors
       you will thrive.
       _Contributing to open source is a marathon, not a sprint_;
    3. **The learning never stops:**
       contributing to open source
       is a rewarding experience,
       it will push you
       to learn new things,
       show you different perspectives
       and help you
       become a better communicator.
       And there's always
       more to learn,
       getting a chance to grow
       with every issue,
       every interaction
       and every feedback.

<!-- Anchors -->

{% if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' -%}
[0]: {{ cookiecutter.__contributing_prefix }}
{% endif -%}
[1]: {{ cookiecutter.__scm_link_url }}/issues
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[2]: {{ cookiecutter.__scm_link_url }}/merge_requests
{%- else %}
[2]: {{ cookiecutter.__scm_link_url }}/pulls
[2x]: {{ cookiecutter.__scm_link_url }}/discussions
{%- endif %}
[2a]: ./for_developers/index.md
[2b]: ./for_others/index.md
[3]: {{ cookiecutter.__scm_link_url }}/blob/master/README.md
{%- if cookiecutter.app_type != 'bare_repo' %}
[4]: https://typer.tiangolo.com/tutorial/
{%- if cookiecutter.__app_group == 'tui' %}
[4a]: https://textual.textualize.io/guide/
{%- endif %}
{%- if cookiecutter.app_type != 'bare_cli' %}
[4b]: https://gitlab.com/galactipy/orbittings
[4c]: https://www.dynaconf.com/
{%- endif %}
[5]: https://gitlab.com/galactipy/nebulog
[6]: https://loguru.readthedocs.io/en/stable/
{%- if cookiecutter.use_bdd %}
[6a]: {{ cookiecutter.__scm_link_url }}/tree/master/tests/features
{%- endif %}
[7]: {{ cookiecutter.__scm_link_url }}/tree/master/tests
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab-ci.yml
{%- else %}
[8]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/workflows
{%- endif %}
[9]: ./policies/ci.md
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[10]: {{ cookiecutter.__gitlab_org }}/epics
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[10]: {{ cookiecutter.__scm_link_url }}/milestones
{%- else %}
[10]: {{ cookiecutter.__scm_link_url }}/projects
{%- endif %}
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[11]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors%3A%3Adelivery&type%5B%5D=issue
[12]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=starter-assignment%3A%3A%2A&type%5B%5D=issue
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[11]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=seeking-contributors&label_name%5B%5D=seeking-builders&type%5B%5D=issue
[12]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=starter-assignment&type%5B%5D=issue
{%- else %}
[11]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Aseeking-contributors%20label%3Aseeking-builders
[12]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Astarter-assignment
{%- endif %}
[13]: {{ cookiecutter.__scm_link_url }}/labels
[14]: ./policies/open_development.md#work-item-tracking
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[15]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&status=Needs%20Triage&type%5B%5D=issue
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[15]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=sts-needs-triage&type%5B%5D=issue
{%- else %}
[15]: {{ cookiecutter.__scm_link_url }}/issues/?q=is%3Aissue%20state%3Aopen%20label%3Asts-needs-triage
{%- endif %}
[16]: https://goauthentik.io/blog/2024-03-07-why-contributing-to-open-source-is-scary/
[17]: ./philosophy.md#start-with-a-{{ cookiecutter.__mr_term_slug }}
[18]: mailto:{{ cookiecutter.email }}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[19]: https://gitlab.com/gitlab-org/gitlab-foss/-/issues/234#note_17497758
{%- else %}
[19]: https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications#about-participating-and-watching-notifications
{%- endif %}
[20]: ./philosophy.md#there-are-no-good-first-issues
