#!/usr/bin/python3

"""The main module for the website-analysis program.

This program allows the user to input a directory containing HTML
files and recieve output files containing analysis
on the data transfer these files would require.

This file can be run as `./main.py`
"""


import argparse
from pathlib import Path


from src.utils import find_directory


def main():
    """Run the website-analysis program."""
    parser = argparse.ArgumentParser(
        prog="Website Analysis",
        description="Python script to analyze local copies of websites",
    )

    parser.add_argument(
        "directory", help="Path to the local copy of the website", type=Path
    )

    args = parser.parse_args()
    try:
        find_directory(args.directory)
    except FileNotFoundError:
        print("Directory not found")
        return
    except NotADirectoryError:
        print("Directory not provided")
        return


if __name__ == "__main__":
    main()
