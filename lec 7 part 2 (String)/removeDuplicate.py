s = "abcdabbcdabbbcccddeeef"
ans = []
for char in s:
    if char not in ans:
        ans.append(char)
res = ' '.join(ans)
print("String after removing duplicate: ", res)               