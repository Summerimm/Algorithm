# 도로의 개수
N, M = map(int, input().split())
K = int(input())
dp = [[0] * (N + 1) for _ in range(M + 1)]
road = []

dp[0][0] = 1
for i in range(K):
    road.append(list(map(int, input().split())))

def check(current, a, b, c, d):
    if current == [a, b, c, d] or current == [c, d, a, b]:
        return True
    else:
        return False

for x in range(M + 1):
    for y in range(N + 1):
        if y > 0:
            for a, b, c, d in road:
                if check([y - 1, x, y, x], a, b, c, d):
                    break
            else:
                dp[x][y] += dp[x][y - 1]
        if x > 0:
            for a, b, c, d in road:
                if check([y, x - 1, y, x], a, b, c, d):
                    break
            else:
                dp[x][y] += dp[x - 1][y]
print(dp[M][N])