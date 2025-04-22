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
xor5 = xor(xor4, random_strs[8])
xor6 = xor(xor5, random_strs[8])
xor7 = xor(xor6, random_strs[8])
print('1.', xor1)
print('2.', xor2)
print('3.', xor3)
print('4.', xor4)
print('5.', xor5)
print('6.', xor6)
print('7.', xor7)
