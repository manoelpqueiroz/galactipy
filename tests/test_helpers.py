from typing import List

from pathlib import Path


def bulk_file_creation(root_directory: Path, *args: str, **kwargs: List[str]) -> list:
    """Create a set of files and directories based on a root directory.

    Parameters
    ----------
    root_directory : str, Path
        Directory to serve as root for the folder structure.
    *args
        Names for the files to be created under `root_directory`.
    **kwargs
        Subdirectories to create should be used as named parameters, while
        files to be placed should be listed as a sequence.

    Returns
    -------
    list
        A list of Path objects created after the function ended its run.

    Raises
    ------
    TypeError
        If a value in args is not a string or Path object, and if an argument
        in kwargs is not an iterable.
    """
    list_of_paths = []

    def create_folder_with_items(folder: Path, *items: str) -> list:
        folder_paths = []

        folder.mkdir(exist_ok=True)

        folder_paths.append(folder)

        for file in items:
            try:
                file_path = folder / file

            except TypeError:
                msg = (
                    f"Object {file} with type '{type(file).__name__}' is not supported "
                    "for path creation."
                )
                raise TypeError(msg)

            else:
                file_path.touch()

                folder_paths.append(file_path)

        return folder_paths

    root_folder = create_folder_with_items(root_directory, *args)

    list_of_paths.extend(root_folder)

    for subdirectory, files in kwargs.items():
        try:
            _ = (e for e in files)  # Duck typing way to check if `files` is an iterable

        except TypeError:
            msg = (
                f"Object {files} is not an iterable, so it can not be specified as a "
                f"file for {subdirectory}."
            )
            raise TypeError(msg)

        else:
            sub_folder = root_directory / subdirectory
            sub_folder = create_folder_with_items(sub_folder, *files)

            list_of_paths.extend(sub_folder)

    return list_of_paths
