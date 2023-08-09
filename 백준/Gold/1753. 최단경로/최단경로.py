# 최단 경로
import sys
import heapq
input = sys.stdin.readline

def dijkstra(x):
    q = []
    # (cost, node)
    heapq.heappush(q, (0, x)) # initial condition
    distance[x] = 0 # initial condition
    while q:
        d, node = heapq.heappop(q)
        if d > distance[node]: # 뽑아낸 거리가 기존에 있던 거리보다 클 때
            continue
        for adj in graph[node]: # 인접 노드
            cost = distance[node] + adj[1] # 시작 -> 현재 노드 + 현재 노드 -> 인접 노드
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))

V, E = map(int, input().split())
K = int(input())

INF = 1e9
distance = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    # (node, cost)
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
