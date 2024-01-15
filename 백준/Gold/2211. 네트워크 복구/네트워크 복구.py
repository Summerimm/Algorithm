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
                prev[nxt_node] = now
                distance[nxt_node] = cost
                heapq.heappush(q, (cost, nxt_node))

INF = int(1e9)
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
prev = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)
print(N + 1 - prev.count(0))
for i in range(2, N+1):
    if prev[i] != 0:
        print(i, prev[i])