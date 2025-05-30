from base64 import b64decode
import string

b64fill = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
"""Variable untuk meneyimpan karakter base64 yang nantinya\n
berfungsi untuk mengisi kekurangan pada teks yang hilang"""

for corupt in b64fill: 
    for corupt2 in b64fill: 
        # Mencoba semua kemungkinan karakter
        result = b64decode(f'R{corupt}{corupt2}BR3tCNDUzXzYxWDdZXzRSfQ==')
        if result[:4] == b'FLAG':
            # Menghentikan program jika terdapat hasil yang di harapkan
            print(result)
            break
