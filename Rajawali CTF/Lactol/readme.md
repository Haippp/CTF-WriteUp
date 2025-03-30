# Deskripsi 
Pada challange ini tidak ada sama sekali hint hanya angka ini saja `103 124 106 122 123 124 173 61 163 137 60 143 164 141 154 137 142 162 157 167 175`. 
## Penyelesaian
Awalnya aku mengira ini adalah ordinary number, tapi ketika menggunakan enkripsi ini malah tidak dapat. Setelah diperhatikan lagi cluenya ada pada judulnya yaitu "lactol" pelesetan dari octal. Dan juga dari angka-angkanya gaada yang lebih dari 7, ini merupakan ciri dan pola dari octal yang hanya berisi angka dari 0-7. Berikut hasil programnya :
```python
flag = "103 124 106 122 123 124 173 61 163 137 60 143 164 141 154 137 142 162 157 167 175"
print(''.join(chr(int(f, 8)) for f in flag.split()))
# output : CTFRST{1s_0ctal_brow}
```
Diatas aku menggunakan fungsi integer bawaan dengan format base 8 serta menggunakan list comperhension untuk memperpendek kode dan mengubah angka ASCIInya menjadi karakter.