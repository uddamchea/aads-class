#!/usr/bin/env python3
"""Turning in-order and post-order tree traversals into pre-order"""


def get_preorder(inorder: str, postorder: str) -> str:
    inorder = list(str(inorder))
    postorder = list(str(postorder))

    emptyStr = ""

    root = postorder.pop()
    rootIndex = inorder.index(root)
    rightSubtree = inorder[rootIndex+1:]
    leftSubtree = inorder[:rootIndex]

    if not leftSubtree and not rightSubtree:
        result = emptyStr
        return result

    elif leftSubtree:
        inorder = leftSubtree
        result = emptyStr + root
        get_preorder(inorder, postorder)

    else: 
        inorder = rightSubtree
        result = emptyStr + root
        get_preorder(inorder, postorder)
    # elif \
    #     leftSubtree:
    #     inorder = leftSubtree
    #     get_preorder(inorder, postorder)
    # else:
    #     return tree
        
def main():
    """This is the main function"""
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()