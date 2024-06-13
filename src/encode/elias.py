from bitarray import bitarray

def encode(num):
    '''
    Generate the Elias code for a given positive int
    '''
    # calc bin
    binNum = bitarray(bin(num)[2:])
    res = [binNum]
    while len(binNum) > 1:
        binNum = bitarray(bin(len(binNum) - 1)[2:])
        binNum[0] = 0
        res.append(binNum)
    # concat the bin stream
    code = bitarray()
    i = len(res) - 1
    while i > -1:
        code.extend(res[i])
        i -= 1
    return code

def decode(codeword, start=0):
    '''
    Decodes the Elias code in a bitarray from the start

    Output: decoded int
    '''
    readLen = 1
    end = start + readLen
    while True:
        cur = codeword[start : start + readLen]
        if cur[0] == 1:
            return int('0b' + cur.to01(), 2)
        cur[0] = 1
        start += readLen
        readLen = int('0b' + cur.to01(), 2) + 1
        end += readLen