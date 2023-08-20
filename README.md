# Python Packages Project Generator

<div align="center">

[![Build status][1]][2]
[![Dependencies Status][3]][4]
[![🚀 Your next Python package needs a bleeding-edge project structure.][5]][6]

[![Code style: black][7]][8]
[![Pre-commit][9]][10]
[![Semantic Versions][11]][12]
[![Licence][13]][14]
![Coverage Report][15]

Your next Python package needs a bleeding-edge project structure.
</div>

## TL;DR

```bash
cookiecutter gl:manoelpqueiroz/galactipy --checkout v0.1.0
```

> All you need is the latest version of cookiecutter 😉

## 🚀 Features

In this [cookiecutter 🍪][16] template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.7` and higher.
- [`Poetry`][17] as a dependencies manager. See configuration in [`pyproject.toml`][18] and [`setup.cfg`][19].
- Automatic codestyle with [`black`][20], [`isort`][21] and [`pyupgrade`][22].
- Ready-to-use [`pre-commit`][23] hooks with code-formatting.
- Type checks with [`mypy`][24]; docstring checks with [`darglint`][25]; security checks with [`safety`][26] and [`bandit`][27]
- Testing with [`pytest`][28].
- Ready-to-use [`.editorconfig`][29], [`.dockerignore`][30], and [`.gitignore`][31]. You don't have to worry about those things.

### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow][32] as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`][33]. More details in [makefile-usage][34].
- [Dockerfile][35] for your package.
- Always up-to-date dependencies with [`@dependabot`][36]. You only need to [enable it][37].
- Automatic release notes with [`Release Drafter`][38]. You may see the list of labels in [`release-drafter.yml`][39]. Works perfectly with [Semantic Versions][40] specification.

### Open source community features

- Ready-to-use [Pull Requests templates][41] and several [Issue templates][42].
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`][43] that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan][44]). Configuration is [here][45].
- [Semantic Versions][46] specification with [`Release Drafter`][47].

## 🤯 How to use it

### Installation

To begin using the template consider updating `cookiecutter`

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gh:TezRomacH/python-package-template --checkout v1.1.1
```

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|     **Parameter**     |      **Default value**      | **Description**                                                                                                                                                               |
|:---------------------:|:---------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`           | `python-project`            | [Check the availability of possible name][48] before creating the project. |
| `project_description`    | based on the `project_name` | Brief description of your project. |
| `organization`           | based on the `project_name` | Name of the organization. We need to generate LICENCE and to specify ownership in `pyproject.toml`. |
| `licence`                | `MIT`                       | One of `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`. |
| `minimal_python_version` | `3.7`                       | Minimal Python version. One of `3.7`, `3.8` and `3.9`. It is used for builds, GitHub workflow and formatters (`black`, `isort` and `pyupgrade`). |
| `scm_username`            | based on the `organization` | GitHub or GitLab username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for GitHub. |
| `email`                  | based on the `organization` | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
| `version`                | `0.1.0`                     | Initial version of the package. Make sure it follows the [Semantic Versions][49] specification. |
| `line_length`            | 88                         | The max length per line (used for codestyle with `black` and `isort`). NOTE: This value must be between 50 and 300. |
| `create_example_template` | `cli`                      | If `cli` is chosen generator will create simple CLI application with [`Typer`][50] and [`Rich`][51] libraries. One of `cli`, `none` |

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. 😉

#### Demo

[![Demo of github.com/TezRomacH/python-package-template][52]][53]

### More details

Your project will contain `README.md` file with instructions for development, deployment, etc. You can read [the project README.md template][54] before.

### Initial set up

#### Initialize `poetry`

By running `make install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project][55].

#### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.

### Package example

Want to know more about Poetry? Check [its documentation][56].

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands][57] are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc
</p>
</details>

#### CLI example

If you set `create_example_template` to be `cli` the template comes with a cute little CLI application example. It utilises [`Typer`][58] and [`Rich`][59] for CLI input validation and beautiful formatting in the terminal.

After installation via `make install` (preferred) or `poetry install` you can try to play with the example:

```bash
poetry run <project_name> --help
```

```bash
poetry run <project_name> --name Roman
```

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions][60] standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

### Makefile usage

[`Makefile`][61] contains a lot of functions for faster development.

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

More information [about docker][62].

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

## 🎯 What's next

Well, that's up to you 💪🏻. I can only recommend the packages and articles that helped me.

- [`Typer`][63] is great for creating CLI applications.
- [`Rich`][64] makes it easy to add beautiful formatting in the terminal.
- [`Pydantic`][65] – data validation and settings management using Python type hinting.
- [`Loguru`][66] makes logging (stupidly) simple.
- [`tqdm`][67] – fast, extensible progress bar for Python and CLI.
- [`IceCream`][68] is a little library for sweet and creamy debugging.
- [`orjson`][69] – ultra fast JSON parsing library.
- [`Returns`][70] makes you function's output meaningful, typed, and safe!
- [`Hydra`][71] is a framework for elegantly configuring complex applications.
- [`FastAPI`][72] is a type-driven asynchronous web framework.

Articles:

- [Open Source Guides][73].
- [A handy guide to financial support for open source][74]
- [GitHub Actions Documentation][75].
- Maybe you would like to add [gitmoji][76] to commit names. This is really funny. 😄

## 📈 Releases

You can see the list of available releases on the [GitHub Releases][77] page.

We follow [Semantic Versions][78] specification.

We use [`Release Drafter`][79]. As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
|:-------------------------------------:|:----------------------:|
| `enhancement`, `feature`              | 🚀 Features             |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
| `build`, `ci`, `testing`              | 📦 Build System & CI/CD |
| `breaking`                            | 💥 Breaking Changes     |
| `documentation`                       | 📝 Documentation        |
| `dependencies`                        | ⬆️ Dependencies updates |

## 🧪 TODOs

This template will continue to develop and follow the bleeding edge new tools and best practices to improve the Python development experience.

Here is a list of things that have yet to be implemented:

- Tests coverage reporting ([`Codecov`][80] ?).
- Auto uploading your package to [`PyPI`][81] when new GitHub release is created.
- Automatic creation and deployment of documentation to GitHub pages. I look at [`MkDocs`][82] with [Material Design theme][83] and [`mkdocstrings`][84].
- Code metrics with [`Radon`][85].
- Docstring coverage with [`interrogate`][86]
- `Dockerfile` linting with [`dockerfilelint`][87].
- [Hall of fame][88] from `Sourcerer`.
- Some advanced Python linting (?).
- End-to-end testing and validation of the cookiecutter template.
- Add [`Invoke`][89]
- Add [`Earthly`][90]

## 🛡 Licence

[![Licence][91]][92]

This project is licenced under the terms of the `MIT` licence. See [LICENCE][93] for more details.

## 🏅 Acknowledgements

This template was inspired by several great articles:

- [Hypermodern Python][94]
- [Ultimate Setup for Your Next Python Project][95]
- [Nine simple steps for better-looking python code][96]
- [Modern Python developer's toolkit][97]

and repositories:

- [`Cookiecutter`][98]
- [`wemake-python-package`][99]
- [Audreyr's `cookiecutter-pypackage`][100]
- [Full Stack FastAPI and PostgreSQL - Base Project Generator][101]
- [Cookiecutter Data Science Template: `cdst`][102]

Give them your ⭐️, these resources are amazing! 😉

## 📃 Citation

```bibtex
@misc{galactipy,
  author = {Manoel Pereira de Queiroz},
  title = {Galactipy Python Package Project Generator},
  year = {2023},
  publisher = {GitLab},
  journal = {GitLab repository},
  howpublished = {\url{https://gitlab.com/manoelpqueiroz/galactipy}}
}
```

Markdown source for the badge [![🚀 Your next Python package needs a bleeding-edge project structure.][103]][104]

```markdown
[![🚀 Your next Python package needs a bleeding-edge project structure.][105]][106]
```

[1]: https://github.com/TezRomacH/python-package-template/workflows/build/badge.svg?branch=master&event=push
[2]: https://github.com/TezRomacH/python-package-template/actions?query=workflow%3Abuild
[3]: https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg
[4]: https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot
[5]: https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen
[6]: https://github.com/TezRomacH/python-package-template
[7]: https://img.shields.io/badge/code%20style-black-000000.svg
[8]: https://github.com/psf/black
[9]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[10]: https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml
[11]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg
[12]: https://github.com/TezRomacH/python-package-template/releases
[13]: https://img.shields.io/github/license/TezRomacH/python-package-template
[14]: https://github.com/TezRomacH/python-package-template/blob/master/LICENCE
[15]: ./assets/images/coverage.svg
[16]: https://github.com/cookiecutter/cookiecutter
[17]: https://python-poetry.org/
[18]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/pyproject.toml
[19]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/setup.cfg
[20]: https://github.com/psf/black
[21]: https://github.com/timothycrosley/isort
[22]: https://github.com/asottile/pyupgrade
[23]: https://pre-commit.com/
[24]: https://mypy.readthedocs.io
[25]: https://github.com/terrencepreilly/darglint
[26]: https://github.com/pyupio/safety
[27]: https://github.com/PyCQA/bandit
[28]: https://docs.pytest.org/en/latest/
[29]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.editorconfig
[30]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.dockerignore
[31]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitignore
[32]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/workflows/build.yml
[33]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile#L89
[34]: #makefile-usage
[35]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker/Dockerfile
[36]: https://dependabot.com/
[37]: https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates
[38]: https://github.com/marketplace/actions/release-drafter
[39]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/release-drafter.yml
[40]: https://semver.org/
[41]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/PULL_REQUEST_TEMPLATE.md
[42]: https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/ISSUE_TEMPLATE
[43]: https://github.com/apps/stale
[44]: https://github.com/marketplace/stale
[45]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/.stale.yml
[46]: https://semver.org/
[47]: https://github.com/marketplace/actions/release-drafter
[48]: http://ivantomic.com/projects/ospnc/
[49]: https://semver.org/
[50]: https://github.com/tiangolo/typer
[51]: https://github.com/willmcgugan/rich
[52]: https://asciinema.org/a/422052.svg
[53]: https://asciinema.org/a/422052
[54]: https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D
[55]: https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D#very-first-steps
[56]: https://python-poetry.org/docs/
[57]: https://python-poetry.org/docs/cli/#commands
[58]: https://github.com/tiangolo/typer
[59]: https://github.com/willmcgugan/rich
[60]: https://semver.org/
[61]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile
[62]: https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker
[63]: https://github.com/tiangolo/typer
[64]: https://github.com/willmcgugan/rich
[65]: https://github.com/samuelcolvin/pydantic/
[66]: https://github.com/Delgan/loguru
[67]: https://github.com/tqdm/tqdm
[68]: https://github.com/gruns/icecream
[69]: https://github.com/ijl/orjson
[70]: https://github.com/dry-python/returns
[71]: https://github.com/facebookresearch/hydra
[72]: https://github.com/tiangolo/fastapi
[73]: https://opensource.guide/
[74]: https://github.com/nayafia/lemonade-stand
[75]: https://help.github.com/en/actions
[76]: https://gitmoji.carloscuesta.me/
[77]: https://github.com/TezRomacH/python-package-template/releases
[78]: https://semver.org/
[79]: https://github.com/marketplace/actions/release-drafter
[80]: https://github.com/marketplace/codecov
[81]: https://pypi.org/
[82]: https://www.mkdocs.org/
[83]: https://github.com/squidfunk/mkdocs-material
[84]: https://github.com/pawamoy/mkdocstrings
[85]: https://github.com/rubik/radon
[86]: https://github.com/econchick/interrogate
[87]: https://github.com/replicatedhq/dockerfilelint
[88]: https://github.com/sourcerer-io/hall-of-fame
[89]: http://www.pyinvoke.org/
[90]: https://earthly.dev/
[91]: https://img.shields.io/github/license/TezRomacH/python-package-template
[92]: https://github.com/TezRomacH/python-package-template/blob/master/LICENCE
[93]: https://github.com/TezRomacH/python-package-template/blob/master/LICENCE
[94]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[95]: https://martinheinz.dev/blog/14
[96]: https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf
[97]: https://pycon.switowski.com/
[98]: https://github.com/cookiecutter/cookiecutter
[99]: https://github.com/wemake-services/wemake-python-package
[100]: https://github.com/audreyr/cookiecutter-pypackage
[101]: https://github.com/tiangolo/full-stack-fastapi-postgresql
[102]: https://github.com/crplab/cdst
[103]: https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen
[104]: https://github.com/TezRomacH/python-package-template
[105]: https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen
[106]: https://github.com/TezRomacH/python-package-template
