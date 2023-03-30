str1 = [''] + list(input())
str2 = [''] + list(input())
n, m = len(str1), len(str2)
dp = [[''] * m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if str1[i] == str2[j]:    # 문자열 같은 곳 발견 시
            dp[i][j] = dp[i-1][j-1] + str1[i]    # 대각 문자열 받아와서 더하기
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]): # 같을 땐 i-1 보내야 함
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                
print(len(dp[n-1][m-1]))
print(dp[n-1][m-1])