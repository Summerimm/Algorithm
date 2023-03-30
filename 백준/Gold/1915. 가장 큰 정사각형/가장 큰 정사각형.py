n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

# 오른쪽 아래 꼭짓점의 값이 그 정사각형에서 만들 수 있는 최대 크기
mx = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = int(arr[i][j])
        elif arr[i][j] == '0':
            dp[i][j] = 0
        else:
            dp[i][j] = min(int(dp[i-1][j-1]), int(dp[i-1][j]), int(dp[i][j-1])) + 1
    mx = max(mx, max(dp[i]))    # 그 열에서의 최대 정사각형 크기와 현재 최댓값 비교해서 갱신

print(mx**2)