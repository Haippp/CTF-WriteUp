import string

LOWERCASE_OFFSET = ord("A")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(b16_cipher):
    a = []
    b = []

    for i, d in enumerate(b16_cipher):
        if i % 2 == 0:
            a1 = (ord(d) - 97) * 16
            a.append(a1)
        else:
            b1 = ord(d) - 97
            b.append(b1)

    return "".join(chr(a[i] + b[i]) for i in range(len(a)))

def shift_decode(cipher, key):
    t1 = ord(cipher) - LOWERCASE_OFFSET
    t2 = ord(key) - LOWERCASE_OFFSET

    return ALPHABET[(t1 - t2) % len(ALPHABET)]

cipher = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'

for key in range(97, 122):
    semi_cipher = "".join(shift_decode(c, chr(key)) for c in cipher)
    plain = b16_decode(semi_cipher)
    print('key ['+ chr(key) + ']  : ' + plain)