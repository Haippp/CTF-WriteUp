from pwn import *
from Crypto.Util.number import long_to_bytes

password = 1765037049764047724348114634473658734830490852066061345686916365658618194981097216750929421734812911680434647401939068526285652985802740837961814227312100

koneksi = remote('titan.picoctf.net', 51492)
# #send line after berfungsi untuk mengirimkan teks setelah teks tertentu
koneksi.sendlineafter(b'decrypt.', b'E')
# Setelah milih menunya, kita ketikkan bytes \x02\
koneksi.sendlineafter(b': ', b'\x02')
# Mengambil data sampai pola tertentu. dan di sini saya hanya ingin mengambil data sampai 'mod n)' aja
# simplenya dari input teks sampai pola teks 'mod n)'
koneksi.recvuntil(b'mod n)')
# mengambil hasil enkripsi yang setelah 'mod n)'
hasil_enkripsi = int(koneksi.recvline().strip().decode())

koneksi.sendlineafter(b'decrypt.', b'D')
koneksi.sendlineafter(b': ', str(password * hasil_enkripsi).encode())
koneksi.recvuntil(b'mod n): ')
hasil_dekripsi = int(koneksi.recvline().strip().decode(), 16)//2

pw = long_to_bytes(hasil_dekripsi)
print(pw)