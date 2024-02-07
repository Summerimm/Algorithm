from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if campus[nx][ny] == 'P':
                    cnt += 1
                    q.append((nx, ny))
                elif campus[nx][ny] != 'X':
                    q.append((nx, ny))
                visited[nx][ny] = 1
    return cnt

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            x, y = i, j
            visited[i][j] = 1
            break

ans = bfs(x, y)
if ans == 0:
    print("TT")
else:
    print(ans)