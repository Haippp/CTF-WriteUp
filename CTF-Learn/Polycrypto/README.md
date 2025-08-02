# Polycrypto
## Deskripsi Chalange
Polinomial adalah cabang matematika yang sangat berguna. Polinomial juga dapat menyembunyikan rahasia. Dapatkah Anda menemukan apa yang disembunyikan oleh polinomial ini?

- file: [filed.txt](https://mega.nz/#!mLJXWCIS!ZLpbPEGzhPevFeLGwUv6imuRTl19jiO5q-P7_dVaXoM)
- penjelasan: [Finite field arithmetic](https://en.wikipedia.org/wiki/Finite_field_arithmetic)

## Penyelesaian
Jujur saja, Saya masih kurang paham mengenai polinomial maka dari itu saya akan langsung membahas cara mengubah polinomial ke bentuk biner. Untuk mengubah dari polinomial ke bentuk biner caranya cukup simple yaitu:
1. Cari derajat atau pangkat yang paling tinggi misalnya pada soal ini pangkat tertinggi adalah **206**
2. Nah ketika kita tahu derajat paling tinggi maka kita akan melakukan pengecekan dari 206, 205, 204, ...sampai, 2, 1, 0.
3. Jika x pangkat sekian ada maka tulis 1
4. Jika tidak ada maka tulis 0

Mari kita pakai sebuah contoh soal dengan angka yang kecil agar lebih paham. Misalnya ada nilai berikut `x^7+x^3+x^2+1`, maka derajat paling tinggi adalah 7 dan kita harus melakukan pengecekan dari 7 sampai 0.

```
polinomial = `x^7+x^3+x^2+1`

melakukan pengecekan dari 7 - 0:
x^7 apakah ada?? ya✅       = 1
x^6 apakah ada?? tidak❎    = 0
x^5 apakah ada?? tidak❎    = 0
x^4 apakah ada?? tidak❎    = 0
x^3 apakah ada?? ya✅       = 1
x^2 apakah ada?? ya✅       = 1
x^1 apakah ada?? tidak❎    = 0
x^0/1 apakah ada?? ya✅     = 1

biner = 10001101
```

_#note: caret(^) simbol dari pangkat_

Okey setelah kita paham bagaimana cara kerja nya langsung saja kita membuat skrip untuk mendapatkan flagnya. Algoritmanya cukup simple kita akan membuat fungsi mengubah dari polinomial ke biner setelah itu biner ke bytes ascii. dan yappp begitulah saya dapat flagnya, code nya bisa kalian liat di file [polyToBinary.py](./polyToBinary.py)