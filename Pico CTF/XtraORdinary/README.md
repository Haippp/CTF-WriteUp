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
Saya menemukan pola dimana hasil enkripsi XOR ganji dengan genap memiliki hasil yang sama. Sehingga kita bisa ambil kesimpulan berapa kalipun hasil enkripsinya semisal 7 kali XOR hasilnya akan sama dengan yang 1 kali XOR atau semisal 24 kali XOR hasilnya akan sama dengan yang 2 kali XOR. Jadi kita akan hanya perlu mencoba perulangan sebanyak 5! faktorial atau 120 kali yang dimana simplenya kombinasinya seperti ganjil ganji, ganjil genap, sampai terkahir genap, genap. Solusinya adalah kita melakukan nested for sampai 5x. dan bisa kalian lihat hasilnya, semua kombinasi dipakai disana. 
```python
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    print(i, j, k, l, m)
```
Kemudian untuk XOR normal kita bisa menggunakan sebagian flag yang kita ketahui yaitu `picoCTF` untuk mengetahui keynya. Dan berikut hasil programnya:
```python 
from random import randint
from pwn import xor

def decrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt

cipher = bytes.fromhex("57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637")
key = b'picoCTF{'

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]

for i in range(2):
    cipher = decrypt(cipher, random_strs[0])
    for j in range(2):
        cipher = decrypt(cipher, random_strs[1])
        for k in range(2):
            cipher = decrypt(cipher, random_strs[2])
            for l in range(2):
                cipher = decrypt(cipher, random_strs[3])
                for m in range(2):
                    cipher = decrypt(cipher, random_strs[4])
                    Pkey = decrypt(cipher, key)
                    print(Pkey) 
```
Kita lihat teks mana yang sekiranya masuk akal atau yang bisa dibaca.
```
output :
...
b"(\x15R\x08\x01\x12N-\x14[^\x14\x04&^/C:\nZr\t54D\x01\x1d\x0eL'\t\x19L\x16\x08e\x7f7"
b"Jg7ij2'Yv);uo\x067[!Ho;\x19)\\@&sxo'\x07`m.dm\x04\x14\x17"
b'Mc7zdd+_q-;faP;]&Lo(\x17\x7fPF!wx|)Qlk)`m\x17\x1aA'
b'/\x11R\x1b\x0fDB+\x13_^\x07\npR)D>\nI|_92C\x05\x1d\x1dBq\x05\x1fK\x12\x08vqa'
b'I{6(x};\rc22x$H;Y&Hk4\x16)L[1!jg K)w)`m\x17\x1eY'
b'+\tSI\x13]Ry\x01@W\x19OhR-D:\x0eU}\t%/SS\x0f\x06Kk@\x03K\x12\x08vuy'
b',\rSZ\x1d\x0b^\x7f\x06DW\nA>^+C>\x0eFs_))TW\x0f\x15E=L\x05L\x16\x08e{/'
b"N\x7f6;v+7\x0bd62k*\x1e7_!Lk'\x18\x7f@]6%jt.\x1d%q.dm\x04\x10\x0f"
b'Africa!Aa/;x}\x067B3_d?\x06{TV(dt}lFkj#z}\x11\x1a['
b'#\x14\x17\x08\x08AH5\x03]^\x19\x16&^6Q-\x01^m[="J\x16\x11\x1c\x07f\x02\x1eA\x08\x18pq{'
b'$\x10\x17\x1b\x06\x17D3\x04Y^\n\x18pR0V)\x01Mc\r1$M\x12\x11\x0f\t0\x0e\x18F\x0c\x18c\x7f-'
b'Fbrzm7-Gf+;ksP;D4[d,\x08-XP/`tnb\x10gl$~}\x02\x14\r'
b' \x08\x16I\x1a\x0eTa\x16FW\x14]hR4V-\x05Qb[-9]D\x03\x14\x00*K\x04F\x0c\x18c{5'
...
```
Bisa kita lihat key yang paling masuk akal diantara semua yang ada adalah `Africa!` ini. jadi mari kita tes dan rubah teks yang ada di variable key menjadi `Africa!` Dan yap kita dapat flagnya 
```python
output :
b'xt\'.XH\\7u)8t\x06=<D$Hk:t<lR(+h)"y\x1de:h/9;\x7f'
b'\x1a\x06BO3h5C\x17[]\x15m\x1dU0F:\x0e[\x1f\x1c\x05&JY\rHIYt\x11X\x1aJXP_'
b'\x1d\x02B\\=>9E\x10_]\x06cKY6A>\x0eH\x11J\t M]\r[G\x0fx\x17_\x1eJK^\t'
b"\x7fp'=V\x1eP1r-8g\x08k0B#Lk)zj`T//h:,/\x11c=l/*5)"
b'picoCTF{w41t_s0_1_d1dnt_1nv3nt_x0r???}'
b'\x12\x1b\x06\x0e(t/\x0f\x15FT\x154SY+S-\x01P\x0fN\x1d+S\x1c\x13R\x05T6\x0cR\x00Z^T]'
b'\x15\x1f\x06\x1d&"#\t\x12BT\x06:\x05U-T)\x01C\x01\x18\x11-T\x18\x13A\x0b\x02:\nU\x04ZMZ\x0b'
b'wmc|M\x02J}p01gQ%<Y6[d"j8xY6jv `"S~7v?,1+'
b'\x11\x07\x07O:;3[\x00]]\x18\x7f\x1dU)T-\x05_\x00N\r0DN\x01Z\x02\x18\x7f\x16U\x04ZM^\x13'
```