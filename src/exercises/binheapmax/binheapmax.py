#!/usr/bin/env python3
"""Binary Heap implementation"""

class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self):
        """Initializer"""
        self._heap = []
        self._size = 0

    def _perc_up(self, cur_idx: int) -> None:
        """Move a node up"""
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] > self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = self._heap[parent_idx], self._heap[cur_idx]
            parent_idx = cur_idx    
            # cur_idx = parent_idx

    def _perc_down(self, cur_idx: int) -> None:
        """Move a node down"""
        while 2 * cur_idx + 2 < len(self._heap):
            max_child_idx = self.get_max_child(cur_idx)
            if self._heap[cur_idx] < self._heap[max_child_idx]:
                self._heap[cur_idx], self._heap[max_child_idx] = self._heap[max_child_idx], self._heap[cur_idx]
            else:
                return
            max_child_idx = cur_idx
            # cur_idx = max_child_idx

    def add(self, item: Any) -> None:
        """Add a new item"""
        # TODO: Implement this function
        ...

    def remove(self) -> Any:
        """Remove an item from the heap"""
        # TODO: Implement this function
        ...

    def heapify(self, not_a_heap: list) -> None:
        """Turn a list into a heap"""
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_max_child(self, parent_idx):
        """Get the greater child"""
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 2
        return 2 * parent_idx + 2

    def __len__(self) -> int:
        """Get heap size"""
        return self._size

    def __str__(self) -> str:
        """Heap as a string """
        return str(self._heap)
