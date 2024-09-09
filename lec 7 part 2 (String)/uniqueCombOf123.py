digits = [1,2,3]
count = 0
i = 0
while i<3:
    j = 0
    while j<3:
        k = 0
        while k<3:
            if i!=j and i!=k and j!=k:
                print(digits[i], digits[j], digits[k])
                count += 1
            k += 1
        j += 1
    i += 1                 
print("Total no. of permutaions are: ", count)       