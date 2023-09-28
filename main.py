#!/usr/bin/python3

"""The main module for the website-analysis program.

This program allows the user to input a directory containing HTML
files and recieve output files containing analysis
on the data transfer these files would require.

This file can be run as `./main.py`
"""


import argparse


def main():
    """Run the website-analysis program."""
    parser = argparse.ArgumentParser(
        prog="Website Analysis",
        description="Python script to analyze local copies of websites",
    )

    parser.add_argument(
        "directory", help="Path to the local copy of the website", type=str
    )

    args = parser.parse_args()
    print(args.directory)


if __name__ == "__main__":
    main()
