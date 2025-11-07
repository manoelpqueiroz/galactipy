"""Perform basic string operations to refine logger formatting."""

from functools import lru_cache
from pathlib import Path

from nebulog import logger

logger.disable("{{ cookiecutter.package_name }}")


class LoggerFormatter:
{%- if cookiecutter.docstring_style != 'other' %}
    """Handle formatting calculations for logger output alignment.
{%- if cookiecutter.docstring_style == 'numpy' %}

    Parameters
    ----------
    project_root : Path, optional
        Root directory to scan for Python files. Defaults to parent directory of this
        file.
{%- elif cookiecutter.docstring_style == 'google' %}

    Args:
        project_root: Root directory to scan for Python files. Defaults to parent
        directory of this file.
{%- else %}

    :param project_root: Root directory to scan for Python files. Defaults to parent
        directory of this file.
    :type project_root: Path/None
{%- endif %}
    """
{%- else %}
    """Handle formatting calculations for logger output alignment."""
{%- endif %}

    ADDITIONAL_CHARACTERS = 4  # Additional characters for ".py" and ":" separator
    SHELL_LJUST_TEMPLATE = "[YYYY.mm.dd HH:MM:SS]+sss x critical x "
    SHELL_RJUST_TEMPLATE = " x "  # Separator between message and location
    MINIMUM_WRAPPER_WIDTH = 20

    def __init__(self, project_root: Path | None = None):
        """Initialize formatter with project root directory."""
        self.project_root = self._resolve_project_root(project_root)

    def _resolve_project_root(self, project_root: Path | None) -> Path:
        """Resolve the project root directory."""
        return project_root if project_root is not None else Path(__file__).parents[1]

    @property
    @lru_cache(maxsize=1)
    def python_modules(self) -> tuple[Path, ...]:
{%- if cookiecutter.docstring_style != 'other' %}
        """Get all Python modules in the project.
{%- if cookiecutter.docstring_style == 'numpy' %}

        Returns
        -------
        tuple
            A tuple of Path objects containing all modules of `project_root`.
{%- elif cookiecutter.docstring_style == 'google' %}

        Returns: A tuple of Path objects containing all modules of `project_root`.
{%- else %}

        :return: A tuple of Path objects containing all modules of `project_root`.
        :rtype: tuple
{%- endif %}
        """
{%- else %}
        """Get all Python modules in the project."""
{%- endif %}
        return tuple(self.project_root.glob("**/*.py"))

    @lru_cache(maxsize=1)
    def get_longest_filename(self) -> int:
{%- if cookiecutter.docstring_style != 'other' %}
        """Find the longest filename in the project.
{%- if cookiecutter.docstring_style == 'numpy' %}

        Returns
        -------
        int
            The length of the longest filename inside `project_root`.
{%- elif cookiecutter.docstring_style == 'google' %}

        Returns: The length of the longest filename inside `project_root`.
{%- else %}

        :return: The length of the longest filename inside `project_root`.
        :rtype: int
{%- endif %}
        """
{%- else %}
        """Find the longest filename in the project."""
{%- endif %}
        if not self.python_modules:  # pragma: no cover
            return 0

        return max(len(module.stem) for module in self.python_modules)

    @staticmethod
    def _get_file_linecount(filepath: Path) -> int:
        """Count the number of lines in a single file."""
        try:
            with filepath.open("r", encoding="utf-8") as file:
                return sum(1 for _ in file)
        except (OSError, UnicodeDecodeError) as e:  # pragma: no cover
            logger.warning(f"Could not read file {filepath}: {e}")
            return 0

    @lru_cache(maxsize=1)
    def get_project_linecount_oom(self) -> int:
{%- if cookiecutter.docstring_style != 'other' %}
        """Find the largest order of magnitude of line counts in the project.
{%- if cookiecutter.docstring_style == 'numpy' %}

        Returns
        -------
        int
            Number of digits of the largest line count.
{%- elif cookiecutter.docstring_style == 'google' %}

        Returns: Number of digits of the largest line count.
{%- else %}

        :return: Number of digits of the largest line count.
        :rtype: int
{%- endif %}
        """
{%- else %}
        """Find the largest order of magnitude of line counts in the project."""
{%- endif %}
        if not self.python_modules:  # pragma: no cover
            return 1

        largest_linecount = max(
            self._get_file_linecount(file) for file in self.python_modules
        )

        return len(str(largest_linecount))

    def get_location_padding(self) -> int:
{%- if cookiecutter.docstring_style != 'other' %}
        """Calculate the width necessary to turn location into an aligned column.

        Location is a combination of logging information comprised of `filename:line`.
{%- if cookiecutter.docstring_style == 'numpy' %}

        Returns
        -------
        int
            Total padding width needed for location alignment.
{%- elif cookiecutter.docstring_style == 'google' %}

        Returns: Total padding width needed for location alignment.
{%- else %}

        :return: Total padding width needed for location alignment.
        :rtype: int
{%- endif %}
        """
{%- else %}
        """Calculate the width necessary to turn location into an aligned column.

        Location is a combination of logging information comprised of `filename:line`.
        """
{%- endif %}
        return (
            self.get_longest_filename()
            + self.get_project_linecount_oom()
            + self.ADDITIONAL_CHARACTERS
        )
