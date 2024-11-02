# How to contribute

This project is being actively developed on [***GitLab***][1], with a [mirror][2] set up
on GitHub.

If you are exploring the project in GitHub and wish to open an issue, please do it
directly via the project's [Issues][3] page on GitLab.

## Dependencies

We use `poetry` to manage the [dependencies][4]. If you dont have `poetry`, you should
install with your package manager or `invoke poetry-download`.

To install dependencies and prepare [`pre-commit`][5] hooks you need to run the
`install` command:

```bash
invoke install
invoke pre-commit-install
```

To activate your virtualenv run `poetry shell`, or use your preferred virtual
environment manager.

## Codestyle

After installation you may execute code formatting.

```bash
invoke codestyle
```

### Checks

Many checks are configured for this project. The command `invoke codestyle --check` will
only check Ruff formatting without executing it.

The `invoke check-safety` command will look at the security of your code.

The command `invoke sweep` applies all checks.

### Before submitting

Before submitting your code please do the following steps:

1. Add any changes you want
1. Add tests for the new changes
1. Edit documentation if you have changed something significant
1. Run `invoke codestyle` to format your changes.
1. Run `invoke sweep` to ensure that types, security and docstrings are okay.

## Other help

You can contribute by spreading a word about this template. It would also be a huge
contribution to write a short article on how you are using it in your projects. You can
also share your best practices with us so we can continuously improve the project!

[1]: https://gitlab.com/manoelpqueiroz/galactipy
[2]: https://github.com/manoelpqueiroz/galactipy
[3]: https://gitlab.com/manoelpqueiroz/galactipy/-/issues
[4]: https://github.com/python-poetry/poetry
[5]: https://pre-commit.com/
