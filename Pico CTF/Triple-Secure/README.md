# Triple Secure
## Deskripsi challange
Untuk mendapatkan bendera, Anda harus memecahkan RSA tidak hanya sekali, tetapi tiga kali!

file: [encrypt.py](./encrypt.py) [public-key.txt](./public-key.txt)

## Analisa
Disini terlihat bahwa sebuah ciphertext dienkripsi beberapa kali menggunakan _N_ yang berbeda beda. Akan tetapi bisa kita lihat pada pembuatan enkripsi nya ada hal yang cukup fatal:
```
p = getPrime(1024)
q = getPrime(1024)
r = getPrime(1024)

n1 = p * q
n2 = p * r
n3 = q * r
```
Bisa terlihat diatas bahwa n1, n2, dan n3 nya terbuat dari 3 buah nilai yang sama dan dikombinasikan. Ini bisa kita manfaatkan menggunakan GCD agar mendapatkan satu nilai tertentu. Seperti jika kita melakukan gcd pada *n1*, dan *n2* maka kita akan mendapatkan *p*. Dan begitupun seterusnya. Mari langsung saja kita buat script untuk dekripsinya.

## Penyelesaian
Berikut skrip yang sudah saya buat:
```python
from Crypto.Util.number import long_to_bytes
from math import gcd

n1 = 1519249205981417557494105524889126882216253352057638164345...
n2 = 1589648225960890155930714294194044723278198663250257299109...
n3 = 1686674102429090951505772727521639850573218239886691855048...
e = 65537
c = 55275571305494866268683556383431645566366406459750705638787...

p = gcd(n1, n2)
q, r = n1//p, n2//p

phi = [(p-1)*(q-1), (p-1)*(r-1), (q-1)*(r-1)]
d = [pow(e, -1, phi[i]) for i in range(len(phi))]

for n, d, in zip([n1, n2, n3][::-1], d[::-1]):
    c = pow(c, d, n)

print(long_to_bytes(c).decode())
```
Disini algoritma dari dekripsinya cukup simple, kita cari nilai p, q, dan r nya dengan melakukan gcd pada ketiga n yang kita dapatkan. Kemudian mencari phi nya agar mendapatkan nilai d. dan terakhir melakukan dekripsi RSA dengan di mulai dari nilai n dan d paling akhir ke nilai n dan d paling awal. Dan yappp kita dapat flagnya ;)