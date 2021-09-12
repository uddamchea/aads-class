#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    dict = {}
    for i in dict.items():
        slotLabels = [x for x in range(0, size+1)]
        dict[key] = slotLabels
    print(dict)
    result = key % size
    print(result)
hash_remainder(5,3)
    # raise NotImplementedError


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    #raise NotImplementedError
    pass


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    #raise NotImplementedError
    pass


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    #raise NotImplementedError
    pass


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    #raise NotImplementedError
    pass

