dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = []
    q.append((x, y))
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m and ans[nx][ny] == -1 and board[nx][ny] == 1:
                q.append((nx, ny))
                ans[nx][ny] = ans[cx][cy] + 1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 입력지도
ans = [[-1] * m for _ in range(n)]  # 정답판, 디폴트는 -1
for i in range(n):
    for j in range(m):
        # 지도에서 2이면 출발점 저장, 정답판에 0으로 변경
        if board[i][j] == 2:
            ans[i][j] = 0
            r, c = i, j
        # 지도에서 0이면 정답판에도 0으로 변경
        elif board[i][j] == 0:
            ans[i][j] = 0

bfs(r, c)
for i in range(n):
    print(*ans[i])
