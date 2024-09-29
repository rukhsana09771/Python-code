l = [12, 10, 35, 15, 5]
t = len(l)
mn = l[0]

for i in l:
    if i < mn:
        mn = i
print("Minimum: ", mn)

# Find the GCD
for i in range(mn, 0, -1):
    count = 0  
    for j in l:
        if j % i == 0:
            count += 1
    if count == t:  
        print("GCD: ", i)
        break
