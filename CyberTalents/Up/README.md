# Up
## Deskripsi Challange
Setiap kali Anda naik, Anda akan mendapatkan satu balon
ejxc{T0nY0J_BsUMS4}

## Penyelesaian
Berdasarkan deskripsi kalau kita mencoba menaikkan tiap shifting huruf maka kita bisa melihat pola flag:
```
e -> f
j -> k -> l
x -> y -> z -> a
c -> d -> e -> f -> g
```
Berikut coding untuk penyelesaiannya:
```python
enc = 'ejxc{T0nY0J_BsUMS4}'

ctr = 1
Upp = ord('A') ; Low = ord('a')
flag = ''

for c in enc:
    if c.isupper():
        flag += chr((ord(c) - Upp + ctr) % 26 + Upp)
        ctr += 1
    elif c.islower():
        flag += chr((ord(c) - Low + ctr) % 26 + Low)
        ctr += 1
    elif c.isdigit():
        flag += c
        ctr += 1
    else:
        flag += c

print(flag)
```
Setelah beberapa kali melakukan percobaan penambahan nilai, barulah menemukan yang pas. Bahwa penambahan nilai hanya berlaku pada huruf dan angka saja, serta pada angka nilai hanya di naikkan tapi angka tersebut tidak boleh diubah.