#!/usr/bin/env python3
"""
`stack` implementation

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import heapq
from typing import Any


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """
    LIFO data structure

    Items are added and removed at the same end of the collection
    """

    def __init__(self):
        """Initialize a stack using heapq"""
        # NOTE: Do not modify this method
        self.items = []

    def push(self, item: Any) -> None:
        """
        Add a new item to stack

        :param item: a new item to push onto the stack
        """
        # TODO: Implement this method
        # self.items.insert(0,item)
        heapq.heappush(self.items, (len(self.items) * -1, item))


    def pop(self) -> Any:
        """
        Remove an item from the stack

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        # TODO: Implement this method
        if len(self.items)>0:
            # heapq._heapify_max(self.items)
            return heapq.heappop(self.items)[1]
        else:
            raise StackError("Cannot pop from an empty stack")


    def peek(self) -> Any:
        """
        Look at the top item without removing it

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        # TODO: Implement this method
        if len(self.items)>0:
            # return self.items[len(self.items) * -1][1]
            # using heapq
            return heapq.nsmallest(1, self.items)[0][1]

        else:
            raise StackError("Nothing to see here, the stack is empty")


    def __bool__(self) -> bool:
        """
        Evaluate the stack

        :return: False if the stack is empty, True otherwise
        """
        # TODO: Implement this method
        if len(self.items) != 0:
            return True
        else:
            return False


    def __len__(self) -> int:
        """
        Return the number of items in the stack

        :return: number of items in the stack (0 if the stack is empty)
        """
        # TODO: Implement this method
        return len(self.items)