import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
# --------------------------------------

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
                prev_node[nxt_node] = now
                heapq.heappush(q, (cost, nxt_node))

n = int(input().rstrip())    # 노드의 수
m = int(input().rstrip())    # 간선의 수

INF = int(1e9)

graph = defaultdict(list)
distance = [INF] * (n+1)
prev_node = [0] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))
start, end = map(int, input().rstrip().split())

dijkstra(start)

k = end
ans = [end]
while k != start:
    k = prev_node[k]
    ans.append(k)
ans.reverse()

print(distance[end])
print(len(ans))
print(' '.join(map(str, ans)))