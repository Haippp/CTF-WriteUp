def key2tabel(key: str):
    """
    untuk mengubah key menjadi tabel
    array berukuran 5x5
    """
    if len(key) != 25:
        print('Panjang kunci harus 25!')
        return
    return [list(key[i:i+5]) for i in range(0, len(key), 5)]

def cleaning_text(text: str) -> str:
    """
    Merapikan teks dengan menghapus spasi serta
    semua yang bukan huruf
    """
    cleanText = ''

    for t in text:
        if t.isalpha():
            cleanText += t.upper()
    
    return cleanText
            
def back2format(res: str, format: str) -> str:
    """
    Mengembalikan ke format string awal
    """
    result = ''
    i = 0

    for c in format:
        if c.isalpha() and format.index(c) > 2:
            result += res[i].lower()
            i += 1
        elif c.isalpha():
            result += res[i]
            i += 1
        else:
            result += c

    return result


def find_pos(char: str, keyT: list):
    """
    Untuk mencari karakter pada key square
    dan mengembalikan baris serta kolomnya
    """
    for row, line in enumerate(keyT):
        if char in line:
            return row, line.index(char)


def decryptencrypt(enc: str, key: str) -> str:
    """
    Melakukan seluruh proses enkripsi playfair
    """
    text = cleaning_text(enc)
    keyT = key2tabel(key)
    result = ''

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_pos(a, keyT)
        r2, c2 = find_pos(b, keyT)
        if r1 == r2:
            result += keyT[r1][(c1-1)%5] + keyT[r2][(c2-1)%5]
        elif c1 == c2:
            result += keyT[(r1-1)%5][c1] + keyT[(r2-1)%5][c2]
        else:
            result += keyT[r1][c2] + keyT[r2][c1]

    result = back2format(result, enc)
    return result

key = 'QWERTYUIOPASDFGHKLZXCVBNM'
enc = 'MQDzqdor{Ix4Oa41W_1F_B00h_m1YlqPpPP}'

flag = decryptencrypt(enc, key)
print(f'Flag is: {flag}')