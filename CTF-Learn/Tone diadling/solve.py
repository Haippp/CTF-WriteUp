def ordFormat(N):
    arr = []
    temp = ''
    for x in N:
        temp +=  x
        if int(temp[0]) > 2 and len(temp) >= 2:
            arr.append(int(temp))
            temp = ''
        elif int(temp[0]) <= 2 and len(temp) == 3:
            arr.append(int(temp))
            temp = ''
    print(arr)
    return bytes(arr).decode()
    
N = '67847010810197110123678289808479718265807289125'
print(ordFormat(N))