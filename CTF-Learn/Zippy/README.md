# Zippy - CTFlearn
[auto-zip-cracker.sh](./auto-zip-cracker.sh) merupakan tools pengotomatisan yang saya gunakan untuk penyelesaian challange CTF Zippy. Algoritmanya sebagai berikut:
1. Melakukan perulangan sampai 13(karena total file zipnya 13);
2. Gerbang logika jika iterasinya lt(lessthan/kurang dari) 10 maka ada penambahan 0;
3. Jika lebih maka sesuaikan dengan nilai iterasi;
4. Penggunaan grep untuk memastikan yang diambil hanyalah di dalam tanda petik 1;
5. Penggunaan tr -d "/n" untuk menghapus enter
6. Hasil output nantinya akan di munculkan pada file hash crack.txt