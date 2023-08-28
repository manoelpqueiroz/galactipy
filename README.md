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

> All you need is the latest version of cookiecutter! 😉

## 🚀 Features

In this [cookiecutter 🍪][16] template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.8` and higher;
- [`Poetry`][17] as a dependencies manager. See configuration in [`pyproject.toml`][18];
- Automatic code formatting with [`black`][20], [`isort`][21] and [`pyupgrade`][22], with ready-to-use [`pre-commit`][23] hooks;
- Code and docstring linting with [`flake8`][105], [`pydocstyle`][106] and [`pydoclint`][107];
- Type checks with [`mypy`][24], security checks with [`safety`][26] and [`bandit`][27];
- Testing with [`pytest`][28];
- Ready-to-use [`.editorconfig`][29], [`.dockerignore`][30], and [`.gitignore`][31] files. You don't have to worry about those things.

### Deployment features

- Issue and Merge Request templates for easy integration with `GitLab` and `GitHub`;
- Predefined CI/CD build workflow for [`GitLab CI`][111] and [`Github Actions`][32];
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds etc. with [`Makefile`][33]. More details in [makefile-usage][34];
- [Dockerfile][35] for your package.

#### GitLab vs. GitHub features

You are free to choose whichever platform works best for you and your project. The original template by [TezRomacH][104] was created originally with GitHub in mind, which prompted the creation of a similarly fully-featured template for GitLab users as well.

However, not everything that is available for GitHub users is available to GitLab users, and vice-versa. Please mind the differences between both options.

Below is a comparison between the features available in this package depending on which platform you choose to host your project:

|    **Feature** | **GitLab** | **GitHub** | **Observations** |
|:--------------:|:----------:|:----------:|------------------|
| Issue templates | ✅ | ✅ | Both options feature automatic labels, but GitHub has an extra configuration to prevent the creation of empty issues. |
| Merge/pull requests templates | ✅ | ✅ | |
| Stale issues | ❌ | ✅ | A specific configuration is available for GitHub to mark and automatically close stale issues. |
| Build workflow  | ✅ | ✅ | A basic workflow to install the package and run tests, check codestyle and safety. |
| Greetings workflow | ❌ | ✅ | |
| Dependabot | ❌ | ✅ | [Dependabot][36] is a feature now incorporated into GitHub Security. See [here][37] how to enable it. |
| Release drafter | ❌ | ✅ | [Release Drafter][38] is a custom workflow available on GitHub Marketplace. You may see the list of labels in [`release-drafter.yml`][39]. Works perfectly with [Semantic Versions][40] specification. |
| Changelog configuration | ✅ | ❌ | GitLab provides automatic changelog updates through their [API][110]. You may modify the template in [`changelog_config.yml`][112]. |

### Open source community features

- Ready-to-use [Pull Requests templates][41] and several [Issue templates][42];
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically;
- For GitHub users, [`Stale bot`][43] closes abandoned issues after a period of inactivity (You will only [need to setup free plan][44]). Configuration is [here][45];
- [Semantic Versions][46] specification with [`Release Drafter`][47].

## 🤯 How to use it

### Installation

To begin using the template consider updating `cookiecutter`.

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gl:manoelpqueiroz/galactipy --checkout v0.1.0
```

### Input variables

Template generator will ask you to fill some variables. The input variables, with their default values, are as follows:

|       **Parameter**       |      **Default value**      | **Description**                                                                                                                                                |
|:-------------------------:|:---------------------------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`            | `Python Project`            | [Check the availability of possible names][48] before creating the project. |
| `repo_name`               | based on `project_name`     | Name of the repository to develop the project on. [Check the availability of possible names][48] before creating the project. |
| `package_name`            | based on `project_name`     | PyPI-compliant Python package name. [Check the availability of possible names][48] before creating the project. |
| `project_description`     | based on `project_name`     | A brief description of your project. |
| `version`                 | `0.1.0`                     | Initial version of the package. Make sure it follows the [Semantic Versions][49] specification. |
| `author`                  | `Manoel Pereira de Queiroz` | Name of the author or organisation. Used to generate `LICENCE` and to specify ownership in `pyproject.toml`. |
| `scm_platform`            | `gitlab`                    | One of `gitlab` and `github`. Depending on the choice you will have [different features][109] to work with. |
| `scm_username`            | `manoelpqueiroz`            | GitHub or GitLab username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for either platform. |
| `email`                   | based on `scm_username`     | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
| `licence`                 | `MIT`                       | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `GNU AGLP v3.0`, `GNU LGPL v3.0`, `Mozilla Public License 2.0` and `Apache Software License 2.0`, or `Not open source`. |
| `minimal_python_version`  | `3.8`                       | Minimal Python version. All versions since `3.8` are available to choose. It is used for builds, pipelines and formatters (`black`, `isort` and `pyupgrade`). |
| `use_formatters`          | `True`                      | Option to use code formatters [`black`][20], [`isort`][21] and [`pyupgrade`][22] as pre-commit hooks. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `line_length`             | 88                          | The max length per line, dismiss if `use_formatters` is not used. NOTE: This value must be between 50 and 300. |
| `use_linters`             | `True`                      | Option to use linters [`flake8`][105] and [`pydocstyle`][106]. Depending on the value of `docstring_style`, will also use [`pydoclint`][107]. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `docstring_style`         | `numpy`                     | One of `numpy`, `pep257` or `google`, dismiss if `use_linters` is not used. You can choose `other` to disable `pydoclint` and checks on your docstrings. |
| `create_example_template` | `cli`                       | If `cli` is chosen generator will create simple CLI application with [`Typer`][50] and [`Rich`][51] libraries. One of `cli`, `none`. |
| `create_docker`           | `True`                      | Option to create a [Dockerfile][1] to build an image for your project. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `create_docs`             | `True`                      | Option to create documentation files with [Sphinx][1]. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |

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
poetry run <repo_name> --help
```

```bash
poetry run <repo_name> --name Manoel
```

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions][60] standard;
- Make a commit to `GitLab` or `GitHub`, depending on where you are hosting your code;
- Create a `Release` for your package on the platform;
- And... publish 🙂 `poetry publish --build`.

### Makefile usage

[`Makefile`][61] contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry as a [standalone application][113] run:

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

Run `mypy` static type checker with

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest` with all essential parameters predefined with

```bash
make test
```

</p>
</details>

<details>
<summary>7. Linters</summary>
<p>

Run code and docstring linters with `flake8`, `pydocstyle` and, if you choose `numpy` or `google` style, `pydoclint`.

```bash
make lint
```

</p>
</details>

<details>
<summary>8. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint-all
```

the same as:

```bash
make test && make check-codestyle && make lint && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>9. Docker</summary>
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
<summary>10. Cleanup</summary>
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

Well, that's up to you 💪🏻.

For further setting up your project:

- Look for files and sections marked with `UPDATEME`, these should be updated according to the needs and characteristics of your project;
  - **Tip:** If you use VS Code's [Todo Tree][117] extension, you can even set a specific tag to quickly locate these marks;
- This template assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates so links won't break when you push them to your repo;
- Make sure to create your desired Issue labels on your platform so it ensures you will start tracking them accordingly.

If you want to put your project on steroids, here are a few Python tools which can help you depending on what you want to achieve with your application:

- [`Typer`][63] is great for creating CLI applications. If you chose to generate a CLI example during the Cookiecutter setup, `Typer` will already be among your dependencies;
- [`Rich`][64] makes it easy to add beautiful formatting in the terminal. If you chose to generate a CLI example during the Cookiecutter setup, `Rich` will already be among your dependencies;
- [`tqdm`][67] is a fast, extensible progress bar for Python and CLI;
- [`Python Prompt Toolkit`][116] allows you to create more advanced terminal applications, such as a text editor or even your own shell;
- [`orjson`][69], an ultra fast JSON parsing library;
- [`Pydantic`][65] is data validation and settings management using Python type hinting;
- [`Returns`][70] makes you function's output meaningful, typed, and safe;
- [`Loguru`][66] makes logging (stupidly) simple;
- [`IceCream`][68] is a little library for sweet and creamy debugging;
- [`Hydra`][71] is a framework for elegantly configuring complex applications;
- [`FastAPI`][72] is a type-driven asynchronous web framework.

And here are a few articles which may help you:

- [Open Source Guides][73].
- [A handy guide to financial support for open source][74]
- [GitHub Actions Documentation][75].
- Maybe you would like to add [gitmoji][76] to commit names. This is really funny. 😄

## 📈 Releases

You can see the list of available releases on the [GitLab Releases][77] page.

We follow [Semantic Versions][78] specification.

## 🧪 TODOs

This template will continue to develop and follow the bleeding edge new tools and best practices to improve the Python development experience.

Here is a list of things that have yet to be implemented:

- Tests coverage reporting with [`Coveralls`][80];
- Auto uploading your package to [`PyPI`][81] when new release is created;
- Automatic creation of documentation. We will be using [`Sphinx`][114] with [Furo][115] design;
- Code metrics with [`Radon`][85];
- Docstring coverage with [`interrogate`][86];
- `Dockerfile` linting with [`dockerfilelint`][87];
- [Hall of fame][88] from `Sourcerer`;
- Some advanced Python linting (?);
- End-to-end testing and validation of the cookiecutter template;
- Add [`Invoke`][89];
- Add [`Earthly`][90].

## 🛡 Licence

[![Licence][91]][92]

This project is licenced under the terms of the `MIT` licence. See [LICENCE][93] for more details.

## 🏅 Acknowledgements

Firstly, there is no way this template would exist without the previous phenomenal work by [Roman Tezikov][118] and his fully-featured [`python-package-template`][119]. If there is anyone more deserving of a 🌟 and acknowledgement, it's him! Please give a shoutout and [support][120] if possible.

The original template was inspired by several articles that might be helpful you are starting out managing projects:

- [Hypermodern Python][94];
- [Ultimate Setup for Your Next Python Project][95];
- [Nine simple steps for better-looking python code][96];
- [Modern Python developer's toolkit][97].

And also there are some projects which served as a basis for the original template, but can also be studied as references in project management and template design:

- [`Cookiecutter`][98];
- [Audreyr's `cookiecutter-pypackage`][100];
- [Cookiecutter Data Science Template: `cdst`][102];
- [Full Stack FastAPI and PostgreSQL - Base Project Generator][101];
- [Reusable projects and base bootstrapping with Kedro Starters][121].

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
[![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://kutt.it/7fYqQl)
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
[36]: https://github.com/features/security/software-supply-chain
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
[77]: https://gitlab.com/manoelpqueiroz/galactipy/-/releases
[78]: https://semver.org/
[79]: https://github.com/marketplace/actions/release-drafter
[80]: https://coveralls.io
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
[104]: https://kutt.it/7fYqQl
[105]: https://github.com/PyCQA/flake8
[106]: https://github.com/PyCQA/pydocstyle
[107]: https://github.com/jsh9/pydoclint
[108]: https://github.com/nedbat/coveragepy
[109]: #gitlab-vs-github-features
[110]: https://docs.gitlab.com/ee/user/project/changelogs.html
[111]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitlab-ci.yml
[112]: https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitlab/changelog_config.yml
[113]: https://github.com/python-poetry/install.python-poetry.org
[114]: https://github.com/sphinx-doc/sphinx
[115]: https://github.com/pradyunsg/furo
[116]: https://github.com/prompt-toolkit/python-prompt-toolkit
[117]: https://github.com/Gruntfuggly/todo-tree
[118]: https://github.com/TezRomacH
[119]: https://github.com/TezRomacH/python-package-template
[120]: https://patreon.com/tezikov
[121]: https://docs.kedro.org/en/stable/kedro_project_setup/starters.html
