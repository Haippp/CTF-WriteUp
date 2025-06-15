from pwn import *
from sympy import factorint
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

con = remote('jupiter.challenges.picoctf.org', 18821)

# Chal 1
con.recvuntil(b'q : ') ; q = int(con.recvline())
con.recvuntil(b'p : ') ; p = int(con.recvline())

con.recvuntil(b'(Y/N):') ; con.sendline(b'Y')
con.sendline(str(p * q).encode())

# Chal 2
con.recvuntil(b'n : ') ; n = int(con.recvline())
p, q = factorint(n)

con.recvuntil(b'(Y/N):') ; con.sendline(b'Y')
con.sendline(str(p).encode())

# Chal 3
con.recvuntil(b'(Y/N):') ; con.sendline(b'N')

# Chal 4
con.recvuntil(b'q : ') ; q = int(con.recvline())
con.recvuntil(b'p : ') ; p = int(con.recvline())

con.recvuntil(b'(Y/N):') ; con.sendline(b'Y')
con.sendline(str((p - 1) * (q - 1)).encode())

# Chal 5
con.recvuntil(b'plaintext : ') ; pt = int(con.recvline())
con.recvuntil(b'e : ') ; e = int(con.recvline())

con.recvuntil(b'(Y/N):') ; con.sendline(b'Y')
con.sendline(str(pow(pt, e)).encode())

# Chal 6
con.recvuntil(b'(Y/N):') ; con.sendline(b'N')

# Chal 7
con.recvuntil(b'q : ') ; q = int(con.recvline())
con.recvuntil(b'p : ') ; p = int(con.recvline())
con.recvuntil(b'e : ') ; e = int(con.recvline())

con.recvuntil(b'(Y/N):') ; con.sendline(b'Y')
con.sendline(str(pow(e, -1 ,(p - 1) * (q - 1))).encode())

# Chal 8
con.recvuntil(b'p : ') ; p = int(con.recvline())
con.recvuntil(b'ciphertext : ') ; ct = int(con.recvline())
con.recvuntil(b'e : ') ; e = int(con.recvline())
con.recvuntil(b'n : ') ; n = int(con.recvline())
d = pow(e, -1, (p - 1) * ((n//p) -1)) ; pt = pow(ct, d, n)

con.recvuntil(b'(Y/N):') ; con.sendline(b'Y')
con.sendline(str(pt).encode())

print(long_to_bytes(pt))