# :closed_lock_with_key: Security

[[_TOC_]]

## :placard: Current Vulnerability Status

As of
**November 2025**,
there are no unpatched vulnerabilites
of medium or higher severity
that have been publicly known
for more than 60 days
in the Galactipy codebase.

## :postbox: Reporting Vulnerabilities

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

**`mpq dot dev at pm dot me`**

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
> <details>
>
> **Key fingerprint:**
> ```
> pub   rsa4096 2025-08-28 [SC]
> E3E6 AB38 0C5B 3451 71FA  C076 83D1 10FE 5ADE 9DD2
> uid           [ultimate] Manoel Pereira de Queiroz <mpq.dev@pm.me>
> sub   rsa4096 2025-08-28 [E]
> ```
>
> **Key data:**
> ```
> -----BEGIN PGP PUBLIC KEY BLOCK-----
>
> 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
> zSCCVd4=
> =zZ9a
> -----END PGP PUBLIC KEY BLOCK-----
> ```
> </details>

We prefer all communications
to be in **English**.

## :clipboard: Response Process

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

## :loudspeaker: Disclosure Policy

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
     is sent to the Galactipy
     security mailing list;
   - The changes are pushed
     to the public repository
     and new builds are deployed
     to GitLab Releases;
   - Within **6 hours**
     of the mailing list being notified,
     a copy of the advisory
     will be published
     on the [GitLab Advisory Database][1].

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

## :accept: Supported Versions

Being a Cookiecutter template
with limited scripts
and no public API,
only the **latest version**
of Galactipy
is supported
for security updates.

> [!NOTE]
> Current Galactipy release: **`v0.22.0`**

## :octagonal_sign: Security Measures

Galactipy implements
the following measures
to enhance code security:

- Type hints
  and static analysis
  to prevent common errors;
- User input validation
  during project setup
  to prevent injection attacks;
- Dependency scanning
  and updates
  through Renovate;
- Automated security scans
  using Bandit locally
  and Codacy externally;
- Signed commits
  and releases.

## :lock_with_ink_pen: Security Guarantess

Security guarantees provided
by the project:

- Galactipy does not
  access environment variables;
- Galactipy does not
  spawn external programs;
- Galactipy does not allow
  execution of abribtrary or unsafe code
  in pre and post-gen hooks;
- Galactipy templates
  do not expose sensitive data
  in generated files;
- Galactipy
  does not introduce injection risks
  or uncontrolled behaviour
  due to malformed
  Jinja statements;
- Galactipy
  does not introduce injection risks
  or uncontrolled behaviour
  in generated Python scripts;
- Galactipy templates
  provide default content
  that avoid security misconfigurations;
- Galactipy templates
  provide clear documentation
  about security considerations
  for the generated project.

The Cookiecutter package
guarantees additional levels of containment
by:

- Running hook scripts locally
  on the user's machine
  with the user's own permissions;
- Using Jinja templating,
  which is sandboxed to the extent
  of rendering variables and conditionals
  based on user input;
- Not accessing environment variables
  or executing random code
  beyond the defined hooks;
- Copying files from the template repository
  with support to
  exclude some files from rendering
  to prevent executing or modifying files
  unintentionally.

[1]: https://advisories.gitlab.com/
