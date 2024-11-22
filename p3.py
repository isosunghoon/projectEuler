n = 600851475143
mem = n
for i in range(2,775146):
    while n%i==0:
        mem = n
        n//=i
print(mem)