digits = [1,2,3,4]
count = 0
i = 0
while i<4:
    j = 0
    while j<4:
        k = 0
        while k<4:
            m = 0
            while m<4:
                if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
                     print(digits[i], digits[j], digits[k], digits[m])
                     count += 1
                m += 1     
            k += 1
        j += 1
    i += 1       
print("Total no. of permutaions are: ", count)    
