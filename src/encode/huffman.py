class Huffman_Node:
    '''
    The node structure used in Huffman tree
    '''
    def __init__(self, text) -> None:
        self.left = None
        self.right = None
        self.text = text


def generate_code_table(text):
    '''
    Returns a dict of the Huffman codes. 
    character : str bin code
    '''
    def cmp(item):
        return item[1]
    
    def traverseHuffmanTree(root, code, table):
        '''
        Traverse the tree to get the encoding for each char
        '''
        if not root.left and not root.right:
            table[root.text] = ''.join(code)
            return
        left = code[::]
        right = code[::]
        left.append('0')
        right.append('1')
        traverseHuffmanTree(root.left, left, table)
        traverseHuffmanTree(root.right, right, table)

    # calc frequency
    freq = {}
    for char in text:
        freq[char] = 1 + freq.get(char, 0)
    # sort the dict on the frequency
    sortedChar = sorted(freq.items(), key = cmp)
    # build tree
    rightNode = Huffman_Node(sortedChar[0][0])
    for i in range(1, len(sortedChar)):
        leftNode = Huffman_Node(sortedChar[i][0])
        newNode = Huffman_Node(leftNode.text + rightNode.text)
        newNode.left = leftNode
        newNode.right = rightNode
        rightNode = newNode
    root = newNode
    # build code table
    codeTable = {}
    traverseHuffmanTree(root, [], codeTable)
    return codeTable