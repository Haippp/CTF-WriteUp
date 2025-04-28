# Deskripsi
Sebenarnya untuk deskripsi challange nya full yapping atau cerita panjang yang kurang memberikan arahan atau hubungan tentang cipher ini. Jadi pada intinya dekripsi challangenya menjelaskan bahwa kita ada melihat sebuah tulisan acak yang ada didinding beserta sebuah patung seorang kaisar romawi. Dan kutebak kaisar romawi tersebut adalah Caesar Julius yang ada hubungannya dengan [caesar cipher](https://id.wikipedia.org/wiki/Sandi_Caesar).

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
1. Mengambil cipher text dari parameter m, Yang nantinya parameter m diganti dengan FLAG dari modul secret yang tidak kita ketahui isinya
2. Melakukan perulangan sampai panjang isi dari parameter m
3. Mengambil per karakter berdasarkan [index](https://www.programmerzamannow.com/pemrograman/java/dasar/tipe-data-array/#:~:text=Selain%20itu%2C%20Array%20memiliki%20informasi,mengubah%20data%20di%20dalam%20Array.) dan di simpan di variable ch
4. Pengecekan dengan gerbang logika
5. Jika karakternya bukan alphabet maka langsung simpan
6. Dan jika alphabet maka akan digeser berdasarkan index iterasi.
7. Semua hasil perulangan akan di simpan di c dan nantinya di simpan di file ouput.txt

## Penyelesaian
Setelah kita paham bagaimana algoritma enkripsinya. Sekarang kita akan membuat algoritma dekripsinya. Untuk dekripsinya sebenarnya cukup simple berikut langkahnya:
1. Membuat variable `dec` untuk menyimpan hasil dekripsinya
2. Melakukan perulangan sampai panjang isi teks yang akan di dekripsi.
3. Membuat variable `char_cipher` untuk menyimpan karakter dari [index](https://www.programmerzamannow.com/pemrograman/java/dasar/tipe-data-array/#:~:text=Selain%20itu%2C%20Array%20memiliki%20informasi,mengubah%20data%20di%20dalam%20Array.) sekarang.
4. Menambahkan gerbang logika untuk melakukan pengetesan apakah `char_cipher` yang sekarang merupakan alphabet apa bukan.
5. Jika alphabet maka ordinal dari karakter tersebut akan di kurang 65(desimalnya dari hexa 0x41), Lalu di kurang index sekarang. Kemudian di modulus kan dengan 26 dan baru di tambahkan lagi denga 0x41. baru di simpan ke variable `dec`.
6. Jika bukan alphabet maka langsung saja di simpan di ke variable `dec`.

Berikut hasil dari program algoritma diatas:
```python 
def Trithemius_Decrypt(c):
    dec = ''
    for i in range(len(c)):
        char_cipher = c[i]
        if char_cipher.isalpha():
           dec += chr((((ord(char_cipher) - 0x41) - i) % 26) + 0x41)
        else : 
            dec += char_cipher
    return dec

flag = 'DJF_CTA_ SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL'
print('HTB{'+ Trithemius_Decrypt(flag) + '}')

```
Dan yappp kita dapat flagnya `HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER}`. Sedikit tambahan penjelasan [Trithemius cipher](https://www.cachesleuth.com/trithemius.html) merupakan cipher turunan dari caesar cipher. Bedanya caesar cipher pergeserannya tetap sedangkan trithemius ini dia akan bergeser berdasarkan index iterasi. jadi misalnya huruf pertama digeser sekali maka selanjutnya akan di geser duakali, kemudian tigakali dan seterusnya...