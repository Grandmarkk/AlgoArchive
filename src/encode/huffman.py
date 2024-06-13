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
    
    def traverse_huffman_tree(root, code, table):
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
        traverse_huffman_tree(root.left, left, table)
        traverse_huffman_tree(root.right, right, table)

    # calc frequency
    freq = {}
    for char in text:
        freq[char] = 1 + freq.get(char, 0)
    # sort the dict on the frequency
    sorted_char = sorted(freq.items(), key = cmp)
    # build tree
    right_node = Huffman_Node(sorted_char[0][0])
    for i in range(1, len(sorted_char)):
        left_node = Huffman_Node(sorted_char[i][0])
        new_node = Huffman_Node(left_node.text + right_node.text)
        new_node.left = left_node
        new_node.right = right_node
        right_node = new_node
    root = new_node
    # build code table
    code_table = {}
    traverse_huffman_tree(root, [], code_table)
    return code_table