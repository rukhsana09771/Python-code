x = 0
for i in range(2,5):
    for j in range(1,i):
        x += j
        if x%3==0:
            x -= i
print(x)            