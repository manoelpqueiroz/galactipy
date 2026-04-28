# {{ cookiecutter.project_name }}

<div align="center">

<!-- Project details -->
[![Python support][badge1]][burl1]
[![PyPI Release][badge1a]][burl1]
[![Repository][badge2]][burl2]
{%- if cookiecutter.create_docs and cookiecutter.__scm_platform_lc == 'gitlab' %}
[![Docs][badge2a]][burl2a]
{%- endif %}
{%- if cookiecutter.version_schema != 'trunkver' %}
[![Releases][brel1]][brel2]
{%- endif %}
{%- if cookiecutter.create_docker %}
[![Docker][bdocker1]][bdocker2]
{%- endif %}
{%- if cookiecutter.licence != 'nos' %}
[![Licence][blic1]][blic2]
{%- endif %}
[![Expand your project structure from atoms of code to galactic dimensions.][badge4]][burl4]

<!-- Information on development -->
[![Project type][badge5]][burl5]
[![Project stage][badge6]][burl6]
[![Contributions Welcome][badge7]][burl7]
[![Open issues][badge8]][burl8]
[![Merge Requests][badge9]][burl9]

<!-- Styling policies -->
{%- if cookiecutter.use_bdd %}
[![BDD][bbbd1]][bbbd2]
{%- endif %}
[![Code style: Ruff][badge10]][burl10]
{%- if cookiecutter.docstring_style in ['numpy', 'google', 'sphinx'] %}
[![Docstrings][bdocstr1]][bdocstr2]
{%- endif %}
{%- if cookiecutter.commit_convention == 'gitmoji' %}
[![Gitmoji][badge11]][burl11]
{%- elif cookiecutter.commit_convention == 'conventional' %}
[![Conventional Commits][badge11]][burl11]
{%- elif cookiecutter.commit_convention == 'conventional-gitmoji' %}
[![Conventional Gitmoji][badge11]][burl11]
{%- endif %}
[![Semantic Line Breaks][badge12]][burl12]

<!-- Development utilities -->
[![Poetry][badge13]][burl13]
[![Pre-commit][badge14]][burl14]
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[![Renovate][badge15]][burl15]
{%- else %}
[![Dependabot][badge15]][burl15]
{%- endif %}
[![Bandit][badge16]][burl16]
[![isort][badge17]][burl17]
[![Editorconfig][badge18]][burl18]
{%+ if cookiecutter.licence != 'nos' %}
<!-- Open Source benchmarks -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OpenSSF Best Practices][bossf1]][bossf2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OSSRank][bossf3]][bossf4] -->
{% endif +%}
<!-- Quality assurance -->
{%- if cookiecutter.__version_schema_base == 'effver' %}
[![Intended Effort Versioning][badge19]][burl19]
{%- elif cookiecutter.__version_schema_base == 'semver' %}
[![Semantic Versioning][badge19]][burl19]
{%- elif cookiecutter.__version_schema_base == 'calver' %}
[![Calendar Versioning][badge19]][burl19]
{%- elif cookiecutter.__version_schema_base == 'romver' %}
[![Romantic Versioning][badge19]][burl19]
{%- elif cookiecutter.__version_schema_base == 'solover' %}
[![SoloVer][badge19]][burl19]
{%- elif cookiecutter.__version_schema_base == 'trunkver' %}
[![TrunkVer][badge19]][burl19]
{%- endif %}
{%- if cookiecutter.coverage_service == 'coveralls' %}
[![Coverage][badge20]][burl20]
{%- else %}
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![Code Quality][bqa1]][bqa2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![Coverage][badge20]][burl20] -->
{%- endif %}
[![Pipelines][badge21]][burl21]

_{{ cookiecutter.project_description }}._

{% if cookiecutter.app_type != 'bare_repo' -%}
---

**POWERED BY**

[![Powered by Typer][btyper]][ltyper]
{%- if cookiecutter.__app_group == 'tui' %}
[![Powered by Textual][btextual]][ltextual]
{%- endif %}
{%- if cookiecutter.app_type != 'bare_cli' %}
[![Powered by Orbittings][borbittings]][lorbittings]
{%- endif %}

{% endif -%}
</div>

## :sunrise_over_mountains: Purpose & Function

<!-- DEFINE your project's purpose

  Don't forget to include what problem your project solves

  Also update the ROADMAP.md "Mission" based on this section
-->

## :star_struck: Standout Features

<!-- DEFINE which features your project provides that make it enticing to potential users -->

## :inbox_tray: Installation

{% if cookiecutter.app_type == 'bare_repo' -%}
Use [`pip`][install1] to install {{ cookiecutter.project_name }}:

```bash
pip install -U {{ cookiecutter.repo_name }}
```

## :black_joker: How to Use It

<!-- UPDATEME with basic usage instructions for your project -->

{% else -%}
Use [`pipx`][install1] to install {{ cookiecutter.project_name }}
in an isolated environment:

```bash
pipx install {{ cookiecutter.repo_name }}
```

Then you can run it from the command line:

```bash
{{ cookiecutter.repo_name }} --help
```

## :black_joker: How to Use It

{% if cookiecutter.app_type == 'tui' -%}
You can simply
launch the {{ cookiecutter.project_name }}
by calling `{{ cookiecutter.repo_name }}`
directly.

The top-level command
is also callable
with other options
for fine-grained
control of the application:

> _`{{ cookiecutter.repo_name }} [--version | -v] [(--config | -c) <file>]`_

{% else -%}
The top-level command
is the entry point
for additional
operations:

> _`{{ cookiecutter.repo_name }} [--version | -v]`_

{% if cookiecutter.app_type == 'hybrid' -%}
Launch the terminal interface
with the `{{ cookiecutter.repo_name }} launch` command:

> _`{{ cookiecutter.repo_name }} launch [(--config | -c) <file>]`_

{% endif -%}
{% endif -%}
{% if cookiecutter.create_docs -%}
You can see the complete list of commands
and how to use them properly
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
in our documentation's [_CLI Guide_][htu1] section.
{%- else %}
in our documentation's _CLI Guide_ section.
{%- endif %}

{% endif -%}
{% endif -%}
## :books: Documentation

{% if cookiecutter.create_docs -%}
{{ cookiecutter.project_name }} provides
a comprehensive documentation.
It contains in-depth guides
on how to use it
and the complete API reference,
suited for newcomers
and veteran users alike! :raised_hands:

You can find everything you need
[:rightwards_hand: :rightwards_hand: right here][docs1].
{% else -%}
<!-- UPDATEME with info on how your users can find your documentation for reference -->

{% endif -%}
## :reminder_ribbon: Contributing

There are several ways
to contribute to {{ cookiecutter.project_name }}.
Refer to our [`CONTRIBUTING` guide][burl7]
for all relevant details.

Currently,
we are seeking help
to tackle areas of focus
that are more pressing
to our project's progress
and would make an immediate difference
in helping us achieve our [mission][contributing1].

Here are some key contributions
your can help us with
right now:

- Provide input in [design discussions][contributing2]
  to define the desired features of {{ cookiecutter.project_name }}.
<!-- DEFINE additional areas of assistance as development progresses -->

## :ship: Releases

{% if cookiecutter.version_schema != 'trunkver' -%}
You can see
the list of available releases
on the [{{ cookiecutter.__scm_platform_base }} Releases][release1] page.

{% if cookiecutter.__version_schema_base == 'effver' -%}
We follow [Intended Effort Versioning][release2] specification,
{% elif cookiecutter.__version_schema_base == 'semver' -%}
We follow [Semantic Versioning][release2] specification,
{% elif cookiecutter.__version_schema_base == 'calver' -%}
We follow [Calendar Versioning][release2] specification,
{% elif cookiecutter.__version_schema_base == 'romver' -%}
We follow [Romantic Versioning][release2] specification,
{% elif cookiecutter.__version_schema_base == 'solover' -%}
We follow the [SoloVer][release2] versioning schema,
{% endif -%}
{% else -%}
We follow a trunk-based development cycle,
which dismisses traditional releases and tags.
Instead,
the program is always available
in a working state for users,
with every incremental change to the codebase
being published to PyPI.

To better leverage
our development,
we apply the [TrunkVer][release1] versioning schema
to distribute the package,
{% endif -%}
details can be found in our [`CONTRIBUTING` guide][burl19].
{%- if cookiecutter.create_docker %}

### Run as a Docker Container

{{ cookiecutter.project_name }} also provides
official Docker images
to run the application on a container.
Published images are available
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
via [GitLab Container Registries][docker1].
{%- if cookiecutter.__schema_type == 'segmented' %}

The following tags are available:

{% if cookiecutter.__schema_group == 'semver-like' -%}
<!-- UPDATEME by defining the {{ cookiecutter.__version_s1.lower() }} tag specification once the project reaches v1.0.0 -->
{% endif -%}
{% if cookiecutter.version_schema != 'calver-auto' -%}
- **{{ cookiecutter.__version_s3.title() }} tags** reflect the official releases
  individually;
{% endif -%}
- **{{ cookiecutter.__version_s2.title() }} tags** always mirror
  the latest available changes
  for a {{ cookiecutter.__version_s2.lower() }} release
  (i.e., `{{ cookiecutter.__version_s1 }}.{{ cookiecutter.__version_s2 }}`);
{% if cookiecutter.__schema_group == 'calver' -%}
- **{{ cookiecutter.__version_s1.title() }} tags** always mirror
  the latest available changes
  for a yearly release;
{% endif -%}
- **Nightly tags** functionally work
  as rolling releases,
  but should not be used
  in production environments:
  - The `nightly` tag reflects
    the most recent state
    of the `master` branch;
  - If a pre-release is published,
    it can be run with Docker
{%- if cookiecutter.version_schema == 'calver-auto' %}
    with the `{{ cookiecutter.__version_s1 }}.{{ cookiecutter.__version_s2 }}-nightly` tag.
{%- else %}
    with the `{{ cookiecutter.__version_s1 }}.{{ cookiecutter.__version_s2 }}.{{ cookiecutter.__version_s3 }}-nightly` tag.
{%- endif %}
{%- endif %}
{%- else %}
via [Docker Hub][docker1].
{%- if cookiecutter.__schema_type == 'segmented' %}

The following tags are available:

{% if cookiecutter.version_schema != 'calver-auto' -%}
- **{{ cookiecutter.__version_s3.title() }} tags** reflect the official releases;
{% endif -%}
- **{{ cookiecutter.__version_s2.title() }} tags** always mirror
  the latest available changes
  for a {{ cookiecutter.__version_s2.lower() }} release
  (i.e., `{{ cookiecutter.__version_s1 }}.{{ cookiecutter.__version_s2 }}`);
- **{{ cookiecutter.__version_s1.title() }} tags** always mirror
  the latest available changes
{%- if cookiecutter.__schema_group == 'calver' %}
  for a yearly release
{%- else %}
  for a {{ cookiecutter.__version_s1.lower() }} release
{%- endif %}
  (i.e., `{{ cookiecutter.__version_s1 }}`).
{%- endif %}
{%- endif %}
{%- endif %}

## :shield: Licence
{%- if cookiecutter.licence != 'nos' %}

[![Licence][blic1]][blic2]

This project is licenced
under the terms of the **{{ cookiecutter.__licence_extended }}**.
See [LICENCE][blic2] for more details.

{%- else %}

{{ cookiecutter.project_name }} is _**not**_ open source software.
Please contact the maintainers
for more information
on licencing the project.
{%- endif %}

## :page_with_curl: Citation

We provide a [`CITATION.cff`][cite1] file
to make it easier to cite this project
in your paper.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

## :women_with_bunny_ears: Similar Projects
{%- else %}

## :dancing_women: Similar Projects
{%- endif %}

<!-- UPDATEME with projects that implement similar functionality as yours

  Provide information on which cases those projects might be more suitable than yours for users
  List similar projects that inspired yours
-->

## Credits [![Expand your project structure from atoms of code to galactic dimensions.][badge4]][burl4]

This project was generated with [Galactipy][burl4].

<!-- Anchors -->

[badge1]: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}?style=for-the-badge
[badge1a]: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=pypi&color=3775a9
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[badge2]: https://img.shields.io/badge/GitLab-0B2640?style=for-the-badge&logo=gitlab&logoColor=white
{%- if cookiecutter.create_docs %}
[badge2a]: https://img.shields.io/badge/docs-F79A10?style=for-the-badge&logo=readme&logoColor=white
{%- endif %}
{%- else %}
[badge2]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
{%- endif %}
[badge4]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[badge5]: https://img.shields.io/badge/project%20type-toy-blue?style=for-the-badge
[badge6]: https://img.shields.io/pypi/status/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=theplanetarysociety&label=stage
[badge7]: https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=for-the-badge
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[badge8]: https://img.shields.io/gitlab/issues/open/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=fca326
[badge9]: https://img.shields.io/gitlab/merge-requests/open/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=6fdac9
{%- else %}
[badge8]: https://img.shields.io/github/issues/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=bc4c00
[badge9]: https://img.shields.io/github/issues-pr/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=1f883d
{%- endif %}
[badge10]: https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge&labelColor=grey
{%- if cookiecutter.commit_convention == 'gitmoji' %}
[badge11]: https://img.shields.io/badge/%F0%9F%98%9C_gitmoji-ffdd67?style=for-the-badge
{%- elif cookiecutter.commit_convention == 'conventional' %}
[badge11]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white&style=for-the-badge
{%- elif cookiecutter.commit_convention == 'conventional-gitmoji' %}
[badge11]: https://img.shields.io/badge/conventional-%F0%9F%98%9C%20gitmoji-ffdd67?style=for-the-badge&logo=conventionalcommits&logoColor=white&labelColor=fe5196
{%- endif %}
[badge12]: https://img.shields.io/badge/sembr-FF6441?style=for-the-badge&logo=apmterminals&logoColor=white
[badge13]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[badge14]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[badge15]: https://img.shields.io/badge/Renovate-308BE3?logo=renovate&logoColor=fff&style=for-the-badge
{%- else %}
[badge15]: https://img.shields.io/badge/Dependabot-025E8C?logo=dependabot&logoColor=fff&style=for-the-badge
{%- endif %}
[badge16]: https://img.shields.io/badge/security-bandit-yellow?style=for-the-badge
[badge17]: https://img.shields.io/badge/imports-isort-1674b1?style=for-the-badge&labelColor=ef8336
[badge18]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
{%- if cookiecutter.version_schema == 'effver' %}
[badge19]: https://img.shields.io/badge/effver-0097a7?style=for-the-badge&logo=semver
{%- elif cookiecutter.version_schema == 'semver' %}
[badge19]: https://img.shields.io/badge/semver-3F4551?style=for-the-badge&logo=semver
{%- elif cookiecutter.version_schema == 'calver-auto' %}
[badge19]: https://img.shields.io/badge/calver-5Y.WW-006BFF?style=for-the-badge&logo=protoncalendar&logoColor=white
{%- elif cookiecutter.version_schema == 'calver-explicit' %}
[badge19]: https://img.shields.io/badge/calver-5Y.0M.MICRO-006BFF?style=for-the-badge&logo=protoncalendar&logoColor=white
{%- elif cookiecutter.version_schema == 'romver' %}
[badge19]: https://img.shields.io/badge/romver-DE4F4F?style=for-the-badge&logo=semver
{%- elif cookiecutter.version_schema == 'solover' %}
[badge19]: https://img.shields.io/badge/solover-056473?style=for-the-badge&logo=upptime&logoColor=white
{%- elif cookiecutter.version_schema == 'trunkver' %}
[badge19]: https://img.shields.io/badge/trunkver-3F54A3?style=for-the-badge&logo=roots&logoColor=white
{%- endif %}
{%- if cookiecutter.coverage_service == 'coveralls' %}
[badge20]: https://img.shields.io/coverallsCoverage/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=coveralls
{%- else %}
<!-- TODO Replace the hash `d5402a91aa7b4234bd1c19b5e86a63be` with your project ID in the "Codacy Badge" section available at https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/settings
[badge20]: https://img.shields.io/codacy/coverage/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy -->
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[badge21]: https://img.shields.io/gitlab/pipeline-status/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
{%- else %}
[badge21]: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/build.yml?style=for-the-badge&logo=github
{%- endif %}

[burl1]: {{ cookiecutter.__pypi_url }}
[burl2]: {{ cookiecutter.__scm_repo_url }}
{%- if cookiecutter.create_docs and cookiecutter.__scm_platform_lc == 'gitlab' %}
[burl2a]: {{ cookiecutter.__pages_url }}
{%- endif %}
[burl4]: https://kutt.it/7fYqQl
[burl5]: https://project-types.github.io/#toy
[burl6]: {{ cookiecutter.__scm_repo_latch }}/blob/master/ROADMAP.md#development-stages
[burl7]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md
[burl8]: {{ cookiecutter.__scm_repo_latch }}/issues
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[burl9]: {{ cookiecutter.__scm_repo_latch }}/merge_requests
{%- else %}
[burl9]: {{ cookiecutter.__scm_repo_latch }}/pulls
{%- endif %}
[burl10]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#codestyle
[burl11]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#commit-customs
[burl12]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#semantic-line-breaks
[burl13]: https://python-poetry.org/
[burl14]: {{ cookiecutter.__scm_repo_latch }}/blob/master/.pre-commit-config.yaml
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[burl15]: {{ cookiecutter.__scm_repo_latch }}/blob/master/renovate.json
{%- else %}
[burl15]: {{ cookiecutter.__scm_repo_latch }}/blob/master/.github/dependabot.yml
{%- endif %}
[burl16]: https://bandit.readthedocs.io/en/latest/
[burl17]: https://pycqa.github.io/isort/
[burl18]: {{ cookiecutter.__scm_repo_latch }}/blob/master/.editorconfig
[burl19]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#versioning-customs
{%- if cookiecutter.coverage_service == 'coveralls' %}
[burl20]: https://coveralls.io/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
{%- else %}
[burl20]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/coverage
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[burl21]: {{ cookiecutter.__scm_repo_latch }}/pipelines
{%- else %}
[burl21]: {{ cookiecutter.__scm_repo_latch }}/actions/workflows/build.yml
{%- endif %}

{% if cookiecutter.version_schema != 'trunkver' -%}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[brel1]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=253747
{% else -%}
[brel1]: https://img.shields.io/github/v/release/{{ cookiecutter.scm_namespace}}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=347d39
{% endif -%}
[brel2]: {{ cookiecutter.__scm_repo_latch }}/releases

{% endif -%}
{% if cookiecutter.licence != 'nos' -%}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[blic1]: https://img.shields.io/gitlab/license/{{ cookiecutter.scm_namespace}}/{{ cookiecutter.repo_name }}?style=for-the-badge
{% elif cookiecutter.__scm_platform_lc == 'github' -%}
[blic1]: https://img.shields.io/github/license/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge
{% endif -%}
[blic2]: {{ cookiecutter.__scm_repo_latch }}/blob/master/LICENCE

<!-- TODO Replace the `100` ID with your project's index at https://www.bestpractices.dev/en
[bossf1]: https://img.shields.io/cii/level/100?style=for-the-badge&logo=linux-foundation&label=openssf%20best%20practices
[bossf2]: https://www.bestpractices.dev/en/projects/100 -->
<!-- TODO Replace the `200` ID with your project's index at https://ossrank.com/
[bossf3]: https://shields.io/endpoint?url=https://ossrank.com/shield/200&style=for-the-badge
[bossf4]: https://ossrank.com/p/200 -->

{% endif -%}
{% if cookiecutter.coverage_service == 'codacy' -%}
<!-- TODO Replace the hash `d5402a91aa7b4234bd1c19b5e86a63be` with your project ID in the "Codacy Badge" section available at https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/settings
[bqa1]: https://img.shields.io/codacy/grade/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy
[bqa2]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/dashboard -->

{% endif -%}
{% if cookiecutter.app_type != 'bare_repo' -%}
[btyper]: https://img.shields.io/badge/Typer-black?style=for-the-badge&logo=typer
[ltyper]: https://typer.tiangolo.com/

{% if cookiecutter.__app_group == 'tui' -%}
[btextual]: https://img.shields.io/badge/Textual-272a35?style=for-the-badge&logo=textual
[ltextual]: https://textual.textualize.io/

{% endif -%}
{% if cookiecutter.app_type != 'bare_cli' -%}
[borbittings]: https://img.shields.io/badge/orbittings-007A68?style=for-the-badge&logo=orbittings
[lorbittings]: https://gitlab.com/galactipy/orbittings

{% endif -%}
[install1]: https://pipx.pypa.io/latest/installation/

{% else -%}
[install1]: https://pip.pypa.io/en/stable/installation/

{% endif -%}
{% if cookiecutter.create_docs -%}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[htu1]: {{ cookiecutter.__pages_url }}/user_guide/cli

[docs1]: {{ cookiecutter.__pages_url }}

{% else -%}
[docs1]: {{ cookiecutter.__scm_repo_latch }}/blob/master/docs/index.md

{% endif -%}
{% endif -%}
[contributing1]: {{ cookiecutter.__scm_repo_latch }}/blob/master/ROADMAP.md#project-mission
{%- if cookiecutter.__scm_platform_group == 'glab-paid' %}
[contributing2]: {{ cookiecutter.__scm_repo_latch }}/issues?state=opened&label_name%5B%5D=design%3A%3A%2A&type%5B%5D=issue
{%- elif cookiecutter.__scm_platform_group == 'glab-free' %}
[contributing2]: {{ cookiecutter.__scm_repo_latch }}/issues?state=opened&label_name%5D%5B%5D=design-discovery&or%5Blabel_name%5D%5B%5D=design-formulation&or%5Blabel_name%5D%5B%5D=design-reassessment&type%5B%5D=issue
{%- else %}
[contributing2]: {{ cookiecutter.__scm_repo_latch }}/issues?q=label%3Adesign-discovery%20OR%20label%3Adesign-formulation%20OR%20label%3Adesign-reassessment
{%- endif %}
{%- if cookiecutter.version_schema != 'trunkver' %}

[release1]: {{ cookiecutter.__scm_repo_latch }}/releases
{%- if cookiecutter.__version_schema_base == 'effver' %}
[release2]: https://jacobtomlinson.dev/effver/
{%- elif cookiecutter.__version_schema_base == 'semver' %}
[release2]: https://semver.org/
{%- elif cookiecutter.__version_schema_base == 'calver' %}
[release2]: https://calver.org/
{%- elif cookiecutter.__version_schema_base == 'romver' %}
[release2]: https://github.com/romversioning/romver
{%- elif cookiecutter.__version_schema_base == 'solover' %}
[release2]: https://beza1e1.tuxen.de/SoloVer
{%- endif %}
{%- else %}

[release1]: https://trunkver.org/
{%- endif %}
{%- if cookiecutter.create_docker %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[bdocker1]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=linux-containers&logoColor=C5F4EC&label=image&color=C5F4EC
[bdocker2]: {{ cookiecutter.__docker_repo }}

[docker1]: https://docs.gitlab.com/user/packages/container_registry/
{%- else %}

[bdocker1]: https://img.shields.io/docker/v/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=docker&logoColor=lightblue&label=image&color=lightblue
[bdocker2]: {{ cookiecutter.__docker_repo }}

[docker1]: https://hub.docker.com/
{%- endif %}
{%- endif %}
{%- if cookiecutter.docstring_style == 'numpy' %}

[bdocstr1]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
{%- elif cookiecutter.docstring_style == 'google' %}

[bdocstr1]: https://img.shields.io/badge/docstrings-google-ffbb00?style=for-the-badge&labelColor=00ac47
{%- elif cookiecutter.docstring_style == 'sphinx' %}

[bdocstr1]: https://img.shields.io/badge/docstrings-sphinx%2Frest-ce3f31?style=for-the-badge&labelColor=0a507a
{%- endif %}
{%- if cookiecutter.docstring_style != 'other' %}
[bdocstr2]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#docstring-convention
{%- endif %}

{% if cookiecutter.use_bdd -%}
[bbbd1]: https://img.shields.io/badge/BDD-23D96C?style=for-the-badge&logo=cucumber&logoColor=white
[bbbd2]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CONTRIBUTING.md#behaviour-driven-development

{% endif -%}
[cite1]: {{ cookiecutter.__scm_repo_latch }}/blob/master/CITATION.cff
