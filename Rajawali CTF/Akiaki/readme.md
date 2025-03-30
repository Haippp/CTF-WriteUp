# Deksripsi
Challange ini tidak memiliki hint apa-apa selain angka `67 84 70 82 83 84 123 49 115 95 97 115 99 49 49 95 98 114 111 119 125` cukup mudah menebaknya karena judulnya, Ini merupakan ASCII. ASCII adalah standar pengkodean karakter yang digunakan untuk mewakili teks dalam komputer, peralatan telekomunikasi, dan perangkat lainnya. Dan angka ini merupakan urutan ASCII yang merepresentasikan tiap karakter. Langsung saja kita bikin program pythonya.
## Penyelesaian
```python
Flag = "67 84 70 82 83 84 123 49 115 95 97 115 99 49 49 95 98 114 111 119 125"
print(''.join(chr(int(x)) for x in Flag.split()))
# output : CTFRST{1s_asc11_brow}
```
Algoritma dari program ini dimulai dari pemisahan tiap tiap huruf berdasarkan spasi, melakukan list comprehension x yang nantinya diubah menjadi karakter satu persatu lalu di gabungkan. sebagai informasi tambahan chr() merupakan fungsi untuk mengubah ordinal number menjadi karakter.