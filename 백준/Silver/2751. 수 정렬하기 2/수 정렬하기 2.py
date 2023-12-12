import sys
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    q.append(int(input()))

q.sort()
for i in range(N):
    print(q[i])