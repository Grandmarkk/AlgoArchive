class B_Tree_Node:
    '''
    The node structure used in B-Tree
    '''
    def __init__(self, isRoot=False, isLeaf=False):
        self.elements = []
        self.children = []
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.elmLen = 0
        

    def binarySearch(self, target):
        '''
        Binary search for the target in elements

        Output: 
            the index of the target if found
            the insert index of the target if not found
        '''
        left = 0
        right = len(self.elements) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.elements[mid] == target:
                return mid
            if self.elements[mid] > target:
                right = mid - 1
            elif self.elements[mid] < target:
                left = mid + 1
        return left
        
class BTree:

    def __init__(self, t):
        # branching factor
        self.t = t
        # number of element bounds
        self.lowerBound = t - 1
        self.upperBound = 2 * t - 1
        self.root = B_Tree_Node(True, True)

    def traverse(self):
        '''
        In-order traverse the tree to get the elements in sorted order
        '''

        def traverseHelper(root, words):
            if root:
                for i in range(root.elmLen):
                    if not root.isLeaf:
                        traverseHelper(root.children[i], words)
                    words.append(root.elements[i])
                if not root.isLeaf:
                    traverseHelper(root.children[-1], words)

        words = []
        traverseHelper(self.root, words)
        return words
            

    def search(self, root, target):
        '''
        Find the target in the tree

        Input:
            root: a node in the B-Tree (start search from root node)
            target: the target

        Output:
            the node where the target is found and the index
            None if not found
        '''
        index = root.binarySearch(target)
        # Found
        if index < root.elmLen and root.elements[index] == target:
            return (root, index)
        # Not found, and at leaf node
        if root.isLeaf:
            return None
        # Search in child node
        return self.search(root.children[index], target)
    
    def insert(self, word):
        '''
        Insert the input word if the input word is not in the tree
        '''
        if self.search(self.root, word) == None:
            self.insertHelper(self.root, word)

    def insertHelper(self, root, word):
        '''
        Insert an element into the tree

        Input:
            root: the node where the insertion starts from
            word: the element to be inserted
        '''
        index = root.binarySearch(word)
        # if is root, check if is full
        if root.isRoot and root.elmLen == self.upperBound:
            medianIndex = root.elmLen // 2
            # split the original root node around median
            newLeftNode = B_Tree_Node(False, True if root.isLeaf else False)
            newRightNode = B_Tree_Node(False, True if root.isLeaf else False)
            newLeftNode.elements = root.elements[:medianIndex]
            newLeftNode.children = root.children[:medianIndex+1]
            newLeftNode.elmLen = medianIndex
            newRightNode.elements = root.elements[medianIndex+1:]
            newRightNode.children = root.children[medianIndex+1:]
            newRightNode.elmLen = medianIndex
            # promot the median to be the new root
            newRoot = B_Tree_Node(True, False)
            newRoot.elements.append(root.elements[medianIndex])
            newRoot.elmLen = 1
            newRoot.children = [newLeftNode, newRightNode]
            self.root = newRoot
            # continue insert
            self.insertHelper(self.root, word)
            return
        # check if the next node is full
        if not root.isLeaf and root.children[index].elmLen == self.upperBound:
            curNode = root.children[index]
            medianIndex = curNode.elmLen // 2
            # split the original node around median
            newLeftNode = B_Tree_Node(False, True if curNode.isLeaf else False)
            newRightNode = B_Tree_Node(False, True if curNode.isLeaf else False)
            newLeftNode.elements = curNode.elements[:medianIndex]
            newLeftNode.children = curNode.children[:medianIndex+1]
            newLeftNode.elmLen = medianIndex
            newRightNode.elements = curNode.elements[medianIndex+1:]
            newRightNode.children = curNode.children[medianIndex+1:]
            newRightNode.elmLen = medianIndex
            # add the median element to its parent node
            root.elements.insert(index, curNode.elements[medianIndex])
            # insert the 2 splited nodes in place
            root.children[index] = newRightNode
            root.children.insert(index, newLeftNode)
            root.elmLen += 1
            self.insertHelper(root, word)
            return
        # insert to leaf
        if root.isLeaf:
            root.elements.insert(index, word)
            root.elmLen += 1
            return
        self.insertHelper(root.children[index], word)
    
    def delete(self, word):
        '''
        Delete the input word if the input word is in the tree
        '''
        if self.search(self.root, word) != None:
            self.deleteHelper(self.root, word)

    def deleteHelper(self, root, word):
        '''
        Delete the word in the tree

        Input:
            root: where the delete starts
            word: the target to be deleted
        '''
        index = root.binarySearch(word)
        if root.isLeaf:
            # word in leaf
            if index < root.elmLen and root.elements[index] == word:
                root.elements.pop(index)
                root.elmLen -= 1
            return
        # word in internal node
        if index < root.elmLen and root.elements[index] == word:
            # left child has enough elements
            if root.children[index].elmLen > self.lowerBound:
                leftMax = root.children[index].elements[root.children[index].elmLen-1]
                root.elements[index] = leftMax
                self.deleteHelper(root.children[index], leftMax)
                return
            # right child has enough elements
            elif root.children[index+1].elmLen > self.lowerBound:
                rightMin = root.children[index+1].elements[0]
                root.elements[index] = rightMin
                self.deleteHelper(root.children[index+1], rightMin)
                return
            # none of left and right child have enough elements
            else:
                # if the target is found in the root and the root has only 1 element
                removingRoot = root.isRoot and root.elmLen == 1
                newNode = B_Tree_Node(removingRoot, root.children[index].isLeaf)
                newNode.elements = root.children[index].elements + [root.elements.pop(index)] + root.children[index+1].elements
                newNode.children = root.children[index].children + root.children[index+1].children
                root.elmLen -= 1
                newNode.elmLen = self.lowerBound * 2 + 1
                if removingRoot:
                    self.root = newNode
                else:
                    root.children.pop(index)
                    root.children[index] = newNode
                self.deleteHelper(newNode, word)
                return
        # next node doesn't have enough elements
        elif root.children[index].elmLen == self.lowerBound:
            # not going into the last child
            if index < root.elmLen:
                # borrow from right sibling
                if root.children[index+1].elmLen > self.lowerBound:
                    root.children[index].elements.append(root.elements[index])
                    root.children[index].elmLen += 1
                    root.elements[index] = root.children[index+1].elements.pop(0)
                    root.children[index+1].elmLen -= 1
                    # move child
                    if not root.children[index].isLeaf:
                        root.children[index].children.append(root.children[index+1].children.pop(0))
                    self.deleteHelper(root.children[index], word)
                    return
                # sibling does not have enough elements, merge
                else:
                    removingRoot = root.isRoot and root.elmLen == 1
                    newNode = B_Tree_Node(removingRoot, root.children[index].isLeaf)
                    newNode.elements = root.children[index].elements + [root.elements.pop(index)] + root.children[index+1].elements
                    newNode.children = root.children[index].children + root.children[index+1].children
                    root.elmLen -= 1
                    newNode.elmLen = 2 * self.lowerBound + 1
                    if removingRoot:
                        self.root = newNode
                    else:
                        root.children.pop(index)
                        root.children[index] = newNode
                    self.deleteHelper(newNode, word)
                    return
            # going into the last child
            else:
                # borrow from left sibling
                if root.children[index-1].elmLen > self.lowerBound:
                    root.children[index].elements.insert(0, root.elements[index-1])
                    root.children[index].elmLen += 1
                    root.elements[index-1] = root.children[index-1].elements.pop(-1)
                    root.children[index-1].elmLen -= 1
                    # move child
                    if not root.children[index].isLeaf:
                        root.children[index].children.insert(0, root.children[index-1].children.pop(-1))
                    self.deleteHelper(root.children[index], word)
                    return
                # sibling does not have enough elements, merge
                else:
                    removingRoot = root.isRoot and root.elmLen == 1
                    newNode = B_Tree_Node(removingRoot, root.children[index].isLeaf)
                    newNode.elements = root.children[index-1].elements + [root.elements.pop(index-1)] + root.children[index].elements
                    newNode.children = root.children[index-1].children + root.children[index].children
                    root.elmLen -= 1
                    newNode.elmLen = self.lowerBound * 2 + 1
                    if removingRoot:
                        self.root = newNode
                    else:
                        root.children.pop(index-1)
                        root.children[index-1] = newNode
                    self.deleteHelper(newNode, word)
                    return
        # continue delete in the next node
        self.deleteHelper(root.children[index], word)