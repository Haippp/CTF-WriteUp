# Deskripsi
Sebenarnya untuk deskripsi challange nya full yapping atau cerita panjang yang kurang memberikan arahan atau hubungan tentang cipher ini. Jadi pada intinya dekripsi challangenya menjelaskan bahwa kita ada melihat sebuah tulisan acak yang ada didinding beserta sebuah patung seorang kaisar romawi. Dan kutebak kaisar romawi tersebut adalah Caesar Julius yang ada hubungannya dengan caesar cipher.

Kemudian kita disini juga telah diberikan 2 buah file yaitu file output/flagnya dan source code enkripsinya. Mari kita analisa codenya.
 
## Analisa kode
```python
# Ngambil flag dari file secret
from secret import FLAG
# Librarynya ga kepake bjirrr
from random import randint

def to_identity_map(a):
    # mengembalikan hasil perhitungan :
    # ordinal karakter(misalnya A = 65) - 65(desimalnya dari hexa 0x41)
    return ord(a) - 0x41

def from_identity_map(a):
    # mengembalikan hasil perhitungan :
    # a mod 26(mod 26 untuk membatasi hasil hanya 0 - 25) + 65
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = '' # variable untuk menyimpan ciphertext
    # perulangan sampai panjang isi parameter m
    for i in range(len(m)): 
        # variable menyimpan karakter m index sekarang
        ch = m[i]
        # Gerbang logika untuk mengecek apakah isi dari 
        # variable ch apakah alphabet atau bukan 
        if not ch.isalpha(): 
            # Langsung menyimpan karakter dari ch jika bukan alphabet
            ech = ch
        else:
            # Mengubah karakter menjadi 0 - 25(fungsi dari function to_identity_map)
            chi = to_identity_map(ch)
            # Melakukan pergeseran berdasarkan index(fungsi dari function from_identity_map)
            ech = from_identity_map(chi + i)
        # Menyimpan isi variable ech ke variable c
        c += ech
    # Mengembalikan cipher
    return c

# Membuat folder output.txt untuk menulis deskripsi serta hasil enkripsi
with open('output.txt', 'w') as f:
    f.write('Make sure you wrap the decrypted text with the HTB flag format :-]\n')
    f.write(encrypt(FLAG))
```
Simplenya algoritma yang ada diatas adalah sebagai berikut:
1. Mengambil cipher text dari parameter m
2. Melakukan perulangan sampai panjang isi dari parameter m
3. Mengambil per karakter berdasarkan index dan di simpan di variable ch
4. Pengecekan dengan gerbang logika
5. Jika karakternya bukan alphabet maka langsung simpan
6. Dan jika alphabet maka akan digeser berdasarkan index iterasi.
7. Semua hasil perulangan akan di simpan di c dan nantinya di simpan di file ouput.txt