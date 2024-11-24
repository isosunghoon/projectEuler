import itertools
import numpy as np
#10은 반드시 외각에 있어야 한다
ans = 0
for comb in itertools.combinations([1,2,3,4,5,6,7,8,9], 4):
    # 외각에 comb가 존재하는게 가능한지 확인
    x = 110-(sum(comb)+10)
    if x%5:
        continue
    x //= 5
    #외각에 존재하는 애들 배치
    for perm in itertools.permutations(comb+(10,), 5):
        if perm[0] != min(perm): continue
        # 내부에 존재하는 애들 자동 결정
        A = np.array([
            [1,1,0,0,0],
            [0,1,1,0,0],
            [0,0,1,1,0],
            [0,0,0,1,1],
            [1,0,0,0,1]])
        B = np.array([x - i for i in perm])
        X = np.linalg.solve(A,B).astype('int')
        #valid 한지 check
        chk = True
        for i in range(1,10):
            if (i not in X) and (i not in perm):
                chk = False
                break
        if not chk: continue
        s = int(f'{perm[0]}{X[0]}{X[1]}{perm[1]}{X[1]}{X[2]}{perm[2]}{X[2]}{X[3]}{perm[3]}{X[3]}{X[4]}{perm[4]}{X[4]}{X[0]}')
        ans = max(s, ans)
print(ans)