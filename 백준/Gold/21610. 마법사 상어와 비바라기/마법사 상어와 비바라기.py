# 입력
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

# 8방향
dx8 = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
dy8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

# 대각 4방향
dx4 = (-1, -1,  1, 1)
dy4 = (-1,  1, -1, 1)

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] # 구름 좌표
for d, s in moves:
    # 모든 구름 이동
    moved_clouds = []
    for r, c in clouds:
        # 구름들을 d 방향으로 s만큼 이동(연결되어 있으므로 %N)
        nx = (r + dx8[d] * s) % N 
        ny = (c + dy8[d] * s) % N
        board[nx][ny] += 1 # 물의 양 추가
        moved_clouds.append((nx, ny)) # 이동한 구름 좌표에 추가

    for r, c in moved_clouds:
        # 이동한 구름들의 대각 4방향을 조사하여 count만큼 물의 양 추가    
        cnt = 0
        for d in range(4):
            nx = r + dx4[d]
            ny = c + dy4[d]
            # 구름의 좌표가 연결되어 있지 않으므로 예외처리
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            elif board[nx][ny] > 0: cnt += 1
        board[r][c] += cnt

    new_clouds = []
    for r in range(N):
        for c in range(N):
            # 이동한 구름의 좌표와 같지 않고, 물의 양이 2 이상인 경우
            if (r, c) in moved_clouds or board[r][c] < 2:
                continue
            # 물을 2만큼 줄이고 새로운 구름 배열(new_clouds)에 추가
            board[r][c] -= 2
            new_clouds.append((r, c))
    clouds = new_clouds # 다음 loop에서 사용할 clouds 배열을 new_clouds로 교체

# 물의 양 합 계산 후 출력
result = 0
for r in range(N):
    for c in range(N):
        result += board[r][c]
print(result)