#!/usr/bin/env python3
"""
`trees` implementation and driver
Turning in-order and post-order tree traversals into pre-order
I took inspiration from stackoverflow regarding the logic behind this
"""
def get_preorder(inorder: str, postorder: str) -> str:

    rootList = []
    postorderDict = {}

    def helper(pointer1, pointer2, root):

        if pointer1 > pointer2:
            return root
    
        rootValue = postorder[root]
        root -= 1
        index = postorderDict[rootValue]

        root = helper(index + 1, pointer2, root)
        root = helper(pointer1, index - 1, root)
        rootList.append(rootValue)

        return root

    for i, j in enumerate(inorder):
        postorderDict[j] = i

    helper(0, len(inorder) - 1, len(inorder) - 1)
    
    getPreorder = ""

    while rootList:
        getPreorder += str(rootList.pop())

    return getPreorder

def main():
    """This is the main function"""
    print("Pre-order tree traversal")
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()

