# {{ cookiecutter.project_name }}

<div align="center">

[![Python support][bp1]][bp2]
[![PyPI Release][bp3]][bp2]
[![Repository][bg1]][bp4]
[![Releases][bg2]][bp5]
{%- if cookiecutter.create_docker %}
[![Docker][bd1]][bd2]
{%- endif %}
{%- if cookiecutter.licence != 'Not open source' %}
[![Licence][bl1]][bl2]
{%- endif %}
{%- if cookiecutter.create_docs %}
[![Docs][bc1]][bc2]
{%- endif %}
[![Expand your project structure from atoms of code to galactic dimensions.][bp6]][bp7]

[![Contributions Welcome][bp8]][bp9]
[![Open issues][bg3]][bp10]
[![Merge Requests][bg4]][bg5]

[![Poetry][bp11]][bp12]
[![Bandit][bp13]][bp14]
[![Pre-commit][bp15]][bp16]
[![Editorconfig][bp17]][bp18]
{%- if cookiecutter.use_formatters %}
[![Code style: black][bf1]][bf2]
[![isort][bf3]][bf4]
{%- endif %}
{%- if cookiecutter.use_linters and cookiecutter.docstring_style in ['numpy', 'google', 'pep257'] %}
[![Docstrings][bs1]][bs2]
{%- endif %}

{%- if cookiecutter.licence != 'Not open source' %}
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OpenSSF Best Practices][bo1]][bo2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OSSRank][bo3]][bo4] -->

{%- endif %}
[![Semantic versions][bl3]][bp5]
[![Pipelines][bg6]][bg7]

{{ cookiecutter.project_description }}

</div>

## Very first steps

### Initialize your code

1. Initialize `git` inside your repo:

```bash
cd {{ cookiecutter.repo_name }} && git init
```

2. If you don't have `Poetry` installed run:

```bash
make poetry-download
```

> This installs Poetry as a [standalone application][t1]. If you prefer, you can simply install it inside your virtual environment.

3. Initialize Poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run the codestyle:

```bash
make codestyle
```

1. Upload initial code to {{ cookiecutter.scm_platform }}:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin {{ cookiecutter.__scm_base_url }}.git
git push -u origin main
```
{%- if cookiecutter.__scm_platform_lc == 'github' -%}
### Set up bots

- Set up [Dependabot][h1] to ensure you have the latest dependencies.
- Set up [Stale bot][h2] for automatic issue closing.
{%- endif %}

### Poetry

Want to know more about Poetry? Check [its documentation][t2].

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands][t3] are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc.
</p>
</details>

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions][t4] standard;
- Make a commit to `{{ cookiecutter.scm_platform }}`;
- Create a `{{ cookiecutter.scm_platform }} release`;
- And... publish :slightly_smiling_face: `poetry publish --build`

## :bullseye: What's next

Well, that's up to you :flexed_biceps:.

For further setting up your project:

- Look for files and sections marked with `UPDATEME`, these should be updated according to the needs and characteristics of your project;
  - **Tip:** If you use VS Code's [`Todo Tree`][t5] extension, you can even set a specific tag to quickly locate these marks. Update your `settings.json` with:

```json
"todo-tree.highlights.customHighlight": {
    "UPDATEME": {
        "icon": "pencil",
        "iconColour": "#E63946"
    }
},
"todo-tree.general.tags": [
    "BUG",
    "HACK",
    "FIXME",
    "UPDATEME",
    "TODO",
    "XXX",
    "[ ]"
]
```

- This template assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates so links won't break when you push them to your repo;
- Make sure to create your desired Issue labels on your platform before you start tracking them so it ensures you will be able to filter them from the get-go;
- Make changes to your CI configurations to better suit your needs.

If you want to put your project on steroids, here are a few Python tools which can help you depending on what you want to achieve with your application:

- [`Typer`][t6] is great for creating CLI applications;
- [`Rich`][t7] makes it easy to add beautiful formatting in the terminal;
- [`tqdm`][t8] is a fast, extensible progress bar for Python and CLI;
- [`Python Prompt Toolkit`][t9] allows you to create more advanced terminal applications, such as a text editor or even your own shell;
- [`orjson`][t10], an ultra fast JSON parsing library;
- [`Pydantic`][t11] is data validation and settings management using Python type hinting;
- [`Returns`][t12] makes you function's output meaningful, typed, and safe;
- [`Loguru`][t13] makes logging (stupidly) simple;
- [`IceCream`][t14] is a little library for sweet and creamy debugging;
- [`Hydra`][t15] is a framework for elegantly configuring complex applications;
- [`FastAPI`][t16] is a type-driven asynchronous web framework.

For taking development and exposition of your project to the next level:

- Try out some more badges, not only it looks good, but it also helps people better understand some intricate details on how your project works:
  - You can look at dynamic badges available at [`Shields.io`][t17];
  - There is a myriad of standardised static badges at [`Simple Badges`][t18];
  - [`awesome-badges`][t19] provides a lot of useful resources to help you deal with badges;
- Add your project to [`OpenSSF Best Practices`][t20] and [`OSSRank`][t21] indexes. If you have greater ambitions for your project and/or expects it to scale at some point, it's worth considering adding it to these trackers;
  - There are already badges for those set up in your `README.md` file, just waiting for you to update their URLs with your project's index in both services :beaming_face_with_smiling_eyes:
- Setup a code coverage service for your tests, popular options include:
  - [`Coveralls`][t22] and [`Codecov`][t23] if you need solely test coverage;
  - [`Code Climate`][t24] and [`Codacy`][t25] for fully-featured code analysis;
- Setup a sponsorship page and allow users and organisations who appreciate your project to help raise for its development (and add a badge in the process! :smiling_face_with_sunglasses:). Popular platforms are:
  - [`Liberapay`][t26];
  - [`Open Collective`][t27];
  - [`Ko-fi`][t28];
  - If you host on GitHub, you can set a [Sponsors account][t29] directly integrated into the platform;
  - Of course, you can also set any kind of gateway you wish, what works best for you and your project!

And here are a few articles which may help you:

- [Open Source Guides][t30];
- [A handy guide to financial support for open source][t31];
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
- [GitLab CI Documentation][l1];
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
- [GitHub Actions Documentation][h3];
{%- endif %}
- [Makefile tutorial][t32];
- Maybe you would like to add [gitmoji][t33] to commit names. This is really funny. :grinning_face_with_smiling_eyes:

## :rocket: Features

### Development features

- Support for `Python {{ cookiecutter.minimal_python_version }}` and higher;
- [`Poetry`][t34] as a dependencies manager. See configuration in [`pyproject.toml`][t35];
{%- if cookiecutter.use_formatters %}
- Automatic code formatting with [`black`][f1], [`isort`][f2] and [`pyupgrade`][f3], with ready-to-use [`pre-commit`][f4] hooks;
{%- endif %}
{%- if cookiecutter.use_linters %}
- Code and docstring linting with [`flake8`][s1]{% if cookiecutter.docstring_style not in ['pep257', 'dismiss'] %}, [`pydocstyle`][s2] and [`pydoclint`][s3]{% elif cookiecutter.docstring_style != 'dismiss' %} and [`pydocstyle`][s2]{% endif %};
{% endif %}
- Type checks with [`mypy`][t36], security checks with [`safety`][t37] and [`bandit`][t38];
- Testing with [`pytest`][t39];
- Ready-to-use [`.editorconfig`][t40]{% if cookiecutter.create_docker %}, [`.dockerignore`][d1]{% endif %} and [`.gitignore`][t41] files. You don't have to worry about those things.

### Deployment features

- Issue and {% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates for easy integration with {{ cookiecutter.scm_platform }};
- Predefined CI/CD build workflow for {% if cookiecutter.__scm_platform_lc == 'gitlab' %}[`GitLab CI`][l2]{% elif cookiecutter.__scm_platform_lc == 'github' %}[`Github Actions`][h4]{% endif %};
- Everything is already set up for security checks, {% if cookiecutter.use_formatters %}codestyle checks, code formatting,{% endif %} testing, linting{% if cookiecutter.create_docker %}, docker builds{% endif %} etc with [`Makefile`][t42]. More details in [makefile-usage][t43];
{%- if cookiecutter.create_docker %}
- [Dockerfile][d2] for your package;
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' -%}
- Automatic [`Changelog entries`][l3] updated via [GitLab API][l4] and [template][l5].
{%- elif cookiecutter.__scm_platform_lc == 'github' -%}
- Always up-to-date dependencies with [`Dependabot`][h5]. You will only need to [enable it][h1];
- Automatic drafts of new releases with [`Release Drafter`][h6]. You may see the list of labels in [`release-drafter.yml`][h7]. Works perfectly with [Semantic Versions][t4] specification.
{%- endif %}

### Open source community features

- Ready-to-use [{% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates][t44] and several [Issue templates][t45].
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically;
- **Loads** of predefined [badges][t46] to make your project stand out, you can either keep them, remove as you wish or be welcome to add even more{% if cookiecutter.__scm_platform_lc == 'github' %};{% else %}.{% endif %}
{%- if cookiecutter.__scm_platform_lc == 'github' %}
- [`Stale bot`][h2] closes abandoned issues after a period of inactivity. Configuration is [here][h8];
- [Semantic Versions][t4] specification with [`Release Drafter`][h6].
{%- endif %}

## Installation

```bash
pip install -U {{ cookiecutter.repo_name }}
```

or install with `Poetry`:

```bash
poetry add {{ cookiecutter.repo_name }}
```

{%- if cookiecutter.create_cli %}
Then you can run

```bash
{{ cookiecutter.repo_name }} --help
```

or with `Poetry`:

```bash
poetry run {{ cookiecutter.repo_name }} --help
```
{%- endif %}

### Makefile usage

[`Makefile`][t42] contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry as a [standalone application][t1] run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

Or you can install it with `pip` inside your virtual environment if you prefer.

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements with

```bash
make install
```

Pre-commit hooks could be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

{%- if cookiecutter.use_formatters %}
<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`, and can be run with

```bash
make codestyle

# or use synonym
make formatting
```

For codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

Update all dev libraries to the latest version using one command

```bash
make update-dev-deps
```

</p>
</details>
{%- endif %}

<details>
<summary>{% if cookiecutter.use_formatters %}4{% else %}3{% endif %}. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>{% if cookiecutter.use_formatters %}5{% else %}4{% endif %}. Type checks</summary>
<p>

Run `mypy` static type checker with

```bash
make mypy
```

</p>
</details>

<details>
<summary>{% if cookiecutter.use_formatters %}6{% else %}5{% endif %}. Tests with coverage badges</summary>
<p>

Run `pytest` with all essential parameters predefined with

```bash
make test
```

</p>
</details>

{%- if cookiecutter.use_linters %}
<details>
<summary>{% if cookiecutter.use_formatters %}7{% else %}6{% endif %}. Linters</summary>
<p>

Run code and docstring linters with `flake8`{% if cookiecutter.docstring_style not in ['pep257', 'dismiss'] %}, `pydocstyle` and `pydoclint`{% elif cookiecutter.docstring_style != 'dismiss' %} and `pydocstyle`{% endif %}.

```bash
make lint
```

</p>
</details>
{%- endif %}

<details>
<summary>{% if cookiecutter.use_formatters and cookiecutter.use_linters %}8{% elif cookiecutter.use_formatters or cookiecutter.use_linters %}7{% else %}6{% endif %}. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint-all
```

the same as:

```bash
make test && make check-codestyle && {% if cookiecutter.use_linters %}make lint && {% endif %}make mypy && make check-safety
```

</p>
</details>

{%- if cookiecutter.create_docker %}
<details>
<summary>{% if cookiecutter.use_formatters and cookiecutter.use_linters %}9{% elif cookiecutter.use_formatters or cookiecutter.use_linters %}8{% else %}7{% endif %}. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker][d3].

</p>
</details>
{%- endif %}

<details>
<summary>{% if cookiecutter.use_formatters and cookiecutter.use_linters %}10{% elif cookiecutter.use_formatters or cookiecutter.use_linters %}9{% else %}8{% endif %}. Cleanup</summary>
<p>

Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## :chart_increasing: Releases

You can see the list of available releases on the [{{ cookiecutter.scm_platform }} Releases][t47] page.

We follow [Semantic Versions][t4] specification.

{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
We use [`GitLab Changelog`][l4] entries to track changes. You can categorise commits and Merge Requests made to this project using [git trailers][l6] in your commit messages.
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
We use [`Release Drafter`][h6]. As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.
{%- endif %}

### List of {% if cookiecutter.__scm_platform_lc == 'gitlab' %}trailers and corresponding categories{% elif cookiecutter.__scm_platform_lc == 'github' %}labels and corresponding titles{% endif %}

{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
|            **Git trailer**            |    **Category in CHANGELOG**    |
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
|               **Label**               |      **Title in Releases**      |
{%- endif %}
| :-----------------------------------: | :-----------------------------: |
| `enhancement`, `feature`              | :rocket: Features               |
| `bug`, `refactoring`, `bugfix`, `fix` | :wrench: Fixes & Refactoring    |
| `build`, `ci`, `testing`              | :package: Build System & CI/CD  |
| `breaking`                            | :collision: Breaking Changes    |
| `documentation`                       | :memo: Documentation            |
| `dependencies`                        | :arrow_up: Dependencies updates |

{%- if cookiecutter.__scm_platform_lc == 'github' %}
You can update it in [`release-drafter.yml`][h7].

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

{%- endif %}
{%- if cookiecutter.licence != 'Not open source' %}
## :shield: Licence

[![Licence][bl1]][bl2]

This project is licenced under the terms of the `{{ cookiecutter.licence }}` licence. See [LICENCE][bl2] for more details.

{%- endif %}
## :page_with_curl: Citation

```bibtex
{% raw %}@misc{{% endraw %}{{ cookiecutter.project_name }},
  author = {% raw %}{{% endraw %}{{ cookiecutter.author }}{% raw %}}{% endraw %},
  title = {% raw %}{{% endraw %}{{ cookiecutter.project_description }}{% raw %}}{% endraw %},
  year = {% raw %}{{% endraw %}{% now 'utc', '%Y' %}{% raw %}}{% endraw %},
  publisher = {% raw %}{{% endraw %}{{ cookiecutter.scm_platform }}{% raw %}}{% endraw %},
  journal = {% raw %}{{% endraw %}{{ cookiecutter.scm_platform }} repository{% raw %}}{% endraw %},
  howpublished = {\url{https://github.com/{{ cookiecutter.scm_username }}/{{ cookiecutter.project_name }}{% raw %}}}{% endraw %}
}
```

## Credits [![Expand your project structure from atoms of code to galactic dimensions.][bp6]][bp7]

This project was generated with [`galactipy`][bp7].

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
[bp11]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[bp12]: https://python-poetry.org/
[bp13]: https://img.shields.io/badge/security-bandit-yellow?style=for-the-badge
[bp14]: https://bandit.readthedocs.io/en/latest/
[bp15]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[bp16]: {{ cookiecutter.__scm_link_url }}/blob/master/.pre-commit-config.yaml
[bp17]: https://img.shields.io/badge/Editor%20Config-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[bp18]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
{%+ if cookiecutter.licence != 'Not open source' %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[bl1]: https://img.shields.io/gitlab/license/{{ cookiecutter.scm_username}}/{{ cookiecutter.repo_name }}?style=for-the-badge
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[bl1]: https://img.shields.io/github/license/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge
{%- endif %}
[bl2]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE
[bl3]: https://img.shields.io/badge/%F0%9F%93%A6-semantic%20versions-4053D6?style=for-the-badge

<!-- UPDATEME by replacing `1` with your project's index at https://www.bestpractices.dev/en
[bo1]: https://img.shields.io/cii/level/1?style=for-the-badge&logo=linux-foundation&label=openssf%20best%20practices
[bo2]: https://www.bestpractices.dev/en/projects/1 -->
<!-- UPDATEME by replacing `1` with your project's index at https://ossrank.com/
[bo3]: https://shields.io/endpoint?url=https://ossrank.com/shield/1&style=for-the-badge
[bo4]: https://ossrank.com/p/1 -->
{%- endif %}

[t1]: https://github.com/python-poetry/install.python-poetry.org
[t2]: https://python-poetry.org/docs/
[t3]: https://python-poetry.org/docs/cli/#commands
[t4]: https://semver.org/
[t5]: https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree
[t6]: https://github.com/tiangolo/typer
[t7]: https://github.com/willmcgugan/rich
[t8]: https://github.com/tqdm/tqdm
[t9]: https://github.com/prompt-toolkit/python-prompt-toolkit
[t10]: https://github.com/ijl/orjson
[t11]: https://github.com/samuelcolvin/pydantic/
[t12]: https://github.com/dry-python/returns
[t13]: https://github.com/Delgan/loguru
[t14]: https://github.com/gruns/icecream
[t15]: https://github.com/facebookresearch/hydra
[t16]: https://github.com/tiangolo/fastapi
[t17]: https://shields.io/badges/static-badge
[t18]: https://badges.pages.dev/
[t19]: https://github.com/badges/awesome-badges
[t20]: https://www.bestpractices.dev/en
[t21]: https://ossrank.com/
[t22]: https://coveralls.io/
[t23]: https://about.codecov.io/
[t24]: https://codeclimate.com/velocity/what-is-velocity
[t25]: https://www.codacy.com/
[t26]: https://liberapay.com/
[t27]: https://opencollective.com/
[t28]: https://ko-fi.com/
[t29]: https://github.com/sponsors
[t30]: https://opensource.guide/
[t31]: https://github.com/nayafia/lemonade-stand
[t32]: https://makefiletutorial.com/
[t33]: https://gitmoji.carloscuesta.me/
[t34]: https://python-poetry.org/
[t35]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml
[t36]: https://mypy.readthedocs.io
[t37]: https://docs.safetycli.com/safety-2/
[t38]: https://bandit.readthedocs.io/en/latest/
[t39]: https://docs.pytest.org/en/latest/
[t40]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[t41]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitignore
[t42]: {{ cookiecutter.__scm_link_url }}/blob/master/Makefile
[t43]: #makefile-usage
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[t44]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/merge_request_templates/default.md
[t45]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/issue_templates
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[t44]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/PULL_REQUEST_TEMPLATE.md
[t45]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/ISSUE_TEMPLATE
{%- endif %}
[t46]: https://shields.io/
[t47]: {{ cookiecutter.__scm_link_url }}/releases

{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[bg1]: https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white
[bg2]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=FFCA28
[bg3]: https://img.shields.io/gitlab/issues/open/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=fca326
[bg4]: https://img.shields.io/gitlab/merge-requests/open/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=6fdac9
[bg5]: {{ cookiecutter.__scm_link_url }}/merge_requests
[bg6]: https://img.shields.io/gitlab/pipeline-status/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[bg7]: {{ cookiecutter.__scm_link_url }}/pipelines

[l1]: https://docs.gitlab.com/ee/ci/
[l2]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab-ci.yml
[l3]: {{ cookiecutter.__scm_link_url }}/blob/master/CHANGELOG.md
[l4]: https://docs.gitlab.com/ee/user/project/changelogs.html
[l5]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/changelog_config.yml
[l6]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[bg1]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[bg2]: https://img.shields.io/github/v/release/{{ cookiecutter.scm_username}}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=347d39
[bg3]: https://img.shields.io/github/issues/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=347d39
[bg4]: https://img.shields.io/github/issues-pr/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=347d39
[bg5]: {{ cookiecutter.__scm_link_url }}/pulls
[bg6]: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}/build.yml?style=for-the-badge&logo=github
[bg7]: {{ cookiecutter.__scm_link_url }}/actions/workflows/build.yml

[h1]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[h2]: https://github.com/marketplace/actions/close-stale-issues
[h3]: https://help.github.com/en/actions
[h4]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/workflows/build.yml
[h5]: https://docs.github.com/en/code-security/dependabot
[h6]: https://github.com/marketplace/actions/release-drafter
[h7]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/release-drafter.yml
[h8]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/.stale.yml
{%- endif %}
{%+ if cookiecutter.create_docker %}
[bd1]: https://img.shields.io/docker/v/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=docker&logoColor=lightblue&label=image&color=lightblue
[bd2]: https://hub.docker.com/r/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}

[d1]: {{ cookiecutter.__scm_link_url }}/blob/master/.dockerignore
[d2]: {{ cookiecutter.__scm_link_url }}/blob/master/docker/Dockerfile
[d3]: {{ cookiecutter.__scm_link_url }}/tree/master/docker
{%+ endif %}
{%- if cookiecutter.create_docs %}
[bc1]: https://img.shields.io/badge/docs-{{ cookiecutter.__scm_platform_lc }}%20pages-0a507a?style=for-the-badge
[bc2]: https://{{ cookiecutter.scm_username }}.{{ cookiecutter.__scm_platform_lc }}.io/{{ cookiecutter.repo_name }}
{%+ endif %}
{%- if cookiecutter.use_formatters %}
[bf1]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[bf2]: https://black.readthedocs.io/en/stable/
[bf3]: https://img.shields.io/badge/imports-isort-1674b1?style=for-the-badge&labelColor=ef8336
[bf4]: https://pycqa.github.io/isort/

[f1]: https://black.readthedocs.io/en/stable/
[f2]: https://pycqa.github.io/isort/
[f3]: https://github.com/asottile/pyupgrade
[f4]: https://pre-commit.com/
{%+ endif %}
{%- if cookiecutter.use_linters %}
{%- if cookiecutter.docstring_style == 'numpydoc' %}
[bs1]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
[bs2]: https://numpydoc.readthedocs.io/en/latest/format.html
{%- elif cookiecutter.docstring_style == 'google' %}
[bs1]: https://img.shields.io/badge/docstrings-google-ffbb00?style=for-the-badge&labelColor=00ac47
[bs2]: https://google.github.io/styleguide/pyguide.html
{%- elif cookiecutter.docstring_style == 'pep257' %}
[bs1]: https://img.shields.io/badge/docstrings-pep257-FFD43B?style=for-the-badge&labelColor=3776ab
[bs2]: https://peps.python.org/pep-0257/
{%- endif %}

[s1]: https://flake8.pycqa.org/en/latest/
{%- if cookiecutter.docstring_style != 'dismiss' %}
[s2]: http://www.pydocstyle.org/en/stable/
{%- elif cookiecutter.docstring_style != 'pep257' %}
[s3]: https://github.com/jsh9/pydoclint
{%- endif %}
{%+ endif %}
{%- if cookiecutter.use_linters and cookiecutter.docstring_style == 'numpydoc' %}
[bs1]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
[bs2]: https://numpydoc.readthedocs.io/en/latest/format.html
{%- elif cookiecutter.use_linters and cookiecutter.docstring_style == 'google' %}
[bs1]: https://img.shields.io/badge/docstrings-google-ffbb00?style=for-the-badge&labelColor=00ac47
[bs2]: https://google.github.io/styleguide/pyguide.html
{%- elif cookiecutter.use_linters and cookiecutter.docstring_style == 'pep257' %}
[bs1]: https://img.shields.io/badge/docstrings-pep257-FFD43B?style=for-the-badge&labelColor=3776ab
[bs2]: https://peps.python.org/pep-0257/
{%- endif %}
