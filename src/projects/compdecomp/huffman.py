#!/usr/bin/env python3
"""Huffman coding"""


import argparse
import heapq
import json
import logging
import pathlib
from collections import Counter
from typing import List, Tuple, Union

DATA_DIR = pathlib.Path("data/projects/compdecomp/")

class Node:
    """Class Node"""

    def __init__(self, value, weight: int, left=None, right=None):
        """
        value: letter in the text
        weight: number of times the letter appears in the text
        left: left child in the Huffman tree
        right: right child in the Huffman tree
        """
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"Node({self.value}, {self.weight}, {self.left}, {self.right})"


def build_tree(all_freq: dict) -> Node:
    """
    Construct a Huffman tree from the text
    :param all_freq: frequency table
    :return tuple the tree root
    """
    tree = []

    for i, j in all_freq.items():
        letterAndFreq = Node(i, j)
        heapq.heappush(tree, letterAndFreq)

    while len(tree) > 1:
        leftNode = heapq.heappop(tree)
        rightNode = heapq.heappop(tree)

        rootTuple = Node(tree, leftNode.weight + rightNode.weight)
        rootTuple.left = leftNode
        rootTuple.right = rightNode
        heapq.heappush(tree, rootTuple)

    return(rootTuple)

def traverse_tree(root: Node) -> str:
    """
    Traverse a tree pre-order and return the result
    :param root: tree root
    :return values of a tree
    """
    # pre-order is root-left-right
    leftSubtree = []  
    rightSubtree = []  
    leftSubtree.append(root)

    while len(leftSubtree) > 0:  
        treeNode = leftSubtree.pop()  

        if treeNode.left is None:  
            rightSubtree.append(treeNode)

        else:
            if treeNode.left is not None: 
                leftSubtree.append(treeNode.left)  
            leftSubtree.append(treeNode.right)  

    treeValues = ""

    for i in range(0, len(rightSubtree)):
        rightSubtreeValue = rightSubtree.pop().value
        treeValues += rightSubtreeValue

    return " ".join(treeValues)

def follow_tree(tree: Node, code: str) -> Union[str, None]:
    """
    Follow the code through the tree
    :param tree: tree root
    :param code: code to find
    :return node value or None
    """
    nodeValue = None

    for i in code:

        if i == "0":
            tree = tree.left

        if i == "1":
            tree = tree.right
        
        if tree.left is None and tree.right is None:
            nodeValue = tree.value

    return nodeValue


def mark_tree(d1: dict, d2: dict, root: Node, path: str) -> Union[None, tuple]:
    """
    Generate code for each letter in the text
    :param d1: character-to-code mapping
    :param d2: code-to-character mapping
    :param root: tree root
    :param path: path to the current node
    :return (d1, d2) tuple
    """
    if root.left is None and root.right is None:
        d1[root.value] = path
        d2[path] = root.value

    if root.left is not None:
        if root.left not in d1.keys():
            mark_tree(d1, d2, root.left, path + "0")

    if root.right is not None:
        if root.right not in d1.keys():
            mark_tree(d1, d2, root.right, path + "1")

    return (d1,d2)

def print_codes(d: dict, weights: dict) -> None:
    """
    Print letters of the text and their codes. The output is ordered by the letter weight.
    :param d: character-to-code mapping
    :param weights: character-to-frequency mapping
    """
    print(f"{'Letter':10s}{'Weight':^10s}{'Code':^10s}{'Length':^5s}")


def load_codes(codes: dict) -> Node:
    """
    Build the Huffman tree from the stored code-to-character mapping
    :param codes: code-to-character mapping
    :return root of the Huffman tree
    """
    root = Node(None, None)
    cur = root

    for i in codes:
        val = codes[i]
        for j in range(len(i)):
            if j == len(i) - 1:    
                if i[j] == '0' and cur.left is None:
                    node = Node(None, None)
                    node.value = val
                    cur.left = node
                if i[j] == '1' and cur.right is None:
                    node = Node(None, None)
                    node.value = val
                    cur.right = node
                if i[j] == '0' and cur.left is not None:
                    node = cur.left
                    node.value = val
                if i[j] == '1' and cur.right is not None:
                    node = cur.right
                    node.value = val
            else:
                if i[j] == '0' and cur.left is None:
                    node = Node(None, None)
                    cur.left = node
                    cur = cur.left
                if i[j] == '1' and cur.right is None:
                    node = Node(None, None)
                    cur.right = node
                    cur = cur.right
                if i[j] == '0' and cur.left is not None:
                    cur = cur.left
                if i[j] == '1' and cur.right is not None:
                    cur = cur.right
        cur = root
    return root

def compress(text: str, codes: dict) -> Tuple[bytes, int]:
    """
    Compress text using Huffman coding
    :param text: text to compress
    :param codes: character-to-code mapping
    :return (packed text, padding length) tuple
    """
    leadingZero = 0
    bitStr = "".join(list(codes[i]for i in text))

    while len(bitStr) % 8 > 0:
        leadingZero += 1
        bitStr += "0"

    byteStr = []
    bit_idx = 0

    while bit_idx < len(bitStr):
        byte = bitStr[bit_idx:bit_idx+8]
        byteStr.append(int(byte, 2))
        bit_idx += 8

    return (bytes(byteStr), leadingZero)


def decompress(bytestream: bytes, padding: int, tree: Node) -> str:
    """
    Decompress binary data using Huffman coding
    :param bytestream: bytes from the archived file
    :param padding: padding length
    :param tree: root of the Huffman tree
    :return decompressed (decoded) text
    """
    # test = int.from_bytes(bytestream, "big")
    # bit = bin(test)[2:]
    bit = "".join(format(byte, '08b') for byte in bytestream)
    bitnoPadding = bit[:-padding]

    result = ""
    i = 0
    code = ""
    for i in bitnoPadding:
        code += i
        if follow_tree(tree, code):
            result += follow_tree(tree, code)
            code = ""
    return result
        

    
def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Greet the audience")
    parser.add_argument(
        "-d",
        "--debug",
        help="Enable debug mode",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable verbose mode",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=args.loglevel)
    logging.info("Starting up")

    input_files = ["dead_dad", "alphabet", "example", "preamble"]

    for filename in input_files:
        logging.info("Building the tree")
        with open(DATA_DIR / pathlib.Path(f"{filename}.txt"), "r") as text_file:
            text = text_file.read().strip()
        weights = Counter(text)
        root = build_tree(weights)
        char_to_code, code_to_char = mark_tree({}, {}, root, "")

        logging.info("Text statistics")
        print(f"\n{text}")
        print_codes(char_to_code, weights)
        logging.debug(char_to_code)
        logging.debug(code_to_char)
        logging.debug(traverse_tree(root))

        logging.info("Compressing the text")
        archive, padding_length = compress(text, char_to_code)
        code_to_char["padding"] = padding_length
        print(
            f"Text: {text[:5]} ... {text[-5:]}. Compression ratio: {len(archive) / len(text):.3f}"
        )
        logging.debug(archive)

        logging.info("Loading codes from the file")
        with open(DATA_DIR / pathlib.Path(f"{filename}.json"), "r") as code_file:
            metadata = json.load(code_file)
        root = load_codes(metadata)
        padding_length = metadata.get("padding", 0)
        logging.debug(traverse_tree(root))

        logging.info("Decompressing the archive")
        with open(DATA_DIR / pathlib.Path(f"{filename}.bin"), "rb") as data_file:
            result = decompress(data_file.read(), padding_length, root)
        print(result)


if __name__ == "__main__":
    main()