def pac(n):
    if n==0 or n==1:
        return 1
    else: return n*pac(n-1)

print(pac(40)//pac(20)//pac(20))