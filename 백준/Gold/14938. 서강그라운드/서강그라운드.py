import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue
        
        for nxt_node, nxt_dist in graph[now]:
            cost = dist + nxt_dist
            if cost < distance[nxt_node]:
                distance[nxt_node] = cost
                heapq.heappush(q, (cost, nxt_node))

INF = int(1e9)

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

ans = 0
for i in range(1, n+1):
    cnt = 0
    distance = [INF] * (n+1)
    dijkstra(i)
    for j in range(1, n+1):
        if distance[j] <= m:
            cnt += items[j]
        ans = max(ans, cnt)
print(ans)