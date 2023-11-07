"""This module contains utility functions designed
for use in the 'website-analysis' program
"""

from pathlib import Path


def find_directory(arg: Path) -> bool:
    """Determines if an argument is a directory.

    Parameters:
        arg (Path): The path to check.

    Returns:
        True (bool): If the path is a directory.

    Throws:
        FileNotFoundError: If the path does not exist.
        NotADirectoryError: If the path given is a file, not a directory.
    """
    if not arg.exists():
        raise FileNotFoundError
    if not arg.is_dir():
        raise NotADirectoryError
    return True


def create_report_directory(directory: str or Path = "reports/") -> None:
    """Create the reports directory and any parent directories needed.

    Parameters:
        directory (Path): The directory path to create.
    """
    Path.mkdir(directory, parents=True, exist_ok=True)
