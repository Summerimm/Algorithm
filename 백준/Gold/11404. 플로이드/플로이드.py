n = int(input())
m = int(input())
INF = int(1e9)
cost = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 돌아오는 경우는 없으므로 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            cost[i][j]=0

# 노선이 여러 개일 경우 더 작은 값 저장
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(c, cost[a][b])

# 플로이드-워셜 알고리즘
for k in range(1, n+1):
    # k라운드 진행
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 직접 도착 or 경로 거치는 것 중 작은 것 갱신
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == INF:
            print('0', end=' ')
        else:
            print(cost[i][j], end=' ')
    print()