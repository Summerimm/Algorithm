N, K = map(int, input().split())
tmp1 = 1
tmp2 = 1
for _ in range(K):
    tmp1 *= N
    N -= 1

for _ in range(K):
    tmp2 *= K
    K -= 1

print(tmp1 // tmp2)