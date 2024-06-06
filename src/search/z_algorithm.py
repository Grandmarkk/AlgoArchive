def z_algo(text: str):
    '''
    Gusfield's Z-Algorithm.

    Args:
        text: a string
    
    Return: an array of z-values from the 2nd position
    '''
    length = len(text)
    zVals = [None] * length
    l = 0
    r = 0
    # compute Z2
    left = 0
    right = 1
    curZ = 0
    while right < length and text[left] == text[right]:
        curZ += 1
        left += 1
        right += 1
    if curZ > 0:
        r = curZ
        l = 1
    zVals[1] = curZ

    i = 2
    while i < length - 1:
        # not in the current Z-box
        if i > r:
            left = 0
            right = i
            curZ = 0
            while right < length and text[left] == text[right]:
                curZ += 1
                left += 1
                right += 1
            if curZ > 0:
                r = right - 1
                l = i
            zVals[i] = curZ
        # in the current Z-box
        else:
            if zVals[i - l] < r - i + 1:
                zVals[i] = zVals[i - l]
            else:
                left = r - i + 1
                right = r + 1
                curZ = r - i + 1
                while right < length and text[left] == text[right]:
                    curZ += 1
                    left += 1
                    right += 1
                zVals[i] = curZ
                l = i
                r = right - 1
        i += 1
    if text[-1] == text[0]:
        zVals[-1] = 1
    else:
        zVals[-1] = 0
    return zVals[1::]