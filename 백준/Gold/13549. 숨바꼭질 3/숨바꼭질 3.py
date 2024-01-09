import heapq

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

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
N, K = map(int, input().split())
mx = max(N, K)
graph = [[] for _ in range(4 * mx + 1)]
distance = [INF] * (4 * mx + 1)

graph[0].append((1, 1))
graph[1].append((0, 1))
graph[1].append((2, 0))
for i in range(2, 2 * mx + 1):
    graph[i].append((i-1, 1))
    graph[i].append((i+1, 1))
    graph[i].append((2 * i, 0))

dijkstra(N)
print(distance[K])