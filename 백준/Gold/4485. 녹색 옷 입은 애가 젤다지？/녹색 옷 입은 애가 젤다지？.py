# 녹색 옷 입은 애가 젤다지?
from heapq import *

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dijkstra(r, c):
    q = []
    heappush(q, (cave[r][c], r, c))
    rupee[r][c] = cave[r][c]
    while q:
        rup, x, y = heappop(q)
        if rup > rupee[x][y]:
            continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                rup = rupee[x][y] + cave[nx][ny]
                if rup < rupee[nx][ny]:
                    rupee[nx][ny] = rup
                    heappush(q, (rup, nx, ny))

cnt = 0
while True:
    N = int(input())
    if not N:
        break
    else:
        cnt += 1
        cave = [list(map(int, input().split())) for _ in range(N)]
        rupee = [[1e9] * N for _ in range(N)]
        dijkstra(0, 0)
        print(f"Problem {cnt}:", rupee[N-1][N-1])