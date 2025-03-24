# Memasukkan teks tersebut kedalam sebuah array kemudian di split/dipotong
# dan diubah menjadi integer
chiper = [int(n) for n in '3 8 9 16 5 18 12 1 14 7 11 1 8'.split()]

# selanjutnya angka angka tersebut satu persatu di jumlahkan dengan 64
# 65 pada ASCII adalah A, Seperti yang kita tahu 1 adalah A
# jadi jika 64 + 1 maka akan jadi A
flag = "".join(chr(x + 64) for x in chiper)

# output = CHIPERLANGKAH
print(flag)