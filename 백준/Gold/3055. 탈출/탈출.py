from collections import deque

# 시간이 지남에 따라서 S는 .을 S로 바꾸고(고슴도치가 지나온 길)
# *가 갈 수 있는 모든 길은 .을 *로 바꾸기(물이 넘친 길)
# S는 *이나 X를 못 지나감
# S의 최단 경로 구하기(BFS)

n, m = map(int, input().split()) # n은 행, m은 열
graph = [list(input()) for i in range(n)] # 
distance = [[0] * m for i in range(n)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 큐 구현을 위해 deque 사용
queue = deque()


# BFS
def bfs(Dx, Dy):
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # Destination x와 y의 값이 S로 바뀌었을 때, 즉 비버의 집에 고슴도치가 도착했을 때
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나지 않은 경우만 
            if 0 <= nx < n and 0 <= ny < m:
                # 현재 고슴도치의 위치이고, 이동하려는 위치가 '.', 'D'일 경우 'S'로 바꿈
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1 # 거리 그래프 + 1
                    queue.append((nx, ny)) # 다음 위치 큐에 넣기
                # 현재 물의 위치이고, 이동하려는 위치가 '.', 'S'일 경우 '*'로 바꿈
                elif (graph[nx][ny] =='.' or graph[nx][ny] =='S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    queue.append((nx,ny))
    return "KAKTUS"

for x in range(n):
    for y in range(m):
        if graph[x][y] == 'S':
            queue.append((x, y)) # 고슴도치의 위치
        elif graph[x][y] == 'D':
            Dx, Dy = x, y # destination x, y

for x in range(n):
    for y in range(m):
        if graph[x][y] == '*':
            queue.append((x, y)) # 물의 위치

print(bfs(Dx, Dy))