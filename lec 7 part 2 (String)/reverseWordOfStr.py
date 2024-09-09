s = "Learning Python is very Easy"
sp = s.split()
revStr = ""
l = len(sp) - 1
while l>=0:
    revStr = revStr + sp[l] + " "
    l -= 1
print(revStr)