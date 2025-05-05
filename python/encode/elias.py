from bitarray import bitarray

def encode(num):
    '''
    Generate the Elias code for a given positive int

    Args:
        num: a positive integer

    Return:
        a bitarray of Elias code
    '''
    # calc bin
    bin_num = bitarray(bin(num)[2:])
    res = [bin_num]
    while len(bin_num) > 1:
        bin_num = bitarray(bin(len(bin_num) - 1)[2:])
        bin_num[0] = 0
        res.append(bin_num)
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

    Args:
        codeword: a bitarray of Elias code
        start: the index to start decoding

    Return: decoded int
    '''
    read_len = 1
    end = start + read_len
    while True:
        cur = codeword[start : start + read_len]
        if cur[0] == 1:
            return int('0b' + cur.to01(), 2)
        cur[0] = 1
        start += read_len
        read_len = int('0b' + cur.to01(), 2) + 1
        end += read_len