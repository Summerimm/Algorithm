def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
        return 1
    elif rootA > rootB:
        parent[rootA] = rootB
        return 1
    else:
        return 0

N, M = map(int, input().split())

parent = [0] * (N+1)  # 부모 배열
Ecnt = 0  # 간선 수
ans = 0  # 유지비 합

# 부모 배열 초기화
for i in range(1, N+1):
    parent[i] = i

# 간선 추가 및 유지비 순 정렬
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort()

for c, a, b in graph:
    # 사이클
    if not union(parent, a, b):
        continue
    else:
        Ecnt += 1
        ans += c
        if N == 2:
            print(0)
        elif Ecnt == N - 2:
            print(ans)
            break
