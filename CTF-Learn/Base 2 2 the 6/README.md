# Deskripsi
Tidak ada penjelasan khusus hanya kata-kata bahwa banyak cara untuk encoding dan decoding serta teks cipher `Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9`.

## Identifikasi
Kita bisa menebak cipher ini sebenarnya dari judul challange dan bentuk ciphernya. Dari judul challange yaitu Base 2, 2 the 6 yang mengarah pada 6bit biner `111111` yang merupakan salah satu teknik dari base 64 yang memisah 8 bit menjadi 6 bit biner. Dan dari pola ciphernya yang memiliki perpaduan angka dan alphabet yang merupakan karakter karakter yang ada pada base 64. 

## Penyelesaian
Karna sudah tahu apa ciphernya mari langsung saja kita buat program untuk melakukan dekripsinya:
```python
import base64

encode_text = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"

print(base64.b64decode(encode_text).decode('utf-8'))
#output : CTF{FlaggyWaggyRaggy}
```
Dan yapp kita dapat flagnya XD.