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
[![Contributions Welcome][bp8]][bp9]
[![Open issues][bscm3]][bp10]
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
[![Semantic Line Breaks][bp11]][bp12]

<!-- Development utilities -->
[![Poetry][bp13]][bp14]
[![Pre-commit][bp15]][bp16]
[![Bandit][bp17]][bp18]
[![isort][bfo3]][bfo4]
[![Editorconfig][bp19]][bp20]
{%+ if cookiecutter.licence != 'nos' %}
<!-- Open Source benchmarks -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OpenSSF Best Practices][boss1]][boss2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OSSRank][boss3]][boss4] -->
{% endif +%}
<!-- Quality assurance -->
[![Semantic versions][bp21]][bp5]
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
{% else -%}
Use [`pip`][fs1] to install {{ cookiecutter.project_name }}:

```bash
pip install -U {{ cookiecutter.repo_name }}
```
{%- endif %}

## :reminder_ribbon: Contributing

There are several ways
to contribute to {{ cookiecutter.project_name }}.
Refer to our [CONTRIBUTING guide][bp9]
for all relevant details.

## :dart: What's next

Well, that's up to you. :muscle:

For further setting up your project:

- [ ] Look for files and sections marked with `TODO` (which must be addressed in order for your project to run properly) and `UPDATEME` (optional settings if you feel inclined to);
  - If you use VS Code, install the [`Todo Tree`][wn1] extension to easily locate and jump to these marks, they are already configured in your `settings.json` file;
- [ ] Make sure to create your desired Issue labels on your platform before you start tracking them so it ensures you will be able to filter them from the get-go;
- [ ] Make changes to your CI configurations to better suit your needs.

- In order to reduce user prompts and keep things effective, the template generates files with a few assumptions:
  - It assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates and `README.md` file so links won't break when you push them to your repo;
  - It generates a PyPI badge assuming you will be able to publish your project under `{{ cookiecutter.repo_name }}`, change it otherwise;
{%- if cookiecutter.create_docker and cookiecutter.__scm_platform_lc == 'github' %}
  - It generates a Docker badge assuming you also use `{{ cookiecutter.scm_username }}` for Docker Hub and you will push your image under `{{ cookiecutter.repo_name }}`, change it otherwise.
{%- elif cookiecutter.create_docker and cookiecutter.__scm_platform_lc == 'gitlab' %}
  - It assumes you will be pushing container images to the GitLab Container Registry at `{{ cookiecutter.scm_username}}/{{ cookiecutter.repo_name }}`, change it otherwise.
{%- endif %}

If you want to put your project on steroids, here are a few Python tools which can help you depending on what you want to achieve with your application:

- [`Typer`][wn2] is great for creating CLI applications;
- [`Textual`][wn3] allows you to create more advanced terminal applications, such as a text editor or even your own shell;
- [`Rich`][wn4] makes it easy to add beautiful formatting in the terminal;
- [`tqdm`][wn5] is a fast, extensible progress bar for Python and CLI;
- [`orjson`][wn6], an ultra fast JSON parsing library;
- [`Pydantic`][wn7] is data validation and settings management using Python type hinting;
- [`Returns`][wn8] makes you function's output meaningful, typed, and safe;
- [`Loguru`][wn9] makes logging (stupidly) simple;
- [`IceCream`][wn10] is a little library for sweet and creamy debugging;
- [`Hydra`][wn11] is a framework for elegantly configuring complex applications;
- [`FastAPI`][wn12] is a type-driven asynchronous web framework.

For taking development and exposition of your project to the next level:

- Try out some more badges, not only it looks good, but it also helps people better understand some intricate details on how your project works:
  - You can look at dynamic badges available at [`Shields.io`][wn13];
  - There is a myriad of standardised static badges at [`Simple Badges`][wn14];
  - [`awesome-badges`][wn15] provides a lot of useful resources to help you deal with badges;
- Setup a code coverage service for your tests, popular options include:
  - [`Coveralls`][wn18] and [`Codecov`][wn19] if you need solely test coverage;
  - [`Code Climate`][wn20] and [`Codacy`][wn21] for fully-featured code analysis{% if cookiecutter.licence != 'nos' %};{% else %}.{% endif %}
{%- if cookiecutter.licence != 'nos' %}
- Add your project to [`OpenSSF Best Practices`][wno1] and [`OSSRank`][wno2] indexes. If you have greater ambitions for your project and/or expects it to scale at some point, it's worth considering adding it to these trackers;
  - There are already badges for those set up in your `README.md` file, just waiting for you to update their URLs with your project's index in both services :beaming_face_with_smiling_eyes:
- Setup a sponsorship page and allow users and organisations who appreciate your project to help raise for its development (and add a badge in the process! :sunglasses:). Popular platforms are:
  - [`Liberapay`][wno3];
  - [`Open Collective`][wno4];
  - [`Ko-fi`][wno5];
{%- if cookiecutter.__scm_platform_lc == 'github' %}
  - You can set a [Sponsors account][hubo1] directly integrated into GitHub;
{%- endif %}
  - Of course, you can also set any kind of gateway you wish, what works best for you and your project!
{%- endif %}

And here are a few articles which may help you:
{%+ if cookiecutter.licence != 'nos' %}
- [Open Source Guides][wno6];
- [A handy guide to financial support for open source][wno7];
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
- [GitLab CI Documentation][lab2];
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
- [GitHub Actions Documentation][hub3];
{%- endif %}
- [A Comprehensive Look at Testing in Software Development][wn22] is an article that lays out why testing is crucial for development success. Eric's blog is actually a great reference, covering topics ranging from the basics to advanced techniques and best practices;
- [Robust Exception Handling][wn23];
- [Why Your Mock Doesn't Work][wn24];
- [Managing TODOs in a codebase][wn25].

## :rocket: Features

### Development features

- Support for `Python {{ cookiecutter.minimal_python_version }}` and higher;
{%- if cookiecutter.app_type in ['tui', 'hybrid'] %}
- Provides minimal boilerplate code for a CLI with TUI application, using [`Typer`][app1] and [`Textual`][app2];
{%- elif cookiecutter.app_type == 'cli' %}
- Provides minimal boilerplate code for a CLI application, using [`Typer`][app1];
{%- elif cookiecutter.app_type == 'bare_repo' %}
- Provides minimal boilerplate files to jumpstart your project development, no code provided to restrict your design!
{%- endif %}
- Uses [`Poetry`][ft1] as the dependency manager and extends functionality with [`dynamic versioning`][ft2], [`virtual environment bundling`][ft3], dependency [`export`][ft4] and [`update resolution`][ft5]. See configuration in [`pyproject.toml`][ft6];
- Automatic code formatting with [`ruff`][fo1], with ready-to-use [`pre-commit`][fo2] hooks and several rules already selected for linting;
- Type checks with [`mypy`][ft7], security checks with [`safety`][ft8] and [`bandit`][ft9];
- Testing with [`pytest`][ft10]{% if cookiecutter.use_bdd %} and [`behaviour-driven development`][bdd1] configuration for managing scenarios;{% endif %}
- Code quality integrations with {% if cookiecutter.__coverage_lc == 'coveralls' %}[`Coveralls`][ft11]{% elif cookiecutter.__coverage_lc == 'codacy' %}[`Codacy`][ft11]{% endif %} via CI/CD;
- Predefined VS Code [`settings.json`][ft12] with quality-of-life configuration for editor, workbench, debugging and more;
- Ready-to-use [`.editorconfig`][ft13]{% if cookiecutter.create_docker %}, [`.dockerignore`][docker1]{% endif %} and [`.gitignore`][ft14] files. You don't have to worry about those things.

### Deployment features

- Predefined CI/CD build workflow with {% if cookiecutter.__scm_platform_lc == 'gitlab' %}[`GitLab CI`][lab3]{% elif cookiecutter.__scm_platform_lc == 'github' %}[`Github Actions`][hub4]{% endif %};
- Automatic package uploads to [`PyPI`][ft15] test and production repositories;
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting{% if cookiecutter.create_docker %}, docker builds{% endif %} etc with [`Invoke`][ft16];
{%- if cookiecutter.create_docker %}
- [`Dockerfile`][docker2] for your package, with CI/CD workflows to publish your image to a container registry;
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
- Automatic [`Changelog entries`][lab4] updated via [GitLab API][lab5] and [template][lab8].
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
- Always up-to-date dependencies with [`Dependabot`][hub5]. You will only need to [enable it][hub1];
- Automatic drafts of new releases with [`Release Drafter`][hub6]. You may see the list of labels in [`release-drafter.yml`][hub7].
{%- endif %}

### Project management features

- Issue and {% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates for easy integration with {{ cookiecutter.scm_platform }};
- Workflows to mark and close abandoned issues after a period of inactivity with {% if cookiecutter.__scm_platform_lc == 'gitlab' %}GitLab [`Triage Policies`][lab9]{% elif cookiecutter.__scm_platform_lc == 'github' %}[`Stale Bot`][hub8]{% endif %};
- {% if cookiecutter.commit_convention == 'gitmoji' %}[Gitmoji][bcv2]{% elif cookiecutter.commit_convention == 'conventional' %}[Conventional Commits][bcv2]{% elif cookiecutter.commit_convention == 'conventional-gitmoji' %}A mix of both [Gitmoji][cv1] and [Conventional Commits][bcv2]{% endif %} as the standard for commit titles.

### Open source community features

- Ready-to-use [{% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates][ft17] and several [Issue templates][ft18];
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CITATION.cff` and `SECURITY.md` are generated automatically;
- **Loads** of predefined [badges][ft19] to make your project stand out, you can either keep them, remove as you wish or be welcome to add even more.

## :chart_with_upwards_trend: Releases

You can see the list of available releases on the [{{ cookiecutter.scm_platform }} Releases][r1] page.

We follow [Semantic Versions][fs2] specification.
{%+ if cookiecutter.__scm_platform_lc == 'gitlab' %}
We use [`GitLab Changelog`][lab5] entries to track changes. You can categorise commits and Merge Requests made to this project using [git trailers][lab10] in your commit messages.
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
We use [`Release Drafter`][hub6]. As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.
{%- endif %}

### List of {% if cookiecutter.__scm_platform_lc == 'gitlab' %}trailers and corresponding categories{% elif cookiecutter.__scm_platform_lc == 'github' %}labels and corresponding titles{% endif %}
{%+ if cookiecutter.__scm_platform_lc == 'gitlab' %}
|            **Git trailer**            |    **Category in CHANGELOG**    |
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
|               **Label**               |      **Title in Releases**      |
{%- endif %}
| :-----------------------------------: | :-----------------------------: |
| `enhancement`, `feature`              | :rocket: Features               |
| `bug`, `refactoring`, `bugfix`, `fix` | :wrench: Fixes & Refactoring    |
| `build`, `ci`, `testing`              | :package: Build System & CI/CD  |
| `breaking`                            | :boom: Breaking Changes         |
| `documentation`                       | :memo: Documentation            |
| `dependencies`                        | :arrow_up: Dependencies updates |
{%- if cookiecutter.__scm_platform_lc == 'github' %}

You can update it in [`release-drafter.yml`][hub7].

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.
{%- endif %}
{%+ if cookiecutter.licence != 'nos' %}
## :shield: Licence

[![Licence][blic1]][blic2]

This project is licenced under the terms of the `{{ cookiecutter.licence }}` licence. See [LICENCE][blic2] for more details.
{% endif +%}
## :page_with_curl: Citation

```bibtex
{% raw %}@misc{{% endraw %}{{ cookiecutter.project_name }},
  author = {% raw %}{{% endraw %}{{ cookiecutter.author }}{% raw %}}{% endraw %},
  title = {% raw %}{{% endraw %}{{ cookiecutter.project_description }}{% raw %}}{% endraw %},
  year = {% raw %}{{% endraw %}{% now 'utc', '%Y' %}{% raw %}}{% endraw %},
  publisher = {% raw %}{{% endraw %}{{ cookiecutter.scm_platform }}{% raw %}}{% endraw %},
  journal = {% raw %}{{% endraw %}{{ cookiecutter.scm_platform }} repository{% raw %}}{% endraw %},
  howpublished = {% raw %}{{% endraw %}\url{% raw %}{{% endraw %}{{ cookiecutter.__scm_base_url}}{% raw %}}}{% endraw %}
}
```

## Credits [![Expand your project structure from atoms of code to galactic dimensions.][bp6]][bp7]

This project was generated with [`galactipy`][bp7].

<!-- Anchors -->

[bp1]: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}?style=for-the-badge
[bp2]: https://pypi.org/project/{{ cookiecutter.repo_name }}/
[bp3]: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=pypi&color=3775a9
[bp4]: {{ cookiecutter.__scm_base_url }}
[bp5]: {{ cookiecutter.__scm_link_url }}/releases
[bp6]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[bp7]: https://kutt.it/7fYqQl
[bp8]: https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=for-the-badge
[bp9]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md
[bp10]: {{ cookiecutter.__scm_link_url }}/issues
[bp11]: https://img.shields.io/badge/sembr-367DA9?style=for-the-badge&logo=read.cv&logoColor=white
[bp12]: https://sembr.org/
[bp13]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[bp14]: https://python-poetry.org/
[bp15]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[bp16]: {{ cookiecutter.__scm_link_url }}/blob/master/.pre-commit-config.yaml
[bp17]: https://img.shields.io/badge/security-bandit-yellow?style=for-the-badge
[bp18]: https://bandit.readthedocs.io/en/latest/
[bp19]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[bp20]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[bp21]: https://img.shields.io/badge/semantic%20versions-4053D6?style=for-the-badge&logo=semver
{%+ if cookiecutter.licence != 'nos' %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[blic1]: https://img.shields.io/gitlab/license/{{ cookiecutter.scm_username}}/{{ cookiecutter.repo_name }}?style=for-the-badge
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[blic1]: https://img.shields.io/github/license/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge
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
[bcov1]: https://img.shields.io/coverallsCoverage/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=coveralls
[bcov2]: https://coveralls.io/{{ cookiecutter.__scm_platform_lc }}/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}
{% elif cookiecutter.__coverage_lc == 'codacy' %}
<!-- TODO Replace the hash `d5402a91aa7b4234bd1c19b5e86a63be` with your project ID in the "Codacy Badge" section available at https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}/settings
[bcov1]: https://img.shields.io/codacy/grade/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy
[bcov2]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}/dashboard
[bcov3]: https://img.shields.io/codacy/coverage/d5402a91aa7b4234bd1c19b5e86a63be?style=for-the-badge&logo=codacy
[bcov4]: https://app.codacy.com/{{ cookiecutter.__scm_platform_redux }}/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}/coverage -->
{% endif +%}
{% if cookiecutter.app_type != 'bare_repo' -%}
[fs1]: https://pipx.pypa.io/latest/installation/
{% else -%}
[fs1]: https://pip.pypa.io/en/stable/installation/
{% endif -%}
[fs2]: https://semver.org/

[wn1]: https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree
[wn2]: https://github.com/tiangolo/typer
[wn3]: https://github.com/Textualize/textual
[wn4]: https://github.com/willmcgugan/rich
[wn5]: https://github.com/tqdm/tqdm
[wn6]: https://github.com/ijl/orjson
[wn7]: https://github.com/samuelcolvin/pydantic/
[wn8]: https://github.com/dry-python/returns
[wn9]: https://github.com/Delgan/loguru
[wn10]: https://github.com/gruns/icecream
[wn11]: https://github.com/facebookresearch/hydra
[wn12]: https://github.com/tiangolo/fastapi
[wn13]: https://shields.io/badges/static-badge
[wn14]: https://badges.pages.dev/
[wn15]: https://github.com/badges/awesome-badges
[wn16]: https://www.bestpractices.dev/en
[wn17]: https://ossrank.com/
[wn18]: https://coveralls.io/
[wn19]: https://about.codecov.io/
[wn20]: https://codeclimate.com/velocity/what-is-velocity
[wn21]: https://www.codacy.com/
[wn22]: https://pytest-with-eric.com/introduction/types-of-software-testing/
[wn23]: https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/
[wn24]: https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
[wn25]: https://medium.com/babylon-engineering/todo-find-a-title-for-the-article-fee79708ca15
{%+ if cookiecutter.licence != 'nos' %}
[wno3]: https://liberapay.com/
[wno4]: https://opencollective.com/
[wno5]: https://ko-fi.com/
[wno6]: https://opensource.guide/
[wno7]: https://github.com/nayafia/lemonade-stand
{% endif %}
{% if cookiecutter.app_type in ['tui', 'hybrid', 'cli'] -%}
[app1]: https://typer.tiangolo.com/
{% endif -%}
{% if cookiecutter.app_type in ['tui', 'hybrid'] %}
[app2]: https://textual.textualize.io/
{%- endif %}

[ft1]: https://python-poetry.org/
[ft2]: https://github.com/mtkennerly/poetry-dynamic-versioning
[ft3]: https://github.com/python-poetry/poetry-plugin-bundle
[ft4]: https://github.com/python-poetry/poetry-plugin-export
[ft5]: https://github.com/MousaZeidBaker/poetry-plugin-up
[ft6]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml
[ft7]: https://mypy.readthedocs.io
[ft8]: https://docs.safetycli.com/safety-2/
[ft9]: https://bandit.readthedocs.io/en/latest/
[ft10]: https://docs.pytest.org/en/latest/
{%- if cookiecutter.__coverage_lc == 'coveralls' %}
[ft11]: https://coveralls.io/
{%- elif cookiecutter.__coverage_lc == 'codacy' %}
[ft11]: https://www.codacy.com/
{%- endif %}
[ft12]: {{ cookiecutter.__scm_link_url }}/blob/master/.vscode/settings.json
[ft13]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[ft14]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitignore
[ft15]: https://pypi.org/
[ft16]: https://docs.pyinvoke.org/en/stable/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[ft17]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/merge_request_templates/default.md
[ft18]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/issue_templates
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[ft17]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/PULL_REQUEST_TEMPLATE.md
[ft18]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/ISSUE_TEMPLATE
{%- endif %}
[ft19]: https://shields.io/

[r1]: {{ cookiecutter.__scm_link_url }}/releases
{%+ if cookiecutter.__scm_platform_lc == 'gitlab' %}
[bscm1]: https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white
[bscm2]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=FFCA28
[bscm3]: https://img.shields.io/gitlab/issues/open/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=fca326
[bscm4]: https://img.shields.io/gitlab/merge-requests/open/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=6fdac9
[bscm5]: {{ cookiecutter.__scm_link_url }}/merge_requests
[bscm6]: https://img.shields.io/gitlab/pipeline-status/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[bscm7]: {{ cookiecutter.__scm_link_url }}/pipelines

[lab2]: https://docs.gitlab.com/ee/ci/
[lab3]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab-ci.yml
[lab4]: {{ cookiecutter.__scm_link_url }}/blob/master/CHANGELOG.md
[lab5]: https://docs.gitlab.com/ee/user/project/changelogs.html
[lab8]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/changelog_config.yml
[lab9]: https://gitlab.com/explore/catalog/components/gitlab-triage
[lab10]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[bscm1]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[bscm2]: https://img.shields.io/github/v/release/{{ cookiecutter.scm_username}}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=347d39
[bscm3]: https://img.shields.io/github/issues/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=bc4c00
[bscm4]: https://img.shields.io/github/issues-pr/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=1f883d
[bscm5]: {{ cookiecutter.__scm_link_url }}/pulls
[bscm6]: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}/build.yml?style=for-the-badge&logo=github
[bscm7]: {{ cookiecutter.__scm_link_url }}/actions/workflows/build.yml

[hub1]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[hub3]: https://help.github.com/en/actions
[hub4]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/workflows/build.yml
[hub5]: https://docs.github.com/en/code-security/dependabot
[hub6]: https://github.com/marketplace/actions/release-drafter
[hub7]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/release-drafter.yml
[hub8]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/.stale.yml
{%- if cookiecutter.licence != 'nos' %}

[hubo1]: https://github.com/sponsors
{%- endif %}
{%- endif %}
{%+ if cookiecutter.create_docker %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[bdocker1]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=linux-containers&logoColor=C5F4EC&label=image&color=C5F4EC
[bdocker2]: {{ cookiecutter.__scm_base_url }}/container_registry
{%- else %}
[bdocker1]: https://img.shields.io/docker/v/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=docker&logoColor=lightblue&label=image&color=lightblue
[bdocker2]: https://hub.docker.com/r/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}
{%- endif %}

[docker1]: {{ cookiecutter.__scm_link_url }}/blob/master/.dockerignore
[docker2]: {{ cookiecutter.__scm_link_url }}/blob/master/docker/Dockerfile
{%+ endif %}
[bfo1]: https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge&labelColor=grey
[bfo2]: https://docs.astral.sh
[bfo3]: https://img.shields.io/badge/imports-isort-1674b1?style=for-the-badge&labelColor=ef8336
[bfo4]: https://pycqa.github.io/isort/

[fo1]: https://black.readthedocs.io/en/stable/
[fo2]: https://pre-commit.com/

{%- if cookiecutter.docstring_style == 'numpy' %}
[bli1]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
[bli2]: https://numpydoc.readthedocs.io/en/latest/format.html
{%- elif cookiecutter.docstring_style == 'google' %}
[bli1]: https://img.shields.io/badge/docstrings-google-ffbb00?style=for-the-badge&labelColor=00ac47
[bli2]: https://google.github.io/styleguide/pyguide.html
{%- elif cookiecutter.docstring_style == 'pep257' %}
[bli1]: https://img.shields.io/badge/docstrings-pep257-FFD43B?style=for-the-badge&labelColor=3776ab
[bli2]: https://peps.python.org/pep-0257/
{%- endif %}

{%- if cookiecutter.use_bdd %}
[bbbd1]: https://img.shields.io/badge/BDD-23D96C?style=for-the-badge&logo=cucumber&logoColor=white
[bbbd2]: https://cucumber.io/

[bdd1]: https://cucumber.io/
{%- endif %}
{%- if cookiecutter.commit_convention == 'gitmoji' %}
[bcv1]: https://img.shields.io/badge/%F0%9F%98%9C_gitmoji-ffdd67?style=for-the-badge
[bcv2]: https://gitmoji.dev/
{%- elif cookiecutter.commit_convention == 'conventional' %}
[bcv1]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white&style=for-the-badge
[bcv2]: https://conventionalcommits.org
{%- elif cookiecutter.commit_convention == 'conventional-gitmoji' %}
[bcv1]: https://img.shields.io/badge/conventional-%F0%9F%98%9C%20gitmoji-ffdd67?style=for-the-badge&logo=conventionalcommits&logoColor=white&labelColor=fe5196
[bcv2]: https://conventionalcommits.org
[cv1]: https://gitmoji.dev/
{%- endif %}
