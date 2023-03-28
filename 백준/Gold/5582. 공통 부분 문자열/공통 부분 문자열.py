string = input()
target = input()
s, t = len(string), len(target)
dp = [[0] * (s+1) for _ in range(t+1)]

mx = 0
for i in range(1, t+1):
    for j in range(1, s+1):
        if target[i-1] == string[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            mx = max(mx, dp[i][j])

print(mx)