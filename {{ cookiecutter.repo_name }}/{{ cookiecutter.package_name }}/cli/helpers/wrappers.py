"""Decorators used to streamline Typer application behaviour."""
from collections.abc import Callable
from functools import wraps

import typer


def naked_command(app: typer.Typer) -> Callable:
    """Display help and exit a Typer app when it is invoked without a subcommand.

    The default behaviour for Click command groups is to exit with a status code 2 when
    invoked without a subcommand. This function should be used as a decorator to
    override this behaviour and exit the program with status 0 instead.

    Parameters
    ----------
    app : Typer
        The Typer application instance to attach the callback to. The Typer object
        must have been instantiated without the `no_args_is_help` parameter, otherwise
        the CLI will break upon invocation.

    Returns
    -------
    Callable
        A decorator function that wraps the callback.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        @app.callback(invoke_without_command=True)
        def wrapper(ctx: typer.Context, *args, **kwargs):
            if not ctx.invoked_subcommand:
                ctx.get_help()
                raise typer.Exit(0)

            return func(ctx, *args, **kwargs)

        return wrapper

    return decorator
