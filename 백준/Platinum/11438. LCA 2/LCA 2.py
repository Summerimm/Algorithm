import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def first_parent(cur, d):
    visited[cur] = 1
    depth[cur] = d
    for next in adj[cur]:
        if not visited[next]:
            parent[next][0] = cur  # 바로 위에 있는 부모만 넣기
            first_parent(next, d + 1)

# 희소 배열 사용
def all_parent():
    for i in range(1, maxlevel):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a, b):
    if a == 1 or b == 1:
        return 1

    # target = a(depth 작은 쪽), compare = b(depth 큰 쪽)
    if depth[a] < depth[b]:
        a, b = b, a

    # a와 b 깊이 동일하게 만들기
    for i in range(maxlevel -1, -1, -1):
        if depth[parent[a][i]] >= depth[b]:
            a = parent[a][i]    # 부모로 한 번에 올라가기

    if a == b:
        return a

    # 같은 depth이므로 공통 조상 찾기
    for i in range(maxlevel -1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]    # a, b 동시에 부모로 올라가기
            b = parent[b][i]
    return parent[a][0]


maxlevel = 18  # log_2_100000 = 16.06, 부모값을 저장하기 위한 크기

N = int(input())

parent = [[0] * maxlevel for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

first_parent(1, 1)
all_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
