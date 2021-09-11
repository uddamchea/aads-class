#!/usr/bin/env python3
"""
A Classy Problem
"""

from typing import Dict, List


def classify(people: dict) -> list[str]:
    for key, value in people.items():
        cleanValue = value.split("-")
        cleanValue = cleanValue[::-1]
        people[key] = cleanValue
    #print(people)

    cleanValueList = list(people.values())
    maxValueList=[]
    for x in range(0, len(cleanValueList)):
        maxValueList.append(len(cleanValueList[x]))
        maxValue = max(maxValueList)
    #print(max(maxValueList))

    for key, value in people.items():
        for y in range(maxValue - len(value)):
            value.insert(len(value), "middle")
        people[key] = value
    #print(people)

    for key, value in people.items():
        for z in range(len(value)):
            if value[z] == "lower":
                value[z] = 1
            if value[z] == "middle":
                value[z] = 2
            if value[z] == "upper":
                value[z] = 3
        people[key] = value
    #print(people)

    for key, value in people.items():
        for e in range(len(value)):
            strings = [str(integer) for integer in value]
            a_string = "".join(strings)
        people[key] = a_string
    #print(people)

    resultDict = {k: v for k,v in sorted(people.items(), key= lambda v: v[1], reverse=True)}
    #return resultDict
    #print(resultDict)

    answers = list(resultDict.keys())
    #print(answers)
    return answers

def read_file(filename: str) -> dict[str, str]:
    data = open(filename, "r")
    dict = {}
    for i in data:
        splitData = i.split()
        splitData.pop()
        cleanData = [s.replace(":", "") for s in splitData]
        dict[cleanData[0]] = "".join(cleanData[1:])
    return dict

def main():
    """Entry point"""
    people = read_file("data/projects/classy/classy01.txt")
    print(classify(people))

if __name__ == "__main__":
    main()