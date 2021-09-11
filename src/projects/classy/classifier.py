#!/usr/bin/env python3
"""
A Classy Problem
"""

from typing import Dict, List


def classify(people: dict) -> list[str]:
    pass

def read_file(filename: str) -> dict[str, str]:
    data = open(filename, "r")
    dict = {}
    for i in data:
        splitData = i.split()
        splitData.pop()
        cleanData = [s.replace(":", "") for s in splitData]
        dict[cleanData[0]] = "".join(cleanData[1:])
    #print(dict)

def main():
    """Entry point"""
    people = read_file("data/projects/classy/classy01.txt")
    print(classify(people))

if __name__ == "__main__":
    main()