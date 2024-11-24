def fac(n):
    if n==0 or n==1:
        return 1
    else: return n*fac(n-1)

print(sum([int(i) for i in str(fac(100))]))