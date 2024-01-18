import heapq

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

M, N = map(int, input().split())
graph = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

q = []
heapq.heappush(q, (0, 0, 0))

while q:
    cnt, x, y = heapq.heappop(q)
    if x == N - 1 and y == M - 1:
        print(cnt)
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if graph[nx][ny] == '0':
                heapq.heappush(q, (cnt, nx, ny))
            elif graph[nx][ny] == '1':
                heapq.heappush(q, (cnt + 1, nx, ny))
            visited[nx][ny] = 1