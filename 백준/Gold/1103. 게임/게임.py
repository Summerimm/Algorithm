import sys
sys.setrecursionlimit(10**6)

def dfs(vi, vj, cnt):
    global result
    result = max(result, cnt)   # 각 지점을 dfs하면서 구한 cnt들 중에 max값만 저장함
    for k in range(4):
        ni, nj = vi + int(arr[vi][vj]) * di[k], vj + int(arr[vi][vj]) * dj[k]   # 이동 지점 ni, nj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 'H' and cnt+1 > dp[ni][nj]:   
            # 범위 내, 구멍X, 이동하는 지점에서의 cnt가 그 지점에 대해 앞에서 계산한 cnt보다 클 때
            if visited[ni][nj]:         # 가는 루트 중 이미 방문함
                print(-1)               # 무한 루프이므로 -1
                exit()
            else:
                dp[ni][nj] = cnt + 1
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1)    # 다음 지점에 대해 시행
                visited[ni][nj] = 0     # 더 이상 움직일 수 있는 지점이 없으면 돌아와서 미방문 처리

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]

result = 0
dfs(0, 0, 1)
print(result)