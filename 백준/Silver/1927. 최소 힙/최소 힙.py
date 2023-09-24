# 최소 힙
from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    k = int(input())
    if not k:
        if q:
            print(heappop(q))
        else:
            print(0)
    else:
        heappush(q, k)
