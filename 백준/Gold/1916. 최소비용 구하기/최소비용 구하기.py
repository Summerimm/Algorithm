# 최소비용 구하기
import sys
input = sys.stdin.readline

import heapq

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0
    while q:
        d, node = q.pop(0)
        if d > distance[node]:
            continue
        for nextnode, nextcost in graph[node]:
            cost = distance[node] + nextcost
            if cost < distance[nextnode]:
                distance[nextnode] = cost
                heapq.heappush(q, (cost, nextnode))

N = int(input())
M = int(input())

INF = 1e9
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

s, e = map(int, input().split())
dijkstra(s)
print(distance[e])
