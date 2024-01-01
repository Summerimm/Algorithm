from collections import deque

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 0, 1, 0]
dy = [0, 0, 0, 1, 0, -1]
def bfs(q):
    while q:
        cz, cx, cy = q.popleft()
        for k in range(6):
            nz, nx, ny = cz + dz[k], cx + dx[k] , cy + dy[k]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomatos[nz][nx][ny] == 0:
                tomatos[nz][nx][ny] = tomatos[cz][cx][cy] + 1
                q.append((nz, nx, ny))

M, N, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 1:
                q.append((i, j, k))

bfs(q)

ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 0:
                print(-1)
                exit()
            elif tomatos[i][j][k] > ans:
                ans = tomatos[i][j][k]
print(ans - 1)