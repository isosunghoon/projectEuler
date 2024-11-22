for a in range(1,501):
    for b in range(a,1001-a):
        if (a**2+b**2)==(1000-a-b)**2:
            print(a,b,1000-a-b,a*b*(1000-a-b))