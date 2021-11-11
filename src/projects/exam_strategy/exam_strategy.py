#!/usr/bin/env python3
"""
Exam strategy
"""

from collections import namedtuple
from typing import List, Tuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: List[Item]) -> List[int]:
    """
    General Knapsack solution.
    This function takes the knapsack capacity and the list of items (named tuples) to consider.
    The function returns a list of chosen indices.
    This function is optional but highly recommended.
    Use of the named tuple Item is optional but encouraged.
    """
    value = []
    weight = []

    for i in items:
        value.append(i[0])
        weight.append(i[1])

    Item = []
    numberofQuestion = weight[0]
    
    Item = [[0 for i in range(capacity+1)] for i in range(numberofQuestion+1)]

    value.pop(0)
    weight.pop(0)

    for i in range(numberofQuestion+1): 
        for j in range(capacity + 1):

            # m[0,w] = 0
            if i == 0 or j == 0:
                Item[i][j] = 0

            # m[i,w] = m[i-1,w] if wi > w
            elif weight[i-1] > j:
                Item[i][j] = Item[i-1][j]

            # m[i,w] = max(m[i-1,w], m[i-1,w-wi]+vi) if wi <= w
            else:
                Item[i][j] = max(Item[i-1][j], Item[i-1][j-weight[i-1]] + value[i-1])
    
    indeces = Item[numberofQuestion][capacity]
    currentCapacity = capacity
    result = []

    for i in range(numberofQuestion, 0, -1):

        if Item[numberofQuestion][capacity] != Item[i-1][currentCapacity]:
            result.append([i-1])
            result.append(weight[i - 1]) 
            Item[numberofQuestion][capacity] -= value[i - 1] 
            currentCapacity -= weight[i - 1]
            
    final=[j for i in result[::2] for j in i]
    final.reverse()
    return [final, indeces]



def pick_questions_to_answer(filename: str) -> Tuple[List[int], int]:
    """
    Main selection function
    This function takes file name as an argument.
    The function returns a tuple of two items: the list of chosen indices and total point value of all selected questions.
    """
    chosenIndices = []
    file = open(filename)
    for line in file:
        line = line.split()
        if line:          
            line = [int(float(i)) for i in line]
            chosenIndices.append(line)
    return (knapsack(chosenIndices[0][0], chosenIndices))

def main():
    """Entry point"""
    for i in range(1, 6):
        filename = f"data/projects/exam_strategy/questions{i}.in"
        selection = pick_questions_to_answer(filename)
        print(
            f"Case {i}: Items {sorted(selection[0])} sum up to {selection[1]}"
        )


if __name__ == "__main__":
    main()