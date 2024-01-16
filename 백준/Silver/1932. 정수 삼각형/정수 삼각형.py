N = int(input())
dp = [[] for _ in range(N)]
for i in range(N):
    a = [0] + list(map(int, input().split())) + [0]
    dp[i] = a

for i in range(N-1):
    for j in range(1, i+3):
        dp[i+1][j] += max(dp[i][j-1], dp[i][j])
print(max(dp[-1]))