class BST_Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, root) -> None:
        self.root = root

    def search(self, target) -> BST_Node:
        def helper(node, target):
            if node == None:
                return None
            if node.key == target:
                return node
            if node.key > target:
                return helper(node.left, target)
            elif node.key < target:
                return helper(node.right, target)
        return helper(self.root, target)

    def insert(self, key) -> None:
        def helper(node, key):
            if node.key == key:
                return
            if node.key > key:
                if node.left == None:
                    node.left = BST_Node(key)
                    return
                else:
                    helper(node.left, key)
            elif node.key < key:
                if node.right == None:
                    node.right = BST_Node(key)
                    return
                else:
                    helper(node.right, key)
        helper(self.root, key)

    def delete(self, target) -> None:
        def min_value_node(node):
            current = node
            # Loop down to find the leftmost leaf
            while current and current.left is not None:
                current = current.left
            return current
        
        def helper(node, target):
            if node is None:
                return node
            if target < node.key:
                node.left = helper(node.left, target)
            elif target > node.key:
                node.right = helper(node.right, target)
            else:
                # Node with only one child or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # Node with two children:
                temp = min_value_node(node.right)
                node.key = temp.key
                node.right = helper(node.right, temp.key)
            return node
        self.root = helper(self.root, target)
                

    def traversal(self):
        def helper(node):
            if node == None:
                return
            helper(node.left)
            keys.append(node.key)
            helper(node.right)

        keys = []
        helper(self.root)
        return keys