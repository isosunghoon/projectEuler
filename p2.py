fibo = [1]
x = 2
while x<=4000000:
    fibo.append(x)
    x = fibo[-1]+fibo[-2]
print(sum([i for i in fibo if i%2==0]))