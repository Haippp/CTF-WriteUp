transmission1 = open('transmission1.txt', 'r').read()
transmission2 = open('transmission2.txt', 'r').read()
transmission3 = open('transmission3.txt', 'r').read()

biner = ''

for p, b in zip(transmission1, transmission2):
    if b == '+':
        if p == '|':
            biner += '1' 
        elif p == '-':
            biner += '0'
    else:
        if p == chr(92):
            biner += '1'
        elif p == '/':
            biner += '0'

print(bytes.fromhex(hex(int(biner, 2))[2:]))