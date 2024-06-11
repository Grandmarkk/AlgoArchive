def getR(pattern: str):
    '''
    build Ri for bad character rule
    '''

    '''
    
    rVals = []
    m = len(pattern)
    rVals.append({})
    for i in range(1, m):
        ri = {}
        for j in range(i):
            ri[pattern[j]] = j
        rVals.append(ri)
    return rVals
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


def getGS(pattern: str):
    '''
    build good suffix array
    '''
    zSfx = getZ(pattern[::-1])[::-1]
    m = len(pattern)
    gs = []
    for i in range(m + 1):
        gs.append(-1)
    for i in range(m - 1):
        j = m - zSfx[i]
        gs[j] = i
    return gs
    

def getMP(pattern: str):
    '''
    build matched prefix array
    '''
    m = len(pattern)
    z = getZ(pattern)
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


def boyerMoore(text: str, pattern: str):
    ans = []
    r = getR(pattern)
    gs = getGS(pattern)
    mp = getMP(pattern)
    m = len(pattern)
    n = len(text)
    tIndex = m - 1
    pIndex = m - 1
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

pattern = "wn"
text = "mmomqmpwncbxqtzbfgtrduuneeiwiclaypajvzrezxalchdsctgjyebqwbods"
print(boyerMoore(text, pattern))