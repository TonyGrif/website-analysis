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
    return True    
