# Suspecious message
## Deskripsi Challange
Hello! My friend Fari send me this suspecious message: 'MQDzqdor{Ix4Oa41W_1F_B00h_m1YlqPpPP}' and photo.png. Help me decrypt this!

![alt text](image.png)
## Penyelesaian
Ini merupakan Playfair cipher yang bisa di lihat dari tabel 5x5. Singkatnya cara kerja dari cipher ini adalah:
1. Membuat key berukuran 5x5
2. Mengubah plain text menjadi diagram 2 buah huruf
3. Melakukan substitusi sebagai berikut:
- Jika di kolom yang sama akan di geser ke bawah satu kolom
- Jika di baris yang sama akan di geser ke kanan satu baris
- Jika membentuk _square/rectangle_ maka tukar poisi kolom

Untuk program dekripsinya bisa di lihat di [PlayFair.py](./PlayFair.py)