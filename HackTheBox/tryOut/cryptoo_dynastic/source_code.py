# Ngambil flag dari file secret
from secret import FLAG
# Librarynya ga kepake bjirrr
from random import randint

def to_identity_map(a):
    # mengembalikan hasil perhitungan :
    # ordinal karakter(misalnya A = 65) - 65(desimalnya dari hexa 0x41)
    return ord(a) - 0x41

def from_identity_map(a):
    # mengembalikan hasil perhitungan :
    # a mod 26(mod 26 untuk membatasi hasil hanya 0 - 25) + 65
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = '' # variable untuk menyimpan ciphertext
    # perulangan sampai panjang isi parameter m
    for i in range(len(m)): 
        # variable menyimpan karakter m index sekarang
        ch = m[i]
        # Gerbang logika untuk mengecek apakah isi dari 
        # variable ch apakah alphabet atau bukan 
        if not ch.isalpha(): 
            # Langsung menyimpan karakter dari ch jika bukan alphabet
            ech = ch
        else:
            # Mengubah karakter menjadi 0 - 25(fungsi dari function to_identity_map)
            chi = to_identity_map(ch)
            # Melakukan pergeseran berdasarkan index(fungsi dari function from_identity_map)
            ech = from_identity_map(chi + i)
        # Menyimpan isi variable ech ke variable c
        c += ech
    # Mengembalikan cipher
    return c

# Membuat folder output.txt untuk menulis deskripsi serta hasil enkripsi
with open('output.txt', 'w') as f:
    f.write('Make sure you wrap the decrypted text with the HTB flag format :-]\n')
    f.write(encrypt(FLAG))