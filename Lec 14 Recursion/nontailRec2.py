def non_tail_rec(n):
    if(n<=1):
        return
    else:
        print(n-3)
        non_tail_rec(n-1)
        print(n-1)
        non_tail_rec(n-2)
        print(n)
        non_tail_rec(n-3)
        print(n-2)
non_tail_rec(5)