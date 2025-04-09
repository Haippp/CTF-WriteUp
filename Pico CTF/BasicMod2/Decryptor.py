# Text flag
flag = "104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42"
# Arayy Karakter Set 
KarakterSet = [x for x in "abcdefghijklmnopqrstuvwxyz0123456789_"]
# Variable untuk menyimpan sekaligus melakukan dekripsinya
Decrypt = "".join(KarakterSet[pow(int(n), -1, 41) - 1] for n in flag.split())
# Menampilkan hasil dekripsi dan membungkusnya kedalam flag picoCTF
print('picoCTF{'+ Decrypt + '}')