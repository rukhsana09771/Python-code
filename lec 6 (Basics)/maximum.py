a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
c = int(input("Enter 3rd no.: "))
if a>b and a>c:
    print("Maximum is: ", a)
elif b>c:
    print("Maximum is: ", b)  
else:
    print("Maximum is: ", c)    