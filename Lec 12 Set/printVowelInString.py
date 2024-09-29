w = input("Enter any string: ")
s = set(w)
v = {'a', 'e', 'i', 'o', 'u'}
d = s.intersection(v)
print("Vowels present in string: ", d)