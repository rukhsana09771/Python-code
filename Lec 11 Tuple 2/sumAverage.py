t = eval(input("Enter Tuple: "))
sum = 0
count = 0
for i in t:
    sum += i
    count += 1
print("Sum: ", sum)
avg = sum/count
print("Avg: ", avg)    