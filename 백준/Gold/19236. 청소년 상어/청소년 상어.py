import copy
# (0, 0)에서 시작
# 상어 먹기, 먹힌 자리는 0
# 물고기 이동(전체 시뮬레이션 -> 이동하려는 위치가 바깥이거나 상어 위치면 방향 틀기)
# 상어 이동(갈 수 있는 칸들을 후보지로...여러칸 이동 가능) -> 가려는 방향 * 크기(1씩 늘리기)
# dfs를 통해 쭉 들어감(상어가 이동할 수 있는 칸이 없을 때까지-물고기가 없는 칸으로는 이동 불가)
# dfs 들어갈 때마다 최댓값 갱신

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
def dfs(si, sj, score, board):
    global ans
    score += board[si][sj][0]
    ans = max(ans, score)
    # 먹고 난 뒤 해당 칸은 0
    board[si][sj][0] = 0

    # 물고기 움직임
    for num in range(1, 17):
        ci, cj = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == num:   # 순서 해당 물고기 만남
                    ci, cj = x, y     # 이동할 물고기 현재 위치
                    break
        if ci == -1 and cj == -1:     # 번호 존재X (이미 상어한테 먹힌 경우)
            continue
        f_d = board[ci][cj][1]        # 이동할 물고기의 방향

        for i in range(8):
            nd = (f_d + i) % 8    # 바뀐 방향(0일 때 그대로, 1일 때 -45도 틀음)
            ni, nj = ci + di[nd], cj + dj[nd]
            if not (0 <= ni < 4 and 0<= nj < 4) or (ni == si and nj == sj):
                continue
            board[ci][cj][1] = nd
            board[ni][nj], board[ci][cj] = board[ci][cj], board[ni][nj]
            break
    
    # 상어 먹음
    s_d = board[si][sj][1]  # 상어의 방향
    for i in range(1, 5):
        ni = si + di[s_d] * i
        nj = sj + dj[s_d] * i
        if (0 <= ni < 4 and 0<= nj < 4) and board[ni][nj][0] > 0:
            dfs(ni, nj, score, copy.deepcopy(board))

ans = 0
board = [[[0, 0] for _ in range(4)] for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))

    for j in range(4):
        # 물고기 번호, 방향
        board[i][j][0] = data[2*j]
        board[i][j][1] = data[2*j+1] - 1

dfs(0, 0, 0, board)
print(ans)