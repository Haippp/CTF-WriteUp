# Deskripsi

Deskripsi challangenya dia meminta kita untuk melihat metode baru yang dia ciptakan yang tidak pernah dilihat sebelumnya. Dia juga menjelaskan telah banyak menambahkan for loops akan tetapi dia sendiri ga paham tujuannya buat apa😂. dan di bawah deskripsinya kita telah diberikan da buah file yaitu file python untuk enkripsinya dan file output.txt hasil dari enkripsinya.

## Pembahasan

Kita buka terlebih dahulu program python yang telah disediakan, Kemudian akan kita coba baca dan pahami bagaimana cara kerja programnya.

```python
#!/usr/bin/env python3

from random import randint

with open('flag.txt', 'rb') as f:
    flag = f.read()

with open('secret-key.txt', 'rb') as f:
    key = f.read()

def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

ctxt = encrypt(flag, key)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]

for random_str in random_strs:
    for i in range(randint(0, pow(2, 8))):
        for j in range(randint(0, pow(2, 6))):
            for k in range(randint(0, pow(2, 4))):
                for l in range(randint(0, pow(2, 2))):
                    for m in range(randint(0, pow(2, 0))):
                        ctxt = encrypt(ctxt, random_str)

with open('output.txt', 'w') as f:
    f.write(ctxt.hex())
```

Secara garis besar alur dari cara kerja program enkripsinya adalah sebagai berikut :

1. Mengimport function randint(random integer) dari library random.
2. Membuka file flag.txt yang nantinya isi dari file tersebut dimasukkan ke sebuah variable flag.
3. Membuka file secret-key.txt yang nantinya isi dari file tersebut dimasukkan kesebuah variable key.
4. Sebuah function bernama encrypt yang berfungsi untuk melakukan enkripsi XOR repeating key.
5. Melakukan enkripsi XOR dengan variable flag dan key.
6. Membuat sebuah variable array bernama random_strs yang menyimpan teks (bytes my encryption method, is absolutely impenetrable, ever, ever, ever, ever, ever, ever, break it).
7. Melakukan sebuah for loops brutall untuk semua bytes random_strs yang ada sekitar lebih dari ratusan kali per string bytes yang ada.
8. Kemudian menulis sebuah file output.txt yang merupakan hasil enkripsi XOR sebelumnya yang di hex kan.
   Terlihat cukup kompleks karena banyak sekali proses enrkipsi XOR di dalamnya dengan banyak percobaan XOR yang ada🥲.

## Penyelesaian

Setelah kita lihat alur dari program enkripsinya maka tahapan selanjutnya adalah membuat dekripsinya, caranya dengan membalik proses enkripsi yang ada. Mulai dari paling bawah yaitu hasil ciphernya akan kita ubah dari hex menjadi bytes. 
Kemudian tantangan terbesar yang kita hadapi adalah langkah ini, bagaimana cara kita memngatasi percobaan perulangan yang berkali-kali XOR dengan random string yang ada. Ini sempat membuat saya pusing karena setelah di cek hasil perulangannya sampai ratusan hingga ribuan per string bytes yang ada. Akan tetapi setelah saya coba melihat hasil XOR yang beberapa kali ini dengan mencoba menambahkan beberapa syntax hasil enkripsi XOR beberapa kali seperti di bawah.
```python
xor1 = xor(flag, random_strs[8])
xor2 = xor(xor1, random_strs[8])
xor3 = xor(xor2, random_strs[8])
xor4 = xor(xor3, random_strs[8])
print('1.', xor1)
# output : 1. b'2\x13\x10G2z{n\x04]Q\x1au\x1c};D6\x03_J/\x026O_\x05\x1a(^d\x0bT\x17\x1emSA'
print('2.', xor2)
# output : 2. b'Weu5W\x0c\x1e\x1ca+4h\x10j\x18I!@f-/YgD*)`hM(\x01y1a{\x1f67'
print('3.', xor3)
# output : 3. b'2\x13\x10G2z{n\x04]Q\x1au\x1c};D6\x03_J/\x026O_\x05\x1a(^d\x0bT\x17\x1emSA'
print('4.', xor4)
# output : 4. b'Weu5W\x0c\x1e\x1ca+4h\x10j\x18I!@f-/YgD*)`hM(\x01y1a{\x1f67'
```
Saya menemukan pola dimana hasil enkripsi XOR ganji dengan genap memiliki hasil yang sama. Sehingga kita bisa ambil kesimpulan berapa kalipun hasil enkripsinya semisal 7 kali XOR hasilnya akan sama dengan yang 1 kali XOR atau semisal 24 kali XOR hasilnya akan sama dengan yang 2 kali XOR. Jadi kita akan hanya perlu mencoba perulangan sebanyak 5! faktorial atau 120 kali yang dimana simplenya kombinasinya seperti ganjil ganji, ganjil genap, sampai terkahir genap, genap.
