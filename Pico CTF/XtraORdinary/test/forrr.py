from random import randint
from pwn import xor

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

cipher = bytes.fromhex("57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637")
random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

hasil = ''
for i in range(len(random_strs) ** 2):
    for j in range(2):
        
        for rndm_bStr in random_strs[::-1]:
            hasil += str(rndm_bStr)
        print(hasil)
        hasil = ''
    print('\n\n')

        