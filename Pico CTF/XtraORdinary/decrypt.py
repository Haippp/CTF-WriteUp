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
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]

xor1 = xor(cipher, random_strs[8])
xor2 = xor(xor1, random_strs[8])
xor3 = xor(xor2, random_strs[8])
xor4 = xor(xor3, random_strs[8])

# for random_str in random_strs:
#     for i in range(randint(0, pow(2, 8))):
#         for j in range(randint(0, pow(2, 6))):
#             for k in range(randint(0, pow(2, 4))):
#                 for l in range(randint(0, pow(2, 2))):
#                     for m in range(randint(0, pow(2, 0))):
#                         with open('testXOR1.txt', 'a') as f:
#                             f.write(f'{i}. {random_str}')
#                         ctxt = encrypt(cipher, random_str)