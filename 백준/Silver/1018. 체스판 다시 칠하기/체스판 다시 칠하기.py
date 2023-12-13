def check(r, c, k):
    global ans
    tmp = 0
    for i in range(r, r+8):
        for j in range(c, c+8):
            if board[i][j] != order[k]:
                tmp += 1
            k = (k + 1) % 2
        k = (k + 1) % 2
    ans = min(ans, tmp)

order = ['B', 'W']
N, M = map(int, input().split())
board = []
ans = 64

for _ in range(N):
    board.append(list(input()))

for i in range(N - 7):
    for j in range(M - 7):
        check(i, j, 0)
        check(i, j, 1)
print(ans)