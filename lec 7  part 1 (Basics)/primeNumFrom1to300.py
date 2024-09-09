''' a = int(input("Enter a no.: "))
count = 0
for i in range(2,a+1):
    c = 0
    for j in range(1,i+1):
        if i%j==0:
            c += 1
    if c==2: 
      print(i)
      count += 1
print("Total prime no. is: ", count)  
'''

# using while loop
a = int(input("Enter a no.: "))
c = 0
j = 1
while j<=a:
    i = 1
    count = 0
    while i<=j:
        if j%i==0:
            count += 1
        i += 1 
    if count==2: 
        print(j)
        c += 1
    j += 1    
print("Total prime no. is: ",c)