def buildZ(text: str):
    '''
    Gusfield's Z-Algorithm.

    Args:
        text: a string
    
    Return: an array of z-values from the 2nd position
    '''
    length = len(text)
    zVals = [0] * length
    l, r = 0, 0
    for i in range(1, length):
        if i <= r:
            zVals[i] = min(r - i + 1, zVals[i - l])
        while i + zVals[i] < length and text[zVals[i]] == text[i + zVals[i]]:
            zVals[i] += 1
        if i + zVals[i] - 1 > r:
            l = i
            r = i + zVals[i] - 1 
    return zVals