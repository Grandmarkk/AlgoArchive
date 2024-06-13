
class Binary_Heap:
    def __init__(self):
        self.heap = []
        self.key_set = set()  # To keep track of the keys in the heap

    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            min_value = self.heap.pop()
            self.key_set.remove(min_value)
            return min_value
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.key_set.remove(root)
        self._heapify_down(0)  # Fix the heap property from the root down
        return root

    def decrease_key(self, old_key, new_key):
        if old_key not in self.key_set:
            print(f"Key {old_key} not found in the heap.")
            return
        if new_key in self.key_set:
            print(f"Key {new_key} already exists in the heap. Decrease key skipped.")
            return

        index = self.heap.index(old_key)
        self.heap[index] = new_key
        self.key_set.remove(old_key)
        self.key_set.add(new_key)
        self._heapify_up(index)

    def insert(self, key):
        if key in self.key_set:
            print(f"Key {key} already exists in the heap. Insertion skipped.")
            return
        self.heap.append(key)
        self.key_set.add(key)
        self._heapify_up(len(self.heap) - 1)  # Fix the heap property from the last element up

    def delete(self, key):
        if key in self.key_set:
            self.decrease_key(key, self.heap[0] - 1)
            self.extract_min()

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap the current element with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)