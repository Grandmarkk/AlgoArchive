def merge_sort(ary):
    '''
    Sort the input array in non decreasing order.

    Args:
        ary: the input array
    '''
    length = len(ary)
    if length < 2:
        return ary
    mid = length // 2
    return merge(merge_sort(ary[:mid]), merge_sort(ary[mid:]))
    

def merge(ary1, ary2):
    '''
    Merge the two input arrays

    Args:
        ary1: array 1
        ary2: array 2

    Return: the merged array
    '''
    ary = []
    while ary1 and ary2:
        if ary1[0] < ary2[0]:
            ary.append(ary1.pop(0))
        else:
            ary.append(ary2.pop(0))
    while ary1:
        ary.append(ary1.pop(0))
    while ary2:
        ary.append(ary2.pop(0))
    return ary