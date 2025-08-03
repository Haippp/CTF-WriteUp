# The Safest Encryption
## Deskripsi Challange
Saya mencegat file zip ini, isinya tampaknya dienkripsi, tetapi sepertinya kuncinya juga ada di sana. Bisakah Anda mencoba memulihkan file yang dienkripsi?

- file: [CTFlearn.zip](https://ctflearn.com/challenge/download/1092)

## Penyelesaian
Sejujurnya saya tahu enkripsi apa berdasarkan commnet yang ada. Enkripsi yang digunakan disini adalah XOR, dimana salah satu file entah itu .txt atau .pdf merupakan ciphertext dan plaintext. Jadi saya langsung membuat skrip untuk melakukan dekripsinya. Disini untuk skripnya cukup gampang kita bisa menggunakan _function open()_  dan _'rb'_ untuk bisa membaca bytesnya. Kemudian menggunakan _function xor()_ dari _library pwn_. Berikut skripnya:
```python
from pwn import xor 

with open('CTFLearn.pdf', 'rb') as file1, open('CTFLearn.txt', 'rb') as file2: 
    var1 = file1.read() 
    var2 = file2.read() 
    flag = xor(var1, var2) 
    with open('result', 'wb') as result: result.write(flag)
```