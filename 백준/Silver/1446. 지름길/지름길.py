import heapq

INF = int(1e9)

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))   # (거리, 현재 위치)
    distance[x] = 0    # 시작위치 거리는 미리 초기화
    while q:
        dist, now = heapq.heappop(q)    # graph 기반의 (현재 위치까지 소요 거리, 현재 위치)
        
        # 정답 보드에 쓰여진 거리 값보다 graph 기반의 소요거리가 더 클 때는 패스
        if dist > distance[now]:
            continue
				# 현재 위치와 연결된 지름길 정보 (도착 지점, 소요 거리) 중에서
        for adjnode, adjcost in graph[now]:
            cost = dist + adjcost    # 현재 위치까지 소요거리 + 다음 지점까지 거리
            if cost < distance[adjnode]:    # 정답 보드 업데이트 가능하면
                distance[adjnode] = cost    # 업데이트 후
                heapq.heappush(q, (cost, adjnode))    # 해당 지점 기준으로 큐 넣기

N, D = map(int, input().split())    # 지름길 개수, 고속도로 길이
graph = [[] for _ in range(D+1)]    # 지름길 정보 기입
distance = [INF] * (D+1)    # 최소거리 정답 보드

# 거리 1로 초기화
for i in range(D):
    graph[i].append((i+1, 1))   # (도착지점, 거리)

# 지름길 있는 경우 업데이트
for _ in range(N):
    s, e, length = map(int, input().split())
    if e > D:
        continue
    graph[s].append((e, length))    # (도착지점, 거리) 정보 추가

dijkstra(0)    # 0부터 시작
print(distance[D])    # 마지막 지점에 적힌 최소거리