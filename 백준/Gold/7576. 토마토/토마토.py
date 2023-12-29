from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(q):
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if  0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[cx][cy] + 1
                q.append((nx, ny))

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            q.append((i, j))

bfs(q)

ans = 0
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 0:
            print(-1)
            exit()
        elif tomatos[i][j] > ans:
            ans = tomatos[i][j]
print(ans - 1)
