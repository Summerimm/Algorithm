T = int(input())

arr = []
for _ in range(T):
    n = int(input())
    arr.append(n)

mx = max(arr)
dp = [0] * (mx + 1)
dp[1], dp[2], dp[3] = 1, 2, 3
for i in range(4, mx + 1):
    dp[i] = dp[i-1] + (dp[i-2] - dp[i-3])
    if i % 3 == 0:
        dp[i] += 1

for k in arr:
    print(dp[k])