N = int(input())
nums = list(map(int, input().split()))
goal = nums[-1]     # 타겟 숫자

dp = [[0] * 21 for _ in range(N-1)]
dp[0][nums[0]] = 1          # 초기값 8에 경우의 수 1넣기


for i in range(1, N-1):     # nums 순서대로 돌면서
    for j in range(21):     # dp배열 확인해서
        if dp[i-1][j]:      # 해당 숫자가 나오는 경우가 존재하면
            tmp1 = j + nums[i]      # 현재 숫자를 더한 값
            tmp2 = j - nums[i]      # 현재 숫자를 뺀 값
            if 0<= tmp1 <= 20:      # 0~20 사이면
                dp[i][tmp1] += dp[i-1][j]    # 해당 인덱스에서 tmp1의 경우의 수
            if 0<= tmp2 <= 20:
                dp[i][tmp2] += dp[i-1][j] 

print(dp[N-2][goal])