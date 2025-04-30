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
