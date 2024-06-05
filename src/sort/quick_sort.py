def quick_sort(ary, start=None, end=None):
    '''
    Sort the input array in non decreasing order.

    Args:
        ary: an array
    '''
    start = 0 if not isinstance(start, (int, float)) else start
    end = len(ary) - 1 if not isinstance(end, (int, float)) else end
    if (start < end):
        partitionIndex = partition(ary, start, end)
        quick_sort(ary, start, partitionIndex - 1)
        quick_sort(ary, partitionIndex + 1, end)
    return ary

def partition(ary, start, end):
    '''
    Partition the array around the pivot.

    Args:
        ary: an array
        start: the start index
        end: the end index
    '''
    pivot = start
    index = pivot + 1
    i = index
    while (i <= end):
        if (ary[i] < ary[pivot]):
            ary[i], ary[index] = ary[index], ary[i]
            index += 1
        i += 1
    ary[pivot], ary[index-1] = ary[index-1], ary[pivot]
    return index - 1