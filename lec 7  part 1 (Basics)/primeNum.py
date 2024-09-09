'''' a = int(input("Enter a no.: "))
count = 0
for i in range(1,a+1):
    if a%i==0:
        count += 1
if count==2: 
    print("Prime")
else:
    print("Not Prime")  
'''
# 2nd approach
a = int(input("Enter a no.: "))
count = 0
i = 1
while i<=a:
    if a%i==0:
        count += 1
    i += 1    
if count==2: 
    print("Prime")
else:
    print("Not Prime") 