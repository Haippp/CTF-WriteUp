# Deskripsi
Pada challange ini tidak ada penjelasan khusus hanya diberikan duabuah file yaitu file enkripsi dan file output, Jadi mari langsung kita analisa aja.

## Analisa 
```python
from random import randint

# Variable angka
a = 288260533169915
# Variable prima
p = 1007621497415251

# Variable flag
FLAG = b'crypto{????????????????????}'


# Function Encrypt
def encrypt_flag(flag):
    # Variable array untuk menyimpan cipher
    ciphertext = []
    # bin : Mengubah integer jadi biner
    # zfill : Padding 0 atau menambahkan
    # Variable plaintext mengubah text dalam bentuk biner
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    print(plaintext)
    for b in plaintext:
        # nilai random dari 1 sampai p
        e = randint(1, p)
        # a pangkat e mod p
        n = pow(a, e, p)
        # jika bit index sekarang 1 maka cipher akan langsung disimpan
        if b == '1':
            ciphertext.append(n)
        # jika bit index sekarang tidak 1 yaitu 0 maka -n mod p
        else:
            n = -n % p
            ciphertext.append(n)
        # Jadi sebenarnya disini adalah bagaimana cara kita menebak apakah ini merupakan 0 atau 1
    return ciphertext


print(encrypt_flag(FLAG))
```
Simplenya algoritma enkripsi diatas seperti berikut:
1. Membuat variable a yang berisi nilai desimal `288260533169915`
2. Membuat variable p yang berisi nilai prima `1007621497415251`
3. Membuat variable flag yang meyimpan teks flagnya
Kemudian pada function enkrip :
1. Membuat variable/wadah untuk menyimpan cipher text.
2. Mengubah perkarakter plaintext menjadi 1byte biner.
3. Membuat sebuah for loop untuk mengubah per bit biner yang di representasikan sebagai b yang ada di plaintext dengan langkahnya sebagai berikut:
- Membuat variable e yang berisi angka random dari 1 - p
- Membuat variable n yang melakukan [modular exponentiation](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/)
- jika nilai b 1 maka nilai n akan langsung disimpan ke cipher text
- jika tidak n dijadikan -n lalu di mod kan p dan baru di simpan

## Penyelesaian
Jadi kesimpulannya Enkripsi ini hanya mengubah 0 atau 1 pada biner menjadi sebuah angka. Untuk mendekripsinya kita perlu tahu apakah angka tersebut merupakan 0(-n) atau 1(n). n kalau di rumuskan menjadi n = a ^ e (mod p) dan -n menjadi -n ≡ p - a (mod p). Dan -n itu disebut sebagai [Modular Negation](https://www.omnicalculator.com/math/modulo-of-negative-numbers).

Kemudian n itu merupakan hasil dari Quadratic Residues, Jadi kita akan menggunakan [legendre symbol](https://en.wikipedia.org/wiki/Legendre_symbol) untuk mengetahui mana yang n dan -n. Dan algoritma untuk mencari legendre symbol adalah [eular criterion](https://en.wikipedia.org/wiki/Euler%27s_criterion) dengan rumus `a ^ ((p - 1)/2) mod p`. Dan beginilah programnya

```python
EncFlag = [67594220461269, 501237540280788, 718316769824518, 296304224247167, 48290626940198, 30829701196032, 521453693392074, 840985324383794, 770420008897119, 745131486581197, ...]

p = 1007621497415251

def decryptor(Enc):
    E = []
    for i, n in enumerate(Enc):
        if pow(n, (p-1)//2, p) == 1:
            E.append(1)
        else:
            E.append(0)
        if (i + 1) % 8 == 0 :
            E.append(" ")
    return "".join(str(x) for x in E)

hasil = "".join(chr(int(x, 2)) for x in decryptor(EncFlag).split())
print(hasil)
```