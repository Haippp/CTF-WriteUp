from pwn import *

TheFray = remote("94.237.59.174", 37639)

TheFray.recvuntil(b"there's a ")
R1 = TheFray.recvline().strip().decode().replace(', you send back ', ' ').split()
TheFray.recvuntil(b"there's a ")
R2 = TheFray.recvline().strip().decode().replace(', you send back ', ' ').split()
TheFray.recvuntil(b"there's a ")
R3 = TheFray.recvline().strip().decode().replace(', you send back ', ' ').split()

Dict = {
    R1[0]: R1[1], 
    R2[0]: R2[1], 
    R3[0]: R3[1]
}

TheFray.sendlineafter(b'(y/n) ', b'y')
TheFray.recvuntil(b'\n')

Question = ''
Answer = ''

while True:
    Question = TheFray.recvline().strip().decode().replace(',', '')
    print(Question)
    Answer = '-'.join(Dict[q] for q in Question.split())
    print(Answer)
    TheFray.sendlineafter(b'do? ', Answer.encode()) 