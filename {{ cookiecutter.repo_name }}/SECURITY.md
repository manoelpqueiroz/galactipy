# :closed_lock_with_key: Security
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#security-guide
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#guide
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}

[[_TOC_]]
{%- endif %}

## Announcements
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#announcements
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#announcements
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

### :placard: Current Vulnerability Status
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-shield-alert-current-vulnerability-status
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-shield-alert-current-vulnerability-status
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

As of
**{% now 'local', '%B %Y' %}**,
there are no unpatched vulnerabilities
of medium or higher severity
that have been publicly known
for more than 60 days
in the {{ cookiecutter.project_name }} codebase.

### :atm: Current Security Advisories
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-radar-current-security-advisories
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-radar-current-security-advisories
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

We publish security advisories
for any vulnerabilities
we address.

As of
**{% now 'local', '%B %Y' %}**,
no security advisories have been announced.

## Guidelines
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#guidelines
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#guidelines
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

### :postbox: Reporting Vulnerabilities
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-mailbox-reporting-vulnerabilities
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-mailbox-reporting-vulnerabilities
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

> [!WARNING]
> Do not open public issues
> that might have security implications!
>
> It is critical that security-related issues
> are reported privately so we have time
> to address them
> before they become public knowledge.

If you think you found a vulnerability,
and even if you are not sure about it,
please report it right away
by sending an email to:

**`{{ cookiecutter.__security_email }}`**

Please include
the requested information listed below
(as much as you can provide)
to help us better understand
the nature and scope
of the possible issue:

- Type of vulnerability;
- Full paths of source file(s)
  related to the manifestation of the issue;
- The location
  of the affected source code
  (tag/branch/commit or direct URL);
- Any special configuration
  required to reproduce the issue;
- Step-by-step instructions
  to reproduce the issue;
- Proof-of-concept or exploit code
  (if possible);
- Impact of the issue, including
  how an attacker might exploit it.

This information will help us
triage your report more quickly.

> [!IMPORTANT]
> If you need to provide secure information
> or your report needs to be encrypted,
> please use our PGP key
> to encrypt your message
> before sending.
<!-- UPDATEME by listing your key data and replacing the commands below with their output
> <details>
>
> **Key fingerprint:**
> ```
> gpg --list-keys --with-fingerprint <ID>
> ```
>
> **Key data:**
> ```
> gpg --export --armor <ID>
> ```
> </details>
-->

We prefer all communications
to be in **English**.

### :clipboard: Response Process
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-clipboard-check-response-process
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-clipboard-check-response-process
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

When you report a vulnerability,
you can expect:

1. **Acknowledgment:**
   we will acknowledge your email within
   **48 hours**;
2. **Verification:**
   we will work to verify the vulnerability
   and its impact;
3. **Remediation:**
   we will develop a fix
   and test it;
4. **Disclosure:**
   once a fix is ready,
   we will coordinate with you
   on the disclosure timeline.

### :loudspeaker: Disclosure Policy
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-volume-2-disclosure-policy
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-volume-2-disclosure-policy
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The following process
will be triggered
once you send
your report:

1. The security report is received
   and is assigned a primary handler;
   - This person will
     coordinate the fix and release process;
   - The problem is validated
     against all supported {{ cookiecutter.project_name }} versions;
   - Once confirmed,
     a list of all affected versions
     is determined;
   - Code is audited
     to find any potential similar problems;
   - Fixes are prepared
     for all supported releases;
   - These fixes are not committed to the public repository
     but rather held locally pending the announcement;
2. A suggested embargo date
   for this vulnerability is chosen
   and a Common Vulnerabilities and Exposures (CVE)
   is requested for the vulnerability;
3. On the embargo date:
   - A copy of the announcement
     is sent to the {{ cookiecutter.project_name }}
     security mailing list;
   - The changes are pushed
     to the public repository
     and new builds are deployed
     to {{ cookiecutter.__scm_platform_base }} Releases;
   - Within **6 hours**
     of the mailing list being notified,
     a copy of the advisory
     will be published
     on the [{{ cookiecutter.__scm_platform_base }} Advisory Database][3].

> [!IMPORTANT]
> Typically,
> the embargo date will be set
> **72 hours**
> from the time the CVE is issued;
> however,
> this may vary
> depending on the severity of the bug
> or difficulty in applying a fix.

This process can take some time,
especially when we need
to coordinate with maintainers
of other projects.
We will try to handle the bug
as quickly as possible.
However,
we must follow
the release process above
to ensure that
we handle disclosure consistently.

### :scroll: Code of Conduct and Vulnerability Reporting Guidelines
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-scroll-text-code-of-conduct-and-vulnerability-reporting-guidelines
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-scroll-text-code-of-conduct-and-vulnerability-reporting-guidelines
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

When reporting security vulnerabilities,
reporters must adhere
to the following guidelines:

1. **Code of Conduct Compliance:**
   all security reports must comply
   with our [Code of Conduct][1];
   reports that violate our code of conduct
   will not be considered
   and may result
   in being banned
   from future participation;
2. **No Harmful Actions:**
   security research
   and vulnerability reporting
   must not:
   - Cause damage to running systems or production environments;
   - Disrupt {{ cookiecutter.project_name }} development or infrastructure;
   - Affect other users' applications or systems;
   - Include actual exploits that could harm users;
   - Involve social engineering or phishing attempts;
3. **Responsible Testing**:
   when testing potential vulnerabilities:
   - Use isolated,
     controlled environments;
   - Do not test
     on production systems
     without prior authorization;
     contact
     the {{ cookiecutter.project_name }} maintainer
     for permission;
   - Do not attempt
     to access or modify
     other users' data;
   - Immediately stop testing
     if unauthorized access
     is gained accidentally;
4. **Report Quality:**
   - Provide clear,
     detailed steps
     to reproduce the vulnerability.
   - Include only
     the minimum proof-of-concept
     required to demonstrate the issue.
   - Remove any malicious payloads
     or components that could cause harm.

Failure to follow these guidelines may result in:

- Rejection of the vulnerability report;
- Forfeiture of any potential bug bounty;
- Temporary or permanent ban
  from associated bug bounty programs;
- Legal action
  in cases of malicious intent.

## For Your Information
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#for-your-information
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#for-your-information
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

### :traffic_light: Severity Levels
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-waves-ladder-severity-levels
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-waves-ladder-severity-levels
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The {{ cookiecutter.project_name }} project's security team
rates security problems
using four severity levels,
depending how serious
we consider the problem to be.
We use
**Low**,
**Medium**,
**High**
and **Critical**.
We refrain
from using numerical scoring
of vulnerabilities.

> [!IMPORTANT]
> We do not support CVSS
> as a method to grade security vulnerabilities,
> so we do not set them
> for CVE records published
> by the {{ cookiecutter.project_name }} project.
> Other organizations may, however,
> set and provide CVSS scores
> for {{ cookiecutter.project_name }} vulnerabilities.
> You will need to decide for yourself
> if you believe they know enough
> about the subjects involved
> to make reasonable assessments.

When deciding the severity level
on a particular issue,
we take all the factors into account:
attack vector,
attack complexity,
required privileges,
necessary build configuration,
protocols involved,
platform specifics
and also
what effects
a possible exploit or trigger of the issue
can lead to,
including
confidentiality,
integrity
or availability problems.

#### Low
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#low
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#low
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

This is a security problem
that is truly hard
or unlikely to exploit
or trigger.
Due to timing,
platform requirements
or the fact that
options or protocols involved
are rare etc.

<!-- UPDATEME with a past example when available -->

#### Medium
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#medium
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#medium
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

This is a security problem
that is less hard than **Low**
to exploit or trigger.
Less strict timing,
wider platform availability
or involving more widely used
options or protocols.
A problem that usually needs something else
to also happen to become serious.

<!-- UPDATEME with a past example when available -->

#### High
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#high
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#high
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

This issue is in itself a serious problem
with real world impact.
Flaws that can easily compromise
the confidentiality,
integrity
or availability of resources.
Exploiting or triggering this problem
is not hard.

<!-- UPDATEME with a past example when available -->

#### Critical
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#critical
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#critical
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Easily exploitable
by a remote unauthenticated attacker
and lead to system compromise
(arbitrary code execution)
without requiring user interaction,
with a common configuration
on a popular platform.
This issue has few restrictions and requirements
and can be exploited easily
using most {{ cookiecutter.project_name }} configurations.

<!-- UPDATEME with a past example when available -->

### :accept: Supported Versions
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-shield-check-supported-versions
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-shield-check-supported-versions
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{% if cookiecutter.version_schema == 'trunkver' -%}
{{ cookiecutter.project_name }} follows the TrunkVer versioning schema,
which brings on a rapid development cycle.
No single version is considered
for long-term support
and users are expected
to always use {{ cookiecutter.project_name }}
with the latest available version.

If a vulnerability is reported,
the advisory will mention
the release in which
said vulnerability
has been addressed.

{% else -%}
The following library versions
are currently supported
for security updates
and vulnerability reporting:

<!-- DEFINE your supported versions for security reporting -->
{%- if cookiecutter.__schema_group == 'calver' %}

|   Version   |   Support Status   | Commentary |
|:-----------:|:------------------:|------------|
{%- if cookiecutter.version_schema == 'calver-auto' %}
| `v1{% now 'local', '%Y.%U' %}` | :white_check_mark: |            |
{%- else %}
| `v1{% now 'local', '%Y.%m' %}` | :white_check_mark: |            |
{%- endif %}
{%- else %}

| Version  |   Support Status   | Commentary |
|:--------:|:------------------:|------------|
{%- if cookiecutter.__schema_group == 'semver-like' %}
| `v0.1.0` | :white_check_mark: |            |
{%- else %}
|   `v1`   | :white_check_mark: |            |
{%- endif %}
{%- endif %}

{% endif -%}
### :thinking: Use Contexts
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-drill-use-contexts
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-drill-use-contexts
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{{ cookiecutter.project_name }} can be used
{%- if cookiecutter.app_type == 'bare_repo' %}
as a pure **Python library**.
This allows developers
to integrate the package's functionality
into their own Python applications.
<!-- DEFINE your project's use cases
  The library exposes a clean API for...
-->

{% else -%}
as a **Python CLI program**,
{%- if cookiecutter.__app_group == 'tui' %}
a **terminal application**
via a Terminal User Interface (TUI)
{%- endif %}
or as a pure **Python library**.
Each use context is detailed below
and each has its own threat model
and security posture notes.

#### Python CLI Program
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#python-cli-program
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#python-cli-program
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{{ cookiecutter.project_name }} ships as a Python module
distributed via [PyPI][2].
The CLI program is built using Typer
and can be installed and executed
directly from the command-line.

The CLI sources are available as independent Typer apps,
with explicit exports and type annotations.
All dependencies are pinned
and verified during the build process
to ensure consistent and secure installations.

#### Python Library
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#python-library
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#python-library
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The package can also be imported directly
as a Python library.
This allows developers
to integrate the package's functionality
into their own Python applications.
<!-- DEFINE your project's use cases
  The library exposes a clean API for...
-->

When used as a library,
the package maintains
the same security posture
as the CLI application,
with verified dependencies
and secure parsing mechanisms.
The library supports
all the same configuration manipulation features
as the command-line interface,
with the same
safe evaluations
of configuration files and variables
to avoid arbitrary code execution.

{% if cookiecutter.__app_group == 'tui' -%}
#### TUI Application
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#tui-application
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#tui-application
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{{ cookiecutter.project_name }} also ships as a TUI application
built with Textual,
available from the CLI
for users to interact
with the program's capabilities.
{%- if cookiecutter.create_docker %}
It is also deployed
as a Docker container,
so it can be run
as a web application.

The container image is built
with the most recent Alpine image for Python **`{{ cookiecutter.minimal_python_version }}`**,
directly from the source code,
and packages all necessary dependencies.
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
SBOM attestations are available
for container images.
{%- endif %}
{%- endif %}

The TUI application is designed
to be run in a secure environment
and follows the same security practices
as the other components of the {{ cookiecutter.project_name }}.
All input handling,
configuration parsing,
and type conversion operations
are performed with the same security considerations
and validation mechanisms
as the CLI and library components.
This ensures consistent security practices
across all usage contexts.

{% endif -%}
{% endif -%}
### :man_supervillain: Threat Model
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-venetian-mark-threat-model
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-venetian-mark-threat-model
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

#### Underlying Primitives
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#underlying-primitives
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#underlying-primitives
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{% if cookiecutter.app_type == 'bare_repo' -%}
<!-- DEFINE your underlying primitives for building the threat model -->

{% else -%}
{{ cookiecutter.project_name }} uses Python Standard Library modules,
including `pathlib` and `logging` (via Nebulog).
These primitives could have bugs or vulnerabilities
from time to time.
The project maintains
an aggressive release schedule
to incorporate the latest Python security patches
and updates.
Since this is a Python package,
the security posture depends
on the Python runtime environment
and the underlying system libraries.
Users are encouraged
to follow Python security advisories
and keep their Python installations
up to date.

The project is also committed to
ensuring robust software supply chain security.
We leverage our releases on PyPI
via trusted publishing
to attest package integrity.
{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
Additionally,
with each release,
we provide detailed provenance metadata
and digital attestations
that allow users
to independently verify
the integrity of our artifacts.
You can access these assets
on the [Releases][4] page
and use [Cosign][5]
to validate them
against the corresponding binaries,
ensuring that what you download
matches exactly
what was intended by the maintainers.

This approach ensures transparency
and builds trust in our software supply chain,
giving users confidence
in the security and integrity
of every release.

{% endif -%}
{% endif -%}
#### Underlying Libraries
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#underlying-libraries
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#underlying-libraries
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{% if cookiecutter.__app_class == 'bare' -%}
<!-- DEFINE your underlying libraries considerations within the threat model -->

{% else -%}
{{ cookiecutter.project_name }} uses
several key dependencies
that are critical
to its operation:

- **Dynaconf:**
  used for
  configuration management and loading;
  Dynaconf is a mature configuration management library
  that handles various configuration formats
  including
  TOML,
  YAML,
  JSON
  and environment variables;
  while Dynaconf doesn't have
  a formal security policy,
  it's actively maintained
  and widely used
  in the Python ecosystem;
- **tomlkit:**
  used for TOML file manipulation;
  this library is responsible
  for parsing and generating
  TOML files;
  it's a well-maintained library
  that handles TOML syntax correctly
  and is actively developed;
- **Platformdirs:**
  used for automatic discovery
  of user paths in the system;
  this library provides
  cross-platform path discovery
  and is well-maintained
  with good security practices.

Vulnerabilities or bugs
could surface in these libraries
from time to time.
These libraries are popular and well-maintained,
but users should monitor
for security advisories
and keep dependencies updated.

{% endif -%}
#### Build Pipelines
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#build-pipelines
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#build-pipelines
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{% if cookiecutter.__app_class == 'bare' -%}
<!-- DEFINE which potential harmful behaviour can take place if {{ cookiecutter.project_name }} is used in CI build pipelines -->

{% else -%}
{{ cookiecutter.project_name }} does not perform downloads
or invoke external programs.
The logic behind {{ cookiecutter.project_name }}
does not access sensitive environment variables
or execute loaded code.
Thus,
especially considering
release artifact provenance material,
it should be safe
to use within build pipelines,
with no possibility
of overwriting or otherwise mutating
user code.
{{ cookiecutter.project_name }} only reads and writes
to configuration files
in user-controlled locations
and does not modify system files
or execute arbitrary code.

{% endif -%}
#### File Access
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#file-access
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#file-access
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{% if cookiecutter.__app_class == 'bare' -%}
<!-- UPDATEME with how, where and when your application accesses files in the user's system -->

{% else -%}
There are several places
where dynamic input
turns into file system operations:

- **Configuration file reading/writing:**
  {{ cookiecutter.project_name }} reads and writes TOML configuration files
  using Orbittings,
  which in turn uses only Dynaconf and tomlkit
  to perform these operations;
  configuration files are stored
  in user-specific directories
  discovered by Platformdirs,
  preventing access
  to system-wide locations;
- **Input parsing and type conversion:**
  a custom API to validate CLI input
  uses `ast.literal_eval`
  to safely convert string inputs
  into appropriate Python types
  (`int`,
  `float`,
  `bool`,
  `list`,
  `tuple`
  and `dict`);
  if `ast.literal_eval` fails,
  the original string is returned
  as a fallback;
  this approach prevents code injection attacks
  while allowing flexible input handling.
- **Path resolution:**
  {{ cookiecutter.project_name }} uses Platformdirs
  to automatically discover
  appropriate user directories
  for configuration files,
  ensuring that files
  are stored in user-accessible locations
  rather than system directories.

Several mitigations are in place
to prevent unauthorized file access:

- Configuration files
  are stored in user-specific directories
  (using Platformdirs)
  to prevent system-wide access;
- File paths are validated
  and restricted to user-controlled locations;
- The custom type conversion API
  uses `ast.literal_eval`,
  which safely evaluates literal expressions
  without executing arbitrary code;
- No arbitrary file path traversal
  is allowed
  — all file operations
  are constrained to the user's configuration directory;
- No external downloads
  or system command execution
  occur during normal operation.

{% endif -%}
### :x: NOT Security Issues
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-door-open-not-security-issues
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-door-open-not-security-issues
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

This is an incomplete list of issues
that are not considered vulnerability issues for {{ cookiecutter.project_name }},
based on its design,
usage contexts
and threat model.

These items represent
intentional design choices,
controlled risks
or edge cases
that do not meet
the criteria of a vulnerability.

#### API Misuse
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#api-misuse
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#api-misuse
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

If a reported issue is only triggered
by an application using the API
in a way that is not documented to work
— or even documented _not to work_ —,
it is probably
not going to be considered a security problem.
We only guarantee secure
and proper functionality
when the APIs are used
as expected and documented.

There can be a discussion
about what the documentation actually means
and how to interpret the text,
which might end up with us
still agreeing that it is a security problem.

#### Local Attackers already Present
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#local-attackers-already-present
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#local-attackers-already-present
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

When an issue can only be attacked or misused
by an attacker present
on the local system or network,
the bar is raised.
If a local user wrongfully has elevated rights
on your system
enough to attack {{ cookiecutter.project_name }},
they can probably already do much worse harm
and the problem is not really in {{ cookiecutter.project_name }}.

#### Debug, Experiments & Feature Flags
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#debug-experiments--feature-flags
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#debug-experiments--feature-flags
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Vulnerabilities in features
which are off by default
(in the official build)
and documented as experimental,
or exist only in debug mode,
are not eligible for reporting
and we do not consider them security problems.

The same applies to scripts and software
which are not installed by default
through `pip`.

{% if cookiecutter.app_type != 'bare_repo' -%}
#### Visible Command-line Arguments
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#visible-command-line-arguments
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#visible-command-line-arguments
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Sensitive user inputs
are not automatically hidden in the CLI.
This is an intentional design choice
for simplicity and compatibility with Typer.
As virtually every argument
can contain sensitive data,
depending on usage,
users are encouraged
to avoid passing sensitive data
via command-line arguments,
as per standard security best practices.

{% endif -%}
#### Busy Loops
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#busy-loops
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#busy-loops
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Busy-loops that consume 100% CPU time
but eventually end
(perhaps due to
a set timeout value
or otherwise)
are not considered security problems.
Applications are supposed
to already handle situations
when the transfer loop legitimately consumes 100% CPU time,
so while a prolonged such busy-loop is a nasty bug,
we do not consider it a security problem.

#### Saving Files
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#saving-files
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#saving-files
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{{ cookiecutter.project_name }} cannot protect against attacks
where an attacker has write access
to the same directory
where {{ cookiecutter.project_name }} is directed to save files.

{% if cookiecutter.app_type != 'bare_repo' -%}
#### Tricking a User to Run a Command Line
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#tricking-a-user-to-run-a-command-line
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#tricking-a-user-to-run-a-command-line
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

A creative,
misleading
or funny looking command line
is not a security problem.
The {{ cookiecutter.project_name }} command-line tool
takes options and URLs on the CLI
and if an attacker can trick the user
to run a specifically crafted {{ cookiecutter.project_name }} commands,
all bets are off.
Such an attacker can just as well
have the user run a much worse command
that can do something fatal
(like `sudo rm -rf /`).

{% endif -%}
#### Upstream Dependencies
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#upstream-dependencies
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#upstream-dependencies
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

The project depends on libraries
like Dynaconf and tomlkit,
which do not have formal security policies.
While these libraries are widely used
and well-maintained,
the project does not consider
problems that can be triggered
only by the use of a legacy dependency
security vulnerabilities.

The project actively monitors
for security advisories
in upstream dependencies
and updates their versions promptly
in the case of vulnerabilities.

<!-- DEFINE additional concepts of non-security-issues -->

### :octagonal_sign: Security Measures
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-door-closed-locked-security-measures
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-door-closed-locked-security-measures
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

{{ cookiecutter.project_name }} implements
the following measures
to enhance code security:

- Type hints
  and static analysis
  to prevent common errors;
{%- if cookiecutter.__app_class != 'bare' %}
- User input validation
  during configuration operations
  to prevent injection attacks;
{%- endif %}
{%- if cookiecutter.__scm_platform_lc == 'github' %}
- Dependency scanning
  and updates
  through Dependabot;
{%- endif %}
- Automated security scans
{%- if cookiecutter.coverage_service == 'Codacy' %}
  using Bandit locally
  and Codacy externally;
{%- else %}
  using Bandit locally;
{%- endif %}
- Signed commits
  and releases.

### :lock_with_ink_pen: Security Guarantees
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-shield-plus-security-guarantees
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-shield-plus-security-guarantees
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

Security guarantees provided
by the project:

{% if cookiecutter.__app_class == 'bare' -%}
<!-- UPDATEME with guarantees your project and upstream dependencies give in regards to security -->

{% else -%}
- {{ cookiecutter.project_name }} does not
  spawn external programs;
- {{ cookiecutter.project_name }} does not allow
  execution of abribtrary or unsafe code;
- {{ cookiecutter.project_name }} does not
  access files outside the user directory,
  and does not access files outside
  `.config/{{ cookiecutter.repo_name }}`
  or `.local/state/log/{{ cookiecutter.repo_name }}`
  unless explicitly instructed
  by the user to do so;
- {{ cookiecutter.project_name }}
  provides clear documentation
  about security considerations
  in its usage guides.

The upstream dependencies
guarantee additional levels of containment
by:

- Accessing only
  a restrict set of environment variables
  — starting with `{{ cookiecutter.__envvar }}`
  and `{{ cookiecutter.__envvar }}_SECRET` —
  via the Orbittings API;
  {{ cookiecutter.project_name }} does not access
  other environment variables
  in the system;
- Handling settings file misconfigurations
  explicitly
  via the Orbittings API.

{% endif -%}
### :speech_balloon: Comments on This Policy
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-speech-comments-on-this-policy
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-speech-comments-on-this-policy
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

If you have any suggestions
on how our security processes
could be improved,
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
please open a [Request for Improvement][6]
on our Issue Tracker.
{%- else %}
please open a [Request for Improvement][4]
in our Discussions page.
{%- endif %}
We will reply to you
in due time.

### :mag: Relevant Policies
{%- if cookiecutter.create_docs %}
<!-- This section is also described in the formal documentation
{%- if cookiecutter.licence != 'nos' %}
  [link]: ./docs/development/security.md#lucide-log-out-relevant-policies
{%- else %}
  [link]: ./docs/noticeboard/advisories/guide.md#lucide-log-out-relevant-policies
{%- endif %}

  REMEMBER TO MIRROR ANY CHANGES ON BOTH FILES
-->
{%- endif %}

<!-- UPDATEME with security policies of third-party libraries relevant to {{ cookiecutter.project_name }} -->

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md
[2]: https://pypi.org/project/{{ cookiecutter.repo_name }}/
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[3]: https://advisories.gitlab.com/
[4]: {{ cookiecutter.__scm_link_url }}/releases
[5]: https://docs.sigstore.dev/cosign/verifying/verify/
[6]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}
[3]: https://github.com/advisories
[4]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
