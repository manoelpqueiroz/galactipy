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
> Current Galactipy release: **`v0.21.0`**

[1]: https://advisories.gitlab.com/
