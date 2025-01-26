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
[![Code style: Ruff][b20]][b21]
[![Docstrings: numpydoc][b22]][b23]

[![Pre-commit][b24]][b25]
[![Editorconfig][b26]][b27]

[![Semantic versions][b28]][b5]
[![Code Quality][b29]][b30]
[![Coverage][b31]][b32]
[![GitLab Pipelines][b33]][b34]

_Expand your project structure from atoms of code to **galactic** dimensions._ :milky_way:
</div>

## TL;DR

```bash
cookiecutter gl:galactipy/galactipy --checkout v0.11.0
```

> All you need is the latest version of cookiecutter! :wink:

## :rocket: Features

In this [cookiecutter :cookie:][ft1] template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.9` and higher;
- Uses [`Poetry`][ft2] as the dependency manager and extends functionality with [`dynamic versioning`][ft3], [`virtual environment bundling`][ft4], dependency [`export`][ft5] and [`update resolution`][ft6]; see configuration in [`pyproject.toml`][ft7];
- Automatic code formatting with [`ruff`][ft8], with ready-to-use [`pre-commit`][ft9] hooks and several rules already selected for linting;
- Type checks with [`mypy`][ft10], security checks with [`safety`][ft11] and [`bandit`][ft12];
- Testing with [`pytest`][ft13] and an option to use [`behaviour-driven development`][ft14] for managing scenarios; more details in [Applying BDD to Your Project][ft15];
- Predefined VS Code [`settings.json`][ft16] with quality-of-life configuration for editor, workbench, debugging and more;
- Ready-to-use [`.editorconfig`][ft17], [`.dockerignore`][ft18] and [`.gitignore`][ft19] files. You don't have to worry about those things.

### Deployment features

- Issue and Merge Request templates for easy integration with GitLab and GitHub;
- Predefined CI/CD build workflow for [`GitLab CI`][ft20] and [`Github Actions`][ft21];
- Automatic package uploads to [`PyPI`][ft22] test and production repositories;
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds etc. with [`invoke`][ft23]. More details in [Invoke Usage][ft24];
- [`Dockerfile`][ft25] for your package, with CI/CD workflows to publish your image to a container registry.

#### GitLab vs. GitHub features

You are free to choose whichever platform works best for you and your project. The original template by [TezRomacH][ft26] was created originally with GitHub in mind, which prompted the creation of a similarly fully-featured template for GitLab users as well.

However, not everything that is available for GitHub users is available to GitLab users, and vice-versa. Please mind the differences between both options.

Below is a comparison between the features available in this package depending on which platform you choose to host your project:

|          **Feature**          |     **GitLab**     |     **GitHub**     | **Observations**                                                                                                                                                                                                                                            |
| :---------------------------: | :----------------: | :----------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Issue templates        | :white_check_mark: | :white_check_mark: | Both options feature automatic labels, but GitHub has an extra configuration to prevent the creation of empty issues.                                                                                                                                       |
| Merge/pull requests templates | :white_check_mark: | :white_check_mark: |                                                                                                                                                                                                                                                             |
|   Project conditions checks   | :white_check_mark: | :white_check_mark: | A basic workflow to install the package and run tests, check codestyle and safety.                                                                                                                                                                          |
|    Publication to TestPyPI    | :white_check_mark: | :white_check_mark: | For GitHub, the workflow uses the official [PyPI Publish action][ft27], while GitLab CI uses the [PyPI API][ft28].                                                                                                                                          |
|      Publication to PyPI      | :white_check_mark: | :white_check_mark: | For GitHub, trusted publishing is used with the PyPI Publish action, while GitLab CI uses the PyPI API.                                                                                                                                                     |
|       Image publication       | :white_check_mark: | :white_check_mark: | For GitHub, images are pushed to [Docker Hub][ft29], while GitLab CI pushes images to the repository's [Container Registry][ft30] by default (and can be reconfigured).                                                                                     |
|        Snapshot images        | :white_check_mark: |        :x:         | For GitLab, the [Docker][ft31] CI/CD component is used and allows for pushing snapshot images for testing when a Merge Request is open.                                                                                                                     |
|      Dockerfile linting       | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component includes a job for linting the Dockerfile with [Hadolint][ft32].                                                                                                                                                          |
| Image vulnerability analysis  | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component uses [Trivy][ft33] to scan the image for vulnerabilities.                                                                                                                                                                 |
|          SBOM files           | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component generates a bill of materials with [CycloneDX][ft34].                                                                                                                                                                     |
|         Stale issues          | :white_check_mark: | :white_check_mark: | GitLab rules are more flexible, marking stale issues only for those not opened by project members.                                                                                                                                                          |
|      Greetings workflow       |        :x:         | :white_check_mark: | GitHub provides workflows to automatically reply to issues and merge requests with the [First Interaction][ft35] action.                                                                                                                                    |
|          Dependabot           |        :x:         | :white_check_mark: | [Dependabot][ft36] is a feature now incorporated into GitHub Security. See [here][ft37] how to enable it.                                                                                                                                                   |
|        Release drafter        |        :x:         | :white_check_mark: | [Release Drafter][ft38] is a custom workflow available on GitHub Marketplace. You may see the list of labels in [`release-drafter.yml`][ft39]. Works perfectly with [Semantic Versions][ft40] specification.                                                |
|    Changelog configuration    | :white_check_mark: |        :x:         | GitLab provides automatic changelog updates through their [API][ft41]. You may modify the template in [`changelog_config.yml`][ft42].                                                                                                                       |
|  CI control over pushed tags  | :white_check_mark: |     :warning:      | GitLab provides full control for tags pushed to the repository using [regex][ft43], while GitHub Actions is more restricted in how it [filters][ft44] workflows to run, and can only apply these filters at the top level, limiting workflow customization. |

### Open source community features

- Ready-to-use [Merge Request templates][ft45] and several [Issue templates][ft46];
- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically;
- **Loads** of predefined [badges][ft47] to make your project stand out: project info, contributions, development practices, development tools and QA status; you can either keep them, remove as you wish or be welcome to add even more;
- Workflows to mark and close abandoned issues after a period of inactivity for both GitLab with [`Triage Policies`][ft48] and GitHub with [`Stale Bot`][ft49];
- [Semantic Versions][ft40] specification with [`Changelog entries`][ft41] or [`Release Drafter`][ft38].

## :exploding_head: How to use it

### Installation

To begin using the template consider updating `cookiecutter`.

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gl:galactipy/galactipy --checkout v0.11.0
```

### Input variables

Cookiecutter will ask you to fill some variables in order to generate the files with everything you need already set up.

The input variables, with their default values, are as follows:

|      **Parameter**       |      **Default value**      | **Description**                                                                                                                                                |
| :----------------------: | :-------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      `project_name`      |      `Python Project`       | A suitable name by which people will refer to, you are free to name it however you wish to.                                                                    |
|       `repo_name`        |   based on `project_name`   | Name of the repository to develop the project on. [Check the availability of possible names][htu1] before creating the project.                                |
|      `package_name`      |   based on `project_name`   | PyPI-compliant Python package name. [Check the availability of possible names][htu1] before creating the project.                                              |
|  `project_description`   |   based on `project_name`   | A brief description of your project.                                                                                                                           |
|         `author`         | `Manoel Pereira de Queiroz` | Name of the author or organisation. Used to generate `LICENCE` and to specify ownership in `pyproject.toml`.                                                   |
|      `scm_platform`      |          `GitLab`           | One of `GitLab` and `GitHub`. Depending on the choice you will have [different features][htu2] to work with.                                                   |
|      `scm_username`      |      `manoelpqueiroz`       | GitHub or GitLab username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for either platform.                               |
|         `email`          |   based on `scm_username`   | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`.                                           |
|        `licence`         |            `MIT`            | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `GNU AGLP v3.0`, `GNU LGPL v3.0`, `Mozilla Public License 2.0` and `Apache Software License 2.0`, or `Not open source`. |
| `minimal_python_version` |            `3.9`            | Minimal Python version. All versions since `3.9` are available to choose. It is used for builds, pipelines and formatters.                                     |
|        `use_ruff`        |           `True`            | :small_red_triangle: Option to use [`ruff`][ft8] as the code formatter, along with a pre-commit hook.                                                          |
|      `line_length`       |             88              | The max length per line, dismiss if `use_ruff` is not used. NOTE: This value must be between 50 and 300.                                                       |
|    `docstring_style`     |           `numpy`           | One of `numpy`, `pep257` or `google`, dismiss if `use_ruff` is not used. You can choose `other` to disable checks on your docstrings.                          |
|    `docstring_length`    |   based on `line_lenght`    | The max length for docstrings, dismiss if `use_ruff` is not used. NOTE: This value must be between 50 and 300 and lower of equal to `line_lenght`.             |
|        `use_bdd`         |           `True`            | :small_red_triangle: Option to use [behaviour-driven development][ft14] for managing tests.                                                                |
|       `create_cli`       |           `True`            | :small_red_triangle: Option to create a simple CLI application with [`Typer`][htu3] and [`Rich`][htu4] libraries.                                              |
|     `create_docker`      |           `True`            | :small_red_triangle: Option to create a [Dockerfile][ft25] to build an image for your project.                                                                 |

> :eight_spoked_asterisk: Input variables marked with :small_red_triangle: are boolean variables, you can dismiss those by typing either `0`, `false`, `f`, `no`, `n` or `off`.

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. :wink:

#### Demo

<div class="termy">

```console
$ cookiecutter gl:galactipy/galactipy
  [1/17] Project name (Python Project): A Decent Python Project
  [2/17] Project slug (a-decent-python-project): a-different-slug
  [3/17] Package name (a_decent_python_project): a_viable_package
  [4/17] Short description of the project (Awesome `a-different-slug` is a Python cli/package created with
https://gitlab.com/galactipy/galactipy): Let's try a cool description
  [5/17] Author or Organisation (The Galactipy Contributors):
  [6/17] In which platform would you like to host your code?
    1 - GitLab
    2 - GitHub
    Choose from [1/2] (1): 2
  [7/17] Platform username (galactipy): myuniqueusername
  [8/17] e-Mail (contact@myuniqueusername.com): g@mail.com
  [9/17] Which licence would you like to use for your project?
    1 - MIT Licence
    2 - 3-Clause BSD
    3 - GNU GPL v3.0
    4 - GNU AGPL v3.0
    5 - GNU LGPL v3.0
    6 - Mozilla Public License 2.0
    7 - Apache Software License 2.0
    8 - Not open source
    Choose from [1/2/3/4/5/6/7/8] (1): 4
  [10/17] Minimal Python version
    1 - 3.9
    2 - 3.10
    3 - 3.11
    4 - 3.12
    5 - 3.13
    Choose from [1/2/3/4/5] (1): 3
  [11/17] Use Ruff for linting and formatting? [y/n] (y): yes
  [12/17] Maximum line length (88):
  [13/17] Which docstring style would you like to use?
    1 - numpy
    2 - google
    3 - pep257
    4 - other
    Choose from [1/2/3/4] (1): 4
  [14/17] Docstring maximum line length (88):
  [15/17] Use behaviour-driven development for testing? [y/n] (y): 1
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

In order to release a new version of the application, a few steps are needed.

Make sure you have a PyPI account and generate an API token, you can then register it in your repository with

```bash
invoke pypi-config <API_token>
```

Then, you're all good to build and publish your package in one go!

```bash
invoke publish
```

You should also [push a tag][htu9] to `GitLab` or `GitHub` and create a `Release` for your application on the platform to ensure users can check the latest version contents.

Of course, you can also rely solely on the CI tools provided by Galactipy to handle building, publishing and releasing automatically, with minimal configuration required! :partying_face:

If you have generated your project with the Docker option enabled, pushing a tag to your repository will also set up the automated workflows to build and publish your image to a container registry.

### Invoke usage

[`invoke`][ft23] contains a lot of functions for faster development.

<details>
<summary>1. Download or remove Poetry</summary>
<p>

To download and install Poetry as a [standalone application][htu10] run:

```bash
invoke poetry-download
```

To uninstall

```bash
invoke poetry-remove
```

Alternatively, you can install it via your package manager (preferred) or any method provided by the [documentation][htu11].

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

More information about Docker [here][htu12].

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

### Applying BDD to Your Project

[Behaviour-driven development][ft14] is a software development paradigm in which domain language is used to describe the behaviour of the code. It sprang up from [test-driven development][htu13].

Think of it as a way to use natural language to describe **what** we want the code to do in order to work on it with more clarity of end-goals and reduce bugs.

In order to apply BDD, however, a crucial perspective must change: tests should be described and written _before_ the code itself. This is to make sure that the application's behaviour (what it should do and what it should _not_ do) are made very clear from the beginning.

If you choose to use BDD for your project, a `features` directory will be created under `tests` and [`pytest-bdd`][htu14] will be added as a dependency. You should place `.feature` files inside this folder to specify them and describe scenarios using the [Gherkin][htu15] language:

```
# tests/features/divide.feature
Feature: Divide numbers
  Scenario: Full division
    When I ask the calculator to divide "21" by "7"
    Then the screen should return "3" as an integer

  Scenario: Division by zero
    When I ask the calculator to divide any number by "0"
    Then the screen should return an error message
```

You would then use `pytest-bdd` to wrap each scenario referred in the feature file as a step by step validation:

```py
from mypackage import divide
from pytest_bdd import scenario, when, then

@scenario("divide.feature", "Full Division")
def test_full_division():
    pass

@when("I ask the calculator to divide \"21\" by \"7\"")
def divide_21_7():
    calculation = divide(21, 7)

    return calculation

@then("The screen should return \"3\" as an integer")
def return_integer():
    assert calculation.display == "3"


@scenario("divide.feature", "Division by Zero")
def test_zero_division():
    pass

@when("I ask the calculator to divide any number by \"0\"")
def divide_by_zero():
    calculation = divide(15, 0)

    return calculation

@then("The screen should return an error message")
def return_integer():
    assert calculation.display == "Error"
```

Then you can simply use `pytest` as you normally would to run the test suite and check the results.

For more information on behaviour-driven development and more advanced cases, please check out the [Cucumber documentation][htu16].

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

## :chart_with_upwards_trend: Galactipy Releases

You can see the list of available releases on the [GitLab Releases][r1] page.

We follow [Semantic Versions][ft40] specification.

We use [`GitLab Changelog`][ft41] entries to track changes. You can categorise commits and Merge Requests made to this project using [git trailers][r2] in your commit messages.

### List of trailers and corresponding categories

|            **Git trailer**            |       **Category in CHANGELOG**        |
| :-----------------------------------: | :------------------------------------: |
|       `enhancement`, `feature`        |           :rocket: Features            |
| `bug`, `refactoring`, `bugfix`, `fix` |      :wrench: Fixes & Refactoring      |
|       `build`, `ci`, `testing`        |     :package: Build System & CI/CD     |
|              `breaking`               |        :boom: Breaking Changes         |
|       `hooks`, `project-config`       |            :gear: Internals            |
|           `template-config`           | :construction_site: Template Internals |
|            `documentation`            |          :memo: Documentation          |
|            `dependencies`             |    :arrow_up: Dependencies updates     |

## :national_park: Roadmap

We aim to continue developing the template, following the bleeding edge new tools and best practices to improve the Python development experience, with the goal of turning Galactipy into the go-to reference for starting new projects, while giving users flexibility in how they wish to set up their repositories.

While we don't have a detailed roadmap for the project, our anticipated developments branch out in three categories.

### Features Previewed in `python-package-template`

Galactipy was born out of [`python-package-template`][ft26], developed by [Roman Tezikov][rd1] at GitHub. Roman's template was at the time the best template for Python projects for its feature richness which included the pre-configured CI workflows and `makefile` aliases that helped developers with day-to-day operations.

While the original project is now archived, there were some features Roman intended to develop and we wish to carry on for Galactipy:

- Documentation structure with [`Sphinx`][rd2] using the [`PyData Sphinx Theme`][rd3];
- Code metrics with [`Radon`][rd4];
- Docstring coverage with [`interrogate`][rd5];
- Build streamlining with [`Earthly`][rd6].

### Mirror GitHub features for GitLab

As the project started on GitHub, features like Dependabot, Release Drafter and stale issue were already set up, but require more research and complexity to implement on GitLab.

We would like Galactipy to have nearly equal functionality between GitHub and GitLab as possible, a considerable effort must be put just to ensure feature parity between the two.

### Quality-of-life Features

We also wish to implement features completely new to the template, especially aiming at streamlining development process so less time is lost setting up a new project and apply software development best practices with available tools for the Python ecosystem:

- Option to choose between test coverage or full code analysis, with providers for each yet to be selected;
- Documentation upload to [`GitLab Pages`][rd7] and [`GitHub Pages`][rd8];
- Update GitHub Actions with the latest popular and useful workflows from the marketplace;
- Add pre-commit hooks for finer control of the development cycle;
- Implement SAST for improving security of your projects.

## :shield: Licence

[![Licence][b6]][b7]

This project is licenced under the terms of the `MIT` licence. See [LICENCE][b7] for more details.

## :sports_medal: Acknowledgements

Firstly, there is no way this template would exist without the previous phenomenal work by [Roman Tezikov][rd1] and his fully-featured [`python-package-template`][ft26]. If there is anyone more deserving of a :star2: and acknowledgement, it's him! Please give a shoutout and [support][ac1] if possible.

The original template was inspired by several articles that might be helpful if you are starting out managing projects:

- [Hypermodern Python][ac2];
- [Ultimate Setup for Your Next Python Project][ac3];
- [Nine simple steps for better-looking python code][ac4];
- [Modern Python developer's toolkit][ac5].

And also there are some projects which can be studied as references in project management and template design:

- [`Cookiecutter`][ac6];
- [Audreyr's `cookiecutter-pypackage`][ac7];
- [Cookiecutter Data Science Template: `cdst`][ac8];
- [Full Stack FastAPI and PostgreSQL - Base Project Generator][ac9];
- [The importance of layered thinking in data engineering][ac10].

Additionally, we would like to thank the teams of the following projects for aiding us during our research and implementation of best practices and tools for Python development:

- [Pelican][ac11].

Give them your :star:, these resources are amazing! :wink:

<small>Galactipy Bot avatar created by [Smashicons][ac12].</small>

## :page_with_curl: Citation

```bibtex
@misc{galactipy,
  author = {Manoel Pereira de Queiroz},
  title = {Galactipy Python Package Project Generator},
  year = {2023, 2024},
  publisher = {GitLab},
  journal = {GitLab repository},
  howpublished = {\url{https://gitlab.com/galactipy/galactipy}}
}
```

Add the badge [![Expand your project structure from atoms of code to galactic dimensions.][b35]][b36] to your project! It would be really appreciated to spread the word of this template.

Here is the Markdown source for it:

```markdown
[![Expand your project structure from atoms of code to galactic dimensions.](https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E)](https://kutt.it/7fYqQl)
```

<!-- Anchors -->

[b1]: https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue?style=for-the-badge
[b2]: https://kutt.it/WlS8Qj
[b3]: https://img.shields.io/badge/GitLab-0B2640?style=for-the-badge&logo=gitlab&logoColor=white
[b4]: https://img.shields.io/gitlab/v/release/galactipy%2Fgalactipy?style=for-the-badge&logo=semantic-release&color=253747
[b5]: https://kutt.it/dFL664
[b6]: https://img.shields.io/gitlab/license/galactipy%2Fgalactipy?style=for-the-badge
[b7]: https://kutt.it/hTjpzN
[b8]: https://img.shields.io/badge/Cookiecutter-D4AA00?style=for-the-badge&logo=Cookiecutter&logoColor=white
[b9]: https://cookiecutter.readthedocs.io/en/stable/
[b10]: https://img.shields.io/badge/project%20type-toy-blue?style=for-the-badge
[b11]: https://project-types.github.io/#toy
[b12]: https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=for-the-badge
[b13]: https://kutt.it/1Q6cYr
[b14]: https://img.shields.io/gitlab/issues/open/galactipy%2Fgalactipy?style=for-the-badge&color=fca326
[b15]: https://kutt.it/2B3qIg
[b16]: https://img.shields.io/gitlab/merge-requests/open/galactipy%2Fgalactipy?style=for-the-badge&color=6fdac9
[b17]: https://kutt.it/YZ7kPX
[b18]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[b19]: https://python-poetry.org/
[b20]: https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge&labelColor=grey
[b21]: https://docs.astral.sh
[b22]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
[b23]: https://numpydoc.readthedocs.io/en/latest/format.html
[b24]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[b25]: https://kutt.it/D4ayxs
[b26]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[b27]: https://kutt.it/fy3pqF
[b28]: https://img.shields.io/badge/semantic%20versions-4053D6?style=for-the-badge&logo=semver
[b29]: https://img.shields.io/codacy/grade/9827f88089954a3680675d7c77e63fd5?style=for-the-badge&logo=codacy
[b30]: https://kutt.it/ByTvpc
[b31]: https://img.shields.io/codacy/coverage/9827f88089954a3680675d7c77e63fd5?style=for-the-badge&logo=codacy
[b32]: https://kutt.it/uxIDHs
[b33]: https://img.shields.io/gitlab/pipeline-status/galactipy%2Fgalactipy?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[b34]: https://kutt.it/zG7nVG
[b35]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[b36]: https://kutt.it/7fYqQl

[ft1]: https://cookiecutter.readthedocs.io/en/stable/
[ft2]: https://python-poetry.org/
[ft3]: https://github.com/mtkennerly/poetry-dynamic-versioning
[ft4]: https://github.com/python-poetry/poetry-plugin-bundle
[ft5]: https://github.com/python-poetry/poetry-plugin-export
[ft6]: https://github.com/MousaZeidBaker/poetry-plugin-up
[ft7]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/pyproject.toml
[ft8]: https://docs.astral.sh/
[ft9]: https://pre-commit.com/
[ft10]: https://mypy.readthedocs.io
[ft11]: https://docs.safetycli.com/safety-2/
[ft12]: https://bandit.readthedocs.io/en/latest/
[ft13]: https://docs.pytest.org/en/latest/
[ft14]: https://cucumber.io/
[ft15]: #applying-bdd-to-your-project
[ft16]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.vscode/settings.json
[ft17]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.editorconfig
[ft18]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.dockerignore
[ft19]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitignore
[ft20]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitlab-ci.yml
[ft21]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/workflows/build.yml
[ft22]: https://pypi.org/
[ft23]: https://docs.pyinvoke.org/en/stable/
[ft24]: #invoke-usage
[ft25]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[ft26]: https://github.com/TezRomacH/python-package-template
[ft27]: https://github.com/marketplace/actions/pypi-publish
[ft28]: https://docs.pypi.org/api/upload/
[ft29]: https://hub.docker.com/
[ft30]: https://docs.gitlab.com/ee/user/packages/container_registry/
[ft31]: https://gitlab.com/explore/catalog/to-be-continuous/docker
[ft32]: https://github.com/hadolint/hadolint
[ft33]: http://trivy.dev/latest/
[ft34]: https://cyclonedx.org/
[ft35]: https://github.com/marketplace/actions/first-interaction
[ft36]: https://docs.github.com/en/code-security/dependabot
[ft37]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[ft38]: https://github.com/marketplace/actions/release-drafter
[ft39]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/release-drafter.yml
[ft40]: https://semver.org/
[ft41]: https://docs.gitlab.com/ee/user/project/changelogs.html
[ft42]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/changelog_config.yml
[ft43]: https://docs.gitlab.com/ee/ci/jobs/job_rules.html#compare-a-variable-to-a-regular-expression
[ft44]: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet
[ft45]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/merge_request_templates/default.md
[ft46]: https://gitlab.com/galactipy/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/issue_templates
[ft47]: https://shields.io/
[ft48]: https://gitlab.com/explore/catalog/components/gitlab-triage
[ft49]: https://github.com/marketplace/actions/close-stale-issues

[htu1]: http://ivantomic.com/projects/ospnc/
[htu2]: #gitlab-vs-github-features
[htu3]: https://typer.tiangolo.com/
[htu4]: https://rich.readthedocs.io/en/latest/
[htu5]: https://gitlab.com/galactipy/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D
[htu6]: https://gitlab.com/galactipy/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D#very-first-steps
[htu7]: https://python-poetry.org/docs/
[htu8]: https://python-poetry.org/docs/cli/#commands
[htu9]: https://git-scm.com/book/en/v2/Git-Basics-Tagging
[htu10]: https://github.com/python-poetry/install.python-poetry.org
[htu11]: https://python-poetry.org/docs/#installation
[htu12]: https://gitlab.com/galactipy/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker
[htu13]: https://tidyfirst.substack.com/p/canon-tdd
[htu14]: https://pytest-bdd.readthedocs.io/en/latest/
[htu15]: https://cucumber.io/docs/gherkin/reference
[htu16]: https://cucumber.io/docs

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

[r1]: https://gitlab.com/galactipy/galactipy/-/releases
[r2]: https://docs.gitlab.com/ee/user/project/changelogs.html#add-a-trailer-to-a-git-commit

[rd1]: https://github.com/TezRomacH
[rd2]: https://github.com/sphinx-doc/sphinx
[rd3]: https://github.com/pydata/pydata-sphinx-theme
[rd4]: https://github.com/rubik/radon
[rd5]: https://github.com/econchick/interrogate
[rd6]: https://earthly.dev/
[rd7]: https://docs.gitlab.com/ee/user/project/pages/
[rd8]: https://pages.github.com/

[ac1]: https://patreon.com/tezikov
[ac2]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[ac3]: https://martinheinz.dev/blog/14
[ac4]: https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf
[ac5]: https://pycon.switowski.com/
[ac6]: https://github.com/cookiecutter/cookiecutter
[ac7]: https://github.com/audreyr/cookiecutter-pypackage
[ac8]: https://github.com/crplab/cdst
[ac9]: https://github.com/tiangolo/full-stack-fastapi-postgresql
[ac10]: https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71
[ac11]: https://github.com/getpelican/pelican
[ac12]: https://www.flaticon.com/free-icons/robot
