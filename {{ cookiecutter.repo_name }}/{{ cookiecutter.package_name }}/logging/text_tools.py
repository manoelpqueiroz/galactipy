"""Perform basic string operations to refine logger formatting."""

from typing import Optional

from functools import lru_cache
from pathlib import Path
from shutil import get_terminal_size
from textwrap import wrap

from nebulog import logger

logger.disable("{{ cookiecutter.package_name }}")


class LoggerFormatter:
    """Handle formatting calculations for logger output alignment."""

    ADDITIONAL_CHARACTERS = 4  # Additional characters for ".py" and ":" separator
    SHELL_LJUST_TEMPLATE = "[YYYY.mm.dd HH:MM:SS]+sss x critical x "
    SHELL_RJUST_TEMPLATE = " x "  # Separator between message and location
    MINIMUM_WRAPPER_WIDTH = 20

    def __init__(self, project_root: Optional[Path] = None):
        """Initialize formatter with project root directory.

        Parameters
        ----------
        project_root : Path, optional
            Root directory to scan for Python files. Defaults to parent directory of
            this file.
        """
        self.project_root = self._resolve_project_root(project_root)

    def _resolve_project_root(self, project_root: Optional[Path]) -> Path:
        """Resolve the project root directory.

        Parameters
        ----------
        project_root : Path, optional
            Root directory to use. If None, defaults to the parent directory of this
            file.
        """
        return project_root if project_root is not None else Path(__file__).parents[1]

    @property
    @lru_cache(maxsize=1)
    def python_modules(self) -> tuple[Path, ...]:
        """Get all Python modules in the project."""
        return tuple(self.project_root.glob("**/*.py"))

    @lru_cache(maxsize=1)
    def get_longest_filename(self) -> int:
        """Find the longest filename in the project."""
        if not self.python_modules:
            return 0

        return max(len(module.stem) for module in self.python_modules)

    @staticmethod
    def _get_file_linecount(filepath: Path) -> int:
        """Count the number of lines in a single file.

        Parameters
        ----------
        filepath : Path
            Path to the file to count lines in.

        Returns
        -------
        int
            Number of lines in the file.
        """
        try:
            with filepath.open("r", encoding="utf-8") as file:
                return sum(1 for _ in file)
        except (OSError, UnicodeDecodeError) as e:
            logger.warning(f"Could not read file {filepath}: {e}")
            return 0

    @lru_cache(maxsize=1)
    def get_project_linecount_oom(self) -> int:
        """Find the largest order of magnitude of line counts in the project.

        Returns
        -------
        int
            Number of digits of the largest line count.
        """
        if not self.python_modules:
            return 1

        largest_linecount = max(
            self._get_file_linecount(file) for file in self.python_modules
        )

        return len(str(largest_linecount))

    def get_location_padding(self) -> int:
        """Calculate the width necessary to turn location into an aligned column.

        Location is a combination of logging information comprised of `filename:line`.

        Returns
        -------
        int
            Total padding width needed for location alignment.
        """
        return (
            self.get_longest_filename()
            + self.get_project_linecount_oom()
            + self.ADDITIONAL_CHARACTERS
        )

    def get_wrapper_limit(self) -> int:
        """Calculate the maximum width for message wrapping.

        Returns
        -------
        int
            Maximum character width for wrapped messages.
        """
        terminal = get_terminal_size()

        wrapper_limit = (
            terminal.columns
            - len(self.SHELL_LJUST_TEMPLATE)
            - len(self.SHELL_RJUST_TEMPLATE)
            - self.get_location_padding()
        )

        return max(wrapper_limit, self.MINIMUM_WRAPPER_WIDTH)  # Ensure minimum width

    def split_message(self, message: str) -> tuple[str, Optional[str]]:
        """Split a message into wrapped lines for proper formatting.

        Parameters
        ----------
        message : str
            The message string to split and format.

        Returns
        -------
        tuple
            A tuple with `message` wrapped as `first_line` and `continuation_lines`. The
            latter will be None if message fits in one line.
        """
        if not message:
            return "", None

        message_lines = wrap(message, width=self.get_wrapper_limit())

        if not message_lines:
            return "", None

        first_line = message_lines[0].ljust(self.get_wrapper_limit())

        if len(message_lines) == 1:
            return first_line, None

        continuation_lines = self._format_continuation_lines(message_lines[1:])
        return first_line, continuation_lines

    def _format_continuation_lines(self, continuation_lines: list[str]) -> str:
        """Format continuation lines with proper indentation.

        Parameters
        ----------
        continuation_lines : list
            Lines to be formatted as continuation lines.

        Returns
        -------
        str
            Formatted continuation lines with the indent defined in
            `SHELL_LJUST_TEMPLATE`.
        """
        indent = " " * len(self.SHELL_LJUST_TEMPLATE)
        return indent + f"\n{indent}".join(continuation_lines)
