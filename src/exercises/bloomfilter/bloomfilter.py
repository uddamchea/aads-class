#!/usr/bin/env python3
"""Bloom filter implementation"""


from zlib import crc32


class BloomFilter:
    def __init__(self, size: int = 11, k: int = 3):
        """Initialize the filter"""
        self.k = k
        self._filter = [False] * size


    def _hash(self, word: str) -> tuple:
        """Return a tuple of k indices"""
        return tuple((crc32(bytes(f"{word}{i}", "utf8")) % len(self._filter) for i in range(self.k)))

    def add(self, word: str):
        """Add a dictionary word to the filter"""
        a = 1
        b = 2
        return a,b
        #call _hash
        #hash the word with k=3 (use loop) to get a tuple of 3 elements
        #call __contains__
        #add into the dict if the an element of the tuple is available

    def __contains__(self, word: str) -> bool:
        """Check if a word in in the filter"""
        return all([self._filter[i] for i in self._hash(word)])

    def __str__(self):
        """Return string representation of the filter"""
        return str(self._filter)

    def __len__(self):
        """Return size of the filter"""
        return len(self._filter)
