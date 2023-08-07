# 국회의원 선거

from heapq import *

N = int(input())
dasom = int(input())

if N == 1:
    print(0)
    exit()

q = []
for _ in range(N-1):
    tmp = int(input())
    heappush(q, [-tmp, tmp])

ans = 0
while (q[0][1] >= dasom):
    dasom += 1
    ans += 1
    q[0][0] += 1
    q[0][1] -= 1
    heapify(q)

print(ans)