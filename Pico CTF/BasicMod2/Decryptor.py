flag = "104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42"
mod = [x for x in "abcdefghijklmnopqrstuvwxyz0123456789_"]
Decrypt = ""

for n in flag.split():
    index = pow(int(n), -1, 41) - 1
    Decrypt += mod[index]

print('picoCTF{'+ Decrypt + '}')
