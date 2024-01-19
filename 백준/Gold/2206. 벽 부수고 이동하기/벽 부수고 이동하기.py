import heapq

INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
visited = [[[INF, INF] for _ in range(M)] for _ in range(N)]

if N == 1 and M == 1:
    print(1)
    exit()

q = []
heapq.heappush(q, (1, 0, 0, 0))
flag = 1
while q:
    dist, wall, x, y = heapq.heappop(q)
    if x == N - 1 and y == M - 1:
        print(min(visited[-1][-1]))
        flag = 0
        break

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        nxt_dist = dist + 1
        if 0 <= nx < N and 0 <= ny < M:
            # 이동 좌표가 벽이 아닐 떄
            if graph[nx][ny] == '0':
                # 현재까지 벽을 0개 부셨고 이동 시 더 최소 거리일 경우
                if wall == 0 and visited[nx][ny][0] > nxt_dist:
                    visited[nx][ny][0] = nxt_dist
                    heapq.heappush(q, (nxt_dist, 0, nx, ny))
                # 현재까지 벽을 1개 부셨고 이동 시 더 최소 거리일 경우
                elif wall == 1 and visited[nx][ny][1] > nxt_dist:
                    visited[nx][ny][1] = nxt_dist
                    heapq.heappush(q, (nxt_dist, 1, nx, ny))
            # 이동 좌표가 벽일 떄
            else:
                # 현재까지 벽을 0개 부셨고 이동 시 더 최소 거리일 경우
                if wall == 0 and visited[nx][ny][1] > nxt_dist:
                    visited[nx][ny][1] = nxt_dist
                    heapq.heappush(q, (nxt_dist, 1, nx, ny))

if flag:
    print(-1)