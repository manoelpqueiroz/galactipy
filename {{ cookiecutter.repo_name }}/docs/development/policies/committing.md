{% raw -%}
---
tags:
  - Development Guides
  - Policies & Rules
---

{% endraw -%}
# Commit Customs
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#commit-customs
  [group]: {{ cookiecutter.__contributing_prefix }}#commit-customs

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#commit-customs

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{% if cookiecutter.commit_convention == 'gitmoji' -%}
## Gitmoji
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in project and group CONTRIBUTING.md guides
  [project]: ../../../../CONTRIBUTING.md#gitmoji
  [group]: {{ cookiecutter.__contributing_prefix }}#gitmoji

  REMEMBER TO INCORPORATE CHANGES FROM BOTH GUIDES WHEN UPDATING THIS FILE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#gitmoji

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{{ cookiecutter.project_name }} uses [Gitmoji][1]
to characterise
the nature of each commit,
you should familiarise yourself
with this method
by looking at
the list of possible Emoji
to be used.
Additionally,
looking at past commits
and which files they modified
is also a good way
to understand how Gitmoji
should be applied
to the project.

Some times a commit
can encompass more than one Gitmoji,
as changes to a file
related to a domain
can only be applied
without breaking the project
by also changing other files.
In this case,
prefer to classify the commit
through the most fundamental change
(i.e., the change
that led to subsequent file changes
from other domains).

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
!!! warning

    The shorthand codes
    specified in the Gitmoji website
    use the GitHub standard.
    For some of the Gitmoji,
    these shorthands are different
    when rendering in GitLab,
    be aware of which ones:

    |       Gitmoji       |     Default Shorthand     |  Shorthand in GitLab  |
    | :-----------------: | :-----------------------: | :-------------------: |
    |       :brick:       |        `:bricks:`         |       `:brick:`       |
    | :construction_site: | `:building_construction:` | `:construction_site:` |
    | :camera_with_flash: |     `:camera_flash:`      | `:camera_with_flash:` |
    |     :card_box:      |     `:card_file_box:`     |     `:card_box:`      |
    |       :goal:        |       `:goal_net:`        |       `:goal:`        |
    |      :pencil:       |         `:memo:`          |      `:pencil:`       |
    | :face_with_monocle: |     `:monocle_face:`      | `:face_with_monocle:` |

{% endif -%}
If the changes
still reflect a work in progress
that will be rebased
at a later moment,
we recommend committing
with the `:construction:` Gitmoji
so the CI will ignore it.

Besides the official Gitmoji,
{{ cookiecutter.project_name }} defines
the following additional Gitmoji
to apply on commits:

<!-- RECORD the specific Gitmoji for this project -->
|     Gitmoji     |     Shorthand     | Usage                              |
| :-------------: | :---------------: | ---------------------------------- |
| :bookmark_tabs: | `:bookmark_tabs:` | Updates to `CHANGELOG.md` entries. |

{% elif cookiecutter.commit_convention == 'conventional' -%}
## Conventional Commits
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#conventional-commits

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

{{ cookiecutter.project_name }} uses [Conventional Commits][1]
to characterise
the nature of each commit,
you should familiarise yourself
with this method.
We follow the [Angular Convention][1a]
to specify
the allowed commit types:

|    Type    | Description                                                                                             |
| :--------: | ------------------------------------------------------------------------------------------------------- |
|   `fix`    | A bug fix.                                                                                              |
|   `feat`   | A new feature.                                                                                          |
|  `build`   | Changes that affect the build system or external dependencies.                                          |
|    `ci`    | Changes to our CI configuration files and scripts.                                                      |
|   `docs`   | Documentation only changes.                                                                             |
|   `perf`   | A code change that improves performance.                                                                |
| `refactor` | A code change that neither fixes a bug nor adds a feature.                                              |
|  `style`   | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons etc.). |
|   `test`   | Adding missing tests or correcting existing tests.                                                      |

Scopes are optional
and used
at the discretion of contributors.
Breaking changes are
preferably identified
with exclamation marks (`!`)
after identifying the type.

Additionally,
looking at past commits
and which files they modified
is also a good way
to understand how the convention
should be applied
to the project.

If the changes
still reflect a work in progress
that will be rebased
at a later moment,
we recommend committing
with the `wip` type
so the CI will ignore it.

{% else -%}
## Conventional Gitmoji
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#conventional-gitmoji

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

{{ cookiecutter.project_name }} uses [Conventional Gitmoji][1]
to characterise
the nature of each commit,
you should familiarise yourself
with this method,
based on [Conventional Commits][1a]
with visual cues added
via Emoji.

The list of commit types
that can be used
are listed below:

|      Type       |            Emoji            |
| :-------------: | :-------------------------: |
|      `fix`      |            :bug:            |
|     `feat`      |         :sparkles:          |
|     `docs`      |          :pencil:           |
|     `style`     |            :art:            |
|   `refactor`    |          :recycle:          |
|     `perf`      |            :zap:            |
|     `test`      |     :white_check_mark:      |
|     `build`     |    :construction_worker:    |
|      `ci`       |        :green_heart:        |
|    `revert`     |          :rewind:           |
|     `dump`      |           :fire:            |
|    `hotfix`     |         :ambulance:         |
|    `deploy`     |          :rocket:           |
|      `ui`       |         :lipstick:          |
|     `init`      |           :tada:            |
|   `security`    |           :lock:            |
|    `secret`     |   :closed_lock_with_key:    |
|     `bump`      |         :bookmark:          |
|   `fix-lint`    |      :rotating_light:       |
|      `wip`      |       :construction:        |
|   `dep-drop`    |        :arrow_down:         |
|   `dep-bump`    |         :arrow_up:          |
|      `pin`      |          :pushpin:          |
|   `analytics`   | :chart_with_upwards_trend:  |
|    `dep-add`    |      :heavy_plus_sign:      |
|    `dep-rm`     |     :heavy_minus_sign:      |
|    `config`     |          :wrench:           |
|    `script`     |          :hammer:           |
|     `lang`      |   :globe_with_meridians:    |
|     `typo`      |          :pencil2:          |
|     `poop`      |           :poop:            |
|     `merge`     | :twisted_rightwards_arrows: |
|    `package`    |          :package:          |
|   `external`    |           :alien:           |
|   `resource`    |           :truck:           |
|    `license`    |      :page_facing_up:       |
|     `boom`      |           :boom:            |
|     `asset`     |           :bento:           |
| `accessibility` |        :wheelchair:         |
|  `source-docs`  |           :bulb:            |
|     `beer`      |           :beers:           |
|     `text`      |      :speech_balloon:       |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|      `db`       |         :card_box:          |
{%- else %}
|      `db`       |       :card_file_box:       |
{%- endif %}
|   `logs-add`    |        :loud_sound:         |
|    `logs-rm`    |           :mute:            |
|    `people`     |    :busts_in_silhouette:    |
|      `ux`       |     :children_crossing:     |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `arch`      |     :construction_site:     |
{%- else %}
|     `arch`      |   :building_construction:   |
{%- endif %}
|    `design`     |          :iphone:           |
|     `mock`      |           :clown:           |
|      `egg`      |            :egg:            |
|    `ignore`     |        :see_no_evil:        |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `snap`      |     :camera_with_flash:     |
{%- else %}
|     `snap`      |       :camera_flash:        |
{%- endif %}
|  `experiment`   |          :alembic:          |
|      `seo`      |            :mag:            |
|     `types`     |           :label:           |
|     `seed`      |         :seedling:          |
|     `flag`      |  :triangular_flag_on_post:  |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `catch`     |           :goal:            |
{%- else %}
|     `catch`     |         :goal_net:          |
{%- endif %}
|   `animation`   |           :dizzy:           |
|  `deprecation`  |        :wastebasket:        |
|     `auth`      |     :passport_control:      |
|  `fix-simple`   |     :adhesive_bandage:      |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|  `exploration`  |     :face_with_monocle:     |
{%- else %}
|  `exploration`  |       :monocle_face:        |
{%- endif %}
|     `dead`      |          :coffin:           |
|   `test-fail`   |         :test_tube:         |
|     `logic`     |          :necktie:          |
|    `health`     |        :stethoscope:        |
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|     `infra`     |           :brick:           |
{%- else %}
|     `infra`     |          :bricks:           |
{%- endif %}
|     `devxp`     |       :technologist:        |
|     `money`     |     :money_with_wings:      |
|   `threading`   |          :thread:           |
|  `validation`   |        :safety_vest:        |
|     `chore`     |           :broom:           |

Scopes are optional
and used
at the discretion of contributors.
Breaking changes are
preferably identified
with exclamation marks (`!`)
after identifying the type.

If the changes
still reflect a work in progress
that will be rebased
at a later moment,
we recommend committing
with the `wip` type
so the CI will ignore it.


{% endif -%}
## Commit Message Structure
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
<!-- This section is also described in the group CONTRIBUTING.md guide
  [link]: {{ cookiecutter.__contributing_prefix }}#commit-message-structure

  REMEMBER TO INCORPORATE CHANGES TO THIS FILE WHEN UPDATING THE GUIDE
-->
{%- else %}
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#commit-message-structure

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Commit messages should be clear
and concise,
and detailing aspects
of the commit
through its body
is strongly encouraged,
as it helps developers
to later understand implementation
and reasoning
behind changes.
The article [_How to Write a Git Commit Message_][2]
is a valuable resource
and reading through it
is strongly recommended
before contributing,
as developers are expected
to apply those principles
when committing.
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
## Git Trailers
<!-- This section is also described in CONTRIBUTING.md
  [link]: ../../../../CONTRIBUTING.md#git-trailers

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->

Every commit should
be identified with the respective [Git trailer][3]
to categorise the type of change being made.
When a new version of {{ cookiecutter.project_name }}
is released through a tag,
a CI pipeline compiles every trailer
to automate the version's release
and update the `CHANGELOG` file
in the root directory.

The available trailers
are listed below
and defined in the [`changelog-config.yml`][4] file:
{%- if cookiecutter.app_type == 'bare_repo' %}

|        Category in CHANGELOG        |                                                          Available Trailers                                                          |
| :---------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: |
|           :new: Additions           |                                                    `feature`<br>`add`<br>`added`                                                     |
|        :arrow_right: Changes        |                               `change`<br>`changes`<br>`changed`<br>`update`<br>`updates`<br>`updated`                               |
| :city_dusk: Deprecations & Removals |    `deprecation`<br>`deprecations`<br>`deprecate`<br>`deprecated`<br>`removal`<br>`removals`<br>`remove`<br>`removed`<br>`sunset`    |
|           :toolbox: Fixes           | `bug`<br>`bugfix`<br>`fix`<br>`fixed`<br>`hotfix`<br>`security`<br>`sec`<br>`critical`<br>`leak`<br>`injection`<br>`typo`<br>`typos` |
|   :arrow_up: Dependencies Updates   |                                                  `dependencies`<br>`dep`<br>`deps`                                                   |
|  :black_circle: Other Developments  |                                                               `other`                                                                |
{%- else %}

|           Category in CHANGELOG            |                                                                                                      Available Trailers                                                                                                      | Use Cases                                                                                                                                                              |
| :----------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| :satellite_orbital: Command-line Interface |                                                                            `cli`<br>`command`<br>`commands`<br>`terminal`<br>`output`<br>`shell`                                                                             | Updates to the CLI API that bridges the interface to the actual program. This encompasses available commands and how things are printed to the user's shell.           |
|            :keyboard: CLI Usage            |                                                   `flag`<br>`flags`<br>`option`<br>`options`<br>`opt`<br>`opts`<br>`argument`<br>`arguments`<br>`arg`<br>`args`<br>`usage`                                                   | Developments that change how the user interacts with the CLI, like options and arguments available for fine-tuning command control.                                    |
{%- if cookiecutter.__app_group == 'tui' %}
|   :computer: User Interface Improvements   |                                             `tui`<br>`ui`<br>`layout`<br>`screen`<br>`element`<br>`elements`<br>`panel`<br>`panels`<br>`widget`<br>`widgets`<br>`accessibility`                                              | Improvements to the terminal user interface (TUI), which can be related to widgets, screens, layout, readability etc.                                                  |
|        :video_game: User Experience        |                                                                     `ux`<br>`xp`<br>`interaction`<br>`navigation`<br>`nav`<br>`shortcut`<br>`shortcuts`                                                                      | All development focused on interaction processes between the user and the terminal user interface, controlling its behaviour.                                          |
{%- endif %}
|          :peacock: Customisation           |                                                            `customization`<br>`customize`<br>`theme`<br>`themes`<br>`theming`<br>`style`<br>`styles`<br>`styling`                                                            | Customisation options for user satisfaction.                                                                                                                           |
|             :beginner: Nudging             |                                                    `nudge`<br>`nudges`<br>`nudging`<br>`tutorial`<br>`tutorials`<br>`hint`<br>`hints`<br>`help`<br>`helper`<br>`helpers`                                                     | Developments that help users navigate and use the application with more ease, like tutorials, notifications, command helpers, argument/option groups, help panels etc. |
|       :electric_plug: Extensibility        | `plugin`<br>`plugins`<br>`hook`<br>`hooks`<br>`event`<br>`events`<br>`entrypoint`<br>`entrypoints`<br>`extension`<br>`extensions`<br>`extend`<br>`scaffold`<br>`scaffolds`<br>`scaffolding`<br>`type`<br>`types`<br>`typing` | Changes related to improving {{ cookiecutter.project_name }} extensibility, like entry points, plugin enablers, improvements to type hints etc.                        |
|    :link: Compatibility & Integrations     |                   `api`<br>`rest`<br>`restful`<br>`integration`<br>`integrations`<br>`integrate`<br>`compatibility`<br>`compat`<br>`service`<br>`services`<br>`webservice`<br>`webservices`<br>`external`                    | Compatibility and integrations with external services and tools.                                                                                                       |
|       :earth_americas: Localisation        |                                                                        `localization`<br>`localize`<br>`translation`<br>`translations`<br>`translate`                                                                        | Changes related to project localisation.                                                                                                                               |
|   :puzzle_piece: Application Components    |                                              `component`<br>`components`<br>`module`<br>`modules`<br>`backend`<br>`performance`<br>`improvement`<br>`improvements`<br>`improve`                                              | Changes to components in the backend not directly affecting user experience.                                                                                           |
|       :floppy_disk: Database Changes       |                                                                                           `database`<br>`db`<br>`data`<br>`schema`                                                                                           | Database-related changes.                                                                                                                                              |
|    :city_dusk: Deprecations & Removals     |                                                              `deprecation`<br>`deprecations`<br>`deprecate`<br>`removal`<br>`removals`<br>`remove`<br>`sunset`                                                               | Changes that mark features and options as deprecated or remove them from the public API.                                                                               |
|              :toolbox: Fixes               |                                                  `bug`<br>`bugfix`<br>`fix`<br>`hotfix`<br>`security`<br>`sec`<br>`critical`<br>`leak`<br>`injection`<br>`typo`<br>`typos`                                                   | Fixes for wrongful behaviour (i.e., bugs).                                                                                                                             |
|    :factory_worker: Codebase Renovation    |                                                 `architecture`<br>`arch`<br>`refactor`<br>`refactors`<br>`refactoring`<br>`rework`<br>`reworks`<br>`reworking`<br>`plumbing`                                                 | Architectural changes, refactoring and other improvements done under the hood.                                                                                         |
|      :arrow_up: Dependencies Updates       |                                                                                              `dependencies`<br>`dep`<br>`deps`                                                                                               |                                                                                                                                                                        |
|    :comet: Build & Release Optimisation    |                             `build`<br>`building`<br>`packaging`<br>`script`<br>`scripts`<br>`ci`<br>`workflow`<br>`workflows`<br>`environment`<br>`env`<br>`infrastructure`<br>`infra`<br>`iac`                             | Improvements to how the project is set up for compilation and release.                                                                                                 |
{%- if cookiecutter.use_bdd %}
|        :repeat: Design & Validation        |                                        `design`<br>`ideation`<br>`test`<br>`tests`<br>`testing`<br>`cov`<br>`coverage`<br>`bdd`<br>`scenario`<br>`scenarios`<br>`story`<br>`stories`                                         | Code integrity validations, tests and feature scenarios specification.                                                                                                 |
{%- else %}
|        :repeat: Design & Validation        |                                                                       `design`<br>`ideation`<br>`test`<br>`tests`<br>`testing`<br>`cov`<br>`coverage`                                                                        | Code integrity validations and unit tests.                                                                                                                             |
{%- endif %}
| :suspension_railway: Developer Experience  |                                           `dev`<br>`devx`<br>`devdep`<br>`devdeps`<br>`pyproject`<br>`tool`<br>`tools`<br>`specification`<br>`specifications`<br>`spec`<br>`specs`                                           | Changes to internal configuration to standardise and ease development workflow.                                                                                        |
|           :books: Documentation            |                                                                                              `documentation`<br>`doc`<br>`docs`                                                                                              | Formal documentation.                                                                                                                                                  |
|         :scroll: Project Policies          |                                  `policy`<br>`policies`<br>`rule`<br>`rules`<br>`milestone`<br>`milestones`<br>`epic`<br>`epics`<br>`roadmap`<br>`template`<br>`templates`<br>`templating`                                   | Changes that altered project rules and/or project-specific documentation.                                                                                              |
|     :gem: Continuous Improvement Feats     |                        `monitor`<br>`monitoring`<br>`tracker`<br>`trackers`<br>`tracking`<br>`log`<br>`logs`<br>`logging`<br>`alert`<br>`alerts`<br>`detection`<br>`detect`<br>`diligence`<br>`rskm`                         | Internal improvements to detect and report issues, targeting CI/CD maturity.                                                                                           |
{%- endif %}

{% endif -%}
<!-- Anchors -->
{%- if cookiecutter.commit_convention == 'gitmoji' %}

[1]: https://gitmoji.dev/
{%- elif cookiecutter.commit_convention == 'conventional' %}

[1]: https://www.conventionalcommits.org/en/v1.0.0/
[1a]: https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md
{%- else %}

[1]: https://github.com/ljnsn/cz-conventional-gitmoji
[1a]: https://www.conventionalcommits.org/en/v1.0.0/
{%- endif %}
[2]: https://cbea.ms/git-commit/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[3]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
[4]: {{ cookiecutter.__scm_repo_latch }}/blob/master/.gitlab/changelog_config.yml
{%- endif %}
