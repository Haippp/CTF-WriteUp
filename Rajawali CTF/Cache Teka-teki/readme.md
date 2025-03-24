# Deskripsi
Di challange ini kita disuruh untuk menebak sebuah chiper berupa angka yaitu : `3 8 9 16 5 18 12 1 14 7 11 1 8` di penjelasannya dijelaskan bahwa ini Chiper ini berupa varian huruf ke angka, sering digunakan dalam cache misteri geocaching

Misteri Geocaching sendiri adalah bagian dari permainan Geocaching, yaitu permainan berburu harta karun di dunia nyata menggunakan koordinat GPS. Dalam Mystery Cache (Cache Misteri), pemain harus memecahkan teka-teki atau tantangan tertentu sebelum menemukan lokasi sebenarnya dari cache yang tersembunyi.
## Penyelesaian
Disini aku coba menebak saja dengan kita konversi dari angka ke huruf, berdasarkan penjelasan sebelumnya yaitu "Chiper ini berupa varian huruf ke angka". Jadi mungkin saja ini A1Z26 yang merupakan angka refresentasi dari urutan huruf, misalnya 1 = a, 2 = b, 3 = c, dan seterusnya. 

Dan berikut program untuk decodenya :
```python
# Memasukkan teks tersebut kedalam sebuah array kemudian di split/dipotong
# dan diubah menjadi integer
chiper = [int(n) for n in '3 8 9 16 5 18 12 1 14 7 11 1 8'.split()]

# selanjutnya angka angka tersebut satu persatu di jumlahkan dengan 64
# 65 pada ASCII adalah A, Seperti yang kita tahu 1 adalah A
# jadi jika 64 + 1 maka akan jadi A
flag = "".join(chr(x + 64) for x in chiper)

# output = CHIPERLANGKAH
print(flag)
```
Nah tinggal kita ikuti formatnya, maka flagnya adalah CTFRST{chiperlangkah}