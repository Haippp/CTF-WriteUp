# 5x5 Crypto
## Deskripsi Challange
Pernah mendengar tentang sistem pesan rahasia 5x5? Jika belum, pada dasarnya ini adalah kotak 5x5 dengan semua huruf alfabet secara berurutan, tanpa huruf k karena c diwakili untuk membuat suara k saja. Cari di Google jika Anda perlu. Sebuah huruf diidentifikasi dengan Baris-Kolom. Semua nilai ditulis dalam huruf besar. Coba: 1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}

## penyelesaian
Dari pola diatas tebakan saya adalah ini merupakan pola substitusi tabel. dimana angka diatas merupakan representasi dari baris dan kolom. Berikut programnya:
```python
import string

enc = '1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}'.replace('-', '').split(',')
alpha = string.ascii_lowercase.replace('k', '')
table = [list(alpha[i:i+5]) for i in range(0, len(alpha), 5)]
flag = ''

for e in enc:
    if len(e) == 2: 
        x, y = list(e)
        flag += table[int(x)-1][int(y)-1]
    else:
        flag += e

print(flag)
```