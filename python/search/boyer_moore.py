from search.z_algorithm import z_algo

def compute_r(pattern: str):
    '''
    Build R for bad character rule.
    R[i] stores the right most char indexes in pattern[0:i]

    Args:
        pattern: a string

    Return: a list of dictionary
    '''
    m = len(pattern)
    rVals = [{}]
    for i in range(33, 127):
        rVals[0][chr(i)] = -1
    i = 1
    while i < m:
        j = 33
        curR = {}
        while j < 127:
            curChar = chr(j)
            curR[curChar] = rVals[i - 1][curChar]
            j += 1
        curR[pattern[i - 1]] = i - 1
        rVals.append(curR)
        i += 1

    return rVals


def compute_good_suffix(pattern: str):
    '''
    Build good suffix array.
    '''
    zSfx = z_algo(pattern[::-1])[::-1]
    m = len(pattern)
    gs = []
    for i in range(m + 1):
        gs.append(-1)
    for i in range(m - 1):
        j = m - zSfx[i]
        gs[j] = i
    return gs
    

def compute_matched_preffix(pattern: str):
    '''
    Build matched prefix array.
    '''
    m = len(pattern)
    z = z_algo(pattern)
    mp = [0] * (m + 1)
    i = len(mp) - 2
    curMax = z[i - 1]
    while i > 0:
        if z[i-1] > curMax:
            mp[i] = z[i-1]
            curMax = z[i-1]
        else:
            mp[i] = curMax
        i -= 1
    mp[0] = m
    
    return mp


def boyer_moore(text: str, pattern: str):
    '''
    Find exact pattern match

    Args:
        text: text sample
        pattern: pattern string
    
    Return: list of match starting positions
    '''
    ans = []
    r = compute_r(pattern)
    gs = compute_good_suffix(pattern)
    mp = compute_matched_preffix(pattern)
    m = len(pattern)
    n = len(text)
    tIndex = m - 1
    pIndex = m - 1
    # scan the text
    while tIndex < n and pIndex > -1:
        if not text[tIndex] == pattern[pIndex]:
            bShift = pIndex - max(r[pIndex][text[tIndex]], 1)
            gShift = m - gs[pIndex + 1] - 1 if gs[pIndex + 1] > -1 else m - mp[pIndex + 1]
            shiftAmount = max(bShift, gShift)
            tIndex += shiftAmount + (m - pIndex - 1)
            pIndex = m - 1
        elif pIndex == 0:
            ans.append(tIndex)
            tIndex += m
            pIndex = m - 1
        else:   
            tIndex -= 1
            pIndex -= 1
    return ans

