import numpy as np
import sort
from tree.binary_search_tree import BST, BST_Node
from tree.b_tree import BTree
from search.boyer_moore import boyer_moore
from tree.binary_heap import Binary_Heap

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

    heap = Binary_Heap()
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    heap.insert(7)
    heap.insert(8)
    heap.insert(4)
    heap.insert(10)
    heap.insert(16)
    heap.insert(12)
    heap.insert(12)
    heap.insert(0)

    print(heap.heap)  # Output the internal heap array
    print(heap.get_min())  # Output the minimum element
    print(heap.extract_min())  # Extract the minimum element and print it
    heap.extract_min()
    heap.insert(-2)
    print(heap.heap)  # Output the internal heap array after extraction