enc = 'ejxc{T0nY0J_BsUMS4}'

ctr = 1
Upp = ord('A') ; Low = ord('a')
flag = ''

for c in enc:
    if c.isupper():
        flag += chr((ord(c) - Upp + ctr) % 26 + Upp)
        ctr += 1
    elif c.islower():
        flag += chr((ord(c) - Low + ctr) % 26 + Low)
        ctr += 1
    elif c.isdigit():
        flag += c
        ctr += 1
    else:
        flag += c

print(flag)