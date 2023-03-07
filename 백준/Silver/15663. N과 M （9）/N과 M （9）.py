def dfs():
    if len(tmp) == M:
        print(*tmp)
        return
    
    dup = 0
    for i in range(N):
        if dup != arr[i] and visited[i] == 0:
            visited[i] = 1
            tmp.append(arr[i])
            dup = arr[i]
            dfs()
            visited[i] = 0
            tmp.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * N
tmp = []
dfs()