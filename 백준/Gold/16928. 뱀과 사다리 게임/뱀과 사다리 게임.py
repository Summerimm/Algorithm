from collections import deque

N, M = map(int, input().split())
board = [0] * 101   # 주사위 굴린 횟수

ladder, snake = {}, {}
for _ in range(N):
    s, e = map(int, input().split())
    ladder[s] = e

for _ in range(M):
    s, e = map(int, input().split())
    snake[s] = e

q = deque([1])
while q:
    x = q.popleft()
    if x == 100:
        print(board[x])
        break
    for dice in range(1, 7):
        nx = x + dice
        if nx <= 100:
            if nx in ladder.keys(): # 이동할 위치에 사다리 있음
                nx = ladder[nx]
            if nx in snake.keys(): # 이동할 위치에 뱀 있음
                nx = snake[nx]
            if not board[nx]: # 이동한 칸이 방문한 적 없을 때
                board[nx] = board[x] + 1
                q.append(nx)