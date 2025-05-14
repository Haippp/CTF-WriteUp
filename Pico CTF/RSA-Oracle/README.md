# RSA Oracle
Cryptography | Medium | 
---
## Deskripsi Challange 
Dapatkah Anda menyalahgunakan oracle? Seorang penyerang dapat menyadap komunikasi antara bank dan perusahaan fintech. Mereka berhasil mendapatkan [pesan](./secret.enc) (ciphertext) dan [password](./password.enc) yang digunakan untuk mengenkripsi pesan tersebut.Setelah melakukan pemeriksaan ulang secara intensif, mereka menemukan bahwa bank tersebut memiliki sebuah oracle yang digunakan untuk mengenkripsi kata sandi dan dapat ditemukan di sini `nc titan.picoctf.net 60866`. Dekripsi kata sandi dan gunakan untuk mendekripsi pesan. Oracle dapat mendekripsi apa pun kecuali kata sandi.

## Observasi
