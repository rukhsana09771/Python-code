s = "abcd"
print("Characters in forward direction:")
i = 0
while i<len(s):
    print(s[i])
    i += 1   

print("Characters in backward direction:")
j = len(s)-1
while j>=0:
    print(s[j])
    j -= 1 