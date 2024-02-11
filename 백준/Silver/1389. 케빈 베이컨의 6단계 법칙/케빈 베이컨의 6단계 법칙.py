import sys
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    if b in graph[a]:
        continue
    else:
        graph[a].append(b)
        graph[b].append(a)

arr = [[INF] * (V+1) for _ in range(V+1)]
for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            arr[i][j] = 0

for i in range(1, V+1):
    for num in graph[i]:
        arr[i][num] = 1

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

mn = INF
for i in range(1, V+1):
    tmp = sum(arr[i]) - INF
    if tmp < mn:
        mn = tmp
        ans = i
print(ans)