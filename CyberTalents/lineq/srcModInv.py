from Crypto.Util.number import inverse, GCD

flag = ''

with open('./CyberTalents/lineq/lineq.txt', 'r') as file:
    for line in file:
        data = line.strip().split()

        a = int(data[0])
        m = int(data[4])
        b = int(data[6])
        x = b * inverse(a, m) % m

        flag += chr(x % 256)

print(flag)