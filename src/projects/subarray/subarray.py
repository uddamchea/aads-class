#!/usr/bin/env python3
"""Subarray"""

def kadane(array: list) -> int:
    total_Sum = 0
    current_Sum = 0
    
    for i in range (0, len(array)):
        current_Sum += array[i]
        
        if total_Sum < current_Sum:
            total_Sum = current_Sum

        if current_Sum <= 0:
            current_Sum = 0

    return total_Sum

def main():
    """This is the main function"""
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane(array))


if __name__ == "__main__":
    main()
