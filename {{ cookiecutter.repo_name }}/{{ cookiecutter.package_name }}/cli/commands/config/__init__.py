"""Manage configuration for {{ cookiecutter.project_name }} via the CLI."""

import typer

from {{ cookiecutter.package_name }}.cli.commands.config.extend import config_extend_app
from {{ cookiecutter.package_name }}.cli.commands.config.get import config_get_app
from {{ cookiecutter.package_name }}.cli.commands.config.set import config_set_app
from {{ cookiecutter.package_name }}.cli.commands.config.unset import config_unset_app

config_app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
    help=(
        ":gear: Perform operations with {{ cookiecutter.project_name }} configuration."
    ),
)

config_app.add_typer(config_get_app)
config_app.add_typer(config_set_app)
config_app.add_typer(config_unset_app)
config_app.add_typer(config_extend_app)
