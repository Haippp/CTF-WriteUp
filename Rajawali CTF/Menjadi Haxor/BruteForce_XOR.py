def XOR_brute_force(cipher):
    for key in range(1, 127):
        decrypted = "".join(chr(ord(c) ^ key) for c in cipher)
        if decrypted[:6] == 'CTFRST':
            print(f'{key}. key({chr(key)}) {decrypted}')


ciphertext = "{l~jklCZJML]g^WJ[]g@WJgQKgPY@WJE"
XOR_brute_force(ciphertext)
