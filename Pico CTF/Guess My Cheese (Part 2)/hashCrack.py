from pwn import *
from hashlib import sha256

HOST = 'verbal-sleep.picoctf.net'
PORT =  60267
PATH = './cheese_list.txt'

conn = remote(HOST, PORT)

def str2hash(text):
    return sha256(text).hexdigest()

def crackTheHash(wordlist_path, target):
    variants = {
        "ori" : lambda s: s,
        "low" : lambda s: s.lower(),
        "upp" : lambda s: s.upper()
    }

    with open(wordlist_path, 'r') as file:
        print('[*] Mencoba membaca wordlist dan melakukan hash cracking')
        for line in file:
            word = line.strip()
            for nama, func in variants.items():
                wordVar = func(word).encode()
                for salt in range(256):
                    raw_salt = bytes([salt])
                    if str2hash(wordVar + raw_salt) == target:
                        print('[+] Keju telah ditemukan :', str2hash(wordVar + raw_salt))
                        print('[+] Keju telah ditemukan :', word)
                        print('[+] Varian :', nama)
                        print('[+] Salt yang digunakan :', hex(salt)[2:])
                        print('[+] Metode salt : appended')
                        print('[+] Keju setelah di berikan salt :', wordVar.decode() + raw_salt.decode('latin-1'))
                        sleep(5)
                        return word, hex(salt)[2:]
                    elif str2hash(raw_salt + wordVar) == target:
                        print('[+] Keju telah ditemukan :', str2hash(wordVar + raw_salt))
                        print('[+] Keju telah ditemukan :', word)
                        print('[+] Varian :', variants)
                        print('[+] Salt yang digunakan :', hex(salt)[2:])
                        print('[+] Metode salt : prepended')
                        print('[+] Keju setelah di berikan salt :', wordVar.decode() + raw_salt.decode('latin-1'))
                        sleep(5)
                        return word, hex(salt)[2:]
                    
    print("[-] Mohon maaf kami tidak menemukan apa apa")
    return None

def getHash():
    conn.recvuntil(b'like to do?')
    conn.sendline(b'g')
    conn.recvuntil(b'encrypted cheese:  ')
    enc = conn.recvline().strip().decode()
    return enc

def sendAnswer(answer1, answer2):
    conn.sendlineafter(b"what's my cheese?\n", answer1)
    conn.sendlineafter(b"what's my salt?\n", answer2)

if __name__ == "__main__":
    cheeseHash = getHash()
    try:
        cheese, salt = crackTheHash(PATH, cheeseHash)
        sendAnswer(cheese, salt)
    except:
        conn.close()
    conn.interactive()