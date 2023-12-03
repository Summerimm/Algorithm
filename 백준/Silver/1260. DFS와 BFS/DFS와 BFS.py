def dfs(n):
    visited[n] = 1
    print(n, end=" ")
    for nxt in adjM[n]:
        if visited[nxt] == 0:
            dfs(nxt)

def bfs(n):
    q = []
    q.append(n)
    visited[n] = 1
    while q:
        t = q.pop(0)
        print(t, end=" ")
        for nxt in adjM[t]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)

V, E, S = map(int, input().split())
adjM = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    adjM[a].append(b)
    adjM[b].append(a)

for i in range(1, V+1):
    adjM[i].sort()

visited = [0] * (V+1)
dfs(S)
print()

visited = [0] * (V+1)
bfs(S)
print()
