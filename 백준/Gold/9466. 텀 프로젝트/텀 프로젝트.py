import sys
sys.setrecursionlimit(10**6)

# dfs 시작점를 한 번씩만 돎 => O(N)
# visited는 계속 유지
# 방문하지 않았던 노드에서 시작할 때마다 (새롭게 cycle list 생성 + dfs)

# dfs 후 다음 노드가 이미 방문한 적 있다면
# (i) 해당 시작점에서 파고들 때 생겼던 cycle이거나
# (ii) 이미 앞 for loop에서 방문 처리됨

# (i)에서 다음 노드가 해당 loop의 cycle list에 존재하면
# 답에서 cycle 길이만큼 빼줌

def dfs(n):
    global cnt
    # 방문 처리 후 일단 모두 cycle list에 넣음
    visited[n] = 1
    cyclelist.append(n)

    # 다음 노드가 이미 방문한 상태
    if visited[arr[n]]:
        # cycle list에 존재
        if arr[n] in cyclelist:
            cnt -= len(cyclelist[cyclelist.index(arr[n]):])
        return
    dfs(arr[n])

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    cnt = N

    for i in range(1, N+1):
        # 중복된 사이클 찾는 것을 방지 O(N)
        if not visited[i]:
            # 이번 cycle list
            cyclelist = []
            dfs(i)

    print(cnt)
