x = [10,20,30,40,50]
ba = bytearray(x)
ba[1] = 100
for i in ba:
    print(i)