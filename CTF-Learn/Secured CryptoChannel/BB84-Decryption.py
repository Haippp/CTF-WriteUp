from base64 import b64decode

Polarize = open('transmission1.txt', 'r').read()
Basis = open('transmission2.txt', 'r').read()
qbit = open('transmission3.txt', 'r').read()

Biner = ''            

for i in range(len(qbit)):
    if qbit[i] == 'v':
        if Basis[i] == '+':
            if Polarize[i] == '|':
                Biner += '1'
            elif Polarize[i] == '-':
                Biner += '0'
        else:
            if Polarize[i] == chr(92):
                Biner += '1'
            elif Polarize[i] == '/':
                Biner += '0'

print(b64decode(bytes.fromhex(hex(int(Biner,2))[2:]).decode()[4:])) 