# Deskripsi
Pada deskripsi challange kita dijelaskan bahwa ini merupakan new type of encryption dan disuruh untuk memecahkan kode rahasianya dan diwrap/dibungkus dengan format `picoCTF{}`. Kemudian kita diberikan sebuah cipher text `ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih ` dan sebuah file yang menghasilkan enkripsi tersebut. Kita langsung saja membuka file nya untuk menganalisa bagaimana cara enkripsinya

## Analisa Program

```python
import string


# variable yang berisi ordnial number dari a yaitu 97.
LOWERCASE_OFFSET = ord("a")
# variable yang berisi string/alphabet sampai 16 huruf.
ALPHABET = string.ascii_lowercase[:16] #output : abcdefghijklmnop

def b16_encode(plain):
	# Variable untuk menyimpan enkripsi b16
	enc = ""
	for c in plain:
		# Mengubah format dari ord ke binary
		binary = "{0:08b}".format(ord(c))
		# Mengambil 4 biner pertama
		enc += ALPHABET[int(binary[:4], 2)]
		# Mengambil 4 biner terakhir
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	# Mengubah karakter cipher menjadi urutan b16
	t1 = ord(c) - LOWERCASE_OFFSET
	# Mengubah karakter key menjadi urutan b16
	t2 = ord(k) - LOWERCASE_OFFSET
	# Menjumlahkan t1 dan t2 kemudian di mod dengan panjang Alphabet
	# dan hasil dari perhitungan tersebut nantinya menjadi index pada array ALPHABET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "b"

# Memastikan bahwa key ada pada ALPHABET
assert all([k in ALPHABET for k in key])
# Memastikan bahwa panjang key hanya 1
assert len(key) == 1

# Melakukan enkripsi pada b16
b16 = b16_encode(flag)
# Menyimpan hasil enkripsi shifting
enc = ""
# Melakukan shifting
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
```

Dari keseluruhan program garis besar dari algoritma ini adalah `Plaintext > Base 16 > Shift/menukar > Cipher`. Setelah tahu garis besarnya bagaimana mari kita pahami lebih dalam mengenai metode enkripsinya.

1. Hal yang pertama yang akan kita bahas adalah function enkripsi b16. Pertama ada variable enc yang nantinya berfungsi untuk menampung hasil enkripsi. Kemdudian ada for loop yang mengambil satu persatu karakter yang ada pada vairable plain text yang kemudian karakter tersebut diubah menjadi byte/8 bit biner. yang nantinya byte tersebut dibagi menjadi 2 bagian(4 biner awal dan 4 biner akhir) yang nantinya 4 biner tersebut diubah menjadi desimal dan dijadikan sebagai index dari array ALPHABET. Dari pola 4 bit biner tersebut dapat kita simpulkan bahwa itu merupakan hexa akan tetapi versi modifikasi, yang mana pada awalnya 1 sampai 9, A sampai F. Diubah menjadi a sampai p.
2. Yang keuda function Shift, Function Shift hanya berfungsi untuk menjumlahkan semicipher dengan key. variable t1 menyimpan ordnial number dari karakter semi cipher yang kemudian nantinya di kurangi dengan LOWERCASE_OFFSET. t2 juga begitu bedanya ordinal numbernya dari karakter key. Misalnya kita ambil contoh semi ciphernya adalah c, kalau c di orndial numberkan maka akan menjadi 99 kita kurangkan dengan 97(LOWERCASE_OFFSET) maka jadilah 2. nantinya variable t1 dan t2 di jumlahkan di mod kan dengan panjang(ALPHABET). sehingga hasil dari perhitungan tersebut akan menjadi index di ALPHABET.

Untuk penjelasan sisanya bisa kalian pahami sendiri dengan membaca penjelasannya di komen pada coding.

## Penyelesaian
Setelah kita memahami bagaimana alur enkripsinya, untuk mendekripsinya kita hanya perlu membalik alurnya seperti berikut `Plaintext < Base 16 < Shift/menukar <  Cipher`. Mari kita bahas lebih detail tentang pembuatan dekripsinya.
1. Shift Decryption, Untuk shift ini cukup mudah kita tinggal mengganti t1 dan t2 yang awalnya dijumlahkan menjadi dikurang.
2. Base 16 Decryption, Karena kita tahu sebelumnya bahwa ini merupakan metode enkripsi [heksadesimal](https://kutu.dev/artikel/meghitung-hexadecimal-octal). Dan kita tidak bisa langsung menjumlahkan dua angka yang ada, berikut rumusnya `a * 16 + b`.
3. Kita akan melakukan for loop dari 97(a) - 122(z), untuk melakukan brute force. 

Berikut hasil programnya :
```python
import string

LOWERCASE_OFFSET = ord("A")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(b16_cipher):
    a = []
    b = []

    for i, d in enumerate(b16_cipher):
        if i % 2 == 0:
            a1 = (ord(d) - 97) * 16
            a.append(a1)
        else:
            b1 = ord(d) - 97
            b.append(b1)

    return "".join(chr(a[i] + b[i]) for i in range(len(a)))

def shift_decode(cipher, key):
    t1 = ord(cipher) - LOWERCASE_OFFSET
    t2 = ord(key) - LOWERCASE_OFFSET

    return ALPHABET[(t1 - t2) % len(ALPHABET)]

cipher = 'cipher text'

for key in range(97, 122):
    semi_cipher = "".join(shift_decode(c, chr(key)) for c in cipher)
    plain = b16_decode(semi_cipher)
    print('key ['+ chr(key) + ']  : ' + plain)
```
Kita test dulu menulis text random untuk memastikan bahwa program dekripsi yang kita buat bisa berfungsi dengan baik. Kita coba menggunakan text `redacted` dengan key `b`.
```
output :
key [a]  : vurtvu
key [b]  : redacted
key [c]  : aTSPRcTS
key [d]  : PCBOARCB
key [e]  : O21>0A21
key [f]  : >! -/0!
key [g]  : -►▼∟▲/►▼
key [h]  : ∟
dst....
```
Okey, karena key b menghasilkan output redacted yang sesuai kita inginkan, berarti program ini memang bekerja dengan baik. Selanjutnya mari kita coba dengan cipher asli.
```
output :
key [a]  : qQqRY[YSVUT[UYWWWYUYTS
key [b]  : v`@`AHJHwBEDvCurJuuDvHFFFuHDHCvvBssv
key [c]  : et_tu?_0797f143e2da9dd3e7555d7372ee1bbe
key [d]  : TcNcd.N/&(&U #"T!SP(SS"T&$$$S&"&!TT QQT
key [e]  : CR=RS↔=▲§↨§D▼↕◄C►BO↨BB◄C§‼‼‼B§◄§►CC▼@@C
key [f]  : 2A,AB
♦♠♦3☺21>♠112♦☻☻☻1♦♦22??2
key [g]  : !01ûóõó"ýðÿ!þ -õ  ÿ!óñññ óÿóþ!!ý..!
key [h]  : ►/
/ ê
ëâäâ◄ìïî►í▼∟ä▼▼î►âààà▼âîâí►►ì↔↔►
key [i]  : ▲ù▲▼ÙùÚÑÓÑÛÞÝÜ
ÓÝÑßßßÑÝÑÜÛ


ÈèÉÀÂÀÿÊÍÌþËýúÂýýÌþÀÎÎÎýÀÌÀËþþÊûûþ
key [k]  : íü×üý·×¸¿±¿î¹¼»íºìé±ìì»í¿½½½ì¿»¿ºíí¹êêí
key [l]  : ÜëÆëì¦Æ§® ®Ý¨«ªÜ©ÛØ ÛÛªÜ®¬¬¬Û®ª®©ÜÜ¨ÙÙÜ
key [m]  : ËÚµÚÛµÌËÊÇÊÊËÊËËÈÈË
key [n]  : ºÉ¤ÉÊ¤»º¹¶¹¹º¹ºº··º
key [o]  : ©¸¸¹st{}{ªuxw©v¨¥}¨¨w©{yyy¨{w{v©©u¦¦©
key [p]  : §§¨bcjljdgfelfjhhhjfjed
key [q]  : qQqRY[YSVUT[UYWWWYUYTS
key [r]  : v`@`AHJHwBEDvCurJuuDvHFFFuHDHCvvBssv
key [s]  : et_tu?_0797f143e2da9dd3e7555d7372ee1bbe
key [t]  : TcNcd.N/&(&U #"T!SP(SS"T&$$$S&"&!TT QQT
key [u]  : CR=RS↔=▲§↨§D▼↕◄C►BO↨BB◄C§‼‼‼B§◄§►CC▼@@C
key [v]  : 2A,AB
♦♠♦3☺21>♠112♦☻☻☻1♦♦22??2
key [w]  : !01ûóõó"ýðÿ!þ -õ  ÿ!óñññ óÿóþ!!ý..!
key [x]  : ►/
/ ê
ëâäâ◄ìïî►í▼∟ä▼▼î►âààà▼âîâí►►ì↔↔►
key [y]  : ▲ù▲▼ÙùÚÑÓÑÛÞÝÜ
ÓÝÑßßßÑÝÑÜÛ
```
Disini kita melihat tidak ada text normal sama sekali, dan text paling normal diantara semuanya adalah pada key `c` yaitu `et_tu?_0797f143e2da9dd3e7555d7372ee1bbe` karna mengingat penjelasan pada deskripsi sebelumnya bahwa text perlu di wrap dengan format picoCTF : `picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}` maka langsung saja ku coba kirim dan challange nya berhasil.

Setelah kucoba telusuri lebih dalam ternyata kalimat tersebut ada maknanya, `et_tu?` merupakan kata kata yang caesar julius yang pernah katakan sebelum kematiannya "Et tu, Brute?" merupakan ungkapan Latin yang secara harfiah berarti "Kamu juga, Brutus?". Ungkapan ini terkenal karena menjadi kata-kata terakhir yang diucapkan Julius Caesar ketika ia ditikam sampai mati oleh teman-temannya dalam drama Shakespeare "Julius Caesar".

Kemudian `0797f143e2da9dd3e7555d7372ee1bbe` merupakan hash md5 text aslinya "Désolé, nous n'avons pas trouvé de correspondance pour ce(s) hash(s)" yang berasal dari bahasa prancis yang artinya "Maaf, kami tidak dapat menemukan kecocokan untuk hash ini". Jadi maksudnya tidak perlu di enkripsikan lagi.