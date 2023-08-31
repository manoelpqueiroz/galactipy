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

- Set up [Dependabot][18] to ensure you have the latest dependencies.
- Set up [Stale bot][19] for automatic issue closing.
{%- endif %}

### Poetry

Want to know more about Poetry? Check [its documentation][20].

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands][21] are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc
</p>
</details>

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions][22] standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

## 🎯 What's next

Well, that's up to you 💪🏻. I can only recommend the packages and articles that helped me.

- [`Typer`][23] is great for creating CLI applications.
- [`Rich`][24] makes it easy to add beautiful formatting in the terminal.
- [`Pydantic`][25] – data validation and settings management using Python type hinting.
- [`Loguru`][26] makes logging (stupidly) simple.
- [`tqdm`][27] – fast, extensible progress bar for Python and CLI.
- [`IceCream`][28] is a little library for sweet and creamy debugging.
- [`orjson`][29] – ultra fast JSON parsing library.
- [`Returns`][30] makes you function's output meaningful, typed, and safe!
- [`Hydra`][31] is a framework for elegantly configuring complex applications.
- [`FastAPI`][32] is a type-driven asynchronous web framework.

Articles:

- [Open Source Guides][33].
- [A handy guide to financial support for open source][34]
- [GitHub Actions Documentation][35].
- Maybe you would like to add [gitmoji][36] to commit names. This is really funny. 😄

## 🚀 Features

### Development features

- Supports for `Python {{ cookiecutter.minimal_python_version }}` and higher.
- [`Poetry`][37] as the dependencies manager. See configuration in [`pyproject.toml`][38] and [`setup.cfg`][39].
- Automatic codestyle with [`black`][40], [`isort`][41] and [`pyupgrade`][42].
- Ready-to-use [`pre-commit`][43] hooks with code-formatting.
- Type checks with [`mypy`][44]; docstring checks with [`darglint`][45]; security checks with [`safety`][46] and [`bandit`][47]
- Testing with [`pytest`][48].
- Ready-to-use [`.editorconfig`][49], [`.dockerignore`][50], and [`.gitignore`][51]. You don't have to worry about those things.

### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow][52] as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`][53]. More details in [makefile-usage][54].
- [Dockerfile][55] for your package.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' -%}
- Automatic [`CHANGELOG`][80] updated via [GitLab API][81] and [template][82].
{%- elif cookiecutter.__scm_platform_lc == 'github' -%}
- Always up-to-date dependencies with [`@dependabot`][56]. You will only [enable it][57].
- Automatic drafts of new releases with [`Release Drafter`][58]. You may see the list of labels in [`release-drafter.yml`][59]. Works perfectly with [Semantic Versions][60] specification.
{%- endif %}

### Open source community features

- Ready-to-use [Pull Requests templates][61] and several [Issue templates][62].
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
{%- if cookiecutter.__scm_platform_lc == 'github' %}
- [`Stale bot`][63] that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan][64]). Configuration is [here][65].
- [Semantic Versions][66] specification with [`Release Drafter`][67].
{%- endif %}

## Installation

```bash
pip install -U {{ cookiecutter.repo_name }}
```

or install with `Poetry`

```bash
poetry add {{ cookiecutter.repo_name }}
```

{%- if cookiecutter.create_example_template == 'cli' %}
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

[`Makefile`][68] contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

</p>
</details>

<details>
<summary>4. Code security</summary>
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
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
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

More information [about docker][69].

</p>
</details>

<details>
<summary>9. Cleanup</summary>
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

## 📈 Releases

You can see the list of available releases on the [GitHub Releases][70] page.

We follow [Semantic Versions][71] specification.

We use [`Release Drafter`][72]. As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`][73].

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 Licence

[![Licence][74]][75]

This project is licenced under the terms of the `{{ cookiecutter.licence }}` licence. See [LICENCE][76] for more details.

## 📃 Citation

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

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.][77]][78]

This project was generated with [`galactipy`][79]

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
[18]: https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates
[19]: https://github.com/apps/stale
[20]: https://python-poetry.org/docs/
[21]: https://python-poetry.org/docs/cli/#commands
[22]: https://semver.org/
[23]: https://github.com/tiangolo/typer
[24]: https://github.com/willmcgugan/rich
[25]: https://github.com/samuelcolvin/pydantic/
[26]: https://github.com/Delgan/loguru
[27]: https://github.com/tqdm/tqdm
[28]: https://github.com/gruns/icecream
[29]: https://github.com/ijl/orjson
[30]: https://github.com/dry-python/returns
[31]: https://github.com/facebookresearch/hydra
[32]: https://github.com/tiangolo/fastapi
[33]: https://opensource.guide/
[34]: https://github.com/nayafia/lemonade-stand
[35]: https://help.github.com/en/actions
[36]: https://gitmoji.carloscuesta.me/
[37]: https://python-poetry.org/
[38]: {{ cookiecutter.__scm_link_url }}/blob/master/pyproject.toml
[39]: {{ cookiecutter.__scm_link_url }}/blob/master/setup.cfg
[40]: https://github.com/psf/black
[41]: https://github.com/timothycrosley/isort
[42]: https://github.com/asottile/pyupgrade
[43]: https://pre-commit.com/
[44]: https://mypy.readthedocs.io
[45]: https://github.com/terrencepreilly/darglint
[46]: https://github.com/pyupio/safety
[47]: https://github.com/PyCQA/bandit
[48]: https://docs.pytest.org/en/latest/
[49]: {{ cookiecutter.__scm_link_url }}/blob/master/.editorconfig
[50]: {{ cookiecutter.__scm_link_url }}/blob/master/.dockerignore
[51]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitignore
<!-- apenas para GH -->
[52]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/workflows/build.yml
[53]: {{ cookiecutter.__scm_link_url }}/blob/master/Makefile#L89
[54]: #makefile-usage
[55]: {{ cookiecutter.__scm_link_url }}/blob/master/docker/Dockerfile
[56]: https://dependabot.com/
[57]: https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates
[58]: https://github.com/marketplace/actions/release-drafter
<!-- apenas para GH -->
[59]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/release-drafter.yml
[60]: https://semver.org/
<!-- condicional a depender da plataforma -->
[61]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/PULL_REQUEST_TEMPLATE.md
<!-- condicional a depender da plataforma -->
[62]: {{ cookiecutter.__scm_link_url }}/tree/master/.github/ISSUE_TEMPLATE
[63]: https://github.com/apps/stale
[64]: https://github.com/marketplace/stale
<!-- aepans para GH -->
[65]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/.stale.yml
[66]: https://semver.org/
[67]: https://github.com/marketplace/actions/release-drafter
[68]: {{ cookiecutter.__scm_link_url }}/blob/master/Makefile
[69]: {{ cookiecutter.__scm_link_url }}/tree/master/docker
[70]: {{ cookiecutter.__scm_link_url }}/releases
[71]: https://semver.org/
[72]: https://github.com/marketplace/actions/release-drafter
<!-- apenas para GH -->
[73]: {{ cookiecutter.__scm_link_url }}/blob/master/.github/release-drafter.yml
[74]: https://img.shields.io/{{ cookiecutter.__scm_platform_lc }}/license/{{ cookiecutter.scm_username }}/{{ cookiecutter.repo_name }}
[75]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE
[76]: {{ cookiecutter.__scm_link_url }}/blob/master/LICENCE
[77]: https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen
[78]: https://gitlab.com/manoelpqueiroz/galactipy
[79]: https://gitlab.com/manoelpqueiroz/galactipy
[80]: {{ cookiecutter.__scm_link_url }}/blob/master/CHANGELOG.md
[81]: https://docs.gitlab.com/ee/user/project/changelogs.html
[82]: {{ cookiecutter.__scm_link_url }}/blob/master/.gitlab/changelog_config.yml
