from collections import deque

N, K = map(int, input().split())
mx = max(N, K)
INF = 1e9
arr = [INF] * (2 * mx + 1)
arr[N] = 0
q = deque()
q.append(N)
while q:
    cx = q.popleft()
    for i in range(3):
        if i == 0:
            nx = cx - 1
        elif i == 1:
            nx = cx + 1
        else:
            nx = cx * 2
        if 0 <= nx <= 2 * mx and arr[nx] > arr[cx] + 1:
            arr[nx] = arr[cx] + 1
            q.append(nx)
print(arr[K])