import pytest

from hooks.post_gen_project import rmdir
from hooks.pre_gen_project import validate_line_length


def test_validate_line_length():
    assert validate_line_length(88) is None

    with pytest.raises(ValueError):
        validate_line_length(1_000)

    with pytest.raises(ValueError):
        validate_line_length(-10)


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
