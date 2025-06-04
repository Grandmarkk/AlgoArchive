#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

void bubbleSort(vector<int> &arr)
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
            return;
        }
    }
}

void selectionSort(vector<int> &arr)
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
}

void insertionSort(vector<int> &arr)
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
}

/**
 * @brief Merge 2 sorted array.
 */
vector<int> merge(vector<int> &arr1, vector<int> &arr2)
{
    vector<int> res;
    int idx1 = 0;
    int idx2 = 0;

    while (idx1 < arr1.size() && idx2 < arr2.size())
    {
        if (arr1[idx1] <= arr2[idx2])
        {
            res.push_back(arr1[idx1]);
            idx1++;
        }
        else
        {
            res.push_back(arr2[idx2]);
            idx2++;
        }
    }

    while (idx1 < arr1.size())
    {
        res.push_back(arr1[idx1]);
        idx1++;
    }

    while (idx2 < arr2.size())
    {
        res.push_back(arr2[idx2]);
        idx2++;
    }

    return res;
}

vector<int> mergeSort(vector<int> &arr)
{
    if (arr.size() < 2)
    {
        return arr;
    }

    int mid = arr.size() / 2;
    vector<int> left;
    vector<int> right;

    for (int i = 0; i < mid; i++)
    {
        left.push_back(arr[i]);
    }

    for (int i = mid; i < arr.size(); i++)
    {
        right.push_back(arr[i]);
    }

    left = mergeSort(left);
    right = mergeSort(right);

    return merge(left, right);
}

/**
 * @brief Put the pivot to its sorted position
 * @param arr the source array
 * @param start left index of the sub-array
 * @param end right index of the sub-array
 * @return the sorted pivot index
 */
int partition(vector<int> &arr, int start, int end)
{
    int pivot = arr[start];
    while (start < end)
    {
        // Find the first elm < pivot from the right
        while (start < end && arr[end] >= pivot)
        {
            end--;
        }
        arr[start] = arr[end];
        // Find the first elm > pivot from the left
        while (start < end && arr[start] <= pivot)
        {
            start++;
        }
        arr[end] = arr[start];
    }
    // Put pivot in place
    arr[start] = pivot;
    return start;
}

void quickSort(vector<int> &arr, int start, int end)
{
    if (start < end)
    {
        int pivot = partition(arr, start, end);
        quickSort(arr, start, pivot - 1);
        quickSort(arr, pivot + 1, end);
    }
}

vector<int> countingSort(vector<int> &arr)
{
    // Find range
    int minNum = arr[0];
    int maxNum = arr[0];
    int length = 0;
    for (int num : arr)
    {
        minNum = min(minNum, num);
        maxNum = max(maxNum, num);
        length++;
    }
    vector<int> counts(maxNum - minNum + 1, 0);
    // Count frequency
    for (int num : arr)
    {
        counts[num - minNum]++; // Offset the min num to 0
    }
    // Construct sorted array
    vector<int> sortedArr(length);
    int i = 0;

    for (int num = 0; num < maxNum - minNum + 1; num++)
    {
        for (int freq = counts[num]; freq > 0; freq--)
        {
            sortedArr[i] = num + minNum;
            i++;
        }
    }

    return sortedArr;
}

/**
 * @brief Sort the input array
 * @param arr the reference of the array
 * @param base the radix
 * @return the sorted array
 */
vector<int> radixSort(vector<int> &arr, int base)
{
    // Get range
    int minNum = arr[0];
    int maxNum = arr[0];
    for (int num : arr)
    {
        minNum = min(minNum, num);
        maxNum = max(maxNum, num);
    }
    // Shift to positive
    if (minNum < 0)
    {
        for (int i = 0; i < arr.size(); i++)
        {
            arr[i] += -minNum;
        }
    }
    // Get max digits
    int cols = 1;
    while (maxNum > 0)
    {
        cols++;
        maxNum /= base;
    }
    int divider = 1;
    while (cols-- > 0)
    {
        // Counting sort
        vector<vector<int>> counts(base);
        for (int num : arr)
        {
            counts[num / divider % base].push_back(num);
        }
        int i = 0;
        for (vector<int> bucket : counts)
        {
            for (int num : bucket)
            {
                arr[i] = num;
                i++;
            }
        }
        divider *= base;
    }
    // Shift Back
    if (minNum < 0)
    {
        for (int i = 0; i < arr.size(); i++)
        {
            arr[i] -= -minNum;
        }
    }
    return arr;
}