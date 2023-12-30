from collections import deque

V = int(input())
E = int(input())
ans = 0

adjM = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    adjM[a].append(b)
    adjM[b].append(a)

visited = [0] * (V+1)
visited[1] = 1
q = deque()
q.append(1)
while q:
    target = q.popleft()
    for k in adjM[target]:
        if visited[k] == 0:
            ans += 1
            visited[k] = 1
            q.append(k)
print(ans)