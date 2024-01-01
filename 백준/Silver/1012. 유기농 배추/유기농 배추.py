dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(r, c):
    q = []
    q.append((r, c))
    while q:
        cx, cy = q.pop(0)
        for k in range(4):
            nx, ny = cx + dx[k] , cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                farm[nx][ny] = 2
                q.append((nx, ny))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                farm[i][j] = 2
                ans += 1
                bfs(i, j)
    print(ans)