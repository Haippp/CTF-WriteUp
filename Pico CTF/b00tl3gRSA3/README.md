# b00tl3gRSA3
## Deskripsi Challange
Mengapa menggunakan p dan q ketika saya bisa menggunakan lebih banyak? Terhubung dengan `nc jupiter.challenges.picoctf.org 4557`.

## Penyelesaian
Setelah saya mencoba menghubungkan ke net cat tersebut, bisa terlihat bahwa n adalah hasil dari perkalian yang banyak. sehingga kita perlu rumus tertentu untuk mencari b nya. Akan tetapi hal ini bukan yang sulit karna untuk mencari totient rumus yang di perlukan hanya seperti berikut: 
![alt text](image.png)

Akan tetapi saya cukup kesulitan dalam memfaktorkan menggunakan python. Karena cukup lambat dan tidak efektif jika kita menggunakan factorint yang hanya cocok untuk n di bawah 200 bit. Setelah melakukan beberapa pencarian saya menemukan website yang gacorrr, dan cocok untuk mencari faktorisasi dari n. Nama websitenya adalah [alpertron](https://www.alpertron.com.ar/ECM.HTM). Dan disini ketika aku memasukkan n ternyata bisa juga memunculkan phi nya. 