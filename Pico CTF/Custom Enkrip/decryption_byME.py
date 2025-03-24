def generator(g, x, p):
    return pow(g, x) % p

def decrypt(sandi, kunci):
    plain_text = []
    sandi = list(sandi)
    for char in sandi:
        plain_text.append(((chr(int(char / kunci / 311)))))
    return "".join(plain_text)


def dynamic_xor_dencrypt(sandi, kunci_teks):
    plain_text = ""
    key_length = len(kunci_teks)
    print(key_length)
    for i, char in enumerate(sandi):
        key_char = kunci_teks[i % key_length]
        decrypt_char = chr(ord(char) ^ ord(key_char))
        plain_text += decrypt_char
    return plain_text[::-1]


def CustomDecrypt(sandi, keyText):
    p = 97
    g = 31

    a = 94
    b = 21
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)

    semi_cipher = decrypt(sandi, key)
    print(f'Semicipher is: {semi_cipher}')
    plainText = dynamic_xor_dencrypt(semi_cipher, keyText)
    print(f'cipher is: {plainText}')

sandi = [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]

CustomDecrypt(sandi, "trudeau")