# 열혈영서
def dfs(n):                                         
    if visited[n]:
        return False                                      
    visited[n] = True

    for i in v[n]:
        if selected[i] == -1 or dfs(selected[i]): 
            # 방문한 적 없는 일 or 앞 직원이 일 변경 가능
            selected[i] = n
            return True
    return False 

# 왼쪽 직원 수, 오른쪽 일 수
N, M = map(int, input().split())

# 직원 인덱스에 해당하는 연결 가능한 일 번호들
v = [list(map(int, input().split()))[1:] for _ in range(N)]

# 해당 일의 담당자 번호가 담기는 배열
selected = [-1] * (M + 1)

for i in range(N):
    visited = [False] * N
    dfs(i)

ans = 0     # 매칭 수
for i in range(1, M+1):
    if selected[i] >= 0:
        ans += 1

print(ans)