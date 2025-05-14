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