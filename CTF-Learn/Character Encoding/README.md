# Deskripsi
Pada challange di jelaskan bahwa pada industri komputer, ditetapkan sebuah standar untuk memfasilitasi pertukaran informasi diantara American Coder. Dan si pembuat  challange membuatnya sedikit lebih sulit, jadi kita di suruh untuk memecahkan kode ini `41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D`.

## Penyelesaian
Berdasarkan penjelasan challange angka angka diatas merupakan angka dari tabel [ASCII](https://id.wikipedia.org/wiki/ASCII) yang memiliki representasi karakter tersendiri. Awalnya aku mengira bahwa ini merupakan desimal ordinal number, akan tetapi setelah dilihat-lihat ketika ada alphabet dibelakangnya menandakan bahwa ini adalah desimal dalam bentuk hexnya.

Untuk programnya nantinya kita akan mengubah hexnya satu persatu menjadi desimal dulu kemudian baru kita gunakan function `chr()` untuk mengubah desimal tersebut menjadi karakter/huruf. Dan berikut programnya:
```python
flag = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
decFlag = "".join(chr(int(f, 16)) for f in flag.split())
print(decFlag)
# output : ABCTF{45C11_15_U53FUL}
```