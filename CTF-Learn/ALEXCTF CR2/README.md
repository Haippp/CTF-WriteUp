# ALEXCTF CR2: Many Time Secret
## Deskripsi Challange
Kali ini Fady belajar dari kesalahan lamanya dan memutuskan untuk menggunakan onetime pad sebagai teknik enkripsinya, tetapi dia tidak pernah tahu mengapa orang menyebutnya one time pad! Flag akan dimulai dengan `ALEXCTF{`.

https://mega.nz/#!DGxBjaDR!tMWkHf0s0svmkboGd-IASHsS9jACxSYx4zi_ETsyzyQ

## Penyelesaian
```python
from pwn import xor
cipher = []

with open('./msg (4)', 'r') as file:
    for line in file:
        cipher.append(line.strip())

for c in cipher:
    print(xor(bytes.fromhex(c), b'ALEXCTF{')[:8])
```
Disini aku mencoba metode membalik enkripsinya untuk mendapatkan keynya. Dengan cara `key = plaintext ^ cipher`. Dan aku mencoba satu persatu cipher yang ada pada file yang di berikan dan hasilnya seperti berikut:
```
output:

b'Dear Frilgs1<GaWa3eykn-w8D'
b'nderstoom)zd<~`Mfrzu&jcZ8D'
b'sed One }`zx<chZ2v\x7fstr}Jq^'
b'n scheme%)^=tvhLv3exg\x7f-Wl\x11'
b'is the ogen=y}jLkceyie-S}E'
b'hod that)`d=qr}Vw~pdohlRtH'
b' proven }f7\x7fy3gQf3rbghf[|\x11'
b'ever if }ar=wvp\x1e{`1{c{y\x1ekT'
b'cure, Le})Zx<xgQe3xv&rbK8P'
b'gree wita)zx<gf\x1eg`t0rcdM8T'
b'ncryptiog)d~tvd[2r}ggr~\x10'
```
Disini dugaan awalku adalah bahwa key nya merupakan flagnya. Kemudian aku mencoba mengxor kan dengan kemungkinan plaintext pertama dengan menambahkan `end` untuk melengkapi kata `Friend` disana.

```python
from pwn import xor
cipher = []

with open('./msg (4)', 'r') as file:
    for line in file:
        cipher.append(line.strip())

for c in cipher:
    print(xor(bytes.fromhex(c), b'ALEXCTF{end')[:11]) # b'Dear FriHER'
```
Dan kita akan menggunakan `HER` untuk menggantikan si `end` tadi.
```python
from pwn import xor
cipher = []

with open('./msg (4)', 'r') as file:
    for line in file:
        cipher.append(line.strip())

for c in cipher:
    print(xor(bytes.fromhex(c), b'ALEXCTF{HER')[:11])
```
```
output:

b'Dear Friend'
b'nderstood m'
b'sed One tim'
b'n scheme, I'
b'is the only'
b'hod that is'
b' proven to '
b'ever if the'
b'cure, Let M'
b'gree with m'
b'ncryption s'
```
Dan outputnya bisa terlihat seperti diatas yang memperkuat dugaan kita bahwa key dari enkripsi ini merupakan flagnya. Hal lain yang memperkuat dugaan kita ada pada judul challangenya `Many Time` yang menjelaskan bahwa enkripsi ini tidak berkesesuaian dengan prinsip `One Time Pad` yang hanya menggunakan satu kali pakai. Dan kita hanya perlu melanjutkan menebak isi teks yang ada, lalu kita akan mendapatkan flagnya XD.