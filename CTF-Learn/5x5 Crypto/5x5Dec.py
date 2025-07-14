import string

enc = '1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}'.replace('-', '').split(',')
alpha = string.ascii_lowercase.replace('k', '')
table = [list(alpha[i:i+5]) for i in range(0, len(alpha), 5)]
flag = ''

for e in enc:
    if len(e) == 2: 
        x, y = list(e)
        flag += table[int(x)-1][int(y)-1]
    else:
        flag += e

print(flag)