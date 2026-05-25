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
[![Renovate Badge][b30]][b31]
[![Editorconfig][b32]][b33]

<!-- Quality Assurance -->
[![Romantic Versioning][b34]][b5]
[![Code Quality][b35]][b36]
[![Coverage][b37]][b38]
[![GitLab Pipelines][b39]][b40]

_Expand your project structure from atoms of code to **galactic** dimensions._ :milky_way:

</div>

## TL;DR

```bash
cookiecutter gl:galactipy/galactipy --checkout v3.3.0
```

**All you need is the latest version of Cookiecutter!** :wink:

## :sparkles: Features

In this [Cookiecutter :cookie:][cookie] template
we combine state-of-the-art libraries
and best development practices for Python.

### :race_car: Start Developing Your App out of the Box

- Supports Python **`3.10`** and higher;
- Provides
  minimal boilerplate code
  for CLI/TUI applications
  with [**Typer**][ft1] and [**Textual**][ft2]
  (or no code at all, you choose)!
  With it, you have:
  - Batteries-included
    configuration setup
    and management
    with [**Orbittings**][ft3];
  - Both
    beautiful logging
    on the terminal
    and easy-to-parse log files
    thanks to [**Nebulog**][ft4];
  - Preconfigured [Noctis][ft5] themes
    to make your application
    shine on the terminal;
- Uses [**Poetry**][ft6]
  as the dependency manager
  and extends functionality
  with [dynamic versioning][ft7],
  [virtual environment bundling][ft8],
  [dependency export][ft9]
  and [update resolution][ft10];
  see configuration
  in [`pyproject.toml`][ft11];
- Automatic code formatting with [**Ruff**][b19],
  with ready-to-use [**pre-commit**][ft12] hooks
  and several rules
  already selected for linting;
- Type checks with [**mypy**][ft13],
  security checks with [**Bandit**][ft14];
- Testing with [**Pytest**][ft15]
  and an option
  to use [behaviour-driven development][ft16]
  for managing scenarios;
  more details in [_How to Handle the Development Cycle with BDD_][ft17];
- Code quality integrations
  with either [**Coveralls**][ft18]
  for more basic test coverage
  or [**Codacy**][ft19]
  for full code analysis,
  both integrated into
  your project's workflow
  via CI/CD;
- Everything is already set up
  for security checks,
  codestyle checks,
  code formatting,
  testing,
  linting,
  docker builds etc.
  with [**Invoke**][ft20];
  more details in [_Invoke Usage_][ft21];
- Predefined VS Code [`settings.json`][ft22]
  with quality-of-life configuration
  for editor,
  workbench,
  debugging
  and more;
- Ready-to-use
  [`.editorconfig`][ft23],
  [`.dockerignore`][ft24]
  and [`.gitignore`][ft25] files;
  you don't have to
  worry about those things.

### :magic_wand: We Assemble the Tools to Ship, You Bring Your Code to Life

- The boilerplate code provided
  with the template
  is already
  100% covered
  by unit tests;
  you can dive in
  directly into
  your project's implementation
  without the hassle of
  handling test cases;
- Predefined CI/CD build workflows
  with [**GitLab CI**][tl1]
  and [**Github Actions**][tl2];
- Automatic package uploads to
  [**PyPI**][tl3] test
  and production repositories;
- Automatic documentation deployment to
  [**GitLab Pages**][tl4]
  and [**GitHub Pages**][tl5];
- A [`Dockerfile`][tl6] for your package,
  with CI/CD workflows
  to publish your image
  to a container registry;
- Automatic release cycles
  with [**GitLab Changelog**][tl7]
  or [**Release Drafter**][tl8];
- Automatic dependency updates
  thanks to [**Renovate**][tl9]
  and [**Dependabot**][tl10].

### :man_golfing: Manage Your Project like a Walk in the Park

- Ready-to-use [Merge Request templates][mgmt1]
  and several [Issue templates][mgmt2]
  for easy integration
  with GitLab and GitHub;
- Workflows to mark and close abandoned issues
  after a period of inactivity
  for both GitLab with [**Triage Policies**][mgmt3]
  and GitHub with [**Stale Bot**][mgmt4];
- Choose the versioning schema
  that best suits your project type
  and development style;
  from **7 different options**
  (yes,
  you can _even_ choose SemVer,
  if you wish :upside_down:);
- Option to choose between
  [Gitmoji][b23],
  [Conventional Commits][mgmt5]
  or a mix of both
  to standardise your commit titles.

### :knot: Nurture the Community around Your Project from Day One

- Provide your users
  with a polished documentation structure,
  complete with user guides,
  API reference
  and announcements
  powered by [**Zensical**][cmty1];
- With Galactipy templates,
  you get more than a `CONTRIBUTING.md` file;
  you have a comprehensive development philosophy,
  drawing inspiration
  from some of the most distinguished
  open source projects;
  we provide
  extensive yet user-friendly guidelines,
  enabling your project
  to onboard new contributors
  and scale effortlessly
  with minimal adjustments;
- Files such as
  `LICENCE`,
  `CODE_OF_CONDUCT.md`,
  `CITATION.cff`,
  `ROADMAP.md`
  and `SECURITY.md`
  are generated automatically;
- **Loads** of predefined [badges][cmty2]
  to make your project stand out;
  you can either keep them,
  remove as you wish
  or be welcome to add even more.

### GitLab vs. GitHub feature comparison chart

You are free to choose
whichever platform works best
for you and your project.
The original template by [TezRomacH][vs1]
was created with GitHub in mind,
which prompted the creation
of a similarly fully-featured template
for GitLab users as well.

However,
not everything that is available for GitHub users
is available to GitLab users,
and vice-versa.
Please mind the differences
between both options.

Below is a comparison
between the features available in this package
depending on which platform
you choose to host your project:

|            Feature            |       GitLab       |       GitHub       | Observations                                                                                                                                                                                                                                                |
| :---------------------------: | :----------------: | :----------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Issue templates        | :white_check_mark: | :white_check_mark: | Both options feature automatic labels, but GitHub has an extra configuration to prevent the creation of empty issues.                                                                                                                                       |
| Merge/pull requests templates | :white_check_mark: |     :warning:      | For GitHub, templates can only be accessed by applying custom [query parameters][vs2] during PR creation.                                                                                                                                                   |
|   Project conditions checks   | :white_check_mark: | :white_check_mark: | A basic workflow to install the package and run tests, check codestyle and safety.                                                                                                                                                                          |
|    Publication to TestPyPI    | :white_check_mark: | :white_check_mark: | For GitHub, the workflow uses the official [PyPI Publish action][vs3], while GitLab CI uses the [PyPI API][vs4].                                                                                                                                            |
|      Publication to PyPI      | :white_check_mark: | :white_check_mark: | Both GitLab and GitHub projects use [trusted publishing][vs5] to upload packages to the canonical PyPI registry. Projects on both platforms will also publish the build files attestations.                                                                 |
|   Documentation publication   | :white_check_mark: | :white_check_mark: | Both GitLab and GitHub projects allow developers to publish documentation to their respective Pages environment. However, publication is disabled by default and should be set up by the user.                                                              |
|   SLSA Level 3 provenances    | :white_check_mark: |        :x:         | GitLab projects use the [SLSA][vs6] CI/CD component to sign the PyPI attestations and the metadata generated during package building to comply with level 3 standards.                                                                                      |
|       Image publication       | :white_check_mark: | :white_check_mark: | For GitHub, images are pushed to [Docker Hub][vs7], while GitLab CI pushes images to the repository's [Container Registry][vs8] by default (and can be reconfigured).                                                                                       |
|        Snapshot images        | :white_check_mark: |        :x:         | For GitLab, the [Docker][vs9] CI/CD component is used and allows for pushing snapshot images for testing when a Merge Request is open.                                                                                                                      |
|      Dockerfile linting       | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component includes a job for linting the Dockerfile with [Hadolint][vs10].                                                                                                                                                          |
| Image vulnerability analysis  | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component uses [Trivy][vs11] to scan the image for vulnerabilities.                                                                                                                                                                 |
|       Docker SBOM files       | :white_check_mark: |        :x:         | The Docker GitLab CI/CD component generates a bill of materials with [CycloneDX][vs12].                                                                                                                                                                     |
|      Dependency scanning      | :white_check_mark: |        :x:         | For GitLab, the [Dependency Scanning][vs13] CI/CD component generates a bill of materials with CycloneDX.                                                                                                                                                   |
|             SAST              | :white_check_mark: |        :x:         | For GitLab, the [SAST][vs14] CI/CD component performs a security analysis and provides a report with its results.                                                                                                                                           |
|       Secret detection        | :white_check_mark: |        :x:         | For GitLab, the [Secret Detection][vs15] CI/CD component performs an analysis on potential leaked secrets in tracked files and provides a report with its results.                                                                                          |
|         Stale issues          | :white_check_mark: | :white_check_mark: | GitLab rules are more flexible, marking stale issues only for those not opened by project members.                                                                                                                                                          |
|      Greetings workflow       |        :x:         | :white_check_mark: | GitHub provides workflows to automatically reply to issues and merge requests with the [First Interaction][vs16] action.                                                                                                                                    |
|      Dependency updates       | :white_check_mark: | :white_check_mark: | To reduce development overhead, GitLab projects use a [Renovate][tl9] configuration which should be paired with a separate repository implementing the [Renovate CI/CD component][vs17], while GitHub projects use [Dependabot][tl10] out of the box.       |
|        Release drafter        |        :x:         | :white_check_mark: | [Release Drafter][tl8] is a custom workflow available on GitHub Marketplace. You may see the list of labels in [`release-drafter.yml`][vs18]. Works perfectly with any SemVer-compatible schema.                                                            |
|    Changelog configuration    | :white_check_mark: |        :x:         | GitLab provides automatic changelog updates through their [API][tl7]. You may modify the template in [`changelog_config.yml`][vs19]. GitLab projects also leverage use of [Galactic Releases][vs20] to manage release cycles and release notes.             |
|         Test Reports          | :white_check_mark: |        :x:         | JUnit XML reports are supported by GitLab to allow [test reports][vs21] to be displayed in pipelines and merge requests.                                                                                                                                    |
|  CI control over pushed tags  | :white_check_mark: |     :warning:      | GitLab provides full control for tags pushed to the repository using [regex][vs22], while GitHub Actions is more restricted in how it [filters][vs23] workflows to run, and can only apply these filters at the top level, limiting workflow customization. |

## :black_joker: How to Use It

### Installation

To begin using the template consider updating Cookiecutter:

```bash
pipx upgrade cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gl:galactipy/galactipy --checkout v3.3.0
```

### Input variables

Cookiecutter will ask you
to fill some variables
in order to generate the files
with everything you need
already set up.

The input variables
are as follows:

|         Variable         |         Type         |        Default value         |                                                                         Valid options                                                                          | Observations                                                                                                                                                                                                                                                                                   |
| :----------------------: | :------------------: | :--------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      `project_name`      |    :writing_hand:    |       `Python Project`       |                                                                              Any                                                                               | A suitable name by which people will refer to.                                                                                                                                                                                                                                                 |
|       `repo_name`        |    :writing_hand:    |   based on `project_name`    |                                                [GitLab-compliant][htu1] values<br>[PyPA-compliant][htu2] values                                                | Name of the repository to develop the project on. [Check the availability of possible names][htu3] before creating the project.                                                                                                                                                                |
|      `package_name`      |    :writing_hand:    |   based on `project_name`    |                                               Valid [Python identifiers][htu4]<br>[PyPA-compliant][htu2] values                                                | [Check the availability of possible names][htu3] before creating the project.                                                                                                                                                                                                                  |
|  `project_description`   |    :writing_hand:    |   based on `project_name`    |                                                                              Any                                                                               | A brief one-line description of your project.                                                                                                                                                                                                                                                  |
|       `copyright`        |    :writing_hand:    | `The Galactipy Contributors` |                                                                              Any                                                                               | Name of the author or organisation which will hold the project's copyright. Used to specify code ownership in `LICENCE`.                                                                                                                                                                       |
|       `maintainer`       |    :writing_hand:    | `Manoel Pereira de Queiroz`  |                                                                              Any                                                                               | Name of the primary maintainer of the project. Used to specify author data in `pyproject.toml` and `CITATION.cff`.                                                                                                                                                                             |
|      `scm_platform`      |    :capital_abcd:    |        `GitLab Free`         |                                               `GitLab Free`<br>`GitLab Premium`<br>`GitLab Ultimate`<br>`GitHub`                                               | Depending on the choice you will have [different features][htu5] to work with.                                                                                                                                                                                                                 |
|     `scm_namespace`      |    :writing_hand:    |         `galactipy`          |                                                [GitLab-compliant][htu1] values<br>Between 2 and 255 characters                                                 | GitHub or GitLab namespace for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for either platform. Can be provided as a nested subgroup separated by slashes.                                                                                                   |
|         `email`          |    :writing_hand:    |   based on `scm_namespace`   |                                                             Values complying with [RFC 5332][htu6]                                                             | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify author data in `pyproject.toml` and `CITATION.cff`.                                                                                                                                                                         |
|        `licence`         |    :capital_abcd:    |            `MIT`             | `MIT`<br>`BSD-3`<br>`GNU GPL v3.0`<br>`GNU AGLP v3.0`<br>`GNU LGPL v3.0`<br>`Mozilla Public License 2.0`<br>`Apache Software License 2.0`<br>`Not open source` | The non-OSS licence option provides policy documents with different rules for project development.                                                                                                                                                                                             |
| `minimal_python_version` |    :capital_abcd:    |            `3.10`            |                                                         `3.10`<br>`3.11`<br>`3.12`<br>`3.13`<br>`3.14`                                                         | Used for builds, pipelines and formatters.                                                                                                                                                                                                                                                     |
|      `line_length`       |        :hash:        |              88              |                                                                       Between 50 and 300                                                                       | The max line length to be validated by the formatter.                                                                                                                                                                                                                                          |
|    `docstring_style`     |    :capital_abcd:    |          `Numpydoc`          |                                                   `Numpydoc`<br>`Google Python Style`<br>`Sphinx`<br>`Other`                                                   | `Other` will only render the docstring short summaries, while all others will detail arguments and returns for public classes, methods and functions.                                                                                                                                          |
|    `docstring_length`    |        :hash:        |    based on `line_length`    |                                                    Between 50 and 300<br>Equal or lower than `line_length`                                                     | The max line length for docstrings to be validated by the formatter.                                                                                                                                                                                                                           |
|     `version_schema`     |    :capital_abcd:    |           `EffVer`           |                          `EffVer`<br>`SemVer`<br>`CalVer (automanaged)`<br>`CalVer (explicit)`<br>`RomVer`<br>`SoloVer`<br>`TrunkVer`                          | Automanaged CalVer provides a CI/CD configuration to automatically create tags and release the package on a weekly basis. The TrunkVer option sets up a new package release on each commit made to the default branch. Other options require a tag to be manually created to trigger releases. |
|   `commit_convention`    |    :capital_abcd:    |          `Gitmoji`           |                                           `Gitmoji`<br>`Conventional Commits`<br>`Conventional Commits with Gitmoji`                                           | The `Conventional Commits` and `Convetional Commits with Gitmoji` options add a pre-commit hook for [Commitizen][htu7] to validate commit message title structure.                                                                                                                             |
|        `use_bdd`         | :small_red_triangle: |            `True`            |                                                                                                                                                                | Option to use [behaviour-driven development][ft16] for managing tests.                                                                                                                                                                                                                         |
|    `coverage_service`    |    :capital_abcd:    |           `Codacy`           |                                                                    `Codacy`<br>`Coveralls`                                                                     | Coveralls provide cove coverage only, while Codacy allows for code quality reports and static analysis.                                                                                                                                                                                        |
|     `create_docker`      | :small_red_triangle: |            `True`            |                                                                                                                                                                | Option to create a [Dockerfile][tl6] and build an image for your project. Also configures CI jobs to publish the image to container registries.                                                                                                                                                |
|      `create_docs`       | :small_red_triangle: |            `True`            |                                                                                                                                                                | Option to create documentation files using [Zensical][cmty1].                                                                                                                                                                                                                                  |
|        `app_type`        |    :capital_abcd:    |     `Integrated CLI+TUI`     |                       `Integrated CLI+TUI`<br>`Hybrid CLI/TUI`<br>`CLI-only application`<br>`Minimal CLI structure`<br>`Bare repository`                       | Depending on the chosen option, configures [Typer][ft1] and [Textual][ft2] as the core dependency libraries.                                                                                                                                                                                   |

> [!NOTE] Legend
>
> |         Icon         | Type      |
> | :------------------: | --------- |
> |    :writing_hand:    | Free text |
> |        :hash:        | Number    |
> |    :capital_abcd:    | Option    |
> | :small_red_triangle: | Boolean   |
>
> Boolean variables can be dismissed by typing either `0`, `false`, `f`, `no`, `n` or `off`.

All input values will be saved in `cookiecutter-config-file.yml`
so that you won't lose them. :wink:

#### About Application Types

The `app_type` Cookiecutter variable
is used to define the level
of sample files
provided by Galactipy
and how the project tree
is structured:

| Application Type          | What's Included                                                                                                                                                                   | Recommended Usage                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Integrated CLI+TUI**    | A TUI-first application, where the top-level command launches the interface. It also includes configuration commands via CLI and allow for additional commands built by the user. | Projects designed to be interacted with mainly through a visual interface.                                                                                                              |
| **Hybrid CLI/TUI**        | Same as Integrated CLI+TUI, with the difference that the interface is launched via its own command.                                                                               | Projects with many-yet-simple operations which can be mastered solely at the command-line, but also targeted at non-power-users who prefer a visual interface to interact with the API. |
| **CLI-only application**  | Removes TUI-related features to solely rely on CLI commands. Still includes the configuration commands and config file management available in TUI options.                       | Projects with simpler interactions that do not require much cognitive load or a visual helper to navigate through operations.                                                           |
| **Minimal CLI structure** | Same as CLI-only application, but removes the API related to configuration management.                                                                                            | Projects that do not require stateful/persisted values to perform their operations from the command-line.                                                                               |
| **Bare repository**       | Removes sample code files altogether while keeping all other development features such as CI/CD configuration and pre-commit hooks.                                               | General-purpose libraries and APIs.                                                                                                                                                     |

### Initial set up

You must have [Poetry][b27] installed
to leverage the features
provided with the Galactipy template.

After creating a project,
ensure you have [Invoke][ft20] installed
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
Check [its documentation][htu8].
Poetry's [commands][htu9]
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
your project will embed [Typer][ft1]
as a dependency,
and [Textual][ft2] will be provided for
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
have a [PyPI][tl3] account
and set up [Trusted Publishing][htu10]
for your project.

Then,
when you [push a tag][htu11]
to GitLab or GitHub,
the preconfigured CI/CD pipeline
will handle building, publishing and releasing automatically,
with minimal configuration required! :partying_face:

> [!NOTE]
> To allow releasing
> directly via CI/CD workflows,
> besides setting up
> a canonical PyPI token,
> you must also
> generate a API token
> for the [TestPyPI][htu12] repository.

If you have generated your project
with the Docker option enabled,
pushing a tag to your repository
will also set up the automated workflows
to build and publish your image
to a container registry.

### Invoke Usage

[`invoke`][ft20] is a library that
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
|  `invoke install`  | :small_red_triangle: Sets up the Poetry virtual environment, installs the dependencies, pre-commit hooks and runs a [mypy][ft13] check. |
| `invoke pyproject` | Checks `pyproject.toml` integrity.                                                                                                      |
|  `invoke update`   | Updates dependencies to their latest compatible release requirements, with an option to update to the latest versions overall.          |

> [!WARNING]
> :small_red_triangle: Invoke must be installed and callable.
> Otherwise, it is recommended to run `poetry install`
> to set up the repository.

#### Quality Assurance Tasks

|      Command       | Details                                                                                          |
| :----------------: | ------------------------------------------------------------------------------------------------ |
| `invoke codestyle` | Format files with [Ruff][b19], with an option to check files only.                               |
|   `invoke lint`    | Check compliance with linting rules, with an option to correct those considered fixable by Ruff. |
|   `invoke mypy`    | Run [mypy][ft13] to check for static typing.                                                     |
|   `invoke test`    | Run the test suite with [Pytest][ft15].                                                          |
|  `invoke report`   | Run the `test` and `mypy` tasks and open their HTML coverage reports.                            |
| `invoke security`  | Run security checks with [Bandit][ft14] and check `pyproject.toml` integrity.                    |

The **`invoke sweep`** task groups all tasks
except for `report`
into a single command.
**`invoke ruff`** can be used
to run the Ruff formatter and linter
with a single command.

#### Project Building & Publishing

|     Command      | Details                                                                                                                             |
| :--------------: | ----------------------------------------------------------------------------------------------------------------------------------- |
|  `invoke build`  | Build the project wheels.                                                                                                           |
| `invoke config`  | :small_red_triangle: Configure PyPI repositories, requiring at least an API token, with optional repository name and URL arguments. |
| `invoke publish` | Publish the project to a registry, defaulting to the canonical PyPI repository, with an option to build the project wheels.         |
|  `invoke docs`   | Build the project documentation with [Zensical][cmty1].                                                                             |

> [!NOTE]
> :small_red_triangle: When provided with no `--repo` option,
> Invoke will configure the connection
> to the [canonical PyPI repository][tl3],
> with only the API token being required.
> When provided with the `--repo testpypi` option instead,
> it will configure the connection
> to [TestPyPI][htu12]
> and no URL is needed.
> Other `--repo` values must also
> receive a `--url` argument
> pointing to the desired custom registry.

#### Docker Operations

|      Command       | Details                                                                                                                                                           |
| :----------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   `invoke login`   | Log in to a container registry. For GitHub users, points to [Docker Hub][vs7]. For GitLab users, points to the repository's [integrated container registry][vs8]. |
| `invoke container` | Build local container images, with the option to set multiple tags and an alternate repository to point.                                                          |
|   `invoke push`    | Push all project images to a container registry, with the option to set an alternate repository to push.                                                          |
|   `invoke prune`   | Remove all local images built for the project, with the option to set an alternate repository to point.                                                           |

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

### How to Handle the Development Cycle with BDD

[Behaviour-driven development][ft16] is a software development paradigm
in which domain language is used
to describe the behaviour of the code.
It emerged as a
sophisticated evolution
of [test-driven development][htu13].

If you choose to use BDD for your project,
a `features` directory will be created under `tests`
and [pytest-bdd][htu14] will be added as a dependency.
You should place `.feature` files inside this folder
to describe **real-life** usage scenarios
using the [Gherkin][htu15] language:

```
# tests/features/root_command.feature
Feature: Command-line interface

  Scenario: Check program version
    When the root program receives the `--version` option
    Then the terminal displays the program's version
    And the program exits without errors
```

You would then use pytest-bdd
to wrap each scenario
referred in the feature file
as a step-by-step validation:

```py
from typer.testing import CliRunner
from pytest_bdd import scenario, when, then, parsers
from python_project.cli.commands.root_command import app

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
you can simply use Pytest
as you normally would
to run the test suite
and check the results.

For more information on behaviour-driven development
and tools to handle
more complex conditions,
please check out the [Cucumber documentation][htu16].

## :motorway: What's next

Well, that's up to you. :muscle:

For further setting up your project:

- Look for files and sections
  marked with special inline comment tags:
  - `TODO` comments must be addressed
    in order for your project
    to run properly
    from end-to-end;
  - `UPDATEME` comments
    point to additional
    settings or content
    you can provide,
    but are not necessary
    to enable development;
  - `DEFINE` comments
    mark sections
    in policy files
    for concepts and content
    specifically tailored
    to your project's context;
  - If you use VS Code,
    install the [**Todo Tree**][wn1] extension
    to easily locate and jump
    to these marks,
    they are already configured
    in the `settings.json` file;
- Make sure to
  create your desired Issue labels
  (and GitLab statuses,
  if you're using GitLab Premium or Ultimate)
  on your repository
  before you start tracking issues;
- Make changes
  to your CI configuration
  to better suit your needs.

> [!IMPORTANT]
> In order to reduce user prompts
> and keep things effective,
> the template generates files
> with a few assumptions:
>
> - It assumes your main Git branch is `master`;
>   if you wish to use another branch name
>   for development,
>   be aware of changes
>   you will have to make in Markdown files
>   so links won't break
>   when you push them to your repo;
> - It defines the `name` setting
>   in `pyproject.toml`
>   assuming you will be able
>   to publish your project to PyPI
>   under `repo_name`,
>   change it otherwise;
> - It specifies the `DEFAULT_DOCKER_REPOSITORY` constant
>   in `tasks.py`
>   assuming you also use `scm_namespace`
>   for Docker Hub
>   and you will push your image
>   under `repo_name`,
>   change it otherwise.

If you want to put your project on steroids,
here are a few Python tools
which can help you depending on
what you want to achieve
with your application:

- If you chose
  to generate a TUI or CLI example
  during the Cookiecutter setup,
  these libraries will already be
  among your dependencies:
  - [**Rich**][wn2] makes it
    easy to add beautiful formatting
    in the terminal;
  - [**Typer**][wn3]
    builds great Command-Line Interfaces (CLI) applications
    with an easy-to-code API
    based on type hints;
  - [**Textual**][wn4] is
    a rapid application development framework
    to create Terminal User Interfaces (TUIs),
    made to be fun to build with;
  - [**Orbittings**][ft3] is
    Galactipy's own utility
    to manage configuration files and settings
    for these CLI/TUI applications; :sunglasses:
  - [**Nebulog**][ft4] makes logging
    stupidly simple (and _beautiful_),
    brought to you by The Galactipy Contributors; :man_dancing:
- [**attrs**][wn5] and [**cattrs**][wn6] work together
  to make data structuring and validation
  your application's powerhouse,
  not its Achilles's heel;
- [**Trio**][wn7] is
  a friendly library
  for async concurrency
  and I/O;
- [**FastAPI**][wn8] is
  a web framework
  for high performance
  and easy learning;
- [**textX**][wn9] allows you
  to build your own Domain-Specific Languages (DSL)
  in plain Python;
- [**Returns**][wn10]
  makes you function's output
  meaningful,
  typed
  and safe;
- [**Hydra**][wn11] is a framework
  for elegantly configuring
  complex applications;
- [**Locust**][wn12]
  allows you to write
  scalable load tests
  in plain Python;
- [**orjson**][wn13] is
  an ultra fast JSON parsing library;
- [**Lark**][wn14] is
  a parsing toolkit for Python,
  built with a focus on
  ergonomics,
  performance
  and modularity.

For taking development
and exposition of your project
to the next level:

- Experiment with additional badges;
  not only they enhance
  your project's appearance
  but also visually communicate key aspects,
  helping visitors quickly grasp
  important details about your work:
  - You can look at dynamic badges
    available at [Shields.io][nl1];
  - There is a myriad of static badges
    for brands and services in general
    at [Simple Badges][nl2];
  - [awesome-badges][nl3] provides
    a lot of useful resources
    on this topic;
- Add your project
  to the [OpenSSF Best Practices][nl4] and [OSSRank][nl5] indexes;
  if you have ambitious goals
  or expect significant growth,
  these indexes provide
  valuable visibility;
  - There are already badges for them
    in your `README.md` file,
    just waiting for you
    to update their URLs
    with your project's index; :grinning:
- Create a sponsorship page
  enabling users and organisations
  to help fund your project's
  growth and development;
  popular plaforms include:
  - [Liberapay][nl6];
  - [Open Collective][nl7];
  - [Ko-fi][nl8];
  - If you host your project on GitHub,
    you can set a [Sponsors account][nl9]
    directly integrated into the platform;
- If you are
  unsure about which versioning logic
  to use,
  check [this list][nl10]
  briefly explaining
  all available options
  with Galactipy
  (and some others more).

And here are a few articles
which may help you:

- [Open Source Guides][res1];
- [A handy guide to financial support for open source][res2];
- [GitLab CI Documentation][res3];
- [GitHub Actions Documentation][res4];
- [A Comprehensive Look at Testing in Software Development][res5];
- [Robust Exception Handling][res6];
- [Why Your Mock Doesn't Work][res7];
- [Managing TODOs in a codebase][res8];
- [The importance of layered thinking in data engineering][res9].

## :chart_with_upwards_trend: Galactipy Releases

You can see
the list of available releases
on the [GitLab Releases][r1] page.

We follow the [Romantic Versioning][r3] specification,
details can be found
in our [`CONTRIBUTING`][r3] guide.

## :map: Roadmap

Galactipy's roadmap is managed
through our [Epics][rd1] page,
which lays out
the current development streams
mapped for delivery.
All official details on
development,
timeline
and deliverables
are found there.
The project's epics are also presented
in the [`ROADMAP`][rd2] file
purely for informational purposes.

## :shield: Licence

[![Licence][b6]][b7]

This project is licenced
under the terms of the MIT licence.
See [`LICENCE`][b7] for more details.

## :sports_medal: Acknowledgements

Firstly,
there is no way this template would exist
without the previous phenomenal work
by [Roman Tezikov][ac1] and his rich [python-package-template][vs1].
If there is anyone more deserving of a :star2:
and acknowledgement,
it's him!
Please give a shoutout
and [support][ac2] if possible.

The original template
was inspired by several articles
that might be helpful
if you are starting out
managing projects:

- [Hypermodern Python][ac3];
- [Ultimate Setup for Your Next Python Project][ac4];
- [Nine simple steps for better-looking python code][ac5];
- [Modern Python developer's toolkit][ac6].

Additionally,
we would like to thank the teams
of the following projects
and individuals
for either aiding us directly
during our research of best practices
and tools for Python development
or whose documentation
have inspired parts of the project:

- [Pelican][ac7];
- [Spark][ac8];
- [React][ac9];
- [Chai][ac10];
- [Harbor][ac11];
- [pandas][ac12];
- [Adrian Ababei][ac13].

Give them your :star:,
these resources are amazing! :wink:

<small>Galactipy Bot avatar created by [Smashicons][ac14].</small>

## :page_with_curl: Citation

We provide a [`CITATION.cff`][cite1] file
to make it easier
to cite this project
in your paper.

## :mega: Spread the Word

Add the badge [![Expand your project structure from atoms of code to galactic dimensions.][b41]][b42]
to your project!
It would be really appreciated
to spread the word of this template.

Here is the Markdown source for it:

```markdown
[![Expand your project structure from atoms of code to galactic dimensions.](https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E)](https://kutt.it/7fYqQl)
```

We would be equally grateful
if you could also do
any of the following:

- Set the notification level to **"Watch"**
  to receive our latest updates; :bell:
- Star the project! :star2:
- Share the project with colleagues; :speaking_head:
- Write a short article
  on how you are using Galactipy
  on your projects; :pencil2:
- Share
  best practices,
  references
  and tools for project management
  with us! :beers:

<!-- Anchors -->

[b1]: https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue?style=for-the-badge
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
[b24]: https://img.shields.io/badge/sembr-FF6441?style=for-the-badge&logo=apmterminals&logoColor=white
[b25]: https://sembr.org/
[b26]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json&style=for-the-badge
[b27]: https://python-poetry.org/
[b28]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
[b29]: https://kutt.it/D4ayxs
[b30]: https://img.shields.io/badge/Renovate-308BE3?logo=renovate&logoColor=fff&style=for-the-badge
[b31]: https://gitlab.com/galactipy/galactipy/-/blob/master/renovate.json
[b32]: https://img.shields.io/badge/Editorconfig-E0EFEF?style=for-the-badge&logo=editorconfig&logoColor=000
[b33]: https://kutt.it/fy3pqF
[b34]: https://img.shields.io/badge/romver-DE4F4F?style=for-the-badge&logo=semver
[b35]: https://img.shields.io/codacy/grade/9827f88089954a3680675d7c77e63fd5?style=for-the-badge&logo=codacy
[b36]: https://kutt.it/ByTvpc
[b37]: https://img.shields.io/codacy/coverage/9827f88089954a3680675d7c77e63fd5?style=for-the-badge&logo=codacy
[b38]: https://kutt.it/uxIDHs
[b39]: https://img.shields.io/gitlab/pipeline-status/galactipy%2Fgalactipy?branch=master&style=for-the-badge&logo=gitlab&logoColor=white&label=master
[b40]: https://kutt.it/zG7nVG
[b41]: https://img.shields.io/badge/made%20with-galactipy%20%F0%9F%8C%8C-179287?style=for-the-badge&labelColor=193A3E
[b42]: https://kutt.it/7fYqQl

[cookie]: https://github.com/cookiecutter/cookiecutter

[ft1]: https://typer.tiangolo.com/
[ft2]: https://textual.textualize.io/
[ft3]: https://gitlab.com/galactipy/orbittings
[ft4]: https://gitlab.com/galactipy/nebulog
[ft5]: https://github.com/liviuschera/noctis
[ft6]: https://python-poetry.org/
[ft7]: https://github.com/mtkennerly/poetry-dynamic-versioning
[ft8]: https://github.com/python-poetry/poetry-plugin-bundle
[ft9]: https://github.com/python-poetry/poetry-plugin-export
[ft10]: https://github.com/MousaZeidBaker/poetry-plugin-up
[ft11]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/pyproject.toml
[ft12]: https://pre-commit.com/
[ft13]: https://mypy.readthedocs.io
[ft14]: https://bandit.readthedocs.io/en/latest/
[ft15]: https://docs.pytest.org/en/latest/
[ft16]: https://cucumber.io/
[ft17]: #how-to-handle-the-development-cycle-with-bdd
[ft18]: https://coveralls.io/
[ft19]: https://www.codacy.com/
[ft20]: https://docs.pyinvoke.org/en/stable/
[ft21]: #invoke-usage
[ft22]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.vscode/settings.json
[ft23]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.editorconfig
[ft24]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.dockerignore
[ft25]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitignore

[tl1]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.gitlab-ci.yml
[tl2]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/workflows/build.yml
[tl3]: https://pypi.org/
[tl4]: https://docs.gitlab.com/user/project/pages/
[tl5]: https://docs.github.com/en/pages
[tl6]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[tl7]: https://docs.gitlab.com/ee/user/project/changelogs.html
[tl8]: https://github.com/marketplace/actions/release-drafter
[tl9]: https://docs.renovatebot.com/
[tl10]: https://docs.github.com/en/code-security/dependabot

[mgmt1]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/merge_request_templates/default.md
[mgmt2]: https://gitlab.com/galactipy/galactipy/-/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/issue_templates
[mgmt3]: https://gitlab.com/explore/catalog/components/gitlab-triage
[mgmt4]: https://github.com/marketplace/actions/close-stale-issues
[mgmt5]: https://www.conventionalcommits.org/en/v1.0.0/

[cmty1]: https://zensical.org/
[cmty2]: https://shields.io/

[vs1]: https://github.com/TezRomacH/python-package-template
[vs2]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/using-query-parameters-to-create-a-pull-request
[vs3]: https://github.com/marketplace/actions/pypi-publish
[vs4]: https://docs.pypi.org/api/upload/
[vs5]: https://docs.pypi.org/trusted-publishers/
[vs6]: https://gitlab.com/explore/catalog/components/slsa
[vs7]: https://hub.docker.com/
[vs8]: https://docs.gitlab.com/ee/user/packages/container_registry/
[vs9]: https://gitlab.com/explore/catalog/to-be-continuous/docker
[vs10]: https://github.com/hadolint/hadolint
[vs11]: http://trivy.dev/latest/
[vs12]: https://cyclonedx.org/
[vs13]: https://gitlab.com/explore/catalog/components/dependency-scanning
[vs14]: https://gitlab.com/explore/catalog/components/sast
[vs15]: https://gitlab.com/explore/catalog/components/secret-detection
[vs16]: https://github.com/marketplace/actions/first-interaction
[vs17]: https://gitlab.com/explore/catalog/to-be-continuous/renovate
[vs18]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.github/release-drafter.yml
[vs19]: https://gitlab.com/galactipy/galactipy/-/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/_templates/.gitlab/changelog_config.yml
[vs20]: https://gitlab.com/explore/catalog/galactipy/components/release
[vs21]: https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html
[vs22]: https://docs.gitlab.com/ee/ci/jobs/job_rules.html#compare-a-variable-to-a-regular-expression
[vs23]: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet

[htu1]: https://docs.gitlab.com/user/reserved_names/
[htu2]: https://packaging.python.org/en/latest/specifications/name-normalization/
[htu3]: http://ivantomic.com/projects/ospnc/
[htu4]: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords
[htu5]: #gitlab-vs-github-features
[htu6]: https://datatracker.ietf.org/doc/html/rfc5322#section-3.4
[htu7]: https://commitizen-tools.github.io/commitizen/
[htu8]: https://python-poetry.org/docs/
[htu9]: https://python-poetry.org/docs/cli/#commands
[htu10]: https://docs.pypi.org/trusted-publishers/
[htu11]: https://git-scm.com/book/en/v2/Git-Basics-Tagging
[htu12]: https://test.pypi.org/
[htu13]: https://tidyfirst.substack.com/p/canon-tdd
[htu14]: https://pytest-bdd.readthedocs.io/en/latest/
[htu15]: https://cucumber.io/docs/gherkin/reference
[htu16]: https://cucumber.io/docs

[wn1]: https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree
[wn2]: https://github.com/willmcgugan/rich
[wn3]: https://github.com/fastapi/typer
[wn4]: https://github.com/Textualize/textual
[wn5]: https://github.com/python-attrs/attrs
[wn6]: https://github.com/python-attrs/cattrs
[wn7]: https://github.com/python-trio/trio
[wn8]: https://github.com/tiangolo/fastapi
[wn9]: https://github.com/textX/textX
[wn10]: https://github.com/dry-python/returns
[wn11]: https://github.com/facebookresearch/hydra
[wn12]: https://github.com/locustio/locust
[wn13]: https://github.com/ijl/orjson
[wn14]: https://github.com/lark-parser/lark

[nl1]: https://shields.io/badges/static-badge
[nl2]: https://badges.pages.dev/
[nl3]: https://github.com/badges/awesome-badges
[nl4]: https://www.bestpractices.dev/en
[nl5]: https://ossrank.com/
[nl6]: https://liberapay.com/
[nl7]: https://opencollective.com/
[nl8]: https://ko-fi.com/
[nl9]: https://github.com/sponsors
[nl10]: https://nesbitt.io/2024/06/24/from-zerover-to-semver-a-comprehensive-list-of-versioning-schemes-in-open-source.html

[res1]: https://opensource.guide/
[res2]: https://github.com/nayafia/lemonade-stand
[res3]: https://docs.gitlab.com/ee/ci/
[res4]: https://help.github.com/en/actions
[res5]: https://pytest-with-eric.com/introduction/types-of-software-testing/
[res6]: https://eli.thegreenplace.net/2008/08/21/robust-exception-handling/
[res7]: https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
[res8]: https://medium.com/babylon-engineering/todo-find-a-title-for-the-article-fee79708ca15
[res9]: https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71

[r1]: https://gitlab.com/galactipy/galactipy/-/releases
[r2]: https://romversioning.github.io/romver/
[r3]: https://gitlab.com/galactipy/galactipy/-/blob/master/CONTRIBUTING.md#versioning-customs

[rd1]: https://gitlab.com/groups/galactipy/-/work_items?sort=updated_desc&state=opened&type%5B%5D=EPIC&or%5Blabel_name%5D%5B%5D=project%3A%3Acookiecutter&or%5Blabel_name%5D%5B%5D=project%3A%3Agalactipy
[rd2]: https://gitlab.com/galactipy/galactipy/-/blob/master/ROADMAP.md

[ac1]: https://github.com/TezRomacH
[ac2]: https://patreon.com/tezikov
[ac3]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[ac4]: https://martinheinz.dev/blog/14
[ac5]: https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf
[ac6]: https://pycon.switowski.com/
[ac7]: https://github.com/getpelican/pelican
[ac8]: https://github.com/apache/spark
[ac9]: https://github.com/facebook/react/
[ac10]: https://github.com/chaijs/chai
[ac11]: https://github.com/goharbor/harbor
[ac12]: https://github.com/pandas-dev/pandas
[ac13]: https://github.com/web247
[ac14]: https://www.flaticon.com/free-icons/robot

[cite1]: https://gitlab.com/galactipy/galactipy/-/blob/master/CITATION.cff
