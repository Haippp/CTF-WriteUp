flag = "01000011 01010100 01000110 01010010 01010011 01010100 01111011 01100010 00110001 01101110 00110100 01110010 01111001 01011111 01100011 00110000 01100100 00110011 01111101"
# int(b, 2) mengubah setiap string biner menjadi angka desimal.
print(''.join(chr(int(b, 2)) for b in flag.split()))

dekripFlag = []
#Bentuk asli list comprehension
for d in flag.split():
    kar = chr(int(d, 2))
    dekripFlag.append(kar)

print(''.join(dekripFlag))