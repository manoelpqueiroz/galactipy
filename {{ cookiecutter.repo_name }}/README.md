# {{ cookiecutter.project_name }}

<div align="center">

<!-- Project details -->
[![Python support][bp1]][bp2]
[![PyPI Release][bp3]][bp2]
[![Repository][bscm1]][bp4]
[![Releases][bscm2]][bp5]
{%- if cookiecutter.create_docker %}
[![Docker][bdocker1]][bdocker2]
{%- endif %}
{%- if cookiecutter.licence != 'nos' %}
[![Licence][blic1]][blic2]
{%- endif %}
[![Expand your project structure from atoms of code to galactic dimensions.][bp6]][bp7]

<!-- Information on development -->
[![Project type][bp8]][bp9]
[![Contributions Welcome][bp10]][bp11]
[![Open issues][bscm3]][bp12]
[![Merge Requests][bscm4]][bscm5]

<!-- Styling policies -->
{%- if cookiecutter.use_bdd %}
[![BDD][bbbd1]][bbbd2]
{%- endif %}
[![Code style: Ruff][bfo1]][bfo2]
{%- if cookiecutter.docstring_style in ['numpy', 'google', 'pep257'] %}
[![Docstrings][bli1]][bli2]
{%- endif %}
{%- if cookiecutter.commit_convention == 'gitmoji' %}
[![Gitmoji][bcv1]][bcv2]
{%- elif cookiecutter.commit_convention == 'conventional' %}
[![Conventional Commits][bcv1]][bcv2]
{%- elif cookiecutter.commit_convention == 'conventional-gitmoji' %}
[![Conventional Gitmoji][bcv1]][bcv2]
{%- endif %}
[![Semantic Line Breaks][bp13]][bp14]

<!-- Development utilities -->
[![Poetry][bp15]][bp16]
[![Pre-commit][bp17]][bp18]
[![Bandit][bp19]][bp20]
[![isort][bfo3]][bfo4]
[![Editorconfig][bp21]][bp22]
{%+ if cookiecutter.licence != 'nos' %}
<!-- Open Source benchmarks -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OpenSSF Best Practices][boss1]][boss2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OSSRank][boss3]][boss4] -->
{% endif +%}
<!-- Quality assurance -->
[![Intended Effort Versioning][bp23]][bp24]
{%- if cookiecutter.__coverage_lc == 'coveralls' %}
[![Coverage][bcov1]][bcov2]
{%- elif cookiecutter.__coverage_lc == 'codacy' %}
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![Code Quality][bcov1]][bcov2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![Coverage][bcov3]][bcov4] -->
{%- endif %}
[![Pipelines][bscm6]][bscm7]

_{{ cookiecutter.project_description }}_

</div>

## Installation

{% if cookiecutter.app_type != 'bare_repo' -%}
Use [`pipx`][fs1] to install {{ cookiecutter.project_name }}
in an isolated environment:

```bash
pipx install {{ cookiecutter.repo_name }}
```

Then you can run it from the command line:

```bash
{{ cookiecutter.repo_name }} --help
```

## Command-line Usage

{% if cookiecutter.app_type == 'tui' %}
You can simply
launch the {{ cookiecutter.project_name }}
by calling `{{ cookiecutter.repo_name }}`
directly.

The top-level command
is also callable
with other options
for fine-grained
control of the application:

> _`{{ cookiecutter.repo_name }} [--version | -v] [--config | -c]`_
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
{% elif cookiecutter.app_type == 'hybrid' %}
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

> _`{{ cookiecutter.repo_name }} launch [--config | -c]`_
>> **`--config`**
>>
>> **`-c`**
>>
>> Specify a custom configuration file
>> to launch the application.
{% elif cookiecutter.app_type == 'cli' %}
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
{% endif %}
### Manage the Configuration

The `{{ cookiecutter.repo_name }} config` command provides
additional subcommands
to manipulate
the settings
for your {{ cookiecutter.project_name }} installation:

> _`{{ cookiecutter.repo_name }} config get [--path] [--secret | -s] KEY`_
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

> _`{{ cookiecutter.repo_name }} config set [--path] [--secret | -s] KEY VALUE`_
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

> _`{{ cookiecutter.repo_name }} config extend [--path] [--secret | -s] [--create-on-missing | -c] KEY VALUE`_
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

> _`{{ cookiecutter.repo_name }} config unset [--path] [--secret | -s] KEY`_
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
Use [`pip`][fs1] to install {{ cookiecutter.project_name }}:

```bash
pip install -U {{ cookiecutter.repo_name }}
```
{%- endif %}

## :reminder_ribbon: Contributing

There are several ways
to contribute to {{ cookiecutter.project_name }}.
Refer to our [`CONTRIBUTING` guide][bp11]
for all relevant details.

## :ship: Releases

You can see
the list of available releases
on the [{{ cookiecutter.__scm_platform_base }} Releases][r1] page.

We follow [Intended Effort Versioning][fs2] specification,
details can be found in our [`CONTRIBUTING` guide][bp24].

{% if cookiecutter.licence != 'nos' -%}
## :shield: Licence

[![Licence][blic1]][blic2]

This project is licenced
under the terms of the **{{ cookiecutter.licence }}** licence.
See [LICENCE][blic2] for more details.

{% endif -%}
## :page_with_curl: Citation

We provide a [`CITATION.cff`][cite1] file
to make it easier to cite this project
in your paper.

## Credits [![Expand your project structure from atoms of code to galactic dimensions.][bp6]][bp7]

This project was generated with [Galactipy][bp7].

<!-- Anchors -->

[bp1]: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}?style=for-the-badge
[bp2]: https://pypi.org/project/{{ cookiecutter.repo_name }}/
[bp3]: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=pypi&color=3775a9
[bp4]: {{ cookiecutter.__scm_base_url }}
[bp5]: {{ cookiecutter.__scm_link_url }}/releases
[bp6]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[bp7]: https://kutt.it/7fYqQl
[bp8]: https://img.shields.io/badge/project%20type-toy-blue?style=for-the-badge
[bp9]: https://project-types.github.io/#toy
[bp10]: https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=for-the-badge
[bp11]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md
[bp12]: {{ cookiecutter.__scm_link_url }}/issues
[bp13]: https://img.shields.io/badge/sembr-367DA9?style=for-the-badge&logo=read.cv&logoColor=white
[bp14]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#semantic-line-breaks
[bp15]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[bp16]: https://python-poetry.org/
[bp17]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[bp18]: {{ cookiecutter.__scm_link_url }}/blob/master/.pre-commit-config.yaml
[bp19]: https://img.shields.io/badge/security-bandit-yellow?style=for-the-badge
[bp20]: https://bandit.readthedocs.io/en/latest/
[bp21]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[bp22]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[bp23]: https://img.shields.io/badge/effver-0097a7?style=for-the-badge&logo=semver
[bp24]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#versioning-customs
{%+ if cookiecutter.licence != 'nos' %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[blic1]: https://img.shields.io/gitlab/license/{{ cookiecutter.scm_namespace}}/{{ cookiecutter.repo_name }}?style=for-the-badge
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[blic1]: https://img.shields.io/github/license/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge
{%- endif %}
[blic2]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE

<!-- TODO Replace the `100` ID with your project's index at https://www.bestpractices.dev/en
[boss1]: https://img.shields.io/cii/level/100?style=for-the-badge&logo=linux-foundation&label=openssf%20best%20practices
[boss2]: https://www.bestpractices.dev/en/projects/100 -->
<!-- TODO Replace the `200` ID with your project's index at https://ossrank.com/
[boss3]: https://shields.io/endpoint?url=https://ossrank.com/shield/200&style=for-the-badge
[boss4]: https://ossrank.com/p/200 -->
{% endif +%}
{% if cookiecutter.__coverage_lc == 'coveralls' %}
[bcov1]: https://img.shields.io/coverallsCoverage/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=coveralls
[bcov2]: https://coveralls.io/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
{% elif cookiecutter.__coverage_lc == 'codacy' %}
<!-- TODO Replace the hash `d5402a91aa7b4234bd1c19b5e86a63be` with your project ID in the "Codacy Badge" section available at https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/settings
[bcov1]: https://img.shields.io/codacy/grade/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy
[bcov2]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/dashboard
[bcov3]: https://img.shields.io/codacy/coverage/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy
[bcov4]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/coverage -->
{% endif +%}
{% if cookiecutter.app_type != 'bare_repo' -%}
[fs1]: https://pipx.pypa.io/latest/installation/
{% else -%}
[fs1]: https://pip.pypa.io/en/stable/installation/
{% endif -%}
[fs2]: https://jacobtomlinson.dev/effver/

[r1]: {{ cookiecutter.__scm_link_url }}/releases
{%+ if cookiecutter.__scm_platform_lc == 'gitlab' %}
[bscm1]: https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white
[bscm2]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=FFCA28
[bscm3]: https://img.shields.io/gitlab/issues/open/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=fca326
[bscm4]: https://img.shields.io/gitlab/merge-requests/open/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=6fdac9
[bscm5]: {{ cookiecutter.__scm_link_url }}/merge_requests
[bscm6]: https://img.shields.io/gitlab/pipeline-status/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[bscm7]: {{ cookiecutter.__scm_link_url }}/pipelines
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[bscm1]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[bscm2]: https://img.shields.io/github/v/release/{{ cookiecutter.scm_namespace}}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=347d39
[bscm3]: https://img.shields.io/github/issues/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=bc4c00
[bscm4]: https://img.shields.io/github/issues-pr/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=1f883d
[bscm5]: {{ cookiecutter.__scm_link_url }}/pulls
[bscm6]: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}/build.yml?style=for-the-badge&logo=github
[bscm7]: {{ cookiecutter.__scm_link_url }}/actions/workflows/build.yml
{%- if cookiecutter.licence != 'nos' %}

{%- endif %}
{%- endif %}
{%+ if cookiecutter.create_docker %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[bdocker1]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_namespace }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=linux-containers&logoColor=C5F4EC&label=image&color=C5F4EC
[bdocker2]: {{ cookiecutter.__scm_base_url }}/container_registry
{%- else %}
[bdocker1]: https://img.shields.io/docker/v/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=docker&logoColor=lightblue&label=image&color=lightblue
[bdocker2]: https://hub.docker.com/r/{{ cookiecutter.scm_namespace }}/{{ cookiecutter.repo_name }}
{%- endif %}
{%+ endif %}
[bfo1]: https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge&labelColor=grey
[bfo2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#codestyle
[bfo3]: https://img.shields.io/badge/imports-isort-1674b1?style=for-the-badge&labelColor=ef8336
[bfo4]: https://pycqa.github.io/isort/
{%- if cookiecutter.docstring_style == 'numpy' %}
[bli1]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
{%- elif cookiecutter.docstring_style == 'google' %}
[bli1]: https://img.shields.io/badge/docstrings-google-ffbb00?style=for-the-badge&labelColor=00ac47
{%- elif cookiecutter.docstring_style == 'pep257' %}
[bli1]: https://img.shields.io/badge/docstrings-pep257-FFD43B?style=for-the-badge&labelColor=3776ab
{%- endif %}
[bli2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#docstring-convention

{%- if cookiecutter.use_bdd %}
[bbbd1]: https://img.shields.io/badge/BDD-23D96C?style=for-the-badge&logo=cucumber&logoColor=white
[bbbd2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#behaviour-driven-development
{%- endif %}
{%- if cookiecutter.commit_convention == 'gitmoji' %}
[bcv1]: https://img.shields.io/badge/%F0%9F%98%9C_gitmoji-ffdd67?style=for-the-badge
{%- elif cookiecutter.commit_convention == 'conventional' %}
[bcv1]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white&style=for-the-badge
{%- elif cookiecutter.commit_convention == 'conventional-gitmoji' %}
[bcv1]: https://img.shields.io/badge/conventional-%F0%9F%98%9C%20gitmoji-ffdd67?style=for-the-badge&logo=conventionalcommits&logoColor=white&labelColor=fe5196
{%- endif %}
[bcv2]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md#commit-customs

[cite1]: {{ cookiecutter.__scm_link_url }}/blob/master/CITATION.cff
