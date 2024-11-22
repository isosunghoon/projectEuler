_ = 2000000

chk = [True for i in range(0,_)]
chk[0],chk[1] = False, False

primes = []

for i in range(2,_):
    if not chk[i]: continue
    primes.append(i)
    for j in range(2*i,_,i):
        chk[j] = False

print(sum(primes))