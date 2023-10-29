n, m = map(int, input().split())

# 윗줄, 왼쪽 줄 padding
rectangle = [[0] * (m+1)] + [[0] + list(map(int, list(input()))) for _ in range(n)]

ans = 0

# (1, 1)부터 (row, col)까지의 합 저장
s = [[0] * (m+1) for _ in range(n+1)]
for row in range(1, n + 1):
    for col in range(1, m + 1):
        s[row][col] = s[row - 1][col] + s[row][col - 1] - s[row - 1][col - 1] + rectangle[row][col]

def rect_sum(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]

# 1) 세로로만 분할
for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = rect_sum(1, 1, n, i)
        r2 = rect_sum(1, i+1, n, j)
        r3 = rect_sum(1, j+1, n, m)
        ans = max(ans, r1 * r2 * r3)

# 2) 가로로만 분할
for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = rect_sum(1, 1, i, m)
        r2 = rect_sum(i+1, 1, j, m)
        r3 = rect_sum(j+1, 1, n, m)
        ans = max(ans, r1 * r2 * r3)

# 3) 전체 세로 분할, 오른쪽 가로 분할
for i in range(1, m):
    for j in range(1, n):
        r1 = rect_sum(1, 1, n, i)
        r2 = rect_sum(1, i+1, j, m)
        r3 = rect_sum(j+1, i+1, n, m)
        ans = max(ans, r1 * r2 * r3)

# 4) 전체 세로 분할, 왼쪽 가로 분할
for i in range(1, n):
    for j in range(1, m):
        r1 = rect_sum(1, 1, i, j)
        r2 = rect_sum(i+1, 1, n, j)
        r3 = rect_sum(1, j+1, n, m)
        ans = max(ans, r1 * r2 * r3)

# 5) 전체 가로 분할, 아래쪽 가로 분할
for i in range(1, n):
    for j in range(1, m):
        r1 = rect_sum(1, 1, i, m)
        r2 = rect_sum(i+1, 1, n, j)
        r3 = rect_sum(i+1, j+1, n, m)
        ans = max(ans, r1 * r2 * r3)

# 6) 전체 가로 분할, 위쪽 가로 분할
for i in range(1, n):
    for j in range(1, m):
        r1 = rect_sum(1, 1, i, j)
        r2 = rect_sum(1, j+1, i, m)
        r3 = rect_sum(i+1, 1, n, m)
        ans = max(ans, r1 * r2 * r3)

print(ans)