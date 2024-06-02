# {{ cookiecutter.project_name }}

<div align="center">

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
{%- if cookiecutter.create_docs %}
[![Docs][bdoc1]][bdoc2]
{%- endif %}
[![Expand your project structure from atoms of code to galactic dimensions.][bp6]][bp7]

[![Contributions Welcome][bp8]][bp9]
[![Open issues][bscm3]][bp10]
[![Merge Requests][bscm4]][bscm5]

[![Poetry][bp11]][bp12]
[![Bandit][bp13]][bp14]
[![Pre-commit][bp15]][bp16]
[![Editorconfig][bp17]][bp18]
{%- if cookiecutter.use_ruff %}
[![Code style: Ruff][bfo1]][bfo2]
[![isort][bfo3]][bfo4]
{%- endif %}
{%- if cookiecutter.use_ruff and cookiecutter.docstring_style in ['numpy', 'google', 'pep257'] %}
[![Docstrings][bli1]][bli2]
{%- endif %}
{%+ if cookiecutter.licence != 'nos' %}
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OpenSSF Best Practices][boss1]][boss2] -->
<!-- UPDATEME by toggling this comment off after replacing your project's index in both anchors below
[![OSSRank][boss3]][boss4] -->
{% endif +%}
[![Semantic versions][blic3]][bp5]
[![Pipelines][bscm6]][bscm7]

_{{ cookiecutter.project_description }}_

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

> This installs Poetry as a [standalone application][fs1]. If you prefer, install it through your distribution's package manager.

3. Initialize Poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run the codestyle:

```bash
make codestyle
```

5. Upload initial code to {{ cookiecutter.scm_platform }}:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin {{ cookiecutter.__scm_base_url }}.git
git push -u origin main
```
{%- if cookiecutter.__scm_platform_lc == 'github' -%}
### Set up bots

- Set up [Dependabot][hub1] to ensure you have the latest dependencies.
- Set up [Stale bot][hub2] for automatic issue closing.
{%- endif %}

### Poetry

Want to know more about Poetry? Check [its documentation][fs2].

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands][fs3] are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc.
</p>
</details>

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions][fs4] standard;
- Make a commit to `{{ cookiecutter.scm_platform }}`;
- Create a `{{ cookiecutter.scm_platform }} release`;
- And... publish :slight_smile: `poetry publish --build`

## :dart: What's next

Well, that's up to you. :muscle:

For further setting up your project:

- Look for files and sections marked with `UPDATEME`, these should be updated according to the needs and characteristics of your project;
  - **Tip:** If you use VS Code's [`Todo Tree`][wn1] extension, you can even set a specific tag to quickly locate these marks. Update your `settings.json` with:

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

- In order to reduce user prompts and keep things effective, the template generates files with a few assumptions:
  - It assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates and `README.md` file so links won't break when you push them to your repo;
  - It generates a PyPI badge assuming you will be able to publish your project under `{{ cookiecutter.repo_name }}`, change it otherwise;
{%- if cookiecutter.create_docker %}
  - It generates a Docker badge assuming you also use `{{ cookiecutter.scm_username }}` for Docker Hub and you will push your image under `{{ cookiecutter.repo_name }}`, change it otherwise;
{%- endif %}
- Make sure to create your desired Issue labels on your platform before you start tracking them so it ensures you will be able to filter them from the get-go;
- Make changes to your CI configurations to better suit your needs.

If you want to put your project on steroids, here are a few Python tools which can help you depending on what you want to achieve with your application:

- [`Typer`][wn2] is great for creating CLI applications;
- [`Rich`][wn3] makes it easy to add beautiful formatting in the terminal;
- [`tqdm`][wn4] is a fast, extensible progress bar for Python and CLI;
- [`Python Prompt Toolkit`][wn5] allows you to create more advanced terminal applications, such as a text editor or even your own shell;
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
- [GitLab CI Documentation][lab1];
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
- [GitHub Actions Documentation][hub3];
{%- endif %}
- [Makefile tutorial][wn22];
- [A Comprehensive Look at Testing in Software Development][wn23] is an article that lays out why testing is crucial for development success. Eric's blog is actually a great reference, covering topics ranging from the basics to advanced techniques and best practices;
- Maybe you would like to add [gitmoji][wn24] to commit names. This is really funny. :grin:

## :rocket: Features

### Development features

- Support for `Python {{ cookiecutter.minimal_python_version }}` and higher;
- [`Poetry`][ft1] as a dependencies manager. See configuration in [`pyproject.toml`][ft2];
{%- if cookiecutter.use_ruff %}
- Automatic code formatting with [`ruff`][fo1], with ready-to-use [`pre-commit`][fo2] hooks and several rules already selected for linting;
{%- endif %}
- Type checks with [`mypy`][ft3], security checks with [`safety`][ft4] and [`bandit`][ft5];
- Testing with [`pytest`][ft6];
- Ready-to-use [`.editorconfig`][ft7]{% if cookiecutter.create_docker %}, [`.dockerignore`][docker1]{% endif %} and [`.gitignore`][ft8] files. You don't have to worry about those things.

### Deployment features

- Issue and {% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates for easy integration with {{ cookiecutter.scm_platform }};
- Predefined CI/CD build workflow for {% if cookiecutter.__scm_platform_lc == 'gitlab' %}[`GitLab CI`][lab2]{% elif cookiecutter.__scm_platform_lc == 'github' %}[`Github Actions`][hub4]{% endif %};
- Everything is already set up for security checks, {% if cookiecutter.use_ruff %}codestyle checks, code formatting,{% endif %} testing, linting{% if cookiecutter.create_docker %}, docker builds{% endif %} etc with [`Makefile`][ft9]. More details in [makefile-usage][ft10];
{%- if cookiecutter.create_docker %}
- [`Dockerfile`][docker2] for your package;
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' -%}
- Automatic [`Changelog entries`][lab3] updated via [GitLab API][lab4] and [template][lab5].
{%- elif cookiecutter.__scm_platform_lc == 'github' -%}
- Always up-to-date dependencies with [`Dependabot`][hub5]. You will only need to [enable it][hub1];
- Automatic drafts of new releases with [`Release Drafter`][hub6]. You may see the list of labels in [`release-drafter.yml`][hub7]. Works perfectly with [Semantic Versions][fs4] specification.
{%- endif %}

### Open source community features

- Ready-to-use [{% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates][ft11] and several [Issue templates][ft12];
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically;
- **Loads** of predefined [badges][ft13] to make your project stand out, you can either keep them, remove as you wish or be welcome to add even more{% if cookiecutter.__scm_platform_lc == 'github' %};{% else %}.{% endif %}
{%- if cookiecutter.__scm_platform_lc == 'github' %}
- [`Stale bot`][hub2] closes abandoned issues after a period of inactivity. Configuration is [here][hub8];
- [Semantic Versions][fs4] specification with [`Release Drafter`][hub6].
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

[`Makefile`][ft9] contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry as a [standalone application][fs1] run:

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
{%+ if cookiecutter.use_ruff %}
<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `ruff`, and can be run with

```bash
make codestyle

# or use synonym
make formatting
```

For formatting checks only, without rewriting files:

```bash
make check-formatting
```

Update all dev libraries to the latest version using one command

```bash
make update-dev-deps
```

</p>
</details>
{% endif +%}
<details>
<summary>{% if cookiecutter.use_ruff %}4{% else %}3{% endif %}. Code security</summary>
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
<summary>{% if cookiecutter.use_ruff %}5{% else %}4{% endif %}. Type checks</summary>
<p>

Run `mypy` static type checker with

```bash
make mypy
```

</p>
</details>

<details>
<summary>{% if cookiecutter.use_ruff %}6{% else %}5{% endif %}. Tests</summary>
<p>

Run `pytest` with all essential parameters predefined with

```bash
make test
```

</p>
</details>
{%+ if cookiecutter.use_ruff %}
<details>
<summary>7. Linters</summary>
<p>

Run code and docstring linters with `ruff`.

```bash
make check-linter
```

</p>
</details>
{% endif +%}
<details>
<summary>{% if cookiecutter.use_ruff %}8{% else %}6{% endif %}. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint-all
```

the same as:

```bash
make test && {% if cookiecutter.use_ruff %}make check-linter && make check-formatting && {% endif %}make mypy && make check-safety
```

</p>
</details>
{%+ if cookiecutter.create_docker %}
<details>
<summary>{% if cookiecutter.use_ruff %}9{% else %}7{% endif %}. Docker</summary>
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

More information [about docker][docker3].

</p>
</details>
{% endif +%}
<details>
<summary>{% if cookiecutter.use_ruff and cookiecutter.create_docker %}10{% elif cookiecutter.use_ruff and not cookiecutter.create_docker %}9{% elif not cookiecutter.use_ruff and cookiecutter.create_docker %}8{% else %}7{% endif %}. Cleanup</summary>
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

## :chart_with_upwards_trend: Releases

You can see the list of available releases on the [{{ cookiecutter.scm_platform }} Releases][r1] page.

We follow [Semantic Versions][fs4] specification.
{%+ if cookiecutter.__scm_platform_lc == 'gitlab' %}
We use [`GitLab Changelog`][lab4] entries to track changes. You can categorise commits and Merge Requests made to this project using [git trailers][lab6] in your commit messages.
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
[bp11]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[bp12]: https://python-poetry.org/
[bp13]: https://img.shields.io/badge/security-bandit-yellow?style=for-the-badge
[bp14]: https://bandit.readthedocs.io/en/latest/
[bp15]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[bp16]: {{ cookiecutter.__scm_link_url }}/blob/master/.pre-commit-config.yaml
[bp17]: https://img.shields.io/badge/Editor%20Config-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[bp18]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
{%+ if cookiecutter.licence != 'nos' %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[blic1]: https://img.shields.io/gitlab/license/{{ cookiecutter.scm_username}}/{{ cookiecutter.repo_name }}?style=for-the-badge
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[blic1]: https://img.shields.io/github/license/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge
{%- endif %}
[blic2]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE
[blic3]: https://img.shields.io/badge/%F0%9F%93%A6-semantic%20versions-4053D6?style=for-the-badge

<!-- UPDATEME by replacing `1` with your project's index at https://www.bestpractices.dev/en
[boss1]: https://img.shields.io/cii/level/1?style=for-the-badge&logo=linux-foundation&label=openssf%20best%20practices
[boss2]: https://www.bestpractices.dev/en/projects/1 -->
<!-- UPDATEME by replacing `1` with your project's index at https://ossrank.com/
[boss3]: https://shields.io/endpoint?url=https://ossrank.com/shield/1&style=for-the-badge
[boss4]: https://ossrank.com/p/1 -->
{% endif +%}
[fs1]: https://github.com/python-poetry/install.python-poetry.org
[fs2]: https://python-poetry.org/docs/
[fs3]: https://python-poetry.org/docs/cli/#commands
[fs4]: https://semver.org/

[wn1]: https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree
[wn2]: https://github.com/tiangolo/typer
[wn3]: https://github.com/willmcgugan/rich
[wn4]: https://github.com/tqdm/tqdm
[wn5]: https://github.com/prompt-toolkit/python-prompt-toolkit
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
[wn22]: https://makefiletutorial.com/
[wn23]: https://pytest-with-eric.com/introduction/types-of-software-testing/
[wn24]: https://gitmoji.dev/
{%+ if cookiecutter.licence != 'nos' %}
[wno3]: https://liberapay.com/
[wno4]: https://opencollective.com/
[wno5]: https://ko-fi.com/
[wno6]: https://opensource.guide/
[wno7]: https://github.com/nayafia/lemonade-stand
{% endif %}
[ft1]: https://python-poetry.org/
[ft2]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml
[ft3]: https://mypy.readthedocs.io
[ft4]: https://docs.safetycli.com/safety-2/
[ft5]: https://bandit.readthedocs.io/en/latest/
[ft6]: https://docs.pytest.org/en/latest/
[ft7]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[ft8]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitignore
[ft9]: {{ cookiecutter.__scm_link_url }}/blob/master/Makefile
[ft10]: #makefile-usage
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[ft11]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/merge_request_templates/default.md
[ft12]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/issue_templates
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[ft11]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/PULL_REQUEST_TEMPLATE.md
[ft12]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/ISSUE_TEMPLATE
{%- endif %}
[ft13]: https://shields.io/

[r1]: {{ cookiecutter.__scm_link_url }}/releases
{%+ if cookiecutter.__scm_platform_lc == 'gitlab' %}
[bscm1]: https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white
[bscm2]: https://img.shields.io/gitlab/v/release/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=FFCA28
[bscm3]: https://img.shields.io/gitlab/issues/open/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=fca326
[bscm4]: https://img.shields.io/gitlab/merge-requests/open/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?style=for-the-badge&color=6fdac9
[bscm5]: {{ cookiecutter.__scm_link_url }}/merge_requests
[bscm6]: https://img.shields.io/gitlab/pipeline-status/{{ cookiecutter.scm_username }}%2F{{ cookiecutter.repo_name }}?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[bscm7]: {{ cookiecutter.__scm_link_url }}/pipelines

[lab1]: https://docs.gitlab.com/ee/ci/
[lab2]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab-ci.yml
[lab3]: {{ cookiecutter.__scm_link_url }}/blob/master/CHANGELOG.md
[lab4]: https://docs.gitlab.com/ee/user/project/changelogs.html
[lab5]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/changelog_config.yml
[lab6]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[bscm1]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[bscm2]: https://img.shields.io/github/v/release/{{ cookiecutter.scm_username}}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=semantic-release&color=347d39
[bscm3]: https://img.shields.io/github/issues/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=347d39
[bscm4]: https://img.shields.io/github/issues-pr/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&color=347d39
[bscm5]: {{ cookiecutter.__scm_link_url }}/pulls
[bscm6]: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}/build.yml?style=for-the-badge&logo=github
[bscm7]: {{ cookiecutter.__scm_link_url }}/actions/workflows/build.yml

[hub1]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[hub2]: https://github.com/marketplace/actions/close-stale-issues
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
[bdocker1]: https://img.shields.io/docker/v/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}?style=for-the-badge&logo=docker&logoColor=lightblue&label=image&color=lightblue
[bdocker2]: https://hub.docker.com/r/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}

[docker1]: {{ cookiecutter.__scm_link_url }}/blob/master/.dockerignore
[docker2]: {{ cookiecutter.__scm_link_url }}/blob/master/docker/Dockerfile
[docker3]: {{ cookiecutter.__scm_link_url }}/tree/master/docker
{%+ endif %}
{%- if cookiecutter.create_docs %}
[bdoc1]: https://img.shields.io/badge/docs-{{ cookiecutter.__scm_platform_lc }}%20pages-0a507a?style=for-the-badge
[bdoc2]: https://{{ cookiecutter.scm_username }}.{{ cookiecutter.__scm_platform_lc }}.io/{{ cookiecutter.repo_name }}
{%+ endif %}
{%- if cookiecutter.use_ruff %}
[bfo1]: https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge&labelColor=grey
[bfo2]: https://docs.astral.sh
[bfo3]: https://img.shields.io/badge/imports-isort-1674b1?style=for-the-badge&labelColor=ef8336
[bfo4]: https://pycqa.github.io/isort/

[fo1]: https://black.readthedocs.io/en/stable/
[fo2]: https://pre-commit.com/
{%+ endif %}
{%- if cookiecutter.use_ruff %}
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
{%- endif %}
