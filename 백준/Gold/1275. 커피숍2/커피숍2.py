import sys
input = sys.stdin.readline

def makeSegTree(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = makeSegTree(start, mid, node * 2) + makeSegTree(mid + 1, end, node * 2 + 1)
    return tree[node]

def segSum(start, end, node):
    if x > end or y < start:        # 범위 밖인 경우
        return 0
    if x <= start and end <= y:     # 범위 내
        return tree[node]
    mid = (start + end) // 2
    return segSum(start, mid, node * 2) + segSum(mid + 1, end, node * 2 + 1)

def segUpdate(start, end, node):
    if aidx < start or aidx > end:  # 범위 밖
        return
    tree[node] -= arr[aidx] - b     # 원래 들어있던 값 빼고 b를 더하기
    if start == end:
        return
    mid = (start + end) // 2
    segUpdate(start, mid, node * 2)
    segUpdate(mid + 1, end, node * 2 + 1)
    

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

# 구간합 세그먼트 트리 생성
tree = [0] * (N*4)                  # 세그먼트 트리 원소 개수(N * 4)
makeSegTree(0, N-1, 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:                       # 인덱스 수정
        x, y = y, x
    x, y = x-1, y-1             
    print(segSum(0, N-1, 1))        # x부터 y번째까지의 합
    aidx = a - 1
    segUpdate(0, N-1, 1)            # segtree에서 모두 a를 b로 바꾸는 함수
    arr[aidx] = b
