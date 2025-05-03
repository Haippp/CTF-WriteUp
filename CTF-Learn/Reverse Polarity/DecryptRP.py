def Binary8Bit(binary):
    dec = ""
    for i, c in enumerate(binary, 1):
        if i % 8 == 0:
            dec += c + ' '
        else:
            dec += c
    return dec

cipher = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"
biner = Binary8Bit(cipher)
flag = "".join(chr(int(b, 2)) for b in biner.split())
print(flag)