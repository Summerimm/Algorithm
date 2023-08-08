# 영역 구하기

def bfs(si, sj):
    q = []
    q.append((si, sj))
    arr[si][sj] = 1
    ans = 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<M and 0<=nj<N and not arr[ni][nj]:
                q.append((ni, nj))
                arr[ni][nj] = 1
                ans += 1
    return ans


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            arr[i][j] = 1

ans = []
cnt = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            area = bfs(i, j)
            ans.append(area)
            cnt += 1

ans.sort()
print(cnt)
print(*ans)