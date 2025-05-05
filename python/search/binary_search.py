def binary_search(ary, target):
    '''
    Binary search the target in the array.

    Args:
        ary: an array sorted in increasing order
        target: the value to search for

    Returns:
        the index of the target in the array if found, -1 if not found
    '''
    left = 0
    right = len(ary) - 1
    while left <= right:
        mid = (left + right) // 2
        cur = ary[mid]
        if cur == target:
            return mid
        elif cur < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1