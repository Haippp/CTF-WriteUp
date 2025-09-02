# Lineq
## Deskripsi CHallange
Dapatkah Anda menyelesaikan beberapa persamaan untuk kami? Petunjuk: Untuk fungsi invers modular. gunakan (dari Crypto.Util.number import inverse)

## Penyelesaian
Isi dari teks yang dikirimkan:
```
Lineq.txt

15345857135052644158 * x[0] mod 15914389274045831441 = 10753153698913165324
10107862342967460188 * x[1] mod 12471333000718257439 = 8412981602133999892
15514951512896411 * x[2] mod 11189085043185963643 = 1482464683316586574
4918093547848646552 * x[3] mod 14953553045254805869 = 2025900790652430240
9458472078791077712 * x[4] mod 16969044464796096757 = 5398900907079313999
10389810153032407159 * x[5] mod 12219369241978883401 = 7029759589492702570
10317166141181737080 * x[6] mod 11051035063490494121 = 3468633932944308360
4739071230119101568 * x[7] mod 12446419077417014895 = 8675623443003281737
5602877978471499087 * x[8] mod 17033822019842116078 = 10322234074859615825
6817739495547298027 * x[9] mod 9516363895804911673 = 4437950083761802261
6427678547440599488 * x[10] mod 15079736889469193431 = 3279819731898553304
9457480281190568299 * x[11] mod 10650632135951148921 = 9305609025967996118
3811243068786264022 * x[12] mod 17812647846133398533 = 11526794456945961531
775941643434169870 * x[13] mod 11412472367550805013 = 4738382726559211541
7024610526778714279 * x[14] mod 9778393688778074575 = 5323545124401969226
11651575732234344955 * x[15] mod 16630642531754496501 = 2873213552124115822
6625087805180364133 * x[16] mod 9364964556418467329 = 2787565658998643270
3669801280657684382 * x[17] mod 14097382369878612419 = 7567005815588497736
5443984100737085739 * x[18] mod 10512797518085747507 = 7873334411288369657
12346616364541216766 * x[19] mod 15943449689777265613 = 3904160665454908058
8986565623928863916 * x[20] mod 18324134584075223407 = 188593124624644258
944611705353292388 * x[21] mod 11593718893451959913 = 5953933343058555785
9480419754515455118 * x[22] mod 14797616246348898583 = 13228205597299662061
6357470584650383564 * x[23] mod 10888050221402213645 = 3331190950406564692
4804105847411349449 * x[24] mod 15964574501738046999 = 9808705001033677355
The flag is chr(x[0]%256)+chr(x[1]%256)+...
```
Nah jadi intinya kita harus mencari x menggunakan modular invers dari koefisien. Dibangku smp kita pernah belajar aljabar yang berfungsi untuk mencari nilai _x_ yang tidak di ketahui seperti  misalnya : 
```
a * x = b maka x = b / a

Note:
a * x = b maka x = b / a

Note :
# a koefisien
# x nilai yang di cari
# b hasil perhitungan
```
Cukup simpel jika mencari x pada aritmatika, Kita hanya perlu memindah ruaskan dan mengubah semisal dari perkalian menjadi pembagian, penjumlahan menjadi pengurangan dan begitupun sebaliknya. 

Sekarang pertanyaanya adalah bagaimana dengan modulus apakah sama? Apakah harus di balik juga? Jawabannya adalah jelas berbeda. Berikut rumus untuk mencari nilai x pada modulus:
```
a * x mod m = b maka x = b * a ^ -1 mod m

a * x = b maka x = b / a

Note :
# a koefisien
# x nilai yang di cari
# m nilai modulus
# b hasil perhitungan
```
Nahh.. Jadi alurnya berbeda dengan aritmatika dasar. Untuk mencari x tersebut kita perlu mengalikan b dengan invers dari a dan kemudian kita moduluskan lagi dengan m. Logikanya invers a itu sama saja dengan pembagian pada aljabar linear. 

Dan untuk mencari invers kita hanya perlu menggunakan function yang sudah di sediakan pada library *Crypto.Util.number*. Kemudian sesuai yang ada difile .txt. Setelah dapat x kita hanya perlu memoduluskannya dan mengubahnya menjadi karakter ascii. Untuk melihat program yang saya buat bisa kalian [klik disini](./srcModInv.py).