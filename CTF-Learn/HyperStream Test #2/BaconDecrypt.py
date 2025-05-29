def bacon_cipher(c):
    result = ''

    for b in c:
        if b == 'A':
            result += '0'
        else:
            result += '1'

    return ' '.join(result[i:i+5] for i in range(0,len(result),5))


flag = 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB'
alphabet = 'abcdefghiklmnopqrstuwxyz'

print(''.join(alphabet[int(b, 2)] for b in bacon_cipher(flag).split()))