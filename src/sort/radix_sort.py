import math

def radixSort(nums, base):
    if (len(nums) < 2):
        return nums
    # find min
    minNum = nums[0]
    for i in nums:
        if (i < minNum):
            minNum = i
    # shift nums to positive
    if (minNum < 0):
        i = 0
        while (i < len(nums)):
            nums[i] += -minNum
            i += 1
    # find max
    maxNum = nums[0]
    for i in nums:
        if (i > maxNum):
            maxNum = i
    # find max digit length
    numOfCol = math.floor(math.log(maxNum, base)) + 1
    # counting sort on radix
    dev = 1
    while (numOfCol > 0):
        # initialize buckets
        count = []
        for x in range(base):
            count.append([])
        # count
        for aryElement in nums:
            count[aryElement // dev % base].append(aryElement)
        # sort
        sortedAry = []
        for bucket in count:
            for element in bucket:
                sortedAry.append(element)
        nums = sortedAry
        dev *= base
        numOfCol -= 1
    # shift nums back
    if (minNum < 0):
        i = 0
        while (i < len(nums)):
            nums[i] += minNum
            i += 1
    return nums