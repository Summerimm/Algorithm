import sys
from collections import defaultdict

T = int(input()) # 5
n = int(input()) # 4
A = list(map(int, input().split())) # [1, 3, 1, 2]
m = int(input()) # 3
B = list(map(int, input().split())) # [1, 3, 2]

ans = 0
A_dict = defaultdict(int)

for i in range(n): # 0 ~ 3
    for j in range(i, n):
        A_dict[sum(A[i:j+1])] += 1 # 같은 합의 가짓수 + 1
        # {1: 2, 4: 2, 5: 1, 7: 1, 3: 2, 6: 1, 2: 1}

for i in range(m): # 0 ~ 2
    for j in range(i, m):
        ans += A_dict[T - sum(B[i:j+1])] # 5에서 B의 합 뺀 값이 A에 얼마나 들어있는지 

print(ans)