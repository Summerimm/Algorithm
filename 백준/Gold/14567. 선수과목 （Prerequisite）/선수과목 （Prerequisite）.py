# 선수과목(Prerequisite)
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
inDegree = [1] * (V+1)

for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, V+1):
    for b in graph[i]:
        inDegree[b] = max(inDegree[b], inDegree[i]+1)
        
print(*inDegree[1:])