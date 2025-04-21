# Deskripsi
Pada deskripsi challange kita dijelaskan bahwa ini merupakan new type of encryption dan disuruh untuk memecahkan kode rahasianya dan diwrap/dibungkus dengan format `picoCTF{}`. Kemudian kita diberikan sebuah cipher text `ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih ` dan sebuah file yang menghasilkan enkripsi tersebut. Kita langsung saja membuka file nya untuk menganalisa bagaimana cara enkripsinya

## Analisa
```python
import string

#Titik Awal pergeseran
LOWERCASE_OFFSET = ord("a")
#hanya menampilkan string/alphabet sampai 16 huruf.
ALPHABET = string.ascii_lowercase[:16] #output : abcdefghijklmnop	

def b16_encode(plain):
	# Variable untuk menyimpan enkripsi b16
	enc = ""
	for c in plain:
		# Mengubah format dari ord ke binary
		binary = "{0:08b}".format(ord(c))
		# Mengambil 4 biner pertama
		enc += ALPHABET[int(binary[:4], 2)]
		# Mengambil 4 biner terakhir
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	# Mengubah karakter cipher menjadi urutan b16
	t1 = ord(c) - LOWERCASE_OFFSET
	# Mengubah karakter key menjadi urutan b16
	t2 = ord(k) - LOWERCASE_OFFSET
	# Menjumlahkan t1 dan t2 kemudian di mod dengan panjang Alphabet 
	# dan hasil dari perhitungan tersebut nantinya menjadi index pada array ALPHABET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "b"

# Memastikan bahwa key ada pada ALPHABET
assert all([k in ALPHABET for k in key])
# Memastikan bahwa panjang key hanya 1
assert len(key) == 1

# Melakukan enkripsi pada b16
b16 = b16_encode(flag)
# Menyimpan hasil enkripsi shifting
enc = ""
# Melakukan shifting
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
```
Dari keseluruhan program garis besar dari algoritma ini adalah `Plaintext > B16 > Shifting > Cipher`. Setelah tahu garis besarnya bagaimana mari kita pahami lebih dalam mengenai metode enkripsinya. 

Hal yang pertama yang akan kita bahas adalah function enkripsi b16. Pertama ada variable enc yang nantinya berfungsi untuk menampung hasil enkripsi. Kemdudian ada for loop yang mengambil satu persatu karakter yang ada pada vairable plain text yang kemudian karakter tersebut diubah menjadi byte/8 bit biner. 

