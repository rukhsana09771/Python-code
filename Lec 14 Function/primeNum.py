def prime(n, count):
    for i in range(1,n+1):
        if n%i==0:
            count += 1
    if count==2: 
        print("Prime")
    else:
        print("Not Prime")            

prime(7, 0)