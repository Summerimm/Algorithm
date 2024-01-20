def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        for j in range(2 * M + W):
            now = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            if distance[nxt] > distance[now] + cost:
                distance[nxt] = distance[now] + cost
                if i == N - 1:
                    return True
    return False

INF = int(1e9)
T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []
    distance = [INF] * (N+1)

    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    negative_cycle = bellman_ford(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")