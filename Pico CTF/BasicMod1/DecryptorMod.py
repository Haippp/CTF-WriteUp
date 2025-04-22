flag = "350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213 "
karSet = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"]
decrypt = "".join(karSet[int(n) % 37] for n in flag.split())
print('picoCTF{' + decrypt + '}')