# 집합의 표현
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])     # x의 루트 노드 찾기
    parent[x] = p           # 부모 갱신
    return p

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    # 숫자가 큰 쪽의 부모를 작은 숫자로
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    tp, a, b = map(int, input().split())
    if tp == 0:     # 합집합
        union(a, b)
    else:           # 같은 집합에 존재하는지 확인
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')