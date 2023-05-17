from pathlib import Path


def findDirectory(arg: Path) -> bool:
    """
    Determine if a given path is a directory.

    Parameters:
    arg (Path): Given path to analyze.

    Returns:
    True (bool): If the path exists and is a directory.
    False (bool): If the path is nonexistent or if the path is not a directory.
    """
    if not arg.exists():
        print("Not a valid destination")
        return False

    if not arg.is_dir():
        print("Please specify a directory, not a file")
        return False

    return True
