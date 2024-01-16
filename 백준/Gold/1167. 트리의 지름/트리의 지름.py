def dfs(node, dist):
    for v, d in graph[node]:
        cost = dist + d
        if visited[v] == -1:
            visited[v] = cost
            dfs(v, cost)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    num, *arr, end = map(int, input().split())
    for i in range(len(arr) // 2):
        graph[num].append((arr[2 * i], arr[2 * i + 1]))

# 아무 노드 잡고 최대 거리에 있는 노드 찾기 => 이 노드가 트리의 한 끝 지점
# 1번 노드를 기준으로 잡고 있음
visited = [-1] * (N+1) # 방문 배열이자 최대 거리가 담기는 배열
visited[1] = 0
dfs(1, 0)
tmp_dist = max(visited) # 1번 노드로부터 최대 거리
tmp_node = visited.index(tmp_dist) # 트리의 한 끝 지점

# 트리의 한 끝 지점에서 dfs 돌려 찾은 최대 거리가 트리의 지름
visited = [-1] * (N+1)
visited[tmp_node] = 0
dfs(tmp_node, 0)

print(max(visited))