import heapq

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
garr = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            si, sj = i, j
        elif arr[i][j] == 'F':
            ei, ej = i, j
        elif arr[i][j] == 'g':
            garr.append((i, j))

for i, j in garr:
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '.':
            arr[ni][nj] = '*'

q = []
heapq.heappush(q, (0, 0, si, sj))
v = [[0] * M for _ in range(N)]
v[si][sj] = 1

while q:
    a, b, i, j = heapq.heappop(q)

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not v[ni][nj]:
            v[ni][nj] = 1
            if arr[ni][nj] == '.':
                heapq.heappush(q, (a, b, ni, nj))
            elif arr[ni][nj] == '*':
                heapq.heappush(q, (a, b+1, ni, nj))
            elif arr[ni][nj] == 'g':
                heapq.heappush(q, (a+1, b, ni, nj))
            else:
                print(a, b)
                exit()