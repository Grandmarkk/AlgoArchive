#include <vector>

class MaxHeap
{
private:
    int count;
    std::vector<int> content;

    void heapifyUp(int index)
    {
        int parentIdx = (index - 1) / 2;
        while (index > 0 && content[parentIdx] < content[index])
        {
            std::swap(content[parentIdx], content[index]);
            index = parentIdx;
            parentIdx = index / 2;
        }
    }

    void heapifyDown(int index)
    {
        while (index < count)
        {
            int leftIdx = 2 * index + 1;
            int rightIdx = 2 * index + 2;
            if (leftIdx < count && rightIdx < count && content[index] < content[leftIdx] && content[index] < content[rightIdx]) // Smaller than both children
            {
                // Swap with greater child
                if (content[leftIdx] <= content[rightIdx])
                {
                    std::swap(content[index], content[rightIdx]);
                    index = rightIdx;
                }
                else
                {
                    std::swap(content[index], content[leftIdx]);
                    index = leftIdx;
                }
            }
            else if (leftIdx < count && content[index] < content[leftIdx]) // Smaller than left child
            {
                std::swap(content[index], content[leftIdx]);
                index = leftIdx;
            }
            else if (rightIdx < count && content[index] < content[rightIdx]) // Smaller than right child
            {
                std::swap(content[index], content[rightIdx]);
                index = rightIdx;
            }
            else
            {
                break;
            }
        }
    }

    void buildHeap()
    {
        int index = count / 2 - 1;
        while (index >= 0)
        {
            heapifyDown(index);
            index--;
        }
    }

public:
    MaxHeap()
    {
        count = 0;
        content = {};
    }

    MaxHeap(std::vector<int> arr)
    {
        count = arr.size();
        content = arr;
        buildHeap();
    }

    int top()
    {
        return count > 0 ? content[0] : -1;
    }

    void pop()
    {
        if (count > 0)
        {
            count--;
            content[0] = content[count];
            content.pop_back();
            heapifyDown(0);
        }
    }

    void push(int val)
    {
        count++;
        content.push_back(val);
        heapifyUp(count - 1);
    }

    bool empty()
    {
        return count == 0;
    }

    int size()
    {
        return count;
    }
};