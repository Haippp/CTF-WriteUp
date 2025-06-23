from pwn import *

fill = string.ascii_lowercase + string.digits + 'CTF{_}'
conn = remote('mercury.picoctf.net', 6276)
flag = '' ; knownEnc = ['', ]

conn.recvuntil(b'flag: '); Encflag = conn.recvline().strip().decode()

while '}' not in flag:
    for f in fill:
        print(flag + f)
        conn.recvuntil(b'give me: '); sending = conn.sendline(flag + f)
        conn.recvuntil(b'you go: '); result = conn.recvline().strip().decode()
        for k in knownEnc:
            result = result.replace(k, '')
        if result in Encflag:
            flag += f
            knownEnc.append(result)
            break

print('Flag : ' + flag)
