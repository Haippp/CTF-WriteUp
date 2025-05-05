from random import randint
from pwn import xor

def decrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

cipher = bytes.fromhex("57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637")
key = b'Africa!'

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

for i in range(2):
    cipher = decrypt(cipher, random_strs[0])
    for j in range(2):
        cipher = decrypt(cipher, random_strs[1])
        for k in range(2):
            cipher = decrypt(cipher, random_strs[2])
            for l in range(2):
                cipher = decrypt(cipher, random_strs[3])
                for m in range(2):
                    cipher = decrypt(cipher, random_strs[4])
                    Pkey = decrypt(cipher, key)
                    print(Pkey) 
