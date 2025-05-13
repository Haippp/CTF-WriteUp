# Deskripsi
Layanan ini memberikan Anda sebuah bendera terenkripsi. Dapatkah Anda mendekripsinya hanya dengan N & e?

Sambungkan ke program dengan netcat:
`$ nc verbal-sleep.picoctf.net 60275`

## Penyelesaian
Setelah ku sambungkan ke program aku mendapatkan N, e serta ciphertextnya
```bash
nc verbal-sleep.picoctf.net 60275
N: 24775683251054697162052786445426411680683225647528773075043879694627067401560410197543696618065058595576765678761800666599084113189468876409066230971805298
e: 65537
cyphertext: 15354983422019433901132458435099676408640777543785700187708892069840606454546846835202636499656613229056894541775376130018349027247903727797529556008411767
```
Terlebih dahulu kita akan mencari private key(`d`) untuk mendekripsi ciphertextnya. Pada rsa rumus untuk mendapatkan `d` adalah dengan menggunakan rumus invers `d  ≡ e ^ -1 mod φ(N)`. Akan tetapi kita belum tau `φ(N)`. untuk mencari `φ(N)` rumusnya `φ(N) = (p-1)(q-1)` dan p dan q merupakan hasil dari pemfaktoran `N = p * q`. Jadi algoritmanya sebagai berikut:

1. Mencari faktorisasi dari N.
2. Hasil faktoriasinya akan menjadi nilai untuk mencari totient φ(N).
3. Kemudian mencari d dari hasil invers e ^ -1 mod φ(N).
4. Baru menghitung Plaintext = ciphertext ^ d mod N.

Dan berikut hasil dari programnya:
```python
from Crypto.Util.number import long_to_bytes
from sympy import factorint

N = 24775683251054697162052786445426411680683225647528773075043879694627067401560410197543696618065058595576765678761800666599084113189468876409066230971805298
e = 65537
ct = 15354983422019433901132458435099676408640777543785700187708892069840606454546846835202636499656613229056894541775376130018349027247903727797529556008411767

p,q = factorint(N)
totient = (p-1) * (q-1)
d = pow(e, -1, totient)

pt = pow(ct, d, N)
print(long_to_bytes(pt))
```
Mungkin sebagian ada yang bingung kenapa ada penggunaan long to bytes untuk menampilkan hasil, Jawaban simplenya karna di file encryptnya menggunakan bytes to long🤣. Cuman untuk cara kerja dari bytes to long adalah mengubah bytes misalnya `b'ABC'` yang binarynya merupakan  `01000001 01000010 01000011` kemudian binary tersebut digabungkan menjadi satu `010000010100001001000011` dan dihitung integernya dan jadilah longinteger berikut `4276803`.