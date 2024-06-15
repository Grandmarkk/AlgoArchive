def encode(text, dictionary_size, buffer_size):
    i = 0
    encoded_output = []
    while i < len(text):
        match_length = 0
        match_distance = 0
        for j in range(max(0, i - dictionary_size), i):
            length = 0
            while length < buffer_size and i + length < len(text) and text[j + length] == text[i + length]:
                length += 1
            if length > match_length:
                match_length = length
                match_distance = i - j
        encoded_output.append((match_distance, match_length, text[i + match_length] if i + match_length < len(text) else ''))
        i += match_length + 1
    return encoded_output

def decode(codeword):
    decoded_output = []
    curLen = 0
    for offset, length, next_char in codeword:
        for i in range(curLen - offset, curLen - offset + length):
            decoded_output.append(decoded_output[i])
        decoded_output.append(next_char)
        curLen += length + 1
    return ''.join(decoded_output)