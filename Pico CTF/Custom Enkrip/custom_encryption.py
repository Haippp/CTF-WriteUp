from random import randint
import sys


def generator(g, x, p):
    #pow is firstArgs ^ secondArgs
    return pow(g, x) % p


def encrypt(plain_text, key):
    # membuat variable array untuk si chiper.
    cipher = []
    # melakukan perulangan berdsarkan panjang 
    # karakter plain text
    for char in plain_text:
        cipher.append(((ord(char) * key *311)))
        #kemudian mengubah karakter jadi ordinal 
        # number dan mengalikannya dengan key dan
        # 311 lalu menambahkannya ke chiper dan 
        # mengembalikan nilai chiper
    return cipher

def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else: 
        return True


def dynamic_xor_encrypt(plain_text, text_key):
    #membuat sebuah wadah variable untuk menampung sandinya.
    cipher_text = ""
    #membuat variable yang berisi nilai panjang kunci.
    key_length = len(text_key)
    #membuat pengulangan untuk 
    for i, char in enumerate(plain_text[::-1]):#membalik plain text 
        #membuat key_char agar sesuai panjang plain_text
        key_char = text_key[i % key_length]
        #membuat XOR enkrip dengan membandingkan char dan keychar
        encrypted_char = chr(ord(char) ^ ord(key_char))
        #Menambahkan karakter yang sudah di enkripsi ke variable chiper text
        cipher_text += encrypted_char
    return cipher_text


def test(plain_text, text_key):
    # membuat dua buah variable yang prime
    p = 97
    g = 31
    # memastikan kedua variable bernilai prime agar bisa di lanjutkan
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    # membuat variable yang berisi nilai acak dari a-10 sampai a
    a = randint(p-10, p)
    b = randint(g-10, g)
    # menampilkan hasil nilai random tersebut.
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    # print(f"a = {u}")
    # print(f"b = {v}")
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    # print(f"a = {key}")
    # print(f"b = {b_key}")
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    print(f'Semi cipher is: {semi_cipher}')
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')


if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")
