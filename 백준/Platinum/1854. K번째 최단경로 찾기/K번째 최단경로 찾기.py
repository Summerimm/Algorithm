# K번째 최단경로 찾기
# dp를 2차원으로 k번째까지 존재
# k-1번째 값을 비교해주면 된다
# k가 2라고 가정하면 i번째 노드엔 초기값 INF, INF가 들어있다
# 처음에 i까지 가는 길이가 10이 나오면 INF, 10 으로 바뀌고
# 10 INF로 정렬 후 다음에 2가 들어오면 2, 10으로 바뀌게 된다

# 즉, 어떤 수가 들어와도 가장 작은 값이 0번째, 두 번째 작은 값이 1번째에 들어옴
# 그 다음 각 노드별로 k-1번째 값을 출력해주면 된다.

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):
    dp[start][0] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        cur_dist, node = heapq.heappop(queue)   # cur_dist: 1번부터 현재 노드까지의 거리, node: 현재 노드
        for ad_node, d in graph[node]:          # 현재 노드에 대한 인접 노드에 대해 모두 수행(다익스트라)
            # ad_node: 인접 노드, d: 현재노드부터 인접노드까지 거리
            next_dist = cur_dist + d            # next_dist 다음 노드까지의 거리: cur_dist + d
            if next_dist < dp[ad_node][K-1]:    # 모두 
                dp[ad_node][K-1] = next_dist
                dp[ad_node].sort()
                heapq.heappush(queue, [next_dist, ad_node])

V, E, K = map(int, input().split())     # V: 정점 개수, E: 간선 개수, K: k번째 최단 경로
graph = [[] for _ in range(V+1)]
dp = [[INF] * K for _ in range(V+1)]    # [INF, INF]처럼 개수 K만큼 계속해서 업데이트

# graph = [[], [[2, 2], [3, 7], [4, 5], [5, 6]], [[4, 2], [3, 4]], [[4, 6], [5, 8]], [], [[2, 4], [4, 1]]]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
dijkstra(1)

for i in range(1, V+1):
    if dp[i][K-1] == INF:
        print(-1)
    else:
        print(dp[i][K-1])
