a = int(input("Enter 1st no.: "))
b = int(input("Enter 2nd no.: "))
c = int(input("Enter 3rd no.: "))
d = int(input("Enter 4th no.: "))
min = a if (a<b and a<c and a<d)  else(b if (b<c and b<d) else(c if c<d else d))
print("minmum value: ", min)