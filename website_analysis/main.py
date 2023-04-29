#!/usr/bin/python3

import argparse
from pathlib import Path

from writers.writer import WriteManager

def main():
    parser = argparse.ArgumentParser(
        prog="Website Analysis",
        description="Python script to analyze local copies of websites"
    )

    parser.add_argument(
        "directory",
        help="Directory containing the local copy of the website", 
        type=str
    )

    args = parser.parse_args()

    found = findDirectory(path)
    if not found:
        return

    wMan = WriteManager()
    wMan.write()
    
    return

def findDirectory(arg: Path) -> bool:
    arg = arg.resolve()
    
    if not arg.exists():
        print(f"{arg} is not a valid destination")
        return False

    if not arg.is_dir():
        print(f"{arg} is not a directory") 
        return False

    return True

if __name__ == "__main__":
    main()
