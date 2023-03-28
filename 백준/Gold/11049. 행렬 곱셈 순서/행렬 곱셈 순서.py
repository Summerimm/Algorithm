INF = 2 ** 31
N = int(input())
dp = [[0] * N for _ in range(N)]
row = [0] * N
col = [0] * N

for i in range(N):
    r, c = map(int, input().split())
    row[i] = r
    col[i] = c

for cnt in range(1, N): # cnt: 볼 행렬의 개수 -> 를 늘려가야함
    for i in range(N):  # i: 시작 행렬의 인덱스
        j = i + cnt     # j: 마지막 행렬의 인덱스
        if j >= N:
            break
        tmp = INF
        for k in range(i, j):   # k: 자르는 지점의 인덱스
            tmp = min(tmp, dp[i][k] + dp[k+1][j] + row[i] * col[k] * col[j])
        dp[i][j] = tmp

print(dp[0][N-1])