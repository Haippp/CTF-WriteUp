# Easy Peasy
![](https://img.shields.io/badge/challange_by-picoCTF-blue) ![](https://img.shields.io/badge/difficulty-Medium-yellow)
## 📝Deskripsi Challange
Donald sudah benar-benar gila. Untuk mencegah kekacauan dunia, kamu menculiknya. Sebelum penculikan, dia mencoba mengirim satu pesan terenkripsi kepada istrinya, Melania. Beruntung kamu berhasil menyadap pesan tersebut. Donald mengakui bahwa dia menggunakan enkripsi AES-CBC - sebuah algoritma blok dengan panjang blok 16 byte. (diwakili oleh 32 karakter)

Pesan tersebut adalah: {391e95a15847cfd95ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}

Formatnya berisi vektor inisialisasi (IV) te rlebih dahulu, diikuti teks terenkripsi (c), dipisahkan oleh tanda titik dua, semuanya dibungkus dalam kurung kurawal. {IV,c} Setelah menyiksanya dengan mencuri rambut palsunya, dia memberitahu Anda teks asli pesan tersebut adalah:

FIRE_NUKES_MELA!

Sebagai hacker yang bersemangat, tentu saja Anda mencoba memanfaatkan pesan ini. Untuk mendapatkan bendera, ubah pesan yang akan dibaca Melania menjadi: SEND_NUDES_MELA!

Kirimkan bendera dalam format: flag{IV,c}  

Karakter-karakter tersebut diubah menjadi heksadesimal, dan satu byte diwakili oleh dua karakter; misalnya, string "84" mewakili karakter "F" dalam pesan dan seterusnya.

## 🧩Penyelesaian
Pada aes terdapat sebuah serangan bernama bit-flipping attack, serangan ini memungkinkan kita untuk mengubah isi hasil dekripsi menjadi apa yang kita mau. Syaratnya adalah kita mengetahui isi pesan asli yang ingin kita ubah.

Diatas kita disuruh mengubah teks *FIRE_NUKES_MELA!* menjadi *SEND_NUDES_MELA!*. Disini sudah terpenuhi syarat untuk melakukan bitflipping attack. Adapun cara manipulasinya adalah dengan menggunakan xor dengan rumus sebagai berikut:
```math
new_iv = pesan_asli ^ iv ^ pesan manipulasi
```

Nah karena xor memiliki sifat komutatif(pengelompokan) dan asosiatif(pertukaran) maka dari itu serangan ini bisa dilakukan. Untuk coding lebih lengkapnya bisa di cek di [solve.py](./solve.py)