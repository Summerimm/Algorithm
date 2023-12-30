from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        c = q.popleft()
        for k in adjL[c]:
            if not visited[k]:
                visited[k] = 1
                q.append(k)

N, M = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        bfs(i)
        ans += 1
print(ans)