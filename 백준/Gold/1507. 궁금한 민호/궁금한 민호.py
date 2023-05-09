# 궁금한 영서

N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
way = [[1] * N for _ in range(N)]
ans = 0

for k in range(N):
    for a in range(N):
        for b  in range(N):
            if a == b or b == k or k == a:
                continue
            if dist[a][b] == dist[a][k] + dist[k][b]:
                way[a][b] = 0
            elif dist[a][b] > dist[a][k] + dist[k][b]:
                ans = -1
if ans != -1:
    for i in range(N):
        for j in range(i, N):
            if way[i][j]:
                ans += dist[i][j]

print(ans)