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
[![Code style: Ruff][b24]][b25]
[![Docstrings: numpydoc][b26]][b27]

[![Semantic versions][b28]][b5]
[![GitLab Pipelines][b29]][b30]
[![Coverage][b31]][b32]

_Expand your project structure from atoms of code to **galactic** dimensions._ :milky_way:
</div>

## TL;DR

```bash
cookiecutter gl:manoelpqueiroz/galactipy --checkout v0.6.1
```

> All you need is the latest version of cookiecutter! :wink:

## :rocket: Features

In this [cookiecutter :cookie:][ft1] template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.9` and higher;
- [`Poetry`][ft2] as a dependencies manager. See configuration in [`pyproject.toml`][ft3];
- Automatic code formatting with [`ruff`][ft4], with ready-to-use [`pre-commit`][ft5] hooks and several rules already selected for linting;
- Type checks with [`mypy`][ft6], security checks with [`safety`][ft7] and [`bandit`][ft8];
- Testing with [`pytest`][ft9];
- Predefined VS Code [`settings.json`][ft10] with quality-of-life configuration for editor, workbench, debugging and more;
- Ready-to-use [`.editorconfig`][ft11], [`.dockerignore`][ft12] and [`.gitignore`][ft13] files. You don't have to worry about those things.

### Deployment features

- Issue and Merge Request templates for easy integration with GitLab and GitHub;
- Predefined CI/CD build workflow for [`GitLab CI`][ft14] and [`Github Actions`][ft15];
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds etc. with [`invoke`][ft16]. More details in [Invoke Usage][ft17];
- [`Dockerfile`][ft18] for your package.

#### GitLab vs. GitHub features

You are free to choose whichever platform works best for you and your project. The original template by [TezRomacH][ft19] was created originally with GitHub in mind, which prompted the creation of a similarly fully-featured template for GitLab users as well.

However, not everything that is available for GitHub users is available to GitLab users, and vice-versa. Please mind the differences between both options.

Below is a comparison between the features available in this package depending on which platform you choose to host your project:

|          **Feature**          |     **GitLab**     |     **GitHub**     | **Observations**                                                                                                                                                                                             |
|:-----------------------------:|:------------------:|:------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Issue templates               | :white_check_mark: | :white_check_mark: | Both options feature automatic labels, but GitHub has an extra configuration to prevent the creation of empty issues. |
| Merge/pull requests templates | :white_check_mark: | :white_check_mark: | |
| Stale issues                  | :x:                | :white_check_mark: | A specific configuration is available for GitHub to mark and automatically close stale issues. |
| Build workflow                | :white_check_mark: | :white_check_mark: | A basic workflow to install the package and run tests, check codestyle and safety. |
| Greetings workflow            | :x:                | :white_check_mark: | |
| Dependabot                    | :x:                | :white_check_mark: | [Dependabot][ft20] is a feature now incorporated into GitHub Security. See [here][ft21] how to enable it. |
| Release drafter               | :x:                | :white_check_mark: | [Release Drafter][ft22] is a custom workflow available on GitHub Marketplace. You may see the list of labels in [`release-drafter.yml`][ft23]. Works perfectly with [Semantic Versions][ft24] specification. |
| Changelog configuration       | :white_check_mark: | :x:                | GitLab provides automatic changelog updates through their [API][ft25]. You may modify the template in [`changelog_config.yml`][ft26]. |

### Open source community features

- Ready-to-use [Merge Request templates][ft27] and several [Issue templates][ft28];
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically;
- **Loads** of predefined [badges][ft29] to make your project stand out, you can either keep them, remove as you wish or be welcome to add even more;
- For GitHub users, [`Stale bot`][ft30] closes abandoned issues after a period of inactivity. Configuration is [here][ft31];
- [Semantic Versions][ft24] specification with [`Changelog entries`][ft25] or [`Release Drafter`][ft22].

## :exploding_head: How to use it

### Installation

To begin using the template consider updating `cookiecutter`.

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gl:manoelpqueiroz/galactipy --checkout v0.6.1
```

### Input variables

Cookiecutter will ask you to fill some variables in order to generate the files with everything you need already set up.

The input variables, with their default values, are as follows:

|       **Parameter**       |      **Default value**      | **Description**                                                                                                                                                     |
|:-------------------------:|:---------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`            | `Python Project`            | A suitable name by which people will refer to, you are free to name it however you wish to. |
| `repo_name`               | based on `project_name`     | Name of the repository to develop the project on. [Check the availability of possible names][htu1] before creating the project. |
| `package_name`            | based on `project_name`     | PyPI-compliant Python package name. [Check the availability of possible names][htu1] before creating the project. |
| `project_description`     | based on `project_name`     | A brief description of your project. |
| `version`                 | `0.1.0`                     | Initial version of the package. Make sure it follows the [Semantic Versions][ft24] specification. |
| `author`                  | `Manoel Pereira de Queiroz` | Name of the author or organisation. Used to generate `LICENCE` and to specify ownership in `pyproject.toml`. |
| `scm_platform`            | `GitLab`                    | One of `GitLab` and `GitHub`. Depending on the choice you will have [different features][htu2] to work with. |
| `scm_username`            | `manoelpqueiroz`            | GitHub or GitLab username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for either platform. |
| `email`                   | based on `scm_username`     | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
| `licence`                 | `MIT`                       | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `GNU AGLP v3.0`, `GNU LGPL v3.0`, `Mozilla Public License 2.0` and `Apache Software License 2.0`, or `Not open source`. |
| `minimal_python_version`  | `3.9`                       | Minimal Python version. All versions since `3.9` are available to choose. It is used for builds, pipelines and formatters. |
| `use_ruff`                | `True`                      | :small_red_triangle: Option to use [`ruff`][ft4] as the code formatter, along with a pre-commit hook. |
| `line_length`             | 88                          | The max length per line, dismiss if `use_ruff` is not used. NOTE: This value must be between 50 and 300. |
| `docstring_style`         | `numpy`                     | One of `numpy`, `pep257` or `google`, dismiss if `use_ruff` is not used. You can choose `other` to disable checks on your docstrings. |
| `docstring_length`        | based on `line_lenght`      | The max length for docstrings, dismiss if `use_ruff` is not used. NOTE: This value must be between 50 and 300 and lower of equal to `line_lenght`. |
| `create_cli`              | `True`                      | :small_red_triangle: Option to create a simple CLI application with [`Typer`][htu3] and [`Rich`][htu4] libraries. |
| `create_docker`           | `True`                      | :small_red_triangle: Option to create a [Dockerfile][ft18] to build an image for your project. |

> :eight_spoked_asterisk: Input variables marked with :small_red_triangle: are boolean variables, you can dismiss those by typing either `0`, `false`, `f`, `no`, `n` or `off`.

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. :wink:

#### Demo

<div class="termy">

```console
$ cookiecutter gl:manoelpqueiroz/galactipy
  [1/17] Project name (Python Project): A Decent Python Project
  [2/17] Project slug (a-decent-python-project): a-different-slug
  [3/17] Package name (a_decent_python_project): a_viable_package
  [4/17] Short description of the project (Awesome `a-different-slug` is a Python cli/package created with
https://gitlab.com/manoelpqueiroz/galactipy): Let's try a cool description
  [5/17] Project version (0.1.0): 1.100.9-rc7+build.456893a
  [6/17] Author or Organisation (Manoel Pereira de Queiroz):
  [7/17] In which platform would you like to host your code?
    1 - GitLab
    2 - GitHub
    Choose from [1/2] (1): 2
  [8/17] Platform username (manoelpqueiroz): myuniqueusername
  [9/17] e-Mail (contact@myuniqueusername.com): g@mail.com
  [10/17] Which licence would you like to use for your project?
    1 - MIT Licence
    2 - 3-Clause BSD
    3 - GNU GPL v3.0
    4 - GNU AGPL v3.0
    5 - GNU LGPL v3.0
    6 - Mozilla Public License 2.0
    7 - Apache Software License 2.0
    8 - Not open source
    Choose from [1/2/3/4/5/6/7/8] (1): 4
  [11/17] Minimal Python version
    1 - 3.9
    2 - 3.10
    3 - 3.11
    4 - 3.12
    5 - 3.13
    Choose from [1/2/3/4/5] (1): 3
  [12/17] Use Ruff for linting and formatting? [y/n] (y): yes
  [13/17] Maximum line length (88):
  [14/17] Which docstring style would you like to use?
    1 - numpy
    2 - google
    3 - pep257
    4 - other
    Choose from [1/2/3/4] (1): 4
  [15/17] Docstring maximum line length (88):
  [16/17] Would you like to create your project with CLI implementation? [y/n] (y): on
  [17/17] Containerize your application with Docker? [y/n] (y): no

Your project A Decent Python Project is created.

1) Now you can start working on it:

    $ cd a-different-slug && git init

2) If you don't have Poetry installed run:

    $ invoke poetry-download

3) Initialize poetry and install pre-commit hooks:

    $ invoke install
    $ invoke pre-commit-install

4) Run codestyle:

    $ invoke codestyle

5) Upload initial code to GitHub:

    $ git add .
    $ git commit -m ":tada: Initial commit"
    $ git remote add origin https://github.com/myuniqueusername/a-different-slug.git
    $ git push -u origin master
```

</div>

### More details

Your project will contain `README.md` file with instructions for development, deployment etc. You can read [the project README.md template][htu5] before.

### Initial set up

#### Initialize `poetry`

By running `invoke install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project][htu6].

#### Initialize `pre-commit`

By running `invoke pre-commit-install`. Make sure to set up git first via `git init`.

### Package example

Want to know more about Poetry? Check [its documentation][htu7].

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands][htu8] are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc.
</p>
</details>

#### CLI example

If you set `create_cli` to `True` the template comes with a cute little CLI application example. It utilises [`Typer`][htu3] and [`Rich`][htu4] for CLI input validation and beautiful formatting in the terminal.

After installation via `invoke install` (preferred) or `poetry install` you can try to play with the example:

```bash
poetry run <repo_name> --help
```

```bash
poetry run <repo_name> --name Manoel
```

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions][ft24] standard;
- Make a commit to `GitLab` or `GitHub`, depending on where you are hosting your code;
- Create a `Release` for your package on the platform;
- And... publish :slight_smile: `poetry publish --build`.

### Invoke usage

[`invoke`][ft16] contains a lot of functions for faster development.

<details>
<summary>1. Download or remove Poetry</summary>
<p>

To download and install Poetry as a [standalone application][htu9] run:

```bash
invoke poetry-download
```

To uninstall

```bash
invoke poetry-remove
```

Alternatively, you can install it via your package manager (preferred) or any method provided by the [documentation][htu10].

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements with

```bash
invoke install
```

And then add Poetry plugins to make development easier with

```bash
invoke poetry-plugins
```

Pre-commit hooks could be installed after `git init` via

```bash
invoke pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `ruff`, and can be run with

```bash
invoke codestyle

# or use synonym
invoke format
```

For formatting checks only, without rewriting files:

```bash
invoke codestyle --check
```

Aside from the formatter, you can also use `ruff` to lint project files with several preconfigured rules defined in `pyproject.toml`:

```bash
invoke check-linter
```

</p>
</details>

<details>
<summary>4. Code security</summary>
<p>

```bash
invoke check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

Update all dev libraries to the latest version using one command:

```bash
invoke update-dev-deps
```

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker with

```bash
invoke mypy
```

</p>
</details>

<details>
<summary>6. Tests</summary>
<p>

Run `pytest` with all essential parameters predefined with

```bash
invoke test
```

</p>
</details>

<details>
<summary>7. All code-related checks</summary>
<p>

Of course there is a command to ~~rule~~ run all checks in one:

```bash
invoke sweep
```

The same as:

```bash
invoke test check-linter codestyle mypy check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

Build your Docker image with the `latest` tag preconfigured with

```bash
invoke docker-build
```

Remove the Docker image with

```bash
invoke docker-remove
```

More information about Docker [here][htu11].

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>

Delete pycache files:

```bash
invoke pycache-remove
```

Remove package build:

```bash
invoke build-remove
```

Delete .DS_STORE files:

```bash
invoke dsstore-remove
```

Remove .mypycache:

```bash
invoke mypycache-remove
```

Or to remove all above run:

```bash
invoke cleanup
```

</p>
</details>

## :dart: What's next

Well, that's up to you. :muscle:

For further setting up your project:

- Look for files and sections marked with `UPDATEME`, these should be updated according to the needs and characteristics of your project;
  - If you use VS Code, install the [`Todo Tree`][wn1] extension to easily locate and jump to these marks, they are already configured in the `settings.json` file;
- Make sure to create your desired Issue labels on your platform before you start tracking them so it ensures you will be able to filter them from the get-go;
- Make changes to your CI configurations to better suit your needs.

- In order to reduce user prompts and keep things effective, the template generates files with a few assumptions:
  - It assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates and `README.md` file so links won't break when you push them to your repo;
  - It generates a PyPI badge assuming you will be able to publish your project under `repo_name`, change it otherwise;
  - It generates a Docker badge assuming you also use `scm_username` for Docker Hub and you will push your image under `repo_name`, change it otherwise;

If you want to put your project on steroids, here are a few Python tools which can help you depending on what you want to achieve with your application:

- [`Typer`][wn2] is great for creating CLI applications. If you chose to generate a CLI example during the Cookiecutter setup, `Typer` will already be among your dependencies;
- [`Rich`][wn3] makes it easy to add beautiful formatting in the terminal. If you chose to generate a CLI example during the Cookiecutter setup, `Rich` will already be among your dependencies;
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
- Add your project to [`OpenSSF Best Practices`][wn16] and [`OSSRank`][wn17] indexes. If you have greater ambitions for your project and/or expects it to scale at some point, it's worth considering adding it to these trackers;
  - There are already badges for those set up in your `README.md` file, just waiting for you to update their URLs with your project's index in both services; :grinning:
- Setup a code coverage service for your tests, popular options include:
  - [`Coveralls`][wn18] and [`Codecov`][wn19] if you need solely test coverage;
  - [`Code Climate`][wn20] and [`Codacy`][wn21] for fully-featured code analysis;
- Setup a sponsorship page and allow users and organisations who appreciate your project to help raise for its development (and add a badge in the process! :sunglasses:). Popular platforms are:
  - [`Liberapay`][wn22];
  - [`Open Collective`][wn23];
  - [`Ko-fi`][wn24];
  - If you host on GitHub, you can set a [Sponsors account][wn25] directly integrated into the platform;
  - Of course, you can also set any kind of gateway you wish, what works best for you and your project!

And here are a few articles which may help you:

- [Open Source Guides][wn26];
- [A handy guide to financial support for open source][wn27];
- [GitLab CI Documentation][wn28];
- [GitHub Actions Documentation][wn29];
- [A Comprehensive Look at Testing in Software Development][wn30] is an article that lays out why testing is crucial for development success. Eric's blog is actually a great reference, covering topics ranging from the basics to advanced techniques and best practices;
- [Robust Exception Handling][wn31];
- [Why Your Mock Doesn't Work][wn32];
- [Managing TODOs in a codebase][wn33];
- Maybe you would like to add [gitmoji][wn34] to commit names. This is really funny. :grin:

## :chart_with_upwards_trend: Releases

You can see the list of available releases on the [GitLab Releases][r1] page.

We follow [Semantic Versions][ft24] specification.

We use [`GitLab Changelog`][ft25] entries to track changes. You can categorise commits and Merge Requests made to this project using [git trailers][r2] in your commit messages.

### List of trailers and corresponding categories

|            **Git trailer**            |        **Category in CHANGELOG**       |
| :-----------------------------------: | :------------------------------------: |
| `enhancement`, `feature`              | :rocket: Features                      |
| `bug`, `refactoring`, `bugfix`, `fix` | :wrench: Fixes & Refactoring           |
| `build`, `ci`, `testing`              | :package: Build System & CI/CD         |
| `breaking`                            | :boom: Breaking Changes                |
| `hooks`, `project-config`             | :gear: Internals                       |
| `template-config`                     | :construction_site: Template Internals |
| `documentation`                       | :memo: Documentation                   |
| `dependencies`                        | :arrow_up: Dependencies updates        |

## :test_tube: TODOs

This template will continue to develop and follow the bleeding edge new tools and best practices to improve the Python development experience.

Here is a list of things that have yet to be implemented:

- Tests coverage reporting with [`Coveralls`][td1];
- Auto uploading your package to [`PyPI`][td2] when new release is created;
- Automatic creation of documentation. We will be using [`Sphinx`][td3] with the [`PyData Sphinx Theme`][td4];
- Code metrics with [`Radon`][td5];
- Docstring coverage with [`interrogate`][td6];
- `Dockerfile` linting with [`dockerfilelint`][td7];
- [Hall of fame][td8] from `Sourcerer`;
- End-to-end testing and validation of the cookiecutter template;
- Add [`Earthly`][td9].

## :shield: Licence

[![Licence][b6]][b7]

This project is licenced under the terms of the `MIT` licence. See [LICENCE][b7] for more details.

## :sports_medal: Acknowledgements

Firstly, there is no way this template would exist without the previous phenomenal work by [Roman Tezikov][ac1] and his fully-featured [`python-package-template`][ft19]. If there is anyone more deserving of a :star2: and acknowledgement, it's him! Please give a shoutout and [support][ac2] if possible.

The original template was inspired by several articles that might be helpful if you are starting out managing projects:

- [Hypermodern Python][ac3];
- [Ultimate Setup for Your Next Python Project][ac4];
- [Nine simple steps for better-looking python code][ac5];
- [Modern Python developer's toolkit][ac6].

And also there are some projects which can be studied as references in project management and template design:

- [`Cookiecutter`][ac7];
- [Audreyr's `cookiecutter-pypackage`][ac8];
- [Cookiecutter Data Science Template: `cdst`][ac9];
- [Full Stack FastAPI and PostgreSQL - Base Project Generator][ac10];
- [The importance of layered thinking in data engineering][ac11].

Additionally, we would like to thank the teams of the following projects for aiding us during our research and implementation of best practices and tools for Python development:

- [Pelican][ac12].

Give them your :star:, these resources are amazing! :wink:

## :page_with_curl: Citation

```bibtex
@misc{galactipy,
  author = {Manoel Pereira de Queiroz},
  title = {Galactipy Python Package Project Generator},
  year = {2023, 2024},
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

<!-- Anchors -->

[b1]: https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue?style=for-the-badge
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
[b24]: https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge&labelColor=grey
[b25]: https://docs.astral.sh
[b26]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
[b27]: https://numpydoc.readthedocs.io/en/latest/format.html
[b28]: https://img.shields.io/badge/%F0%9F%93%A6-semantic%20versions-4053D6?style=for-the-badge
[b29]: https://img.shields.io/gitlab/pipeline-status/manoelpqueiroz%2Fgalactipy?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[b30]: https://kutt.it/zG7nVG
[b31]: https://img.shields.io/coverallsCoverage/gitlab/manoelpqueiroz/galactipy?style=for-the-badge&logo=coveralls
[b32]: https://kutt.it/uxIDHs
[b33]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[b34]: https://kutt.it/7fYqQl

[ft1]: https://cookiecutter.readthedocs.io/en/stable/
[ft2]: https://python-poetry.org/
[ft3]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/pyproject.toml
[ft4]: https://docs.astral.sh/
[ft5]: https://pre-commit.com/
[ft6]: https://mypy.readthedocs.io
[ft7]: https://docs.safetycli.com/safety-2/
[ft8]: https://bandit.readthedocs.io/en/latest/
[ft9]: https://docs.pytest.org/en/latest/
[ft10]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.vscode/settings.json
[ft11]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.editorconfig
[ft12]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.dockerignore
[ft13]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitignore
[ft14]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitlab-ci.yml
[ft15]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/workflows/build.yml
[ft16]: https://docs.pyinvoke.org/en/stable/
[ft17]: #invoke-usage
[ft18]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[ft19]: https://github.com/TezRomacH/python-package-template
[ft20]: https://docs.github.com/en/code-security/dependabot
[ft21]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[ft22]: https://github.com/marketplace/actions/release-drafter
[ft23]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/release-drafter.yml
[ft24]: https://semver.org/
[ft25]: https://docs.gitlab.com/ee/user/project/changelogs.html
[ft26]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/changelog_config.yml
[ft27]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/merge_request_templates/default.md
[ft28]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/issue_templates
[ft29]: https://shields.io/
[ft30]: https://github.com/marketplace/actions/close-stale-issues
[ft31]: https://gitlab.com/manoelpqueiroz/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/.stale.yml

[htu1]: http://ivantomic.com/projects/ospnc/
[htu2]: #gitlab-vs-github-features
[htu3]: https://typer.tiangolo.com/
[htu4]: https://rich.readthedocs.io/en/latest/
[htu5]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D
[htu6]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D#very-first-steps
[htu7]: https://python-poetry.org/docs/
[htu8]: https://python-poetry.org/docs/cli/#commands
[htu9]: https://github.com/python-poetry/install.python-poetry.org
[htu10]: https://python-poetry.org/docs/#installation
[htu11]: https://gitlab.com/manoelpqueiroz/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker

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
[wn22]: https://liberapay.com/
[wn23]: https://opencollective.com/
[wn24]: https://ko-fi.com/
[wn25]: https://github.com/sponsors
[wn26]: https://opensource.guide/
[wn27]: https://github.com/nayafia/lemonade-stand
[wn28]: https://docs.gitlab.com/ee/ci/
[wn29]: https://help.github.com/en/actions
[wn30]: https://pytest-with-eric.com/introduction/types-of-software-testing/
[wn31]: https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/
[wn32]: https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
[wn33]: https://medium.com/babylon-engineering/todo-find-a-title-for-the-article-fee79708ca15
[wn34]: https://gitmoji.dev/

[r1]: https://gitlab.com/manoelpqueiroz/galactipy/-/releases
[r2]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit

[td1]: https://coveralls.io
[td2]: https://pypi.org/
[td3]: https://github.com/sphinx-doc/sphinx
[td4]: https://github.com/pydata/pydata-sphinx-theme
[td5]: https://github.com/rubik/radon
[td6]: https://github.com/econchick/interrogate
[td7]: https://github.com/replicatedhq/dockerfilelint
[td8]: https://github.com/sourcerer-io/hall-of-fame
[td9]: https://earthly.dev/

[ac1]: https://github.com/TezRomacH
[ac2]: https://patreon.com/tezikov
[ac3]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[ac4]: https://martinheinz.dev/blog/14
[ac5]: https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf
[ac6]: https://pycon.switowski.com/
[ac7]: https://github.com/cookiecutter/cookiecutter
[ac8]: https://github.com/audreyr/cookiecutter-pypackage
[ac9]: https://github.com/crplab/cdst
[ac10]: https://github.com/tiangolo/full-stack-fastapi-postgresql
[ac11]: https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71
[ac12]: https://github.com/getpelican/pelican
