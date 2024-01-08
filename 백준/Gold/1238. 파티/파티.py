import heapq

def dijkstra(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[start][now] < dist:    # 이미 입력되어 있는 값이 현재 노드까지의 거리보다 작다면 이미 방문한 노드
            continue
        
        for nxt_node, nxt_dist in graph[now]:  # 연결된 모든 노드 탐색
            if dist + nxt_dist < distance[start][nxt_node]:    # 기존에 입력되어 있는 값보다 크다면
                distance[start][nxt_node] = dist + nxt_dist    # 갱신
                heapq.heappush(q, (dist + nxt_dist, nxt_node))

N, M, X = map(int, input().split())     # 노드 수, 간선 수, 모임장소

INF = 1e9

graph = [[] for _ in range(N+1)]    # 간선 및 가중치 정보 기입
distance = [[INF] * (N+1) for _ in range(N+1)]  # 최단 거리

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

for i in range(1, N+1):
    dijkstra(graph, i)

ans = 0
for i in range(1, N+1):
    ans = max(ans, distance[i][X] + distance[X][i])
print(ans)