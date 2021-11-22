#!/usr/bin/env python3
"""
Convex Hull

@authors: Roman Yasinovskyy
@version: 2021.11
"""


def get_convex(filename: str) -> list:
    """
    Find points on the convex hull

    Calculate the result with p0 as the lowest-rightmost

    :param filename: name of a file with all all points
    :return: list of point in the correct order (starting with the rightmost-lowest)
    """
    with open(filename) as f:
        data = f.read().splitlines()

    idx = 0
    li = list()
    
    while idx < len(data):
        test = data[idx].split()
        if test[2] != "N":
            li.append(test[0:2])
        idx += 1

    for i in range(0, len(li)):
        for j in range(0, len(li[i])):
            li[i][j] = int(li[i][j])
    # print(li)
    return li


def measure_convex(hull_points: list) -> float:
    """
    Calculate the length of the convex hull

    :param hull_points: all points on the convex hull in counter-clockwise order
    :return: length of the convex hull
    """
    idx = 0
    totaldistance = 0

    while idx < len(hull_points):
        first = hull_points[idx]

        if idx+1 >= len(hull_points):
            second = hull_points[0]

        else:
            second = hull_points[idx+1]

        totaldistance += (((second[0]-first[0])**2)+((second[1]-first[1])**2)) ** 0.5
            
        idx += 1

    # print(totaldistance)  
    return totaldistance  


def main():
    """Entry point"""
    print(f"{'file':20s}{'points':10s}{'length'}")
    for i in [1, 2, 3]:
        filename = f"convexhull{i}.in"
        hull_points = get_convex("data/projects/convexhull/" + filename)
        hull_length = measure_convex(hull_points)
        print(f"{filename:20s}{len(hull_points):<10d}{hull_length}")


if __name__ == "__main__":
    main()
