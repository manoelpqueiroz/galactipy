# :closed_lock_with_key: Security

{% if cookiecutter.__scm_platform_lc == 'gitlab' -%}
[[_TOC_]]
{%- endif %}

## Announcements

### :placard: Current Vulnerability Status

As of
**{% now 'local', '%B %Y' %}**,
there are no unpatched vulnerabilites
of medium or higher severity
that have been publicly known
for more than 60 days
in the {{ cookiecutter.project_name }} codebase.

### :atm: Current Security Advisories

We publish security advisories
for any vulnerabilities
we address.

As of
**{% now 'local', '%B %Y' %}**,
no security advisories have been announced.

## Guidelines

### :postbox: Reporting Vulnerabilities

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

We prefer all communications
to be in **English**.

### :clipboard: Response Process

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

The folllowing process
will be triggered
once you send
your report:

1. The security report is received
   and is assigned a primary handler;
   - This person will
     coordinate the fix and release process;
   - The problem is validated
     against all supported Galactipy versions;
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
     on the [{{ cookiecutter.__scm_platform_base }} Advisory Database][2].

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

### :traffic_light: Severity levels

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

The following library versions
are currently supported
for security updates
and vulnerability reporting:

<!-- UPDATEME with your supported versions -->

| Version  |   Support Status   | Commentary |
|:--------:|:------------------:|------------|
| `v0.1.0` | :white_check_mark: |            |

### :octagonal_sign: Security Measures

{{ cookiecutter.project_name }} implements
the following measures
to enhance code security:

- Type hints
  and static analysis
  to prevent common errors;
- User input validation
  during configuration operations
  to prevent injection attacks;
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

### :lock_with_ink_pen: Security Guarantess

Security guarantees provided
by the project:

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

### :speech_balloon: Comments on This Policy

If you have any suggestions
on how our security processes
could be improved,
please open a [Request for Improvement][3]
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
on our Issue Tracker.
{%- else %}
in our Discussions page.
{%- endif %}
We will reply to you
in due time.

### :mag: Relevant Policies

<!-- UPDATEME with security policies of third-party libraries relevant to {{ cookiecutter.project_name }} -->

[1]: {{ cookiecutter.__scm_link_url }}/blob/master/CONTRIBUTING.md
{%- if cookiecutter.__scm_platform_lc == 'gitlab' %}
[2]: https://advisories.gitlab.com/
[3]: {{ cookiecutter.__scm_link_url }}/issues/new?description_template=Request%20for%20Improvement
{%- else %}
[2]: https://github.com/advisories
[3]: {{ cookiecutter.__scm_link_url }}/discussions/new?category=requests-for-improvement
{%- endif %}
