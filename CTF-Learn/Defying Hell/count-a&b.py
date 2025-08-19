from sympy.ntheory.residue_ntheory import discrete_log

# Nilai dari data.txt
p = 0x8c5378994ef1b
g = 0x02
A = 0x269beb3b0e968
B = 0x4757336da6f70

a = discrete_log(p, A, g)
b = discrete_log(p, B, g)

a_decode = bytes.fromhex(hex(a)[2:]).decode('ascii')
b_decode = bytes.fromhex(hex(b)[2:]).decode('ascii')
print('CTFlearn{' + a_decode + '_' + b_decode + '}')