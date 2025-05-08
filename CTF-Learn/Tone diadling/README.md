# Tone diadling
## Deskripsi Challange
Pada pukul 13.00 saya menelepon paman saya yang berusia 64 tahun 10 bulan yang lalu, tetapi saya hanya mendengar suara itu. Kemudian saya mulai berpikir tentang jam 24 jam.

Saya harap Anda akan membantu saya memecahkan masalah ini
[`you_know_what_to_do.wav`](https://ctflearn.com/challenge/download/889)

## Pembahasan
Audio yang diberikan merupakan enkripsi [DTMF signaling](https://en.wikipedia.org/wiki/DTMF_signaling), DTMF atau Dual Tone Multi-Frequency merupakan teknologi persinyalan yang digunakan dalam telepon, khususnya pada keypad dengan tombol angka.Teknologi ini menghasilkan nada atau sinyal suara untik yang berbeda-beda untuk setiap tombol yang ditekan.

## Penyelesaian 
Langsung saja kita decode aja file .wav-nya menggunakan tools [DTMF decoder](https://dtmf.netlify.app/). Dan kita mendapatkan output berikut: `67847010810197110123678289808479718265807289125`. Setelah berfikir sebentar aku menyimpulkan bahwa ini merupakan ordinal number atau angka pada tabel ASCII. Bisa langsung kalian decode menggunakan tools yang [ASCII code](https://www.dcode.fr/ascii-code) yang ada pada web.

Akan tetapi karna mas-mas anti mainstream ini lebih suka pake python. Jadi mari kita buat algoritma untuk decode ASCII Ordinal Numbernyanya. Kita tahu bahwa tabel ASCII extended hanya sampai 255 dan untuk angka dan huruf biasanya berada di angka puluhan maka jadilah programnya sebagai berikut:
1. Membuat variable array untuk menyimpan hasil dan yang nantinya akan di return.
2. membuat variable temp/sementara untuk menyimpan niali.
3. melakukan forloop dan menambahkan angka tiap perluangan pada variable temp.
4. Menambahkan gerbang logika mengecek index awal temp merupakan nilai yang lebih dari 2 dan panjang variable harus lebih dan sama dengan 2(puluhan) yang nantinya kemudian hasil tersebut ditambahkan/dimasukkan pada variable array. Simplenya ini gerbang logika untuk menambahkan/menyimpan nilai puluhan 
5. Gerbang logika kedua ini juga mengecek nilai index awalnya merupakan 1 atau 2 dan panjang dari variable nya sama dengan 3(raturan) yang nantinya hasil tersebut ditambahkan/dimasukkan pada variable array.
6. Setelah selesai perulangannya nilai dari array tersebut diubah menjadi bytes dan di decode menjadi string.

Dan berikut hasil dari program diatas:
```python
def ordFormat(N):
    arr = []
    temp = ''
    for x in N:
        temp +=  x
        if int(temp[0]) > 2 and len(temp) >= 2:
            arr.append(int(temp))
            temp = ''
        elif int(temp[0]) <= 2 and len(temp) == 3:
            arr.append(int(temp))
            temp = ''
    print(arr)
    return bytes(arr).decode()
    
N = '67847010810197110123678289808479718265807289125'
print(ordFormat(N))
```