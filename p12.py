from sympy import factorint
n=1
while 1:
    f = factorint(n*(n+1)//2)
    x = 1
    for key, item in f.items():
        x*=item+1
    if x>=500:
        break
    n+=1
print(n*(n+1)//2)