N = int(input())
INF = int(1e9)

# 해당 노드로 가는 경로가 없다면 INF로 초기화
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            graph[i][j] = 0
        else:
            graph[i][j] = 1

for i in range(N):
    print(*graph[i])