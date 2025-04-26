# Deskripsi
Pada challange ini dijelaskan bahwa kita menemukan kebocoran website login. Dan disuruh untuk mencari password dari user `cultiris`. Kita telah diberikan duabuah file txt yang satu berisi username dan satunya lagi berisi password. Penjelasan tambahan bahwa nama user dan password urutannya sama.
## Penyelesaian
Bisa di bilang challange ini cukup mudah, bisa kita pecahkan meski tanpa tools menggunakan CTRL + F. Akan tetapi cukup memakan waktu ketika kita mencari passwordnya jika urutan usernya ada di seratus sekian dan kita harus teliti. Jadi oleh karena itu saya akan membuat program python untuk menemukan urutan yang sama dengan urutan username. Berikut algoritmanya:
1. Membuat function untuk mengambil teks yang ada dan menjadikannya array
2. Membuat variable yang menyimpan array teks tersebut
3. Membuat variable untuk menyimpan cipher/passwordnya
4. Membuat perulangan untuk mengecek tiap tiap nama sekaligus urutan menggunakan [enumerate](https://www.w3schools.com/python/ref_func_enumerate.asp)
5. Membuat gerbang logika untuk mengecek nama dan menghentikan program serta menyimpan password
6. Menampilkan hasil

Berikut programnya:
```python
def load_files_into_array(path):
    with open(path, 'r', encoding='utf-8') as p:
        return [line.strip() for line in p]

user = load_files_into_array('usernames.txt')
psswd = load_files_into_array('passwords.txt')

cipher = ""

for i, nama in enumerate(user):
    if nama == 'cultiris':
        cipher = psswd[i]
        break

print(cipher)
# output: cvpbPGS{P7e1S_54I35_71Z3}
```
Dan yap flag tersebut tinggal kita enkripsikan lagi, menggunakan [ROT bruteforce](https://www.dcode.fr/rot-cipher) dan kita menemuka flagnyaa yippi!