# Scrambled: RSA
## Deskripsi Challange
Hmmm, saya ingin tahu apakah Anda sudah mempelajari pelajaran Anda... Mari kita lihat apakah Anda memahami RSA dan bagaimana enkripsi bekerja. Terhubung dengan `nc mercury.picoctf.net 6276`.

## Analisa
Ketika kita mencoba masuk ke programnya, Bisa terlihat bahwa flag/ciphernya nya sangat panjang melebihi n nya. Padahal seharusnya `ct < n` karena ct akan di moduluskan dengan `n` jadi diagnosa awal saya pt(plaintext)nya tidak di moduluskan. Akan tetapi setelah saya mencoba mengetikan 1 untuk mencoba salah satu fitur enkripsinya, yang saya dapatkan malah sebuah angka yang panjang. Ini berarti cara kerja dari enkripsinya adakah `pt ^ e`, plaintext nya hanya di pangkatkan tidak di moduluskan. Akan tetapi setelah saya coba di akar pangkatkan tidak sesuai dengan hasil yang di ingin kan.

Setelah mencoba mencari beberapa hal tentang ini petunjuknya ada pada Scrambled. Metode scramble adalah pembelajaran secara berkelompok dengan mencocokkkan kartu pertanyaan dan kartu jawaban yang telah disediakan sesuai dengan soal. 
```
output: 

I will encrypt whatever you give me: a
Here you go: `96243729013900167384523040150182860504058478827724405317427920278297104977261956836653818570753444947714463150959292588101038349935425922824823994688499587090903007536579770983666573470619514479457284770101002725758728868564766891774504393356743379970969048753015765641014678901937804303987800727180887902807`

I will encrypt whatever you give me: ab
Here you go: 96277023262638979996450368748091706816088289355514942165198082082023818449311625747259967286272686081553912227131599616007494883918168001430070907985088992241152425665374831124823696642647470481147648467725350853321176763408158833043714349932332103043561777666896548845738738952656197536346228046105188272533`96243729013900167384523040150182860504058478827724405317427920278297104977261956836653818570753444947714463150959292588101038349935425922824823994688499587090903007536579770983666573470619514479457284770101002725758728868564766891774504393356743379970969048753015765641014678901937804303987800727180887902807`

I will encrypt whatever you give me: b 
Here you go: 11690448910588792014073577447363441175586612365272318955432026320795010472594804513659904439481632762704923025113940422373635323678259732927716638067863671033537111247843138785141253430036205238871735480138166261558393181877406852588898742631209137732161536026748288421840013153720848339885416557345694501920
```

Bisa terlihat ketika kita mengetikan a dan kemudian ab ada hasil yang sama yang muncul, akan tetapi jika b di awal hasilnya beda, Jadi ini bisa diambil kesimpulan bahwa perlu urutan tertentu untuk menghasilkan nilai yang sesuai.

## Penyelesaian
Setelah selesai menganalisa baru kita membuat sebuah program dari hasil analisa tersebut. Kita akan membuat program untuk melakukan bruteforce untuk mencocokkan hasil angka yang ada, sampai tutup dari kurung kurawal dan programnya akan terhenti. Berikut Algoritma serta programnya:

1. Variabel untuk semua isi kemungkinan
2. Perulangan yang terus berulang sampai ada tutup kurawal
3. Perulangan yang mencoba semua kemungkinan
4. Gerbang logika yang mengecek apakah nilai ada di dalam flag
5. Variabel yang menyimpan hasil yang sesuai

```python
from pwn import *

fill = string.ascii_lowercase + string.digits + 'CTF{_}'
conn = remote('mercury.picoctf.net', 6276)
flag = '' ; knownEnc = ['', ]

conn.recvuntil(b'flag: '); Encflag = conn.recvline().strip().decode()

while '}' not in flag:
    for f in fill:
        print(flag + f)
        conn.recvuntil(b'give me: '); sending = conn.sendline(flag + f)
        conn.recvuntil(b'you go: '); result = conn.recvline().strip().decode()
        for k in knownEnc:
            result = result.replace(k, '')
        if result in Encflag:
            flag += f
            knownEnc.append(result)
            break

print('Flag : ' + flag)
```