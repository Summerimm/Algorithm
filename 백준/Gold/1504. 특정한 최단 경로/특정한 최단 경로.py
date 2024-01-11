import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for nxt_node, nxt_dist in graph[now]:
            cost = dist + nxt_dist
            if cost < distance[nxt_node]:
                distance[nxt_node] = cost
                heapq.heappush(q, (cost, nxt_node))

INF = int(1e9)
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 두 가지 케이스 
# 1 - v1 - v2 - N
# 1 - v2 - v1 - N

# 1-v1, 1-v2 저장
distance = [INF] * (N+1)
dijkstra(1)
path1 = distance[v1]
path2 = distance[v2]

# v1-v2, v1-N 저장
distance = [INF] * (N+1)
dijkstra(v1)
path1 += distance[v2]
path2 += distance[N]

# v2-N, v2-v1 저장
distance = [INF] * (N+1)
dijkstra(v2)
path1 += distance[N]
path2 += distance[v1]

ans = min(path1, path2)
if ans >= INF:
    print(-1)
else:
    print(ans)