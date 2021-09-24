#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    hashRemainder = key % size
    return hashRemainder

def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    keySqrStr = str(key ** 2)
    # Slicing str (: operator)
    hashMidSqr = int(keySqrStr[len(keySqrStr) // 2 - 1 : len(keySqrStr) // 2 + 1]) % size

    if len(keySqrStr) % 2 != 0:
        # Add a padding zero with zfill()
        keySqrStr = keySqrStr.zfill(len(keySqrStr)+1) #this returns a str
        return hashMidSqr
    return hashMidSqr

def hash_folding(key: str, size: int) -> int:
    """Find hash using folding method"""
    keyStr = str(key)
    # removes non digit 
    cleanKey = ''.join(c for c in keyStr if c.isdigit()) #returns a str
    n = 2
    splitKey = [cleanKey[i:i+n] for i in range(0, len(cleanKey), n)]

    for x in range(0, len(splitKey)):
        splitKey[x] = int(splitKey[x])
    totalKeySum = sum(splitKey)
    hashFolding = totalKeySum % size
    
    return hashFolding
        
def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    totalSum = 0 
    for i in range(0, len(key)):
        totalSum += ord(key[i])

    hashStr = totalSum % size
    return hashStr

def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    totalSum = 0 
    for i in range(0, len(key)):
        totalSum += ord(key[i]) * i

    hashStrW = totalSum % size
    return hashStrW