from pathlib import Path


def findDirectory(arg: Path) -> bool:
    if not arg.exists():
        print("Not a valid destination")
        return False

    if not arg.is_dir():
        print("Please specify a directory, not a file")
        return False

    return True
