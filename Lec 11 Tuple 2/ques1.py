x = 2
y = 3
count = 0
while x<y:
    x += 1
    y -= 1
    count += x+y
    if x*y<=6:
        break
print(count)    