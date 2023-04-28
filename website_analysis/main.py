#!/usr/bin/python3

import argparse

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
    print(args.directory)
    
    return

def findDirectory(arg):

    return 

if __name__ == "__main__":
    main()
