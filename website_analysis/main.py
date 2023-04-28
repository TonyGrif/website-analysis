#!/usr/bin/python3

import argparse
from pathlib import Path

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
    path = Path(args.directory)

    found = findDirectory(path)
    if not found:
        return
    
    return

def findDirectory(arg: Path) -> bool:
    if not arg.exists():
        print("Not a valid destination")
        return False

    if not arg.is_dir():
        print("Please specify a directory, not a file") 
        return False

    return True

if __name__ == "__main__":
    main()
