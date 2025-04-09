# Deskripsi
Ini adalah teks flagnya `104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42`. Dari angka angka tersebut nantinya kita disuruh untuk mengambil modulus 41 yang nantinya dicari modular inversnya. Nah hasil dari perhitungan tersebut diubah menjadi karakter dengan ketentuan 1 - 27 adalah Huruf alfabet, 28 - 36 adalah angka desimal, dan 37 adalah underscore.
## Penyelesaian
Kita langsung saja membuat programnya, algoritma dari program tersebut adalah :
1. Membuat variable yang menyimpan teks flagnya
2. Membuat variable array yang berisi Karakter set dengan urutan seperti ketentuan sebelumnya
3. Membuat perulangan for untuk melakukan perhitungan modular invers untuk tiap tiap angka pada flag.
4. dari hasil perhitungan tersebut disimpan yang nantinya akan diubah menjadi karakter berdasarkan hasil perhitungannya
5. Menampilkan hasil dekripsinya dan membungkusnya dalam format flag picoCTF{...}
dan jadilah sebuah program seperti berikut...
```python
# Text flag
flag = "104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42"
# Arayy Karakter Set 
KarakterSet = [x for x in "abcdefghijklmnopqrstuvwxyz0123456789_"]
# Variable untuk menyimpan sekaligus melakukan dekripsinya
Decrypt = "".join(KarakterSet[pow(int(n), -1, 41) - 1] for n in flag.split())
# Menampilkan hasil dekripsi dan membungkusnya kedalam flag picoCTF
print('picoCTF{'+ Decrypt + '}')
# output : picoCTF{1nv3r53ly_h4rd_dadaacaa}
```