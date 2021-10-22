#!/usr/bin/env python3
"""
`anomalycounter` implementation

@authors: Ratanak Uddam Chea
@version: 2021.10
"""

from pathlib import Path

def count(filename: str) -> int:

  anomalyList = []
  anomalyCounter = 0
  readFile = open(filename, "r")

  for anomaly in readFile:
    anomaly = list(anomaly.replace("\n", ""))
    anomalyList.append(anomaly)

  def helper(anomalyList,i, j):

    if len(anomalyList) > i >= 0 and len(anomalyList[0]) > j >= 0 and anomalyList[i][j] == "*":
        anomalyList[i][j] = "."
        helper(anomalyList, i+1, j)
        helper(anomalyList, i-1, j)
        helper(anomalyList, i, j+1)
        helper(anomalyList, i, j-1)

  for i in range(len(anomalyList)):
    for j in range(len(anomalyList[0])):

      if anomalyList[i][j] == "*":
        anomalyCounter += 1
        helper(anomalyList,i, j)

  return anomalyCounter
                   
def main():
    """Entry point"""
    data_dir = "data/projects/anomalycounter/"
    for f in Path(data_dir).glob("*.in"):
        print(f"{f.name}: {count(f)}")


if __name__ == "__main__":
    main()
