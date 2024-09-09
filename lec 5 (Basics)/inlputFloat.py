''' WAP to read 3 float no. from the keyboard & print their sum. '''

a,b,c = [float(x) for x in input("Enter any three float numbers: ").split()]
print("Sum of three float no. is: ", a+b+c)