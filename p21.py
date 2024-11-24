from sympy import factorint
li = [0 for i in range(10001)]

for i in range(1,10001):
    f = factorint(i)
    x = 1
    for key, value in f.items():
        x *= (key**(value+1)-1)//(key-1)
    li[i] = x - i

ans = []
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if i==li[j] and li[i]==j and i!=j:
            ans.append((i, j))
print(sum([i[0]+i[1] for i in ans]))