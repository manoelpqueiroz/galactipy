# Checks & Hooks

Developers are encouraged
to run local tests,
check codestyle and static typing
with the `invoke sweep` command
before committing.

Pre-commit hooks are configured
to block updates not following the rules:

- All files must comply to the [POSIX][1] standard;
- Code files must comply with the Ruff linter.

Ensure both Invoke and Pre-Commit are [installed][2]
in your virtual environment.

<!-- Anchors -->

[1]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206
[2]: ../development_setup.md
