def poly2binary(poly: list, degre: int) -> str:
    binary = ''

    for i in range(degre, 0, -1):
        test = 'x^' + str(i)

        if test in poly:
            binary += '1'
        else:
            binary += '0'
    
    if '1' in poly:
        binary += '1'

    return binary

def binary2bytes(binary: str) -> bytes:
    return bytes.fromhex(hex(int(binary, 2))[2:])

field = open('polycrypto/field.txt', 'r').read()[4:].strip().split(' + ')
flag = poly2binary(field, 206)

print(binary2bytes(flag))