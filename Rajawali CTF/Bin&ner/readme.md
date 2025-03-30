# Deskripsi 
Challange ini cukup mudah karena ini hanyalah sebuah binary yang cuman perlu diubah menjadi karakter. flagnya adalah `01000011 01010100 01000110 01010010 01010011 01010100 01111011 01100010 00110001 01101110 00110100 01110010 01111001 01011111 01100011 00110000 01100100 00110011 01111101` jadi langsung saja kita buatkan programnya.
## Penyelesaian
```python
flag = "01000011 01010100 01000110 01010010 01010011 01010100 01111011 01100010 00110001 01101110 00110100 01110010 01111001 01011111 01100011 00110000 01100100 00110011 01111101"
print(''.join(chr(int(b, 2)) for b in flag.split()))
# Output : CTFRST{b1n4ry_c0d3}
```
Diatas kita menggunakan list komprehension untuk memperpendek kode perulangan. Diatas kita menggunakan fungsi int yang mengubah biner menjadi desimal. yang kemudian nantinya desimal tersebut diubah menjadi karakter berdasarkan table ASCII.