# Deskripsi
Pada challange ini kida diberikan sebuah teks  `\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e`. Saya menebak bahwa ini merupakan [byte](https://cryptography.io/en/3.4/glossary.html). dan ada hint dibelakangnya yang menjelaskan bahwa flagnya dimulai dengan `ctflearn{`.

## Penyelesaian
Saya bisa menebak bahwa xor ini merupakan xor repeating key, yang mana akan mudah di tebak jika keynya pendek dengan mengxor kan sebagian plaintext yang kita ketahui.

Mari kita coba hasil xor dengan sebagian flag yang kita ketahui
```python
from pwn import xor

cipher = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'
print(xor(cipher, b'ctflearn{'))
#output : b'jowlsjowlhq{D`aGudjXkl}}|'
```
Kita sudah mengetahui bahwa keynya adalah `jowls` terlihat dari perulangan kata `jowlsjowl` dengan key panjang key 5 karakter. Dan berikut hasil programnya:
```python
from pwn import xor

cipher = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'
key = xor(cipher, b'ctflearn{')[:5]

print(xor(cipher, key))
# output : b'ctflearn{xor_is_the_goop}'
```