class Binary_Heap:
    def __init__(self):
        self.heap = []

    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self._heapify_down(0)  # Fix the heap property from the root down
        return root

    def decrease_key(self, index, new_val):
        if index >= len(self.heap):
            return
        
        self.heap[index] = new_val
        self._heapify_up(index)  # Fix the heap property from the given index up

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)  # Fix the heap property from the last element up

    def delete(self, index):
        if index >= len(self.heap):
            return
        
        # Replace the element to be deleted with the last element
        self.heap[index] = self.heap.pop()
        if index < len(self.heap):
            self._heapify_up(index)
            self._heapify_down(index)

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

    def heapify(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)