from pwn import *

def xor(pt: bytes, key: bytes) -> bytes:
    ct = [pt[i] ^ key[i] for i in range(len(pt))]
    return bytes(ct)

conn = remote('wily-courier.picoctf.net', 50023)
conn.recvuntil(b'encrypted flag!\n')
enc_flag = bytes.fromhex(conn.recvline().strip().decode())
payload = ('A' * 50000).encode()

conn.sendlineafter(b'to encrypt? ', payload)

conn.recvuntil(b'go!\n')
enc_payload = bytes.fromhex(conn.recvline().strip().decode())

key = xor(payload, enc_payload)
flag = xor(enc_flag, key[-len(enc_flag):]).decode()

print(f'the flag is : picoCTF{{{flag}}}')