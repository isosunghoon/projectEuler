colatz = [0 for i in range (1000001)]
colatz[1] = 1
for i in range(2, 1000001):
    t = i
    while t!=1:
        colatz[i]+=1
        if t%2==0:
            t = t//2
        else:
            t = t*3+1
        if t<=1000000 and colatz[t]!=0:
            colatz[i]+=colatz[t]
            break

import numpy as np
print(np.argmax(np.array(colatz)))