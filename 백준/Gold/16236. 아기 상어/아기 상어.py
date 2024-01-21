from collections import deque

def bfs(shark_x, shark_y, shark_size):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((shark_x, shark_y))
    cand = []

    visited[shark_x][shark_y] = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if 1 <= graph[nx][ny] < shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
                elif graph[nx][ny] == shark_size or graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x = i
            shark_y = j
            shark_time = 0
            shark_size = 2
            shark_eatcnt = 0

while True:
    # 0. 후보군
    cand = deque(bfs(shark_x, shark_y, shark_size))

    # 1. 먹을 수 있는 물고기가 없을 경우, break
    if not cand:
        break
    
    # 2. 가장 짧은 거리로 먹을 수 있는 물고기까지 닿는 거리, 위치 저장
    dist, fish_x, fish_y = cand.popleft()

    # 3. 상어 위치를 물고기 위치로 바꾸고 eatcnt++, time++
    shark_time += dist
    shark_eatcnt += 1

    # 3-1. 상어가 잡아먹은 물고기 수가 크기와 같아지면 size++
    if shark_size == shark_eatcnt:
        shark_size += 1
        shark_eatcnt = 0

    # 3-2. 상어 원래 위치는 0으로, 상어 위치 변경, graph 수정
    graph[shark_x][shark_y] = 0
    shark_x, shark_y = fish_x, fish_y
    graph[shark_x][shark_y] = shark_size

print(shark_time)