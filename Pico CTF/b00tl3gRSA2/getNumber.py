from pwn import *

conn = remote('jupiter.challenges.picoctf.org', 57464)
conn.recvuntil(b'c: '); c = int(conn.recvline().strip().decode())
conn.recvuntil(b'n: '); n = int(conn.recvline().strip().decode())
conn.recvuntil(b'e: '); e = int(conn.recvline().strip().decode())

with open('BreakTheCipher.py', 'a') as file:
    file.write(f'c = {str(c)}\n')
    file.write(f'n = {str(n)}\n')
    file.write(f'e = {str(e)}')