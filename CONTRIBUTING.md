# How to contribute

This project is being actively developed on [***GitLab***][1], with a [mirror][2] set up
on GitHub.

If you are exploring the project in GitHub and wish to open an issue, please do it
directly via the project's [Issues][3] page on GitLab.

## Dependencies

We use `poetry` to manage the [dependencies][4].
If you dont have `poetry`, you should install with `make poetry-download`.

To install dependencies and prepare [`pre-commit`][5] hooks you would need to run
`install` command:

```bash
make install
make pre-commit-install
```

To activate your `virtualenv` run `poetry shell`.

## Codestyle

After installation you may execute code formatting.

```bash
make codestyle
```

### Checks

Many checks are configured for this project. Command `make check-codestyle` will check
pyupgrade, black and isort.

The `make check-safety` command will look at the security of your code.

Comand `make lint` applies all checks.

### Before submitting

Before submitting your code please do the following steps:

1. Add any changes you want
1. Add tests for the new changes
1. Edit documentation if you have changed something significant
1. Run `make codestyle` to format your changes.
1. Run `make lint` to ensure that types, security and docstrings are okay.

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.

[1]: https://gitlab.com/manoelpqueiroz/galactipy
[2]: https://github.com/manoelpqueiroz/galactipy
[3]: https://gitlab.com/manoelpqueiroz/galactipy/-/issues
[4]: https://github.com/python-poetry/poetry
[5]: https://pre-commit.com/
