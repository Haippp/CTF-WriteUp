from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

n = []
e = []
c = []

with open('encrypted-messages.txt', 'r') as file:
    for i, line in enumerate(file):
        if i % 3 == 1:
            e.append(line[3:])
        elif i % 3 == 2:
            c.append(line[3:])
        else:
            n.append(line[3:])
    
for i in range(len(n)):
    enc = int(c[i])
    exp = int(e[i])
    msg = iroot(enc, exp)[0]
    print(long_to_bytes(msg).decode())