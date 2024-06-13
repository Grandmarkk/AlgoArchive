class Node:
    '''
    The tree node structure in suffix tree
    Edges are stored in a dict, each edge maps to the node it's connected to
    '''
    def __init__(self, start, end):
        # key : val, first char of the substring : Node
        self.edges = {}
        self.suffix_link = None
        # Start index of the substring on this node's incoming edge
        self.start = start
        # End index of the substring on this node's incoming edge
        self.end = end

    def edge_len(self, pos):
        # Get the cur edge length
        if self.end < pos + 1:
            return self.end - self.start
        else:
            return pos + 1 - self.start
        
class suffix_tree:
    def __init__(self, text) -> None:
        self.root = Node(None, None)
        self.build_suffix_tree(text)

    def build_suffix_tree(self, text):
        '''
        Build suffix tree for the input text using Ukkonen's algorithm.
        input text must end with '$'
        '''
        self.root.suffix_link = self.root
        # Initialse the active node to root
        active_node = self.root
        # No active edge initially
        active_edge = -1
        # No active length initially
        active_length = 0
        # Right end of the current active edge
        end = -1
        # Number of suffixes
        remainder = 0
        # Temporary pointer for new internal nodes
        cur_node = None
        # Build suffix tree
        i = 0
        while i < len(text):
            char = text[i]
            end += 1
            # Increase suffix count
            remainder += 1
            # Reset cur node
            cur_node = None
            while remainder > 0:
                if active_length == 0:
                    # Active edge is the current position
                    active_edge = i
                if text[active_edge] not in active_node.edges:
                    # Rule 2 alt, new leaf node
                    leaf = Node(end, float('inf'))
                    leaf.suffix_link = self.root
                    active_node.edges[text[active_edge]] = leaf
                    # Add suffix link to new node
                    if cur_node:
                        cur_node.suffix_link = active_node
                    cur_node = active_node
                else:
                    next_node = active_node.edges[text[active_edge]]
                    # Skip/count, jump to the end of cur edge
                    if active_length >= next_node.edge_len(end):
                        active_length -= next_node.edge_len(end)
                        active_edge += next_node.edge_len(end)
                        active_node = next_node
                        continue
                    # Rule 3, do nothing, break
                    if text[active_length + next_node.start] == char:
                        if cur_node and active_node != self.root:
                            cur_node.suffix_link = active_node
                        active_length += 1
                        break
                    # Rule 2 std, split edge
                    split = Node(next_node.start, next_node.start + active_length)
                    split.suffix_link = self.root
                    active_node.edges[text[active_edge]] = split
                    leaf = Node(i, float('inf'))
                    leaf.suffix_link = self.root
                    split.edges[char] = leaf
                    next_node.start += active_length
                    split.edges[text[next_node.start]] = next_node
                    if cur_node:
                        cur_node.suffix_link = split
                    cur_node = split
                remainder -= 1
                # Move to next suffix
                if active_length > 0 and active_node == self.root:
                    active_length -= 1
                    active_edge = i - remainder + 1
                else:
                    if active_node.suffix_link:
                        active_node = active_node.suffix_link
                    else:
                        active_node = self.root
            i += 1
        return self.root
    
    def build_suffix_array(self, root, text_len, suffix_array, depth=0):
        # Leaf node
        if not root.edges:
            # Calculate the position of the suffix in the string
            suffix_array.append(text_len - depth)
        else:
            # DFS in lexicographical order
            for key in sorted(root.edges.keys()):
                child = root.edges[key]
                self.build_suffix_array(child, text_len, suffix_array, depth + child.edge_len(text_len - 1))

