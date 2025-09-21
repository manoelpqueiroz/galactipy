from pathlib import Path
from shutil import chown

from hooks.post_gen_project import rmdir
from hooks.pre_gen_project import validate_docstring_length, validate_line_length

import pytest


def test_validate_line_length():
    assert validate_line_length(88) is None  # type: ignore[func-returns-value]

    with pytest.raises(ValueError):
        validate_line_length(1_000)

    with pytest.raises(ValueError):
        validate_line_length(-10)


def test_validate_docstring_length():
    assert validate_docstring_length(88, 87) is None  # type: ignore[func-returns-value]

    assert validate_docstring_length(88, 88) is None  # type: ignore[func-returns-value]

    with pytest.raises(ValueError):
        validate_docstring_length(88, 100)


class TestRmDir:
    def test_remove_single_file(self, tmp_path):
        file_path = tmp_path / "test_file.txt"
        file_path.touch()

        rmdir(file_path)

        assert not file_path.exists()

    def test_remove_empty_directory(self, tmp_path):
        empty_dir = tmp_path / "empty_dir"
        empty_dir.mkdir()

        rmdir(empty_dir)

        assert not empty_dir.exists()

    def test_remove_directory_with_files(self, tmp_path):
        directory = tmp_path / "test_directory"
        directory.mkdir()

        file_alpha = directory / "alpha.txt"
        file_beta = directory / "beta.txt"
        file_gaga = directory / "gaga.txt"

        file_alpha.touch()
        file_beta.touch()
        file_gaga.touch()

        rmdir(directory)

        assert not directory.exists()
        assert not file_alpha.exists()
        assert not file_alpha.exists()
        assert not file_gaga.exists()

    def test_remove_directories_recursively(self, tmp_path):
        directory = tmp_path / "test_directory"
        directory.mkdir()

        subdirectory = directory / "subdirectory"
        subdirectory.mkdir()

        file_alpha = directory / "alpha.txt"
        file_beta = subdirectory / "beta.txt"
        file_gaga = subdirectory / "gaga.txt"

        file_alpha.touch()
        file_beta.touch()
        file_gaga.touch()

        rmdir(directory)

        assert not directory.exists()
        assert not subdirectory.exists()
        assert not file_alpha.exists()
        assert not file_beta.exists()
        assert not file_gaga.exists()

    def test_remove_nonexistent_path(self):
        nonexistent_path = Path("nonexistent_file_or_dir")

        with pytest.raises(ValueError):
            rmdir(nonexistent_path)

    @pytest.mark.xfail(
        reason="unable to use chown inside test environment as there is no user or group `galactipy-pytest`"  # noqa: E501
    )
    def test_remove_file_without_permission(self, tmp_path):
        file_path = tmp_path / "protected_file.txt"
        file_path.touch()

        chown(file_path, "galactipy-pytest", "galactipy-pytest")

        with pytest.raises(PermissionError):
            rmdir(file_path)

    @pytest.mark.xfail(
        reason="unable to use chown inside test environment as there is no user or group `galactipy-pytest`"  # noqa: E501
    )
    def test_remove_directory_without_permission(self, tmp_path):
        protected_dir = tmp_path / "protected_dir"
        protected_dir.mkdir()

        # TODO chown fails given there is no user or group "galactipy-pytest"
        # Consider implementation through CI/CD
        chown(protected_dir, "galactipy-pytest", "galactipy-pytest")

        with pytest.raises(PermissionError):
            rmdir(protected_dir)
