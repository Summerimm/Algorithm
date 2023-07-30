# 체스

def queen_check(r, c):
    K = max(n-1, m-1)
    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        for k in range(1, K+1):
            ni, nj = r + k * di, c + k * dj
            if 0 <= ni < n and 0 <= nj < m:
                if board[ni][nj] == 'k' or board[ni][nj] == 'p' or board[ni][nj] == 'q':
                    break
                else:
                    board[ni][nj] = 1

def knight_check(r, c):
    for di, dj in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]:
        ni, nj = r + di, c + dj
        if 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] == 0:
                board[ni][nj] = 1

n, m = map(int, input().split())

n_q, *q_list = map(int, input().split())
n_k, *k_list = map(int, input().split())
n_p, *p_list = map(int, input().split())

board = [[0] * m for _ in range(n)]


for i in range(len(p_list)//2):
    p_r, p_c = p_list[2 * i] - 1, p_list[2 * i + 1] - 1
    board[p_r][p_c] = 'p'

for i in range(len(k_list)//2):
    k_r, k_c = k_list[2 * i] - 1, k_list[2 * i + 1] - 1
    board[k_r][k_c] = 'k'

for i in range(len(q_list)//2):
    q_r, q_c = q_list[2 * i] - 1, q_list[2 * i + 1] - 1
    board[q_r][q_c] = 'q'

for i in range(len(k_list)//2):
    k_r, k_c = k_list[2 * i] - 1, k_list[2 * i + 1] - 1
    knight_check(k_r, k_c)

for i in range(len(q_list)//2):
    q_r, q_c = q_list[2 * i] - 1, q_list[2 * i + 1] - 1
    queen_check(q_r, q_c)

ans = 0
for i in range(n):
    ans += board[i].count(0)

print(ans)