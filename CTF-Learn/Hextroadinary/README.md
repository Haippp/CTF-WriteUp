# Deskripsi
Perkenalkan ROXy, seorang pembuat kode yang terobsesi untuk menjadi peretas terbaik di dunia. Dia berspesialisasi dalam kode rahasia pendek yang sulit diuraikan. Nilai-nilai heksa di bawah ini misalnya, dia melakukan sesuatu dengan mereka untuk menghasilkan kode rahasia, bisakah Anda mencari tahu apa itu? Jawaban Anda harus dimulai dengan 0x.

# Penyelesaian
Dari deskripsi dan namanya kita tahu bahwa ini merupakan enkripsi XOR. Jadi kita akan langsung saja membuat program pythonya.
```python
Flag = hex(0xc4115 ^ 0x4cf8)

Print(Flag)
# output : 0xc0ded
```
Disini karna sudah tahu enkripsinya XOR saya langsung saja menggunakan caret(^) yang merupakan simbol bitwse operasi XOR. Kemudian kita akan menambahkan fungsi hex, karena jika kita tidak menambahkannya outputnya akan menjadi desimal. Dan ketika kalian print kita dapat flagnya, lalu tinggal wrap/bungkus dengan format flag `CTFlearn{}`
