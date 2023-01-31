import sys
from collections import defaultdict

n, m, k = map(int,sys.stdin.readline().split())

nums = [0]
for i in range(n):
    nums.append(int(input())) # [0, 1, 2, 3, 4, 5]
partial_sum = [0] * (n + 1) # [0, 0, 0, 0, 0, 0]
diff = defaultdict(int)

for i in range(1, n + 1): # [0, 1, 3, 6, 10, 15]
    partial_sum[i] = partial_sum[i-1] + nums[i]

for j in range(m + k):
    a, b, c = map(int,input().split())
    if a == 1:
        diff[b] = c - nums[b] # dictionary에 b index에서의 변동량 적기
    else:
        diff_b, diff_c = 0 , 0
        for k in diff.keys():
            if k <= b-1: 
                diff_b += diff[k]
            if k <= c: 
                diff_c += diff[k]
        print(partial_sum[c] + diff_c - partial_sum[b-1] - diff_b)