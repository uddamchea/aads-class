
#!/usr/bin/env python3
"""
`trees` implementation and driver
Turning in-order and post-order tree traversals into pre-order

"""
from collections import deque

def get_preorder(inorder: str, postorder: str) -> str:
    
    def helper(pointer1, pointer2, postorder, root, postorderDict, stack):

        if pointer1 > pointer2:
            return root
        
        rootValue = postorder[root]
        root -= 1
        index = postorderDict[rootValue]

        root = helper(index + 1, pointer2, postorder, root, postorderDict, stack)
        root = helper(pointer1, index - 1, postorder, root, postorderDict, stack)
        stack.append(rootValue)

        return root

    postorderDict = {}
    for index, value in enumerate(inorder):
        postorderDict[value] = index

    stack = deque()
    lastIndex = len(inorder) - 1
    helper(0, lastIndex, postorder, lastIndex, postorderDict, stack)
    
    getPreorder = str()

    while stack:
        getPreorder += str(stack.pop())

    return getPreorder

def main():
    """This is the main function"""
    print("Pre-order tree traversal")
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()