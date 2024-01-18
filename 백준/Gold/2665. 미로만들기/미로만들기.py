import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
graph = [list(input()) for _ in range(N)]

q = []
visited = [[0] * N for _ in range(N)]
heapq.heappush(q, (0, 0, 0))

while q:
    cnt, x, y = heapq.heappop(q)
    if x == N - 1 and y == N - 1:
        print(cnt)
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if graph[nx][ny] == '1':
                heapq.heappush(q, (cnt, nx, ny))
            elif graph[nx][ny] == '0':
                heapq.heappush(q, (cnt + 1, nx, ny))
            visited[nx][ny] = 1