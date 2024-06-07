import sort
from tree.binary_search_tree import BST, BST_Node

if __name__ == "__main__":
    root = BST_Node(3)
    bst = BST(root)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(4)
    bst.insert(6)
    bst.insert(6)
    bst.delete(3)
    print(bst.traversal())