# Character
## Deskripsi Challange
Keamanan melalui Kebosanan yang Diinduksi adalah pendekatan favorit pribadi saya. Tidak semenarik seperti The Fray, tetapi saya suka membuatnya sebisa mungkin membosankan untuk melihat rahasia saya, sehingga Anda hanya bisa mendapatkan satu karakter pada satu waktu!

## Penyelesaian
Setelah saya masuki Dockernya dan mencoba programnya, Simplenya disini kita di suruh mengetik indeks satu per satu untuk menampilkan flagnya. Sebenarnya bisa menggunakan cara manual dengan mengetik indeks satu persatu tapi akan cukup memakan waktu lama untuk dapat flagnya jadi saya membuat script bash untuk mengotomatiskan mengetiknya dan hasil output nya nanti kita akan simpan di file txt.

Dan ini lah programnya:
```bash
#!/bin/bash

# Bersihkan file output jika sudah ada
> flag_output.txt

# Terhubung ke server dengan nc dan mengetik otomatis
(
for ((i=0; ; i++)); do
    echo $i  # Kirim index otomatis
    sleep 0.1  # Jeda sedikit (sesuaikan jika butuh lebih cepat)
done
) | nc 83.136.252.13 35374 | tee -a flag_output.txt
```