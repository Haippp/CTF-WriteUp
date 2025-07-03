from pwn import xor
cipher = []

with open('./msg (4)', 'r') as file:
    for line in file:
        cipher.append(line.strip())

for c in cipher:
    print(xor(bytes.fromhex(c), b'ALEXCTF{HERE_GOES_THE_KEY}'))
