n1 = [10,20,30,40]
n2 = [30,40,50,60]
n3 = [i for i in n1 if i not in n2]
print(n3)

n4 = [i for i in n1 if i in n2]
print(n4)