# Deskripsi 
Kami melakukan banyak penggantian untuk mengenkripsi ini. Dapatkah Anda mendekripsinya? Hubungkan dengan `nc jupiter.challenges.picoctf.org 39894.`

## Penyelesaian 
Challange ini cukup mudah karena deskripsi pada challange menjelaskan bahwa ini dibuat dengan banyak subsitusi, Kemudian pada cipher text nya terdapat banyak alphabet acak. Bisa ditebak ini merupakan [aristocrat cipher](https://en.wikipedia.org/wiki/Aristocrat_Cipher) yang mensubsitusikan karakter satu persatu. Dan kita akan langsung menggunakan tools [quipqiup](https://quipqiup.com/).

dan yap hasilnya terlihat flagnya adalah `frequency_is_c_over_lambda_agflcgtyue`