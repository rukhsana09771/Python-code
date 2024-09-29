t = [1,-2,3,-3,5,-5,5,6,-7,7]
pos = []
neg = []
for i in t:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)    
print("Positive num: ", pos)
print("Negative num: ", neg)