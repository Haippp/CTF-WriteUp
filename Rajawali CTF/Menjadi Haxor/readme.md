# Deskripsi
Pada deskripsi challange tertulis "Sepertinya pesan ini harus di Brute Force, tapi mimin lupa apa jenis enskripsinya :(" dari deskripsi tersebut serta judul challangenya. Kita dapat menyimpulkan bahwa pada challange ini kita disuruh untuk melakukan brute force pada enkripsi XOR, jadi aku akan membuat program dan mencoba semua karakter ASCII dari 1 - 127.

Bagi yang tidak tahu ASCII itu apa, ASCII adalah singkatan dari American Standard Code for Information Interchange. ASCII adalah standar internasional untuk mewakili karakter, seperti huruf, angka, dan simbol, dalam komputer.

Nah untuk mendekripsinya cukup mudah kita bisa menggunakan tools brute force XOR online seperti [XOR cipher - by.dcode](https://www.dcode.fr/xor-cipher). Akan tetapi karna saya suka hal menantang saya membuat program nya sendiri menggunakan python.
## Penjelasan program
```python
def XOR_brute_force(cipher):
    for key in range(1, 127):
        decrypted = "".join(chr(ord(c) ^ key) for c in cipher)
        if decrypted[:6] == 'CTFRST':
            print(f'{key}. key({chr(key)}) {decrypted}')


ciphertext = "{l~jklCZJML]g^WJ[]g@WJgQKgPY@WJE"
XOR_brute_force(ciphertext)
```
Program ini berfungsi untuk melakukan bruteforce yang keynya hanya 1 byte, dengan mencoba seluruh byte yang ada pada table ASCII. Dan dilengkapi gerbang logika IF untuk hanya mencetak hasil dekripsi yang hanya menampilkan sesuai format flagnya.

Apabila program ini dijalankan maka akan memunculkan hasil "56. key(8) CTFRST{brute_force_xor_is_haxor}". Ini menunjukkan bahwa flagnya berada pada index 56, yang dalam table ASCII representasinya adalah angka 8.