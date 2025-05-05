# Deskripsi
Pada penjelasannya dijelaskan bahwa ada suara ketukan yang masuk dari kabel. Dan kita mencari tahu apa yang dikatakannya.

mari langsung saja menyambungkan ke `nc jupiter.challenges.picoctf.org 9422.`

## Penyelesaian
Setelah dibuka ada sebuah teks `.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- }`, Dari pola dan penjelasannnya ini merupakan sandi morse. jadi langnsung saja kita gunakan tools [morse](https://morsecode.world/international/translator.html) online. Dan setelah kita dekripsi menggunakan tools tersebut kita mendapatkan flagnya `PICOCTF{M0RS3C0D31SFUN2683824610}`