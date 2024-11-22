def gcd(a,b):
    if a>b:
        a,b = b,a
    if b%a==0:
        return a
    else:
        return gcd(b%a,a)

def lcm(a,b):
    return (a*b)//gcd(a,b)


ans = 1
for i in range(1,20):
    ans = lcm(ans, i)
print(ans)