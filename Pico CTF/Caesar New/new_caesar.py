import string

#Titik Awal pergeseran
LOWERCASE_OFFSET = ord("a")
#hanya menampilkan string/alphabet sampai 16 huruf.
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		# Mengubah format dari ord ke binary
		binary = "{0:08b}".format(ord(c))
		print(binary)
		print(binary[:4])
		# Mengambil 4 biner pertama
		enc += ALPHABET[int(binary[:4], 2)]
		print(binary[4:])
		# Mengambil 4 biner terakhir
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "b"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)