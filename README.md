# Galactipy

<div align="center">

<!-- Project details -->
[![Python support][b1]][b2]
[![Repository][b3]][b2]
[![Releases][b4]][b5]
[![Licence][b6]][b7]
[![Cookiecutter template][b8]][b9]

<!-- Information on development -->
[![Project type][b10]][b11]
[![Contributions Welcome][b12]][b13]
[![Open issues][b14]][b15]
[![Merge Requests][b16]][b17]

<!-- Styling policies -->
[![Code style: Ruff][b18]][b19]
[![Docstrings: numpydoc][b20]][b21]
[![Gitmoji][b22]][b23]
[![Semantic Line Breaks][b24]][b25]

<!-- Development utilities -->
[![Poetry][b26]][b27]
[![Pre-commit][b28]][b29]
[![Editorconfig][b30]][b31]

<!-- Quality Assurance -->
[![Intended Effort versioning][b32]][b5]
[![Code Quality][b33]][b34]
[![Coverage][b35]][b36]
[![GitLab Pipelines][b37]][b38]

_Expand your project structure from atoms of code to **galactic** dimensions._ :milky_way:
</div>

## TL;DR

```bash
cookiecutter gl:galactipy/galactipy --checkout v0.18.2
```

**All you need is the latest version of cookiecutter!** :wink:

## :rocket: Features

In this [cookiecutter :cookie:][ft1] template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.9` and higher;
- Provides
  minimal boilerplate code
  for CLI/TUI applications
  with [`Typer`][ft2] and [`Textual`][ft3]
  -- or no code at all, you choose!
- Turns configuration setup
  and management
  for your application
  super easy
  with [`Dynamanager`][ft4];
- Uses [`Poetry`][ft5] as the dependency manager and extends functionality with [`dynamic versioning`][ft6], [`virtual environment bundling`][ft7], dependency [`export`][ft8] and [`update resolution`][ft9]; see configuration in [`pyproject.toml`][ft10];
- Automatic code formatting with [`ruff`][b19], with ready-to-use [`pre-commit`][ft11] hooks and several rules already selected for linting;
- Type checks with [`mypy`][ft12], security checks with [`bandit`][ft13];
- Testing with [`pytest`][ft14] and an option to use [`behaviour-driven development`][ft15] for managing scenarios; more details in [Applying BDD to Your Project][ft16];
- Code quality integrations with either [`Coveralls`][ft17] for more basic test coverage or [`Codacy`][ft18] for full code analysis, both integrated into your project's workflow via CI/CD;
- Predefined VS Code [`settings.json`][ft19] with quality-of-life configuration for editor, workbench, debugging and more;
- Ready-to-use [`.editorconfig`][ft20], [`.dockerignore`][ft21] and [`.gitignore`][ft22] files. You don't have to worry about those things.

### Deployment features

- Predefined CI/CD build workflow with [`GitLab CI`][ft23] and [`Github Actions`][ft24];
- Automatic package uploads to [`PyPI`][ft25] test and production repositories;
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds etc. with [`invoke`][ft26]. More details in [Invoke Usage][ft27];
- [`Dockerfile`][ft28] for your package, with CI/CD workflows to publish your image to a container registry.
- [Semantic Versions][ft29] specification with [`Changelog entries`][ft30] or [`Release Drafter`][ft31].

### Project management features

- Ready-to-use [Merge Request templates][ft32] and several [Issue templates][ft33] for easy integration with GitLab and GitHub;
- Workflows to mark and close abandoned issues after a period of inactivity for both GitLab with [`Triage Policies`][ft34] and GitHub with [`Stale Bot`][ft35];
- Option to choose between [Gitmoji][b23], [Conventional Commits][ft36] or a mix of both to standardise your commit titles.

### Open source community features

- Files such as: `LICENCE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CITATION.cff` and `SECURITY.md` are generated automatically;
- **Loads** of predefined [badges][ft37] to make your project stand out: project info, contributions, development practices, development tools and QA status; you can either keep them, remove as you wish or be welcome to add even more.

### GitLab vs. GitHub feature comparison chart

You are free to choose whichever platform works best for you and your project. The original template by [TezRomacH][ft38] was created originally with GitHub in mind, which prompted the creation of a similarly fully-featured template for GitLab users as well.

However, not everything that is available for GitHub users is available to GitLab users, and vice-versa. Please mind the differences between both options.

Below is a comparison between the features available in this package depending on which platform you choose to host your project:

|          **Feature**          |     **GitLab**     |     **GitHub**     | **Observations**                                                                                                                                                                                                                                            |
| :---------------------------: | :----------------: | :----------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Issue templates        | :white_check_mark: | :white_check_mark: | Both options feature automatic labels, but GitHub has an extra configuration to prevent the creation of empty issues.                                                                                                                                       |
| Merge/pull requests templates | :white_check_mark: | :white_check_mark: |                                                                                                                                                                                                                                                             |
|   Project conditions checks   | :white_check_mark: | :white_check_mark: | A basic workflow to install the package and run tests, check codestyle and safety.                                                                                                                                                                          |
|    Publication to TestPyPI    | :white_check_mark: | :white_check_mark: | For GitHub, the workflow uses the official [PyPI Publish action][ft39], while GitLab CI uses the [PyPI API][ft40].                                                                                                                                          |
|      Publication to PyPI      | :white_check_mark: | :white_check_mark: | For GitHub, trusted publishing is used with the PyPI Publish action, while GitLab CI uses the PyPI API.                                                                                                                                                     |
|       Image publication       | :white_check_mark: | :white_check_mark: | For GitHub, images are pushed to [Docker Hub][ft41], while GitLab CI pushes images to the repository's [Container Registry][ft42] by default (and can be reconfigured).                                                                                     |
|        Snapshot images        | :white_check_mark: |        :x:         | For GitLab, the [Docker][ft43] CI/CD component is used and allows for pushing snapshot images for testing when a Merge Request is open.                                                                                                                     |
|      Dockerfile linting       | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component includes a job for linting the Dockerfile with [Hadolint][ft44].                                                                                                                                                          |
| Image vulnerability analysis  | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component uses [Trivy][ft45] to scan the image for vulnerabilities.                                                                                                                                                                 |
|          SBOM files           | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component generates a bill of materials with [CycloneDX][ft46].                                                                                                                                                                     |
|         Stale issues          | :white_check_mark: | :white_check_mark: | GitLab rules are more flexible, marking stale issues only for those not opened by project members.                                                                                                                                                          |
|      Greetings workflow       |        :x:         | :white_check_mark: | GitHub provides workflows to automatically reply to issues and merge requests with the [First Interaction][ft47] action.                                                                                                                                    |
|          Dependabot           |        :x:         | :white_check_mark: | [Dependabot][ft48] is a feature now incorporated into GitHub Security. See [here][ft49] how to enable it.                                                                                                                                                   |
|        Release drafter        |        :x:         | :white_check_mark: | [Release Drafter][ft31] is a custom workflow available on GitHub Marketplace. You may see the list of labels in [`release-drafter.yml`][ft50]. Works perfectly with [Semantic Versions][ft29] specification.                                                |
|    Changelog configuration    | :white_check_mark: |        :x:         | GitLab provides automatic changelog updates through their [API][ft30]. You may modify the template in [`changelog_config.yml`][ft51].                                                                                                                       |
|         Test Reports          | :white_check_mark: |        :x:         | JUnit XML reports are supported by GitLab to allow [test reports][ft52] to be displayed in pipelines and merge requests.                                                                                                                                    |
|  CI control over pushed tags  | :white_check_mark: |     :warning:      | GitLab provides full control for tags pushed to the repository using [regex][ft53], while GitHub Actions is more restricted in how it [filters][ft54] workflows to run, and can only apply these filters at the top level, limiting workflow customization. |

## :exploding_head: How to use it

### Installation

To begin using the template consider updating `cookiecutter`:

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gl:galactipy/galactipy --checkout v0.18.2
```

### Input variables

Cookiecutter will ask you to fill some variables in order to generate the files with everything you need already set up.

The input variables, with their default values, are as follows:

|      **Parameter**       |      **Default value**       | **Description**                                                                                                                                                                                                                                                                                 |
| :----------------------: | :--------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      `project_name`      |       `Python Project`       | A suitable name by which people will refer to, you are free to name it however you wish to.                                                                                                                                                                                                     |
|       `repo_name`        |   based on `project_name`    | Name of the repository to develop the project on. [Check the availability of possible names][htu1] before creating the project.                                                                                                                                                                 |
|      `package_name`      |   based on `project_name`    | PyPI-compliant Python package name. [Check the availability of possible names][htu1] before creating the project.                                                                                                                                                                               |
|  `project_description`   |   based on `project_name`    | A brief description of your project.                                                                                                                                                                                                                                                            |
|         `author`         | `The Galactipy Contributors` | Name of the author or organisation. Used to generate `LICENCE` and to specify ownership in `pyproject.toml`.                                                                                                                                                                                    |
|      `scm_platform`      |        `GitLab Free`         | One of `GitLab Free`, `GitLab Premium/Ultimate` and `GitHub`. Depending on the choice you will have [different features][htu2] to work with.                                                                                                                                                    |
|     `scm_namespace`      |         `galactipy`          | GitHub or GitLab namespace for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for either platform.                                                                                                                                                               |
|         `email`          |   based on `scm_namespace`   | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`.                                                                                                                                                                            |
|        `licence`         |            `MIT`             | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `GNU AGLP v3.0`, `GNU LGPL v3.0`, `Mozilla Public License 2.0` and `Apache Software License 2.0`, or `Not open source`.                                                                                                                                  |
| `minimal_python_version` |            `3.9`             | Minimal Python version. All versions since `3.9` are available to choose. It is used for builds, pipelines and formatters.                                                                                                                                                                      |
|      `line_length`       |              88              | The max length per line. NOTE: This value must be between 50 and 300.                                                                                                                                                                                                                           |
|    `docstring_style`     |           `numpy`            | One of `numpy`, `pep257` or `google`. You can choose `other` to disable checks on your docstrings.                                                                                                                                                                                              |
|    `docstring_length`    |    based on `line_lenght`    | The max length for docstrings. NOTE: This value must be between 50 and 300 and lower of equal to `line_lenght`.                                                                                                                                                                                 |
|        `use_bdd`         |            `True`            | :small_red_triangle: Option to use [behaviour-driven development][ft15] for managing tests.                                                                                                                                                                                                     |
|    `coverage_service`    |         `Coveralls`          | One of `Coveralls` for code coverage and `Codacy` for code quality and static analysis.                                                                                                                                                                                                         |
|        `app_type`        |     `Integrated CLI+TUI`     | One of `Integrated CLI+TUI` for a straight TUI application, `Hybrid CLI/TUI` for a CLI application with a preset TUI command, `CLI-only application` with minimal app configuration and `Bare repository` for no sample files at all. Employs [`Typer`][ft2] and [`Textual`][ft3] as libraries. |
|     `create_docker`      |            `True`            | :small_red_triangle: Option to create a [Dockerfile][ft28] to build an image for your project.                                                                                                                                                                                                  |

> [!note]
> Input variables marked with :small_red_triangle: are boolean variables, you can dismiss those by typing either `0`, `false`, `f`, `no`, `n` or `off`.

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. :wink:

### Initial set up

You must have [Poetry][b27] installed
to leverage the features
provided with the Galactipy template.

After creating a project,
ensure you have [Invoke][ft26] installed
and run
the following command
to install dependencies and pre-commit hooks:

```bash
invoke install
```

If you don't have Invoke
available in your system,
run this instead:

```bash
poetry install
invoke hooks
```

Want to know more about Poetry?
Check [its documentation][htu3].
Poetry's [commands][htu4]
are very intuitive
and easy to learn,
streamlining your development process.

### Sample Application

Galactipy is best used
for terminal applications,
either a TUI
or a simple CLI interface.
If you choose any of the options for `app_type`
excluding `Bare repository`,
your project will embed [`Typer`][ft2]
as a dependency,
and [`Textual`][ft3] will be provided for
the `Integrated CLI+TUI` and `Hybrid CLI/TUI` options.

For any of the options providing an interface,
you can call the application
after setting up the virtual environment
via `invoke install` or `poetry install`:

```bash
poetry run <repo_name> --help
```

```bash
poetry run <repo_name> --version
```

Then you can use
the structure provided with Galactipy
to build your application
upon the barebones codebase. :smile:

### Building and releasing your package

To release
a new version of the application,
you must first
have a [PyPI][ft25] account
and generate an API token.

Then, add the registry
to the Poetry configuration with

```bash
invoke config <API_token>
```

You'll be all set
to build and publish your package
in one go!

```bash
invoke publish
```

You should also [push a tag][htu5]
to `GitLab` or `GitHub`
and create a `Release` for your application,
enabling users to
download, track and inspect
the changes
made to the API.

Of course,
you can also
rely solely on the CI tools
provided by Galactipy
to handle building, publishing and releasing automatically,
with minimal configuration required! :partying_face:

>>> [!note]
To allow releasing
directly via CI/CD workflows,
besides setting up
a canonical PyPI token,
you must also
generate a API toke
for the [TestPyPI][htu6] repository.
>>>

If you have generated your project
with the Docker option enabled,
pushing a tag to your repository
will also set up the automated workflows
to build and publish your image
to a container registry.

### Invoke Usage

[`invoke`][ft26] is a library that
enables easy configuration of
shell-oriented subprocesses
as Python functions,
essentially organising a collection of aliases
for all project developers to use.

Below is a list
with the main task groups
and details when relevant.
Available tasks can be viewed
at anytime
with the `invoke --list` command.

#### Environment Setup

|      Command       | Details                                                                                                                                 |
| :----------------: | --------------------------------------------------------------------------------------------------------------------------------------- |
|  `invoke install`  | :small_red_triangle: Sets up the Poetry virtual environment, installs the dependencies, pre-commit hooks and runs a [Mypy][ft12] check. |
| `invoke pyproject` | Checks `pyproject.toml` integrity.                                                                                                      |
|  `invoke update`   | Updates dependencies to their latest compatible release requirements, with an option to update to the latest versions overall.          |

>>> [!warning]
:small_red_triangle: Invoke must be installed and callable.
Otherwise, it is recommended to run `poetry install`
to set up the repository.
>>>

#### Quality Assurance Tasks

|      Command       | Details                                                                                          |
| :----------------: | ------------------------------------------------------------------------------------------------ |
| `invoke codestyle` | Format files with [Ruff][b19], with an option to check files only.                               |
|   `invoke lint`    | Check compliance with linting rules, with an option to correct those considered fixable by Ruff. |
|   `invoke mypy`    | Run [Mypy][ft12] to check for static typing.                                                     |
|   `invoke test`    | Run the test suite with [Pytest][ft14].                                                          |
| `invoke coverage`  | Generate the coverage file for upload to [Coveralls][ft17] or [Codacy][ft18].                    |
| `invoke security`  | Run security checks with [Bandit][ft13] and check `pyproject.toml` integrity.                    |

The **`invoke sweep`** task groups all tasks
except for `coverage`
into a single command.

#### Project Building & Publishing

|     Command      | Details                                                                                                                             |
| :--------------: | ----------------------------------------------------------------------------------------------------------------------------------- |
|  `invoke build`  | Build the project wheels.                                                                                                           |
| `invoke config`  | :small_red_triangle: Configure PyPI repositories, requiring at least an API token, with optional repository name and URL arguments. |
| `invoke publish` | Publish the project to a registry, defaulting to the canonical PyPI repository, with an option to build the project wheels.         |

>>> [!note]
:small_red_triangle: When provided with no `--repo` option,
Invoke will configure the connection
to the [canonical PyPI repository][ft25],
with only the API token being required.
When provided with the `--repo testpypi` option instead,
it will configure the connection
to [TestPyPI][htu6]
and no URL is needed.
Other `--repo` values must also
receive a `--url` argument
pointing to the desired custom registry.
>>>

#### Docker Operations

|      Command       | Details                                                                                                                                                             |
| :----------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   `invoke login`   | Log in to a container registry. For GitHub users, points to [Docker Hub][ft41]. For GitLab users, points to the repository's [integrated container registry][ft42]. |
| `invoke container` | Build local container images, with the option to set multiple tags and an alternate repository to point.                                                            |
|   `invoke push`    | Push all project images to a container registry, with the option to set an alternate repository to push.                                                            |
|   `invoke prune`   | Remove all local images built for the project, with the option to set an alternate repository to point.                                                             |

#### Cleanup Tasks

|         Command         | Details                                                                                                         |
| :---------------------: | --------------------------------------------------------------------------------------------------------------- |
|  `invoke remove-cache`  | Remove `__pycache__` files from the local repository.                                                           |
| `invoke remove-dsstore` | Remove the `.DS_Store` directory from the local repository.                                                     |
|  `invoke remove-mypy`   | Remove the `.mypy_cache` directory from the local repository.                                                   |
|  `invoke remove-ipynb`  | Remove the `.ipynb_checkpoints` directory from the local repository.                                            |
| `invoke remove-pytest`  | Remove the `.pytest_cache` directory and the `.coverage` and `test_report.xml` files from the local repository. |
|  `invoke remove-ruff`   | Remove the `.ruff_cache` directory from the local repository.                                                   |
|  `invoke remove-build`  | Remove wheels built locally.                                                                                    |

The **`invoke cleanup`** task groups all tasks
except for `remove-build`
into a single command.

### Use BDD for handling the development cycle

[Behaviour-driven development][ft15] is a software development paradigm
in which domain language is used
to describe the behaviour of the code.
It emerged as a
sophisticated evolution
of [test-driven development][htu7].

If you choose to use BDD for your project,
a `features` directory will be created under `tests`
and [`pytest-bdd`][htu8] will be added as a dependency.
You should place `.feature` files inside this folder
to describe **real-life** usage scenarios
using the [Gherkin][htu9] language:

```
# tests/features/root_command.feature
Feature: Command-line interface

  Scenario: Invoke with version argument
    When the program is called with the `--version` argument
    Then the program's version is displayed
    And the program is terminated without errors
```

You would then use `pytest-bdd`
to wrap each scenario
referred in the feature file
as a step-by-step validation:

```py
from typer.testing import CliRunner
from python_project.cli.root_command import app
from pytest_bdd import scenario, when, then, parsers

runner = CliRunner()

@scenario("root_command.feature", "Check program version")
def test_cli_with_version_arg():
    pass

@when("the root program receives the `--version` option", target_fixture="cli_run")
def invoke_version_arg():
    return runner.invoke(app, args=["--version"])

@then("the terminal displays the program's version")
def version_display(cli_run, version_string):
    assert cli_run.stdout == version_string

@then("the program exits without errors")
def successful_termination(cli_run):
    assert cli_run.exit_code == 0
```

Once the tests are defined,
you can simply use `pytest`
as you normally would
to run the test suite
and check the results.

For more information on behaviour-driven development
and tools to handle
more complex conditions,
please check out the [Cucumber documentation][htu10].

## :dart: What's next

Well, that's up to you. :muscle:

For further setting up your project:

- Look for files and sections marked with `TODO` (which must be addressed in order for your project to run properly) and `UPDATEME` (optional settings if you feel inclined to);
  - If you use VS Code, install the [`Todo Tree`][wn1] extension to easily locate and jump to these marks, they are already configured in the `settings.json` file;
- Make sure to create your desired Issue labels on your platform before you start tracking them so it ensures you will be able to filter them from the get-go;
- Make changes to your CI configurations to better suit your needs.

- In order to reduce user prompts and keep things effective, the template generates files with a few assumptions:
  - It assumes your main git branch is `master`. If you wish to use another branch name for development, be aware of changes you will have to make in the Issue and Merge Request templates and `README.md` file so links won't break when you push them to your repo;
  - It generates a PyPI badge assuming you will be able to publish your project under `repo_name`, change it otherwise;
  - It generates a Docker badge assuming you also use `scm_namespace` for Docker Hub and you will push your image under `repo_name`, change it otherwise;

If you want to put your project on steroids, here are a few Python tools which can help you depending on what you want to achieve with your application:

- [`Rich`][wn2] makes it easy to add beautiful formatting in the terminal. If you chose to generate a TUI or CLI example during the Cookiecutter setup, `Rich` will already be among your dependencies;
- [`tqdm`][wn3] is a fast, extensible progress bar for Python and CLI;
- [`orjson`][wn4], an ultra fast JSON parsing library;
- [`Pydantic`][wn5] is data validation and settings management using Python type hinting;
- [`Returns`][wn6] makes you function's output meaningful, typed, and safe;
- [`Loguru`][wn7] makes logging (stupidly) simple;
- [`IceCream`][wn8] is a little library for sweet and creamy debugging;
- [`Hydra`][wn9] is a framework for elegantly configuring complex applications;
- [`FastAPI`][wn10] is a type-driven asynchronous web framework.

For taking development and exposition of your project to the next level:

- Try out some more badges, not only it looks good, but it also helps people better understand some intricate details on how your project works:
  - You can look at dynamic badges available at [`Shields.io`][wn11];
  - There is a myriad of standardised static badges at [`Simple Badges`][wn12];
  - [`awesome-badges`][wn13] provides a lot of useful resources to help you deal with badges;
- Add your project to [`OpenSSF Best Practices`][wn14] and [`OSSRank`][wn15] indexes. If you have greater ambitions for your project and/or expects it to scale at some point, it's worth considering adding it to these trackers;
  - There are already badges for those set up in your `README.md` file, just waiting for you to update their URLs with your project's index in both services; :grinning:
- Setup a sponsorship page and allow users and organisations who appreciate your project to help raise for its development (and add a badge in the process! :sunglasses:). Popular platforms are:
  - [`Liberapay`][wn16];
  - [`Open Collective`][wn17];
  - [`Ko-fi`][wn18];
  - If you host on GitHub, you can set a [Sponsors account][wn19] directly integrated into the platform;
  - Of course, you can also set any kind of gateway you wish, what works best for you and your project!
- If you are unsure about the versioning logic to use, check [this list][wn20] with a plethora of options to choose from.

And here are a few articles which may help you:

- [Open Source Guides][wn21];
- [A handy guide to financial support for open source][wn22];
- [GitLab CI Documentation][wn23];
- [GitHub Actions Documentation][wn24];
- [A Comprehensive Look at Testing in Software Development][wn25] is an article that lays out why testing is crucial for development success. Eric's blog is actually a great reference, covering topics ranging from the basics to advanced techniques and best practices;
- [Robust Exception Handling][wn26];
- [Why Your Mock Doesn't Work][wn27];
- [Managing TODOs in a codebase][wn28].

## :chart_with_upwards_trend: Galactipy Releases

You can see the list of available releases on the [GitLab Releases][r1] page.

We follow [Intended Effort Versioning][r2] specification, details can be found in our
[`CONTRIBUTING`][r3] guide.

## :map: Roadmap

Galactipy's roadmap is managed through our [Milestones][rd1] page, which lays out the
current development streams mapped for delivery. All official details on development,
timeline and deliverables are found through those pages. The project's milestones are
also presented in the [`ROADMAP`][rd2] file purely for informational purposes.

## :shield: Licence

[![Licence][b6]][b7]

This project is licenced under the terms of the MIT licence. See [`LICENCE`][b7] for more details.

## :sports_medal: Acknowledgements

Firstly, there is no way this template would exist without the previous phenomenal work by [Roman Tezikov][ac1] and his fully-featured [`python-package-template`][ft38]. If there is anyone more deserving of a :star2: and acknowledgement, it's him! Please give a shoutout and [support][ac2] if possible.

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

Additionally, we would like to thank the teams of the following projects for either aiding us directly during our research of best practices and tools for Python development or whose documentation have inspired parts of the project:

- [Pelican][ac12];
- [Spark][ac13];
- [React][ac14];
- [Chai][ac15];
- [Harbor][ac16].

Give them your :star:, these resources are amazing! :wink:

<small>Galactipy Bot avatar created by [Smashicons][ac17].</small>

## :page_with_curl: Citation

We provide a [`CITATION.cff`][cite1] file to make it easier to cite this project in your
paper.

## :mega: Spread the Word

Add the badge [![Expand your project structure from atoms of code to galactic dimensions.][b39]][b40] to your project! It would be really appreciated to spread the word of this template.

Here is the Markdown source for it:

```markdown
[![Expand your project structure from atoms of code to galactic dimensions.](https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E)](https://kutt.it/7fYqQl)
```

We would be equally grateful if you could also do any of the following:

- Set the notification level to **"Watch"** to receive our latest updates; :bell:
- Star the project! :star2:
- Share the project with colleagues; :speaking_head:
- Write a short article on how you are using Galactipy on your projects; :pencil2:
- Share best practices, references and tools for project management with us! :beers:

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
[b18]: https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge&labelColor=grey
[b19]: https://docs.astral.sh/
[b20]: https://img.shields.io/badge/docstrings-numpydoc-4dabcf?style=for-the-badge&labelColor=4d77cf
[b21]: https://numpydoc.readthedocs.io/en/latest/format.html
[b22]: https://img.shields.io/badge/%F0%9F%98%9C_gitmoji-ffdd67?style=for-the-badge
[b23]: https://gitmoji.dev/
[b24]: https://img.shields.io/badge/sembr-367DA9?style=for-the-badge&logo=read.cv&logoColor=white
[b25]: https://sembr.org/
[b26]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[b27]: https://python-poetry.org/
[b28]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[b29]: https://kutt.it/D4ayxs
[b30]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[b31]: https://kutt.it/fy3pqF
[b32]: https://img.shields.io/badge/effver-0097a7?style=for-the-badge&logo=semver
[b33]: https://img.shields.io/codacy/grade/9827f88089954a3680675d7c77e63fd5?style=for-the-badge&logo=codacy
[b34]: https://kutt.it/ByTvpc
[b35]: https://img.shields.io/codacy/coverage/9827f88089954a3680675d7c77e63fd5?style=for-the-badge&logo=codacy
[b36]: https://kutt.it/uxIDHs
[b37]: https://img.shields.io/gitlab/pipeline-status/galactipy%2Fgalactipy?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[b38]: https://kutt.it/zG7nVG
[b39]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[b40]: https://kutt.it/7fYqQl

[ft1]: https://cookiecutter.readthedocs.io/en/stable/
[ft2]: https://typer.tiangolo.com/
[ft3]: https://textual.textualize.io/
[ft4]: https://gitlab.com/galactipy/dynamanager
[ft5]: https://python-poetry.org/
[ft6]: https://github.com/mtkennerly/poetry-dynamic-versioning
[ft7]: https://github.com/python-poetry/poetry-plugin-bundle
[ft8]: https://github.com/python-poetry/poetry-plugin-export
[ft9]: https://github.com/MousaZeidBaker/poetry-plugin-up
[ft10]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/pyproject.toml
[ft11]: https://pre-commit.com/
[ft12]: https://mypy.readthedocs.io
[ft13]: https://bandit.readthedocs.io/en/latest/
[ft14]: https://docs.pytest.org/en/latest/
[ft15]: https://cucumber.io/
[ft16]: #use-bdd-for-handling-the-development-cycle
[ft17]: https://coveralls.io/
[ft18]: https://www.codacy.com/
[ft19]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.vscode/settings.json
[ft20]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.editorconfig
[ft21]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.dockerignore
[ft22]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitignore
[ft23]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitlab-ci.yml
[ft24]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/workflows/build.yml
[ft25]: https://pypi.org/
[ft26]: https://docs.pyinvoke.org/en/stable/
[ft27]: #invoke-usage
[ft28]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[ft29]: https://semver.org/
[ft30]: https://docs.gitlab.com/ee/user/project/changelogs.html
[ft31]: https://github.com/marketplace/actions/release-drafter
[ft32]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/merge_request_templates/default.md
[ft33]: https://gitlab.com/galactipy/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/issue_templates
[ft34]: https://gitlab.com/explore/catalog/components/gitlab-triage
[ft35]: https://github.com/marketplace/actions/close-stale-issues
[ft36]: https://www.conventionalcommits.org/en/v1.0.0/
[ft37]: https://shields.io/
[ft38]: https://github.com/TezRomacH/python-package-template
[ft39]: https://github.com/marketplace/actions/pypi-publish
[ft40]: https://docs.pypi.org/api/upload/
[ft41]: https://hub.docker.com/
[ft42]: https://docs.gitlab.com/ee/user/packages/container_registry/
[ft43]: https://gitlab.com/explore/catalog/to-be-continuous/docker
[ft44]: https://github.com/hadolint/hadolint
[ft45]: http://trivy.dev/latest/
[ft46]: https://cyclonedx.org/
[ft47]: https://github.com/marketplace/actions/first-interaction
[ft48]: https://docs.github.com/en/code-security/dependabot
[ft49]: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates#enabling-dependabot-version-updates
[ft50]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/release-drafter.yml
[ft51]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/changelog_config.yml
[ft52]: https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html
[ft53]: https://docs.gitlab.com/ee/ci/jobs/job_rules.html#compare-a-variable-to-a-regular-expression
[ft54]: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet

[htu1]: http://ivantomic.com/projects/ospnc/
[htu2]: #gitlab-vs-github-features
[htu3]: https://python-poetry.org/docs/
[htu4]: https://python-poetry.org/docs/cli/#commands
[htu5]: https://git-scm.com/book/en/v2/Git-Basics-Tagging
[htu6]: https://test.pypi.org/
[htu7]: https://tidyfirst.substack.com/p/canon-tdd
[htu8]: https://pytest-bdd.readthedocs.io/en/latest/
[htu9]: https://cucumber.io/docs/gherkin/reference
[htu10]: https://cucumber.io/docs

[wn1]: https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree
[wn2]: https://github.com/willmcgugan/rich
[wn3]: https://github.com/tqdm/tqdm
[wn4]: https://github.com/ijl/orjson
[wn5]: https://github.com/samuelcolvin/pydantic/
[wn6]: https://github.com/dry-python/returns
[wn7]: https://github.com/Delgan/loguru
[wn8]: https://github.com/gruns/icecream
[wn9]: https://github.com/facebookresearch/hydra
[wn10]: https://github.com/tiangolo/fastapi
[wn11]: https://shields.io/badges/static-badge
[wn12]: https://badges.pages.dev/
[wn13]: https://github.com/badges/awesome-badges
[wn14]: https://www.bestpractices.dev/en
[wn15]: https://ossrank.com/
[wn16]: https://liberapay.com/
[wn17]: https://opencollective.com/
[wn18]: https://ko-fi.com/
[wn19]: https://github.com/sponsors
[wn20]: https://nesbitt.io/2024/06/24/from-zerover-to-semver-a-comprehensive-list-of-versioning-schemes-in-open-source.html
[wn21]: https://opensource.guide/
[wn22]: https://github.com/nayafia/lemonade-stand
[wn23]: https://docs.gitlab.com/ee/ci/
[wn24]: https://help.github.com/en/actions
[wn25]: https://pytest-with-eric.com/introduction/types-of-software-testing/
[wn26]: https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/
[wn27]: https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
[wn28]: https://medium.com/babylon-engineering/todo-find-a-title-for-the-article-fee79708ca15

[r1]: https://gitlab.com/galactipy/galactipy/-/releases
[r2]: https://jacobtomlinson.dev/effver/
[r3]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#versioning-customs

[rd1]: https://gitlab.com/galactipy/galactipy/-/milestones
[rd2]: https://gitlab.com/galactipy/galactipy/-/blob/master/ROADMAP.md

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
[ac13]: https://github.com/apache/spark
[ac14]: https://github.com/facebook/react/
[ac15]: https://github.com/chaijs/chai
[ac16]: https://github.com/goharbor/harbor
[ac17]: https://www.flaticon.com/free-icons/robot

[cite1]: https://gitlab.com/galactipy/galactipy/-/blob/master/CITATION.cff
