# {{ cookiecutter.project_name }}

<div align="center">

[![Build status][1]][2]
[![Python Version][3]][4]
[![Dependencies Status][5]][6]

[![Code style: black][7]][8]
[![Security: bandit][9]][10]
[![Pre-commit][11]][12]
[![Semantic Versions][13]][14]
[![Licence][15]][16]
![Coverage Report][17]

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
  - **Tip:** If you use VS Code's [Todo Tree][t5] extension, you can even set a specific tag to quickly locate these marks;
- This template assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates so links won't break when you push them to your repo;
- Make sure to create your desired Issue labels on your platform so it ensures you will start tracking them accordingly.

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

And here are a few articles which may help you:

- [Open Source Guides][t17];
- [A handy guide to financial support for open source][t18];
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
- [GitLab CI Documentation][l1];
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
- [GitHub Actions Documentation][h3];
{%- endif %}
- [Makefile tutorial][t19];
- Maybe you would like to add [gitmoji][t20] to commit names. This is really funny. :grinning_face_with_smiling_eyes:

## :rocket: Features

### Development features

- Support for `Python {{ cookiecutter.minimal_python_version }}` and higher;
- [`Poetry`][t21] as a dependencies manager. See configuration in [`pyproject.toml`][t22];
{%- if cookiecutter.use_formatters %}
- Automatic code formatting with [`black`][f1], [`isort`][f2] and [`pyupgrade`][f3], with ready-to-use [`pre-commit`][f4] hooks;
{%- endif %}
{%- if cookiecutter.use_linters %}
- Code and docstring linting with [`flake8`][s1]{% if cookiecutter.docstring_style not in ['pep257', 'dismiss'] %}, [`pydocstyle`][s2] and [`pydoclint`][s3]{% elif cookiecutter.docstring_style != 'dismiss' %} and [`pydocstyle`][s2]{% endif %};
{% endif %}
- Type checks with [`mypy`][t23], security checks with [`safety`][t24] and [`bandit`][t25];
- Testing with [`pytest`][t26];
- Ready-to-use [`.editorconfig`][t27]{% if cookiecutter.create_docker %}, [`.dockerignore`][d1]{% endif %} and [`.gitignore`][t28] files. You don't have to worry about those things.

### Deployment features

- Issue and {% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates for easy integration with {{ cookiecutter.scm_platform }};
- Predefined CI/CD build workflow for {% if cookiecutter.__scm_platform_lc == 'gitlab' %}[`GitLab CI`][l2]{% elif cookiecutter.__scm_platform_lc == 'github' %}[`Github Actions`][h4]{% endif %};
- Everything is already set up for security checks, {% if cookiecutter.use_formatters %}codestyle checks, code formatting,{% endif %} testing, linting{% if cookiecutter.create_docker %}, docker builds{% endif %} etc with [`Makefile`][t29]. More details in [makefile-usage][t30];
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

- Ready-to-use [{% if cookiecutter.__scm_platform_lc == 'github' %}Pull{% else %}Merge{% endif %} Request templates][t31] and several [Issue templates][t32].
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically{% if cookiecutter.__scm_platform_lc == 'github' %};{% else %}.{% endif %}
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

[`Makefile`][t29] contains a lot of functions for faster development.

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

You can see the list of available releases on the [{{ cookiecutter.scm_platform }} Releases][t33] page.

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
## :shield: Licence

[![Licence][t34]][t35]

This project is licenced under the terms of the `{{ cookiecutter.licence }}` licence. See [LICENCE][t35] for more details.

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

## Credits [![:rocket: Your next Python package needs a bleeding-edge project structure.][t36]][t37]

This project was generated with [`galactipy`][t37]

<!-- apenas para GH -->
[1]: {{ cookiecutter.__scm_link_url }}/workflows/build/badge.svg?branch=master&event=push
<!-- apenas para GH -->
[2]: {{ cookiecutter.__scm_link_url }}/actions?query=workflow%3Abuild
[3]: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg
[4]: https://pypi.org/project/{{ cookiecutter.repo_name }}/
[5]: https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg
<!-- apenas para GH -->
[6]: {{ cookiecutter.__scm_link_url }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot
[7]: https://img.shields.io/badge/code%20style-black-000000.svg
[8]: https://github.com/psf/black
[9]: https://img.shields.io/badge/security-bandit-green.svg
[10]: https://github.com/PyCQA/bandit
[11]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[12]: {{ cookiecutter.__scm_link_url }}/blob/master/.pre-commit-config.yaml
[13]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg
[14]: {{ cookiecutter.__scm_link_url }}/releases
[15]: https://img.shields.io/{{ cookiecutter.__scm_platform_lc }}/license/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}
[16]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE
[17]: ./assets/images/coverage.svg

[t1]: https://github.com/python-poetry/install.python-poetry.org
[t2]: https://python-poetry.org/docs/
[t3]: https://python-poetry.org/docs/cli/#commands
[t4]: https://semver.org/
[t5]: https://github.com/Gruntfuggly/todo-tree
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
[t17]: https://opensource.guide/
[t18]: https://github.com/nayafia/lemonade-stand
[t19]: https://makefiletutorial.com/
[t20]: https://gitmoji.carloscuesta.me/
[t21]: https://python-poetry.org/
[t22]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml
[t23]: https://mypy.readthedocs.io
[t24]: https://docs.safetycli.com/safety-2/
[t25]: https://bandit.readthedocs.io/en/latest/
[t26]: https://docs.pytest.org/en/latest/
[t27]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[t28]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitignore
[t29]: {{ cookiecutter.__scm_link_url }}/blob/master/Makefile
[t30]: #makefile-usage
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[t31]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/merge_request_templates/default.md
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[t31]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/PULL_REQUEST_TEMPLATE.md
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[t32]: {{ cookiecutter.__scm_link_url }}/tree/master/.gitlab/issue_templates
{%- elif cookiecutter.__scm_platform_lc == 'github' %}
[t32]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/ISSUE_TEMPLATE
{%- endif %}
[t33]: {{ cookiecutter.__scm_link_url }}/releases
[t34]: https://img.shields.io/{{ cookiecutter.__scm_platform_lc }}/license/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}
[t35]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE
[t36]: https://img.shields.io/badge/galactipy-%F0%9F%9A%80-brightgreen
[t37]: https://gitlab.com/manoelpqueiroz/galactipy

{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[l1]: https://docs.gitlab.com/ee/ci/
[l2]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab-ci.yml
[l3]: {{ cookiecutter.__scm_link_url }}/blob/master/CHANGELOG.md
[l4]: https://docs.gitlab.com/ee/user/project/changelogs.html
[l5]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/changelog_config.yml
[l6]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
{%- endif %}

{%- if cookiecutter.__scm_platform_lc == 'github' %}
[h1]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[h2]: https://github.com/marketplace/actions/close-stale-issues
[h3]: https://help.github.com/en/actions
[h4]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/workflows/build.yml
[h5]: https://docs.github.com/en/code-security/dependabot
[h6]: https://github.com/marketplace/actions/release-drafter
[h7]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/release-drafter.yml
[h8]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/.stale.yml
{%- endif %}

{%- if cookiecutter.create_docker %}
[d1]: {{ cookiecutter.__scm_link_url }}/blob/master/.dockerignore
[d2]: {{ cookiecutter.__scm_link_url }}/blob/master/docker/Dockerfile
[d3]: {{ cookiecutter.__scm_link_url }}/tree/master/docker
{%- endif %}

{%- if cookiecutter.use_formatters %}
[f1]: https://black.readthedocs.io/en/stable/
[f2]: https://pycqa.github.io/isort/
[f3]: https://github.com/asottile/pyupgrade
[f4]: https://pre-commit.com/
{%- endif %}

{%- if cookiecutter.use_linters %}
[s1]: https://flake8.pycqa.org/en/latest/
{%- elif cookiecutter.docstring_style != 'dismiss' %}
[s2]: http://www.pydocstyle.org/en/stable/
{%- endif %}
{%- if cookiecutter.docstring_style not in ['pep257', 'dismiss'] %}
[s3]: https://github.com/jsh9/pydoclint
{%- endif %}
{%- endif %}
