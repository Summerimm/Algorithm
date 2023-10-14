N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N):
    for j in range(i + arr[i][0], N+1):
        dp[j] = max(dp[j], dp[i] + arr[i][1])

print(dp[-1])
