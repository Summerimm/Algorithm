di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and graph[ni][nj] == graph[i][j]:
                q.append((ni, nj))
                visited[ni][nj] = 1

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=" ")

for i in range(N):
    for j in range(N):
        visited[i][j] = 0
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)