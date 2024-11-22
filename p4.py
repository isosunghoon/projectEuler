def rev(n):
    arr = []
    while n>0:
        arr.append(n%10)
        n//=10
    x = sum([arr[i]*(10**(len(arr)-1-i)) for i in range(len(arr))])
    return x

ans = 0

for i in range(100,1000):
    for j in range(100,1000):
        n = i*j
        if n==rev(n):
            ans = max(ans,n)

print(ans)