N, M = map(int, input().split())
w = [0] + list(map(int, input().split()))
v = [0] + list(map(int, input().split()))
dp = [[0] * (sum(v)+1) for _ in range(N+1)]

# dp[i][j] -> i번째 앱까지 확인했을 때 j의 비용으로 얻을 수 있는 최대 메모리

for i in range(1, N+1):
    for j in range(sum(v)+1):
        if j - v[i] >= 0:   # 배낭 크기가 j이고 i번째 비용이 들어갈 수 있을 때
            dp[i][j] = max(dp[i][j], dp[i-1][j-v[i]] + w[i]) 
        dp[i][j] = max(dp[i][j], dp[i-1][j])    # 항상 비교(i번째 비용을 넣지 않았을 때)

for i in range(sum(v)+1):
    if dp[N][i] >= M:   # 마지막 행에서 처음으로 M이 넘은 순간의 배낭 용량이 최소가 됨
        print(i)
        break