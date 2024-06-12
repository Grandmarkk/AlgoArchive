import numpy as np
import sort
from tree.binary_search_tree import BST, BST_Node
from tree.b_tree import BTree
from search.boyer_moore import boyer_moore

if __name__ == "__main__":
    root = BST_Node(3)
    bst = BST(root)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(4)
    bst.insert(6)
    bst.insert(6)
    bst.delete(2)

    b_tree = BTree(5)
    test_list = [np.random.randint(-100, 100) for i in range(10)]
    for num in test_list:
        b_tree.insert(num)
    print(b_tree.traverse())

    # test boyer-moore
    pattern = "aba"
    text = "abaabababa"
    print(boyer_moore(text, pattern))