# 타임머신
import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    dist[start] = 0
    for i in range(V):  # v-1만큼 돌리고 v번째에도 dist값이 갱신된다면 무한루프가 존재하는 것
        # 모든 간선 확인
        for j in range(E):
            cur = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            # 직접 가는 비용 > 거쳐서 가는 비용
            if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                # V번째에서도 갱신되는 경우 -> 무한루프(음수) 존재
                if i == V - 1:
                    return True
    return False

V, E = map(int, input().split())
edges = []
dist = [INF] * (V + 1)

for _ in range(E):
    s, e, t = map(int, input().split())
    edges.append((s, e, t))

neg_cycle = bellman_ford(1)

# 음수 순환 존재 시 -1
if neg_cycle:
    print('-1')
else:
    for i in range(2, V+1):
        # 도달 불가능 -1
        if dist[i] == INF:
            print('-1')
        # 도달 가능 거리 출력
        else:
            print(dist[i])