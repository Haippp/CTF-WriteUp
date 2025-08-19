# Defying Hell
## Deskripsi Challange
Alice has been sharing secret encrypted messages with Bob. I would really like to know what those are...

I contacted my good friend Eve, a well-known eavesdropper. She sent me the numbers she found at the beginning of their conversation. By the look of things, this looks like a key exchange. If we would find the key, we would be able to decode every message they encrypted with it!

Help me find both private keys. To submit the flag, decode them correctly and wrap them into CTFlearn{<Alice>_<Bob>} format.

Hint: the title of this challenge is a pun... I can't tell you more ;)

## Penyelesaian
Untuk menyelesaikan masalah ini cukup mudah kita hanya perlu menggunakan function *discrate_log()* dari library sympy. Akan tetapi ketika nilai a dan b langsung ku kirim alert yang muncul menunjukkan bahwa flag salah. Dan aku baru sadar bahwa private keys nya perlu di decode terlebih dahulu. Maka dari itu langsung saja saya decode dari integer menjadi string yang bisa di baca. Untuk melihat file program yang saya buat bisa klik [count-a&b.py](./count-a&b.py).