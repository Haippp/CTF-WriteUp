# Cyber Talents: Postbase
## Deskripsi Challange
Kami memiliki huruf dan angka ini dan tidak memahaminya. Kau bisa? R[corrupted] BR3tCNDUzXzYxWDdZXzRSfQ==

## Penyelesaian
Kalau diliat dari pola ciphernya maka ini merupakan base64 akan tetapi terdapat corrupt atau kerusakan pada sebagian hasil ciphernya. Disini kita tidak mengetahui berapa karakter yang kurang pada cipher tersebut, dan pertanyaannya adalah bagaimana cara mengetahuinya???

**Proses Encoding Base64:**
1. Ambil 3 byte (24 bit) data asli
Contoh: 01101000 01100101 01101100 (3 byte)
2. Pecah jadi 4 bagian masing-masing 6 bit
24 bit → empat bagian (6 bit × 4 = 24 bit)
Contoh: 011010 000110 010101 101100
3. Setiap 6 bit itu dikonversi ke 1 karakter base64
Jadi: 3 byte input = 4 karakter output base64

Sesuai penjelasan diatas, karena kita ingin menghitung berapa karakter yang kruang pada base64 maka kita hanya perlu moduluskan panjang cipher yang ada dengan 4.
```python
flag = 'RBR3tCNDUzXzYxWDdZXzRSfQ=='
print(len(flag) % 4) #2
```

Setelah ktia coba programnya maka yang muncul adalah angka 2, jadi kita tahu nih bahwa karakter yang hilang sebanyak 2 karakter. Dan langsung saja kita membuat decryptornya dengan mencoba semua kemungkinan huruf dengan for loop seperti berikut:
```python
from base64 import b64decode
import string

b64fill = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
"""Variable untuk meneyimpan karakter base64 yang nantinya\n
berfungsi untuk mengisi kekurangan pada teks yang hilang"""

for corupt in b64fill: 
    for corupt2 in b64fill: 
        # Mencoba semua kemungkinan karakter
        result = b64decode(f'R{corupt}{corupt2}BR3tCNDUzXzYxWDdZXzRSfQ==')
        if result[:4] == b'FLAG':
            # Menghentikan program jika terdapat hasil yang di harapkan
            print(result)
            break
```
Bisa kalian coba programnya berhasil, dan kita mendapatkan flagnya...
