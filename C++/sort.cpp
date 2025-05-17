#include <vector>
#include <iostream>

using namespace std;

vector<int> bubbleSort(vector<int> arr)
{
    int length = arr.size();
    for (int i = 0; i < length; i++)
    {
        bool swaped = false;
        for (int j = 0; j < length - i - 1; j++)
        {
            // Swap
            if (arr[j + 1] < arr[j])
            {
                swaped = true;
                int temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }
        if (!swaped)
        {
            return arr;
        }
    }
    return arr;
}

vector<int> selectionSort(vector<int> arr)
{
    int left = 0;
    int right = arr.size() - 1;
    while (left < right)
    {
        int minIdx = left;
        // Find min in unsorted part
        for (int i = left + 1; i <= right; i++)
        {
            if (arr[i] < arr[minIdx])
            {
                minIdx = i;
            }
        }
        // Swap
        swap(arr[minIdx], arr[left]);
        left++;
    }
    return arr;
}

vector<int> insertionSort(vector<int> arr)
{
    int left = 1;
    int right = arr.size() - 1;
    while (left <= right)
    {
        int i = left - 1;
        int cur = arr[left];
        // Find place to insert
        while (i >= 0 && arr[i] > cur)
        {
            arr[i + 1] = arr[i];
            i--;
        }
        // Insert
        arr[i + 1] = cur;
        left++;
    }
    return arr;
}