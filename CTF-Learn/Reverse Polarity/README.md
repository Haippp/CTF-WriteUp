# Deskripsi
Saya membeli hard drive baru hanya untuk menyimpan flag saya, namun saya khawatir hard drive tersebut akan rusak. Apa yang harus kulakukan? Satu-satunya yang bisa saya lakukan adalah dengan ini: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101.

## Penyelesaian 
Saya berspekulasi binary ini merupakan beberapa karakter representasi dari ASCII, yang berisi teks flagnya. Jadi saya akan membuat sebuah algoritma untuk programnya sebagai berikut:
1. Memisahkan binary nya per byte(8 bit biner)
2. Mengubah binernya menjadi demsial
3. Mengubah desimalnya menjadi karakter
4. Lalu menggabungkan semua karakternya

Dan ini lah hasil program dari algoritma diatas
```python
def Binary8Bit(binary):
    dec = ""
    for i, c in enumerate(binary, 1):
        if i % 8 == 0:
            dec += c + ' '
        else:
            dec += c
    return dec

cipher = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"
biner = Binary8Bit(cipher)
flag = "".join(chr(int(b, 2)) for b in biner.split())
print(flag)
# CTF{Bit_Flippin}
```