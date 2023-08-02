# 테트로미노

# 1) 세로 3칸 - 주변 7칸 중에 가장 큰 값
# 2) 가로 3칸 - 주변 7칸 중에 가장 큰 값
# 3) 세로 2칸 - 5가지 경우에 대해 가장 큰 값

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

mx = 0
di_1 = [0, 1, 2, 3, 2, 1, 0]
dj_1 = [1, 1, 1, 0, -1, -1, -1]
di_2 = [-1, -1, -1, 0, 1, 1, 1]
dj_2 = [0, 1, 2, 3, 2, 1, 0]
di_3 = [(0, 1), (1, 2), (1, 2), (0, 1), (0, 1)]
dj_3 = [(1, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
for i in range(N):
    for j in range(M):
        # 1) 세로 3칸
        if 0<=i+1<N and 0<=i+2<N:
            addmx = 0
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            for k in range(7):
                ni, nj = i + di_1[k], j + dj_1[k]
                if 0<=ni<N and 0<=nj<M:
                    addmx = max(addmx, arr[ni][nj])
            mx = max(mx, tmp + addmx)
        # 2) 가로 3칸
        if 0<=j+1<M and 0<=j+2<M:
            addmx = 0
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            for k in range(7):
                ni, nj = i + di_2[k], j + dj_2[k]
                if 0<=ni<N and 0<=nj<M:
                    addmx = max(addmx, arr[ni][nj])
            mx = max(mx, tmp + addmx)
        # 3) 세로 2칸
        if 0<=i+1<N:
            addmx = 0
            tmp = arr[i][j] + arr[i+1][j]
            for k in range(5):
                ni_1, nj_1 = i + di_3[k][0], j + dj_3[k][0]
                ni_2, nj_2 = i + di_3[k][1], j + dj_3[k][1]
                if 0<=ni_1<N and 0<=nj_1<M and 0<=ni_2<N and 0<=nj_2<M:
                    addmx = max(addmx, arr[ni_1][nj_1] + arr[ni_2][nj_2])
            mx = max(mx, tmp + addmx)

print(mx)