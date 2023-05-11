#!/usr/bin/python3

import argparse
from pathlib import Path

from utilities import findDirectory
from website.site import Website
from writers.writer import WriteManager


def main():
    parser = argparse.ArgumentParser(
        prog="Website Analysis",
        description="Python script to analyze local copies of websites",
    )

    parser.add_argument(
        "directory", help="Directory containing the local copy of the website", type=str
    )

    args = parser.parse_args()
    path = Path(args.directory)

    found = findDirectory(path)
    if not found:
        return

    site = Website(path)

    wMan = WriteManager(site)
    wMan.write()

    return


if __name__ == "__main__":
    main()
