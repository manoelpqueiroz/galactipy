# Galactipy

<div align="center">

[![Build status][1]][2]
[![Dependencies Status][3]][4]
[![:rocket: Your next Python package needs a bleeding-edge project structure.][5]][6]

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

> All you need is the latest version of cookiecutter! :winking_face:

## :rocket: Features

In this [cookiecutter :cookie:][n1] template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.8` and higher;
- [`Poetry`][n2] as a dependencies manager. See configuration in [`pyproject.toml`][n3];
- Automatic code formatting with [`black`][n4], [`isort`][n5] and [`pyupgrade`][n6], with ready-to-use [`pre-commit`][n7] hooks;
- Code and docstring linting with [`flake8`][n8], [`pydocstyle`][n9] and [`pydoclint`][n10];
- Type checks with [`mypy`][n11], security checks with [`safety`][n12] and [`bandit`][n13];
- Testing with [`pytest`][n14];
- Ready-to-use [`.editorconfig`][n15], [`.dockerignore`][n16], and [`.gitignore`][n17] files. You don't have to worry about those things.

### Deployment features

- Issue and Merge Request templates for easy integration with GitLab and GitHub;
- Predefined CI/CD build workflow for [`GitLab CI`][n18] and [`Github Actions`][n19];
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds etc. with [`Makefile`][n20]. More details in [makefile-usage][n21];
- [Dockerfile][n22] for your package.

#### GitLab vs. GitHub features

You are free to choose whichever platform works best for you and your project. The original template by [TezRomacH][n23] was created originally with GitHub in mind, which prompted the creation of a similarly fully-featured template for GitLab users as well.

However, not everything that is available for GitHub users is available to GitLab users, and vice-versa. Please mind the differences between both options.

Below is a comparison between the features available in this package depending on which platform you choose to host your project:

|          **Feature**          |     **GitLab**      |     **GitHub**      | **Observations**                                                                                                                                                                                       |
|:-----------------------------:|:-------------------:|:-------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Issue templates               | :check_mark_button: | :check_mark_button: | Both options feature automatic labels, but GitHub has an extra configuration to prevent the creation of empty issues. |
| Merge/pull requests templates | :check_mark_button: | :check_mark_button: | |
| Stale issues                  | :cross_mark:        | :check_mark_button: | A specific configuration is available for GitHub to mark and automatically close stale issues. |
| Build workflow                | :check_mark_button: | :check_mark_button: | A basic workflow to install the package and run tests, check codestyle and safety. |
| Greetings workflow            | :cross_mark:        | :check_mark_button: | |
| Dependabot                    | :cross_mark:        | :check_mark_button: | [Dependabot][n24] is a feature now incorporated into GitHub Security. See [here][n25] how to enable it. |
| Release drafter               | :cross_mark:        | :check_mark_button: | [Release Drafter][n26] is a custom workflow available on GitHub Marketplace. You may see the list of labels in [`release-drafter.yml`][n27]. Works perfectly with [Semantic Versions][n28] specification. |
| Changelog configuration       | :check_mark_button: | :cross_mark:        | GitLab provides automatic changelog updates through their [API][n29]. You may modify the template in [`changelog_config.yml`][n30]. |

### Open source community features

- Ready-to-use [Merge Request templates][n31] and several [Issue templates][n32];
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically;
- For GitHub users, [`Stale bot`][n33] closes abandoned issues after a period of inactivity. Configuration is [here][n34];
- [Semantic Versions][n28] specification with [`Changelog entries`][n29] or [`Release Drafter`][n26].

## :exploding_head: How to use it

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

|       **Parameter**       |      **Default value**      | **Description**                                                                                                                                                                                                 |
|:-------------------------:|:---------------------------:|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`            | `Python Project`            | [Check the availability of possible names][n35] before creating the project. |
| `repo_name`               | based on `project_name`     | Name of the repository to develop the project on. [Check the availability of possible names][n35] before creating the project. |
| `package_name`            | based on `project_name`     | PyPI-compliant Python package name. [Check the availability of possible names][n35] before creating the project. |
| `project_description`     | based on `project_name`     | A brief description of your project. |
| `version`                 | `0.1.0`                     | Initial version of the package. Make sure it follows the [Semantic Versions][n28] specification. |
| `author`                  | `Manoel Pereira de Queiroz` | Name of the author or organisation. Used to generate `LICENCE` and to specify ownership in `pyproject.toml`. |
| `scm_platform`            | `GitLab`                    | One of `GitLab` and `GitHub`. Depending on the choice you will have [different features][n36] to work with. |
| `scm_username`            | `manoelpqueiroz`            | GitHub or GitLab username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for either platform. |
| `email`                   | based on `scm_username`     | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
| `licence`                 | `MIT`                       | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `GNU AGLP v3.0`, `GNU LGPL v3.0`, `Mozilla Public License 2.0` and `Apache Software License 2.0`, or `Not open source`. |
| `minimal_python_version`  | `3.8`                       | Minimal Python version. All versions since `3.8` are available to choose. It is used for builds, pipelines and formatters. |
| `use_formatters`          | `True`                      | Option to use code formatters [`black`][n4], [`isort`][n5] and [`pyupgrade`][n6] as pre-commit hooks. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `line_length`             | 88                          | The max length per line, dismiss if `use_formatters` is not used. NOTE: This value must be between 50 and 300. |
| `use_linters`             | `True`                      | Option to use linters [`flake8`][n8] and [`pydocstyle`][n9]. Depending on the value of `docstring_style`, will also use [`pydoclint`][n10]. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `docstring_style`         | `numpy`                     | One of `numpy`, `pep257` or `google`, dismiss if `use_linters` is not used. You can choose `other` to disable `pydoclint` and checks on your docstrings. |
| `create_cli`              | `True`                      | Option to create a simple CLI application with [`Typer`][n37] and [`Rich`][n38] libraries. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `create_docker`           | `True`                      | Option to create a [Dockerfile][n39] to build an image for your project. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `create_docs`             | `True`                      | Option to create documentation files with [`Sphinx`][n40]. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. :winking_face:

#### Demo

[![Demo of github.com/TezRomacH/python-package-template][n41]][n42]

### More details

Your project will contain `README.md` file with instructions for development, deployment etc. You can read [the project README.md template][n43] before.

### Initial set up

#### Initialize `poetry`

By running `make install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project][n44].

#### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.

### Package example

Want to know more about Poetry? Check [its documentation][n45].

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands][n46] are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc.
</p>
</details>

#### CLI example

If you set `create_cli` to `True` the template comes with a cute little CLI application example. It utilises [`Typer`][n37] and [`Rich`][n38] for CLI input validation and beautiful formatting in the terminal.

After installation via `make install` (preferred) or `poetry install` you can try to play with the example:

```bash
poetry run <repo_name> --help
```

```bash
poetry run <repo_name> --name Manoel
```

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions][n28] standard;
- Make a commit to `GitLab` or `GitHub`, depending on where you are hosting your code;
- Create a `Release` for your package on the platform;
- And... publish :slightly_smiling_face: `poetry publish --build`.

### Makefile usage

[`Makefile`][n47] contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry as a [standalone application][n48] run:

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

More information [about docker][n49].

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

## :bullseye: What's next

Well, that's up to you :flexed_biceps:.

For further setting up your project:

- Look for files and sections marked with `UPDATEME`, these should be updated according to the needs and characteristics of your project;
  - **Tip:** If you use VS Code's [Todo Tree][n50] extension, you can even set a specific tag to quickly locate these marks;
- This template assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates so links won't break when you push them to your repo;
- Make sure to create your desired Issue labels on your platform so it ensures you will start tracking them accordingly.

If you want to put your project on steroids, here are a few Python tools which can help you depending on what you want to achieve with your application:

- [`Typer`][n51] is great for creating CLI applications. If you chose to generate a CLI example during the Cookiecutter setup, `Typer` will already be among your dependencies;
- [`Rich`][n52] makes it easy to add beautiful formatting in the terminal. If you chose to generate a CLI example during the Cookiecutter setup, `Rich` will already be among your dependencies;
- [`tqdm`][n53] is a fast, extensible progress bar for Python and CLI;
- [`Python Prompt Toolkit`][n54] allows you to create more advanced terminal applications, such as a text editor or even your own shell;
- [`orjson`][n55], an ultra fast JSON parsing library;
- [`Pydantic`][n56] is data validation and settings management using Python type hinting;
- [`Returns`][n57] makes you function's output meaningful, typed, and safe;
- [`Loguru`][n58] makes logging (stupidly) simple;
- [`IceCream`][n59] is a little library for sweet and creamy debugging;
- [`Hydra`][n60] is a framework for elegantly configuring complex applications;
- [`FastAPI`][n61] is a type-driven asynchronous web framework.

And here are a few articles which may help you:

- [Open Source Guides][n62];
- [A handy guide to financial support for open source][n63];
- [GitLab CI Documentation][n64];
- [GitHub Actions Documentation][n65];
- [Makefile tutorial][n66];
- Maybe you would like to add [gitmoji][n67] to commit names. This is really funny. :grinning_face_with_smiling_eyes:

## :chart_increasing: Releases

You can see the list of available releases on the [GitLab Releases][n68] page.

We follow [Semantic Versions][n28] specification.

We use [`GitLab Changelog`][n29] entries to track changes. You can categorise commits and Merge Requests made to this project using [git trailers][n69] in your commit messages.

### List of trailers and corresponding categories

|            **Git trailer**            |    **Category in CHANGELOG**    |
| :-----------------------------------: | :-----------------------------: |
| `enhancement`, `feature`              | :rocket: Features               |
| `bug`, `refactoring`, `bugfix`, `fix` | :wrench: Fixes & Refactoring    |
| `build`, `ci`, `testing`              | :package: Build System & CI/CD  |
| `breaking`                            | :collision: Breaking Changes    |
| `documentation`                       | :memo: Documentation            |
| `dependencies`                        | :arrow_up: Dependencies updates |

## :test_tube: TODOs

This template will continue to develop and follow the bleeding edge new tools and best practices to improve the Python development experience.

Here is a list of things that have yet to be implemented:

- Tests coverage reporting with [`Coveralls`][n70];
- Auto uploading your package to [`PyPI`][n71] when new release is created;
- Automatic creation of documentation. We will be using [`Sphinx`][n72] with [`Furo`][n73] design;
- Code metrics with [`Radon`][n74];
- Docstring coverage with [`interrogate`][n75];
- `Dockerfile` linting with [`dockerfilelint`][n76];
- [Hall of fame][n77] from `Sourcerer`;
- Some advanced Python linting (?);
- End-to-end testing and validation of the cookiecutter template;
- Add [`Invoke`][n78];
- Add [`Earthly`][n79].

## :shield: Licence

[![Licence][13]][14]

This project is licenced under the terms of the `MIT` licence. See [LICENCE][14] for more details.

## :sports_medal: Acknowledgements

Firstly, there is no way this template would exist without the previous phenomenal work by [Roman Tezikov][n80] and his fully-featured [`python-package-template`][n23]. If there is anyone more deserving of a :glowing_star: and acknowledgement, it's him! Please give a shoutout and [support][n81] if possible.

The original template was inspired by several articles that might be helpful you are starting out managing projects:

- [Hypermodern Python][n82];
- [Ultimate Setup for Your Next Python Project][n83];
- [Nine simple steps for better-looking python code][n84];
- [Modern Python developer's toolkit][n85].

And also there are some projects which can be studied as references in project management and template design:

- [`Cookiecutter`][n86];
- [Audreyr's `cookiecutter-pypackage`][n87];
- [Cookiecutter Data Science Template: `cdst`][n88];
- [Full Stack FastAPI and PostgreSQL - Base Project Generator][n89];
- [The importance of layered thinking in data engineering][n90].

Give them your :star:, these resources are amazing! :winking_face:

## :page_with_curl: Citation

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

Markdown source for the badge [![:rocket: Your next Python package needs a bleeding-edge project structure.][5]][6]

```markdown
[![:rocket: Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/galactipy-%F0%9F%9A%80-brightgreen)](https://kutt.it/7fYqQl)
```

[1]: https://github.com/TezRomacH/python-package-template/workflows/build/badge.svg?branch=master&event=push
[2]: https://github.com/TezRomacH/python-package-template/actions?query=workflow%3Abuild
[3]: https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg
[4]: https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot
[5]: https://img.shields.io/badge/galactipy-%F0%9F%9A%80-brightgreen
[6]: https://kutt.it/7fYqQl
[7]: https://img.shields.io/badge/code%20style-black-000000.svg
[8]: https://github.com/psf/black
[9]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[10]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/.pre-commit-config.yaml
[11]: https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg
[12]: https://gitlab.com/manoelpqueiroz/galactipy/-/releases
[13]: https://img.shields.io/gitlab/license/manoelpqueiroz/galactipy
[14]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/LICENCE
[15]: ./assets/images/coverage.svg

[n1]: https://cookiecutter.readthedocs.io/en/stable/
[n2]: https://python-poetry.org/
[n3]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/pyproject.toml
[n4]: https://black.readthedocs.io/en/stable/
[n5]: https://pycqa.github.io/isort/
[n6]: https://github.com/asottile/pyupgrade
[n7]: https://pre-commit.com/
[n8]: https://flake8.pycqa.org/en/latest/
[n9]: http://www.pydocstyle.org/en/stable/
[n10]: https://github.com/jsh9/pydoclint
[n11]: https://mypy.readthedocs.io
[n12]: https://docs.safetycli.com/safety-2/
[n13]: https://bandit.readthedocs.io/en/latest/
[n14]: https://docs.pytest.org/en/latest/
[n15]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.editorconfig
[n16]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.dockerignore
[n17]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitignore
[n18]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitlab-ci.yml
[n19]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/workflows/build.yml
[n20]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile
[n21]: #makefile-usage
[n22]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[n23]: https://github.com/TezRomacH/python-package-template
[n24]: https://docs.github.com/en/code-security/dependabot
[n25]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[n26]: https://github.com/marketplace/actions/release-drafter
[n27]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/release-drafter.yml
[n28]: https://semver.org/
[n29]: https://docs.gitlab.com/ee/user/project/changelogs.html
[n30]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/changelog_config.yml
[n31]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/merge_request_templates/default.md
[n32]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/issue_templates
[n33]: https://github.com/marketplace/actions/close-stale-issues
[n34]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/.stale.yml
[n35]: http://ivantomic.com/projects/ospnc/
[n36]: #gitlab-vs-github-features
[n37]: https://typer.tiangolo.com/
[n38]: https://rich.readthedocs.io/en/latest/
[n39]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[n40]: https://www.sphinx-doc.org/en/master/
[n41]: https://asciinema.org/a/422052.svg
[n42]: https://asciinema.org/a/422052
[n43]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D
[n44]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D#very-first-steps
[n45]: https://python-poetry.org/docs/
[n46]: https://python-poetry.org/docs/cli/#commands
[n47]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile
[n48]: https://github.com/python-poetry/install.python-poetry.org
[n49]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker
[n50]: https://github.com/Gruntfuggly/todo-tree
[n51]: https://github.com/tiangolo/typer
[n52]: https://github.com/willmcgugan/rich
[n53]: https://github.com/tqdm/tqdm
[n54]: https://github.com/prompt-toolkit/python-prompt-toolkit
[n55]: https://github.com/ijl/orjson
[n56]: https://github.com/samuelcolvin/pydantic/
[n57]: https://github.com/dry-python/returns
[n58]: https://github.com/Delgan/loguru
[n59]: https://github.com/gruns/icecream
[n60]: https://github.com/facebookresearch/hydra
[n61]: https://github.com/tiangolo/fastapi
[n62]: https://opensource.guide/
[n63]: https://github.com/nayafia/lemonade-stand
[n64]: https://docs.gitlab.com/ee/ci/
[n65]: https://help.github.com/en/actions
[n66]: https://makefiletutorial.com/
[n67]: https://gitmoji.carloscuesta.me/
[n68]: https://gitlab.com/manoelpqueiroz/galactipy/-/releases
[n69]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
[n70]: https://coveralls.io
[n71]: https://pypi.org/
[n72]: https://github.com/sphinx-doc/sphinx
[n73]: https://github.com/pradyunsg/furo
[n74]: https://github.com/rubik/radon
[n75]: https://github.com/econchick/interrogate
[n76]: https://github.com/replicatedhq/dockerfilelint
[n77]: https://github.com/sourcerer-io/hall-of-fame
[n78]: http://www.pyinvoke.org/
[n79]: https://earthly.dev/
[n80]: https://github.com/TezRomacH
[n81]: https://patreon.com/tezikov
[n82]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[n83]: https://martinheinz.dev/blog/14
[n84]: https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf
[n85]: https://pycon.switowski.com/
[n86]: https://github.com/cookiecutter/cookiecutter
[n87]: https://github.com/audreyr/cookiecutter-pypackage
[n88]: https://github.com/crplab/cdst
[n89]: https://github.com/tiangolo/full-stack-fastapi-postgresql
[n90]: https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71
