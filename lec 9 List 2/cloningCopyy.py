x = [10, 20, 30, 40]
y = x.copy()
print(id(x))
print(id(y))
y[1] = 100
print(x)
print(y)