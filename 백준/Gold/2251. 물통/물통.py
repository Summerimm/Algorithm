# 물통
from collections import deque

def pour(a, b):
    if not visited[a][b]:
        visited[a][b] = 1
        q.append((a, b))

def bfs():
    while q:
        # a : 현재 A물통의 양, b: 현재 B물통의 양, c: 현재 C물통의 양
        a, b = q.popleft()
        c = C - a - b

        # A 물통이 비어있는 경우
        if a == 0:
            ans.append(c)
        
        # a -> b
        move = min(a, B - b)  # (A 현재 용량, B 남은 용량) 중 작은 양
        pour(a - move, b + move)
        # a -> c
        move = min(a, C - c)
        pour(a - move, b)
        # b -> a
        move = min(b, A - a)
        pour(a + move, b - move)
        # b -> c
        move = min(b, C - c)
        pour(a, b - move)
        # c -> a
        move = min(c, A - a)
        pour(a + move, b)
        # c -> b
        move = min(c, B - b)
        pour(a, b + move)

A, B, C = map(int, input().split())

q = deque()
visited = [[0] * (B+1) for _ in range(A+1)]

q.append((0, 0))    # A, B의 현재 용량
visited[0][0] = 1   # 경우의 수 방문 배열

ans = []

bfs()
ans.sort()
print(*ans)
