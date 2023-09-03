# Galactipy

<div align="center">

[![Python support][b1]][b2]
[![Repository][b3]][b2]
[![Releases][b4]][b5]
[![Licence][b6]][b7]
[![Cookiecutter template][b8]][b9]

[![Project type][b10]][b11]
[![Contributions Welcome][b12]][b13]
[![Open issues][b14]][b15]
[![Merge Requests][b16]][b17]

[![Poetry][b18]][b19]
[![Pre-commit][b20]][b21]
[![Editorconfig][b22]][b23]
[![Code style: black][b24]][b25]
[![Docstrings: numpydoc][b26]][b27]

[![Semantic versions][b28]][b5]
[![GitLab Pipelines][b29]][b30]
[![Coverage][b31]][b32]

_Expand your project structure from atoms of code to **galactic** dimensions._ :milky_way:
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
- **Loads** of predefined [badges][n33] to make your project stand out, you can either keep them, remove as you wish or be welcome to add even more;
- For GitHub users, [`Stale bot`][n34] closes abandoned issues after a period of inactivity. Configuration is [here][n35];
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
| `project_name`            | `Python Project`            | [Check the availability of possible names][n36] before creating the project. |
| `repo_name`               | based on `project_name`     | Name of the repository to develop the project on. [Check the availability of possible names][n36] before creating the project. |
| `package_name`            | based on `project_name`     | PyPI-compliant Python package name. [Check the availability of possible names][n36] before creating the project. |
| `project_description`     | based on `project_name`     | A brief description of your project. |
| `version`                 | `0.1.0`                     | Initial version of the package. Make sure it follows the [Semantic Versions][n28] specification. |
| `author`                  | `Manoel Pereira de Queiroz` | Name of the author or organisation. Used to generate `LICENCE` and to specify ownership in `pyproject.toml`. |
| `scm_platform`            | `GitLab`                    | One of `GitLab` and `GitHub`. Depending on the choice you will have [different features][n37] to work with. |
| `scm_username`            | `manoelpqueiroz`            | GitHub or GitLab username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for either platform. |
| `email`                   | based on `scm_username`     | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
| `licence`                 | `MIT`                       | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `GNU AGLP v3.0`, `GNU LGPL v3.0`, `Mozilla Public License 2.0` and `Apache Software License 2.0`, or `Not open source`. |
| `minimal_python_version`  | `3.8`                       | Minimal Python version. All versions since `3.8` are available to choose. It is used for builds, pipelines and formatters. |
| `use_formatters`          | `True`                      | Option to use code formatters [`black`][n4], [`isort`][n5] and [`pyupgrade`][n6] as pre-commit hooks. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `line_length`             | 88                          | The max length per line, dismiss if `use_formatters` is not used. NOTE: This value must be between 50 and 300. |
| `use_linters`             | `True`                      | Option to use linters [`flake8`][n8] and [`pydocstyle`][n9]. Depending on the value of `docstring_style`, will also use [`pydoclint`][n10]. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `docstring_style`         | `numpy`                     | One of `numpy`, `pep257` or `google`, dismiss if `use_linters` is not used. You can choose `other` to disable `pydoclint` and checks on your docstrings. |
| `create_cli`              | `True`                      | Option to create a simple CLI application with [`Typer`][n38] and [`Rich`][n39] libraries. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `create_docker`           | `True`                      | Option to create a [Dockerfile][n40] to build an image for your project. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |
| `create_docs`             | `True`                      | Option to create documentation files with [`Sphinx`][n41]. You can dismiss it by typing `0`, `false`, `f`, `no`, `n` or `off`. |

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. :winking_face:

#### Demo

<div class="termy">

```console
$ cookiecutter gl:manoelpqueiroz/galactipy
  [1/24] Project name (Python Project): A Decent Python Project
  [2/24] Project slug (a-decent-python-project): a-different-slug
  [3/24] Package name (a_decent_python_project): a_viable_package
  [4/24] Short description of the project (Awesome `a-different-slug` is a Python cli/package created with
https://gitlab.com/manoelpqueiroz/galactipy): Let's try a cool description
  [5/24] Project version (0.1.0): 1.100.9-rc7+build.456893a
  [6/24] Author or Organisation (Manoel Pereira de Queiroz):
  [7/24] In which platform would you like to host your code?
    1 - GitLab
    2 - GitHub
    Choose from [1/2] (1): 2
  [8/24] Platform username (manoelpqueiroz): myuniqueusername
  [9/24] e-Mail (contact@myuniqueusername.com): g@mail.com
  [10/24] Which licence would you like to use for your project?
    1 - MIT Licence
    2 - 3-Clause BSD
    3 - GNU GPL v3.0
    4 - GNU AGPL v3.0
    5 - GNU LGPL v3.0
    6 - Mozilla Public License 2.0
    7 - Apache Software License 2.0
    8 - Not open source
    Choose from [1/2/3/4/5/6/7/8] (1): 4
  [11/24] Minimal Python version
    1 - 3.8
    2 - 3.9
    3 - 3.10
    4 - 3.11
    Choose from [1/2/3/4] (1): 3
  [12/24] Use Black, isort and pyupgrade for formatting? [y/n] (y): yes
  [13/24] Maximum line length (88):
  [14/24] Use flake8 and pydocstyle for linting? [y/n] (y): true
  [15/24] Which docstring style would you like to use? "numpy" and "google" styles will add pydoclint as a dependency.
    1 - numpy
    2 - google
    3 - pep257
    4 - other
    Choose from [1/2/3/4] (1): 4
  [16/24] create_cli [y/n] (y): on
  [17/24] Containerize your application with Docker? [y/n] (y): no
  [18/24] Create project documentation with Sphinx? [y/n] (y): false

Your project A Decent Python Project is created.

1) Now you can start working on it:

    $ cd a-different-slug && git init

2) If you don't have Poetry installed run:

    $ make poetry-download

3) Initialize poetry and install pre-commit hooks:

    $ make install
    $ make pre-commit-install

4) Run codestyle:

    $ make codestyle

5) Upload initial code to GitHub:

    $ git add .
    $ git commit -m ":tada: Initial commit"
    $ git remote add origin https://github.com/myuniqueusername/a-different-slug.git
    $ git push -u origin master
```

</div>

### More details

Your project will contain `README.md` file with instructions for development, deployment etc. You can read [the project README.md template][n42] before.

### Initial set up

#### Initialize `poetry`

By running `make install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project][n43].

#### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.

### Package example

Want to know more about Poetry? Check [its documentation][n44].

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands][n45] are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc.
</p>
</details>

#### CLI example

If you set `create_cli` to `True` the template comes with a cute little CLI application example. It utilises [`Typer`][n38] and [`Rich`][n39] for CLI input validation and beautiful formatting in the terminal.

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

[`Makefile`][n46] contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry as a [standalone application][n47] run:

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

More information [about docker][n48].

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
  - **Tip:** If you use VS Code's [`Todo Tree`][n49] extension, you can even set a specific tag to quickly locate these marks. Update your `settings.json` with:

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

- [`Typer`][n50] is great for creating CLI applications. If you chose to generate a CLI example during the Cookiecutter setup, `Typer` will already be among your dependencies;
- [`Rich`][n51] makes it easy to add beautiful formatting in the terminal. If you chose to generate a CLI example during the Cookiecutter setup, `Rich` will already be among your dependencies;
- [`tqdm`][n52] is a fast, extensible progress bar for Python and CLI;
- [`Python Prompt Toolkit`][n53] allows you to create more advanced terminal applications, such as a text editor or even your own shell;
- [`orjson`][n54], an ultra fast JSON parsing library;
- [`Pydantic`][n55] is data validation and settings management using Python type hinting;
- [`Returns`][n56] makes you function's output meaningful, typed, and safe;
- [`Loguru`][n57] makes logging (stupidly) simple;
- [`IceCream`][n58] is a little library for sweet and creamy debugging;
- [`Hydra`][n59] is a framework for elegantly configuring complex applications;
- [`FastAPI`][n60] is a type-driven asynchronous web framework.

For taking development and exposition of your project to the next level:

- Try out some more badges, not only it looks good, but it also helps people better understand some intricate details on how your project works:
  - You can look at dynamic badges available at [`Shields.io`][n61];
  - There is a myriad of standardised static badges at [`Simple Badges`][n62];
  - [`awesome-badges`][n63] provides a lot of useful resources to help you deal with badges;
- Add your project to [`OpenSSF Best Practices`][n64] and [`OSSRank`][n65] indexes. If you have greater ambitions for your project and/or expects it to scale at some point, it's worth considering adding it to these trackers;
  - There are already badges for those set up in your `README.md` file, just waiting for you to update their URLs with your project's index in both services :beaming_face_with_smiling_eyes:
- Setup a code coverage service for your tests, popular options include:
  - [`Coveralls`][n66] and [`Codecov`][n67] if you need solely test coverage;
  - [`Code Climate`][n68] and [`Codacy`][n69] for fully-featured code analysis;
- Setup a sponsorship page and allow users and organisations who appreciate your project to help raise for its development (and add a badge in the process! :smiling_face_with_sunglasses:). Popular platforms are:
  - [`Liberapay`][n70];
  - [`Open Collective`][n71];
  - [`Ko-fi`][n72];
  - If you host on GitHub, you can set a [Sponsors account][n73] directly integrated into the platform;
  - Of course, you can also set any kind of gateway you wish, what works best for you and your project!

And here are a few articles which may help you:

- [Open Source Guides][n74];
- [A handy guide to financial support for open source][n75];
- [GitLab CI Documentation][n76];
- [GitHub Actions Documentation][n77];
- [Makefile tutorial][n78];
- Maybe you would like to add [gitmoji][n79] to commit names. This is really funny. :grinning_face_with_smiling_eyes:

## :chart_increasing: Releases

You can see the list of available releases on the [GitLab Releases][n80] page.

We follow [Semantic Versions][n28] specification.

We use [`GitLab Changelog`][n29] entries to track changes. You can categorise commits and Merge Requests made to this project using [git trailers][n81] in your commit messages.

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

- Tests coverage reporting with [`Coveralls`][n82];
- Auto uploading your package to [`PyPI`][n83] when new release is created;
- Automatic creation of documentation. We will be using [`Sphinx`][n84] with [`Furo`][n85] design;
- Code metrics with [`Radon`][n86];
- Docstring coverage with [`interrogate`][n87];
- `Dockerfile` linting with [`dockerfilelint`][n88];
- [Hall of fame][n89] from `Sourcerer`;
- Some advanced Python linting (?);
- End-to-end testing and validation of the cookiecutter template;
- Add [`Invoke`][n90];
- Add [`Earthly`][n91].

## :shield: Licence

[![Licence][b6]][b7]

This project is licenced under the terms of the `MIT` licence. See [LICENCE][b7] for more details.

## :sports_medal: Acknowledgements

Firstly, there is no way this template would exist without the previous phenomenal work by [Roman Tezikov][n92] and his fully-featured [`python-package-template`][n23]. If there is anyone more deserving of a :glowing_star: and acknowledgement, it's him! Please give a shoutout and [support][n93] if possible.

The original template was inspired by several articles that might be helpful if you are starting out managing projects:

- [Hypermodern Python][n94];
- [Ultimate Setup for Your Next Python Project][n95];
- [Nine simple steps for better-looking python code][n96];
- [Modern Python developer's toolkit][n97].

And also there are some projects which can be studied as references in project management and template design:

- [`Cookiecutter`][n98];
- [Audreyr's `cookiecutter-pypackage`][n99];
- [Cookiecutter Data Science Template: `cdst`][n100];
- [Full Stack FastAPI and PostgreSQL - Base Project Generator][n101];
- [The importance of layered thinking in data engineering][n102].

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

Add the badge [![Expand your project structure from atoms of code to galactic dimensions.][b33]][b34] to your project! It would be really appreciated to spread the word of this template.

Here is the Markdown source for it:

```markdown
[![Expand your project structure from atoms of code to galactic dimensions.](https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E)](https://kutt.it/7fYqQl)
```

[b1]: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?style=for-the-badge
[b2]: https://kutt.it/WlS8Qj
[b3]: https://img.shields.io/badge/GitLab-0B2640?style=for-the-badge&logo=gitlab&logoColor=white
[b4]: https://img.shields.io/gitlab/v/release/manoelpqueiroz%2Fgalactipy?style=for-the-badge&logo=semantic-release&color=253747
[b5]: https://kutt.it/dFL664
[b6]: https://img.shields.io/gitlab/license/manoelpqueiroz%2Fgalactipy?style=for-the-badge
[b7]: https://kutt.it/hTjpzN
[b8]: https://img.shields.io/badge/Cookiecutter-D4AA00?style=for-the-badge&logo=Cookiecutter&logoColor=white
[b9]: https://cookiecutter.readthedocs.io/en/stable/
[b10]: https://img.shields.io/badge/project%20type-toy-blue?style=for-the-badge
[b11]: https://project-types.github.io/#toy
[b12]: https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=for-the-badge
[b13]: https://kutt.it/1Q6cYr
[b14]: https://img.shields.io/gitlab/issues/open/manoelpqueiroz%2Fgalactipy?style=for-the-badge&color=fca326
[b15]: https://kutt.it/2B3qIg
[b16]: https://img.shields.io/gitlab/merge-requests/open/manoelpqueiroz%2Fgalactipy?style=for-the-badge&color=6fdac9
[b17]: https://kutt.it/YZ7kPX
[b18]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[b19]: https://python-poetry.org/
[b20]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[b21]: https://kutt.it/D4ayxs
[b22]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[b23]: https://kutt.it/fy3pqF
[b24]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[b25]: https://black.readthedocs.io/en/stable/
[b26]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
[b27]: https://numpydoc.readthedocs.io/en/latest/format.html
[b28]: https://img.shields.io/badge/%F0%9F%93%A6-semantic%20versions-4053D6?style=for-the-badge
[b29]: https://img.shields.io/gitlab/pipeline-status/manoelpqueiroz%2Fgalactipy?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[b30]: https://kutt.it/zG7nVG
[b31]: https://img.shields.io/coverallsCoverage/gitlab/manoelpqueiroz/galactipy?style=for-the-badge&logo=coveralls
[b32]: https://kutt.it/uxIDHs
[b33]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[b34]: https://kutt.it/7fYqQl

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
[n33]: https://shields.io/
[n34]: https://github.com/marketplace/actions/close-stale-issues
[n35]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/.stale.yml
[n36]: http://ivantomic.com/projects/ospnc/
[n37]: #gitlab-vs-github-features
[n38]: https://typer.tiangolo.com/
[n39]: https://rich.readthedocs.io/en/latest/
[n40]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[n41]: https://www.sphinx-doc.org/en/master/
[n42]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D
[n43]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D#very-first-steps
[n44]: https://python-poetry.org/docs/
[n45]: https://python-poetry.org/docs/cli/#commands
[n46]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile
[n47]: https://github.com/python-poetry/install.python-poetry.org
[n48]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker
[n49]: https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree
[n50]: https://github.com/tiangolo/typer
[n51]: https://github.com/willmcgugan/rich
[n52]: https://github.com/tqdm/tqdm
[n53]: https://github.com/prompt-toolkit/python-prompt-toolkit
[n54]: https://github.com/ijl/orjson
[n55]: https://github.com/samuelcolvin/pydantic/
[n56]: https://github.com/dry-python/returns
[n57]: https://github.com/Delgan/loguru
[n58]: https://github.com/gruns/icecream
[n59]: https://github.com/facebookresearch/hydra
[n60]: https://github.com/tiangolo/fastapi
[n61]: https://shields.io/badges/static-badge
[n62]: https://badges.pages.dev/
[n63]: https://github.com/badges/awesome-badges
[n64]: https://www.bestpractices.dev/en
[n65]: https://ossrank.com/
[n66]: https://coveralls.io/
[n67]: https://about.codecov.io/
[n68]: https://codeclimate.com/velocity/what-is-velocity
[n69]: https://www.codacy.com/
[n70]: https://liberapay.com/
[n71]: https://opencollective.com/
[n72]: https://ko-fi.com/
[n73]: https://github.com/sponsors
[n74]: https://opensource.guide/
[n75]: https://github.com/nayafia/lemonade-stand
[n76]: https://docs.gitlab.com/ee/ci/
[n77]: https://help.github.com/en/actions
[n78]: https://makefiletutorial.com/
[n79]: https://gitmoji.carloscuesta.me/
[n80]: https://gitlab.com/manoelpqueiroz/galactipy/-/releases
[n81]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit
[n82]: https://coveralls.io
[n83]: https://pypi.org/
[n84]: https://github.com/sphinx-doc/sphinx
[n85]: https://github.com/pradyunsg/furo
[n86]: https://github.com/rubik/radon
[n87]: https://github.com/econchick/interrogate
[n88]: https://github.com/replicatedhq/dockerfilelint
[n89]: https://github.com/sourcerer-io/hall-of-fame
[n90]: http://www.pyinvoke.org/
[n91]: https://earthly.dev/
[n92]: https://github.com/TezRomacH
[n93]: https://patreon.com/tezikov
[n94]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[n95]: https://martinheinz.dev/blog/14
[n96]: https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf
[n97]: https://pycon.switowski.com/
[n98]: https://github.com/cookiecutter/cookiecutter
[n99]: https://github.com/audreyr/cookiecutter-pypackage
[n100]: https://github.com/crplab/cdst
[n101]: https://github.com/tiangolo/full-stack-fastapi-postgresql
[n102]: https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71
