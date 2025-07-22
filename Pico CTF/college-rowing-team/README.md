# college-rowing-team
## Deskripsi Challange
Saya baru saja bergabung dengan tim dayung kampus saya! Untuk memberikan kesan pertama yang baik, saya mulai mengirimkan pesan otomatis yang positif kepada rekan satu tim saya setiap hari. Saya bahkan mengirimi mereka bendera dari waktu ke waktu!
file :
- [encrypt](./encrypt.py)
- [massage](./encrypted-messages.txt)

## Penyelesaian
Setelah saya membuka file pesannya saya melihat bahwa e nya atau exponennya itu cukup rendah. Serta c atau pesan terenkripsinya lebih kecil dari pada n. Jadi mungkin saja bahwa pesan tersebut hanya di pangkatkan dan tidak di moduluskan.

Kita hanya perlu untuk mencari akar pangkatnya. Berikut program saya:
```python
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

n = []
e = []
c = []

with open('encrypted-messages.txt', 'r') as file:
    for i, line in enumerate(file):
        if i % 3 == 1:
            e.append(line[3:])
        elif i % 3 == 2:
            c.append(line[3:])
        else:
            n.append(line[3:])
    
for i in range(len(n)):
    enc = int(c[i])
    exp = int(e[i])
    msg = iroot(enc, exp)[0]
    print(long_to_bytes(msg).decode())
```
Dann yappp kita dapat flagnya 😃🚩.