# Easy Peasy
![](https://img.shields.io/badge/challange_by-picoCTF-blue) ![](https://img.shields.io/badge/difficulty-Medium-yellow)
## 📝Deskripsi Challange
Pad sekali pakai tidak dapat dipecahkan, tetapi dapatkah Anda memulihkan flag? (Bungkus dengan picoCTF{})

- koneksi : `nc xxxxx.picoctf.net xxxx`
- file : [otp.py](./otp.py).

## 🧩Penyelesaian
Setelah saya analisa codingnya saya mendapatkan logic dari programnya dimana jenis enkripsinya merupakan otp sesusai dengan judul file. Key yang digunakan berasal dari suatu file jadi bukan sebuah hasil acak atau sebagainya. Dan keynya berbeda beda tergantung kapan data dimasukkan. Contoh diawal data yang dimasukkan adalah flag maka key yang digunakan adalah 0 sampai panjang flag, inputan seterusnya key yang digunakan adalah urutan seteleh panjang keynya. Dan ada dua hal menarik disini:
```python
# Bagian pertama
KEY_LEN = 50000

# Bagian kedua
if stop >= KEY_LEN:
	stop = stop % KEY_LEN
	key = kf[start:] + kf[:stop]
```
Nahh dari kode diatas kita dapat kesimpulan bahwa key yang ada di file tersebut terbatas hanya sampai *50000*, kemudian jika lebih dari itu maka akan kembali lagi ke awal. Nah oleh karena itu solusi untuk bisa menyelesaikan challange ini adalah dengan mengirimkan sebuah karakter sebanyak 50000. Kemudian kita ambil bagian paling akhir yang merupakan key yang digunakan untuk mengxorkan flagnya. Dan dengan begitu kita bisa menyelesaikan challangenya.

Untuk program otomasi yang ku gunakan bisa kaliak lihat pada file [OTP_BREAK.py](./OTP-Break.py)