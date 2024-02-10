from itertools import combinations

T = int(input())
for _ in range(T):
    dct = {}
    N = int(input())
    for i in range(N):
        a, b = map(str, input().split())
        if b not in dct.keys():
            dct[b] = 1
        else:
            dct[b] += 1
    
    ans = 1
    for k in dct.keys():
        ans *= dct[k] + 1
    print(ans - 1)