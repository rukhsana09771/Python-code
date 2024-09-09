s = input("Enter a string: ")
revStr = ""
l = len(s) - 1
while l>=0:
    revStr += s[l]
    l -= 1
print(revStr)     