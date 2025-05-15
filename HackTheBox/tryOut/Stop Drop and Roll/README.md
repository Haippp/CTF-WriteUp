# Stop Drop and Roll
## Deskripsi Challange
The Fray: Video Game adalah salah satu permainan yang paling populer di masa lalu... yah, kami tidak ingat berapa lama. "Komputer" kita sekarang ini tidak dapat berjalan lebih dari itu, dan memiliki kecenderungan untuk menjadi berulang-ulang...

## Analisa
Setelah memasuki netcatnya, Kita disini disuruh untuk mengikuti aturan main seperti:
1. Jika saya memberi tahu Anda ada GORGE, Anda mengirim kembali STOP
2. Jika saya memberi tahu Anda ada PHREAK, Anda mengirim kembali DROP
3. Jika saya memberi tahu Anda ada FIRE, Anda mengirim kembali ROLL
Jadi misalnya GORGE, GORGE, FIRE maka kita perlu mengiril STOP-STOP-ROLL. Atau misalnya PHREAK maka yang kita kirim DROP.

## Penyelesaian
Setelah kita memahami bagaimana cara kerjanya ini lah hasil programnya 
```python
from pwn import *

TheFray = remote("94.237.59.174", 37639)

TheFray.recvuntil(b"there's a ")
R1 = TheFray.recvline().strip().decode().replace(', you send back ', ' ').split()
TheFray.recvuntil(b"there's a ")
R2 = TheFray.recvline().strip().decode().replace(', you send back ', ' ').split()
TheFray.recvuntil(b"there's a ")
R3 = TheFray.recvline().strip().decode().replace(', you send back ', ' ').split()

Dict = {
    R1[0]: R1[1], 
    R2[0]: R2[1], 
    R3[0]: R3[1]
}

TheFray.sendlineafter(b'(y/n) ', b'y')
TheFray.recvuntil(b'\n')

Question = ''
Answer = ''

while True:
    Question = TheFray.recvline().strip().decode().replace(',', '')
    print(Question)
    Answer = '-'.join(Dict[q] for q in Question.split())
    print(Answer)
    TheFray.sendlineafter(b'do? ', Answer.encode()) 
```
Program diatas bekerja dengan cara:
1. Mengkoneksikan ke nc target
2. Mengambil teks GORGE, STOP dan sebagainya dan di simpan ke R1, R2, R3
3. Teks tersebut kemudian di simpan ke dalam dictionary yang fungsinya untuk ketika key nya di panggil maka valuenya akan muncul
4. mengirim y otomatis ketika ada teks (y/n) 
5. Mengambil pertanyaan yang nantinya di simpan ke dalam array
6. Melakukan perulangan untuk mengambil semua data yang ada pada variable question untuk menjadi key pada Dictionary

Dan yap setelah berpuluh-puluh atau ratusan akhirnya kita dapat flagnya.
```
flag: HTB{1_wiLl_sT0p.....} 
```