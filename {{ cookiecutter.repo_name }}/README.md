# {{ cookiecutter.project_name }}

<div align="center">

<!-- Project details -->
[![Python support][badge1]][burl1]
[![PyPI Release][badge1a]][burl1]
[![Repository][badge2]][burl2]
[![Releases][badge3]][burl3]
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
[![Bandit][badge15]][burl15]
[![isort][badge16]][burl16]
[![Editorconfig][badge17]][burl17]
{%+ if cookiecutter.licence != 'nos' %}
<!-- Open Source benchmarks -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OpenSSF Best Practices][bossf1]][bossf2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OSSRank][bossf3]][bossf4] -->
{% endif +%}
<!-- Quality assurance -->
[![Intended Effort Versioning][badge18]][burl18]
{%- if cookiecutter.__coverage_lc == 'coveralls' %}
[![Coverage][badge19]][burl19]
{%- elif cookiecutter.__coverage_lc == 'codacy' %}
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![Code Quality][bqa1]][bqa2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![Coverage][badge19]][burl19] -->
{%- endif %}
[![Pipelines][badge20]][burl20]

_{{ cookiecutter.project_description }}_

{% if cookiecutter.app_type != 'bare_repo' -%}
---

**POWERED BY**

[![Powered by Typer][btyper]][ltyper]
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
[![Powered by Textual][btextual]][ltextual]
{%- endif %}
[![Powered by Orbittings][borbittings]][lorbittings]

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

{% if cookiecutter.app_type != 'bare_repo' -%}
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
>> **`--version`**
>>
>> **`-v`**
>>
>> Print
>> the current version of the program
>> and exit.
>
>> **`--config`**
>>
>> **`-c`**
>>
>> Specify a custom configuration file
>> to launch the application.

{% elif cookiecutter.app_type == 'hybrid' -%}
The top-level command
is the entry point
for additional
operations:

> _`{{ cookiecutter.repo_name }} [--version | -v]`_
>> **`--version`**
>>
>> **`-v`**
>>
>> Print
>> the current version of the program
>> and exit.

### Launch the Interface

Launch the terminal interface
with the `{{ cookiecutter.repo_name }} launch` command:

> _`{{ cookiecutter.repo_name }} launch [(--config | -c) <file>]`_
>> **`--config`**
>>
>> **`-c`**
>>
>> Specify a custom configuration file
>> to launch the application.

{% elif cookiecutter.app_type == 'cli' -%}
The top-level command
is the entry point
for additional
operations:

> _`{{ cookiecutter.repo_name }} [--version | -v]`_
>> **`--version`**
>>
>> **`-v`**
>>
>> Print
>> the current version of the program
>> and exit.

{% endif -%}
### Manage the Configuration

The `{{ cookiecutter.repo_name }} config` command provides
additional subcommands
to manipulate
the settings
for your {{ cookiecutter.project_name }} installation:

> _`{{ cookiecutter.repo_name }} config get [--path <file>] [--secret | -s] KEY`_
>> **`KEY`**
>>
>> The configuration key
>> to be retrieved. **[required]**
>
>> **`--path`**
>>
>> Specify
>> a custom configuration file.
>
>> **`--secret`**
>>
>> **`-s`**
>>
>> Retrieve configuration
>> from the secret manager instead.

> _`{{ cookiecutter.repo_name }} config set [--path <file>] [--secret | -s] KEY VALUE`_
>> **`KEY`**
>>
>> The configuration key
>> to be retrieved. **[required]**
>
>> **`VALUE`**
>>
>> The value to be stored
>> with the key. **[required]**
>
>> **`--path`**
>>
>> Specify
>> a custom configuration file.
>
>> **`--secret`**
>>
>> **`-s`**
>>
>> Store configuration
>> in the secret manager instead.

> _`{{ cookiecutter.repo_name }} config extend [--path <file>] [--secret | -s] [--create-on-missing | -c] KEY VALUE`_
>> **`KEY`**
>>
>> The configuration key
>> to be extended. **[required]**
>
>> **`VALUE`**
>>
>> The value to be appended
>> to the key. **[required]**
>
>> **`--path`**
>>
>> Specify
>> a custom configuration file.
>
>> **`--secret`**
>>
>> **`-s`**
>>
>> Store configuration
>> in the secret manager instead.
>
>> **`--create-on-missing`**
>>
>> **`-c`**
>>
>> Add the provided value
>> in an array
>> if the setting is not set.
>> Will raise an error
>> otherwise.

> _`{{ cookiecutter.repo_name }} config unset [--path <file>] [--secret | -s] KEY`_
>> **`KEY`**
>>
>> The configuration key
>> to be removed. **[required]**
>
>> **`--path`**
>>
>> Specify
>> a custom configuration file.
>
>> **`--secret`**
>>
>> **`-s`**
>>
>> Retrieve configuration
>> from the secret manager instead.

{% else -%}
Use [`pip`][install1] to install {{ cookiecutter.project_name }}:

```bash
pip install -U {{ cookiecutter.repo_name }}
```

## :black_joker: How to Use It

<!-- UPDATEME with basic usage instructions for your project -->

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

You can see
the list of available releases
on the [{{ cookiecutter.__scm_platform_base }} Releases][release1] page.

We follow [Intended Effort Versioning][release2] specification,
details can be found in our [`CONTRIBUTING` guide][burl18].

{% if cookiecutter.licence != 'nos' -%}
## :shield: Licence

[![Licence][blic1]][blic2]

This project is licenced
under the terms of the **{{ cookiecutter.__licence_extended }}**.
See [LICENCE][blic2] for more details.

{% else -%}
{{ cookiecutter.project_name }} is _**not**_ open source software.
Please contact the maintainers
for more information
on licencing the project.

{% endif -%}
## :page_with_curl: Citation

We provide a [`CITATION.cff`][cite1] file
to make it easier to cite this project
in your paper.

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
## :women_with_bunny_ears: Similar Projects
{%- else -%}
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
[badge3]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=253747
{%- else %}
[badge2]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[badge3]: https://img.shields.io/github/v/release/{{ cookiecutter.scm_namespace}}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=347d39
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
[badge15]: https://img.shields.io/badge/security-bandit-yellow?style=for-the-badge
[badge16]: https://img.shields.io/badge/imports-isort-1674b1?style=for-the-badge&labelColor=ef8336
[badge17]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[badge18]: https://img.shields.io/badge/effver-0097a7?style=for-the-badge&logo=semver
{%- if cookiecutter.__coverage_lc == 'coveralls' %}
[badge19]: https://img.shields.io/coverallsCoverage/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=coveralls
{%- else %}
<!-- TODO Replace the hash `d5402a91aa7b4234bd1c19b5e86a63be` with your project ID in the "Codacy Badge" section available at https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/settings
[badge19]: https://img.shields.io/codacy/coverage/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy -->
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[badge20]: https://img.shields.io/gitlab/pipeline-status/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
{%- else %}
[badge20]: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/build.yml?style=for-the-badge&logo=github
{%- endif %}

[burl1]: https://pypi.org/project/{{ cookiecutter.repo_name }}/
[burl2]: {{ cookiecutter.__scm_base_url }}
[burl3]: {{ cookiecutter.__scm_link_url }}/releases
[burl4]: https://kutt.it/7fYqQl
[burl5]: https://project-types.github.io/#toy
[burl6]: {{ cookiecutter.__scm_link_url }}/blob/master/ROADMAP.md#development-stages
[burl7]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md
[burl8]: {{ cookiecutter.__scm_link_url }}/issues
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[burl9]: {{ cookiecutter.__scm_link_url }}/merge_requests
{%- else %}
[burl9]: {{ cookiecutter.__scm_link_url }}/pulls
{%- endif %}
[burl10]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#codestyle
[burl11]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commit-customs
[burl12]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#semantic-line-breaks
[burl13]: https://python-poetry.org/
[burl14]: {{ cookiecutter.__scm_link_url }}/blob/master/.pre-commit-config.yaml
[burl15]: https://bandit.readthedocs.io/en/latest/
[burl16]: https://pycqa.github.io/isort/
[burl17]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[burl18]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#versioning-customs
{%- if cookiecutter.__coverage_lc == 'coveralls' %}
[burl19]: https://coveralls.io/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
{%- else %}
[burl19]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/coverage
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[burl20]: {{ cookiecutter.__scm_link_url }}/pipelines
{%- else %}
[burl20]: {{ cookiecutter.__scm_link_url }}/actions/workflows/build.yml
{%- endif %}

{% if cookiecutter.licence != 'nos' -%}
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[blic1]: https://img.shields.io/gitlab/license/{{ cookiecutter.scm_namespace}}/{{ cookiecutter.repo_name }}?style=for-the-badge
{% elif cookiecutter.__scm_platform_lc == 'github' -%}
[blic1]: https://img.shields.io/github/license/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge
{% endif -%}
[blic2]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE

<!-- TODO Replace the `100` ID with your project's index at https://www.bestpractices.dev/en
[bossf1]: https://img.shields.io/cii/level/100?style=for-the-badge&logo=linux-foundation&label=openssf%20best%20practices
[bossf2]: https://www.bestpractices.dev/en/projects/100 -->
<!-- TODO Replace the `200` ID with your project's index at https://ossrank.com/
[bossf3]: https://shields.io/endpoint?url=https://ossrank.com/shield/200&style=for-the-badge
[bossf4]: https://ossrank.com/p/200 -->

{% endif -%}
{% if cookiecutter.__coverage_lc == 'codacy' -%}
<!-- TODO Replace the hash `d5402a91aa7b4234bd1c19b5e86a63be` with your project ID in the "Codacy Badge" section available at https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/settings
[bqa1]: https://img.shields.io/codacy/grade/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy
[bqa2]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/dashboard -->

{% endif -%}
{% if cookiecutter.app_type != 'bare_repo' -%}
[btyper]: https://img.shields.io/badge/Typer-black?style=for-the-badge&logo=typer
[ltyper]: https://typer.tiangolo.com/
{% if cookiecutter.app_type in ['tui', 'hybrid'] -%}
[btextual]: https://img.shields.io/badge/Textual-272a35?style=for-the-badge&logo=textual
[ltextual]: https://textual.textualize.io/
{% endif -%}
[borbittings]: https://img.shields.io/badge/orbittings-007A68?style=for-the-badge&logo=orbittings
[lorbittings]: https://gitlab.com/galactipy/orbittings

[install1]: https://pipx.pypa.io/latest/installation/

{% else -%}
[install1]: https://pip.pypa.io/en/stable/installation/

{% endif -%}
[contributing1]: {{ cookiecutter.__scm_link_url }}/blob/master/ROADMAP.md#project-mission
{%- if cookiecutter.scm_platform == 'GitLab Premium/Ultimate' %}
[contributing2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5B%5D=design%3A%3A%2A&type%5B%5D=issue
{%- elif cookiecutter.scm_platform == 'GitLab Free' %}
[contributing2]: {{ cookiecutter.__scm_link_url }}/issues?state=opened&label_name%5D%5B%5D=design-discovery&or%5Blabel_name%5D%5B%5D=design-formulation&or%5Blabel_name%5D%5B%5D=design-reassessment&type%5B%5D=issue
{%- else %}
[contributing2]: {{ cookiecutter.__scm_link_url }}/issues?q=label%3Adesign-discovery%20OR%20label%3Adesign-formulation%20OR%20label%3Adesign-reassessment
{%- endif %}

[release1]: {{ cookiecutter.__scm_link_url }}/releases
[release2]: https://jacobtomlinson.dev/effver/
{%- if cookiecutter.create_docker %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[bdocker1]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=linux-containers&logoColor=C5F4EC&label=image&color=C5F4EC
[bdocker2]: {{ cookiecutter.__scm_base_url }}/container_registry
{%- else %}

[bdocker1]: https://img.shields.io/docker/v/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=docker&logoColor=lightblue&label=image&color=lightblue
[bdocker2]: https://hub.docker.com/r/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
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
[bdocstr2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#docstring-convention
{%- endif %}

{% if cookiecutter.use_bdd -%}
[bbbd1]: https://img.shields.io/badge/BDD-23D96C?style=for-the-badge&logo=cucumber&logoColor=white
[bbbd2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#behaviour-driven-development

{% endif -%}
[cite1]: {{ cookiecutter.__scm_link_url }}/blob/master/CITATION.cff
