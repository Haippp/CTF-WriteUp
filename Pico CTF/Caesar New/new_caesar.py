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
	# dan hasil dari perhitungan tersebut nantinya menjadi index array ALPHABET
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