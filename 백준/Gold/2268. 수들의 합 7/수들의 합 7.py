import sys
input = sys.stdin.readline

def Sum(s, e, idx, left, right):
    if left > e or right < s:       # 범위 밖
        return 0
    if left <= s and right >= e:    # 범위 안
        return tree[idx]
    mid = (s + e) // 2
    return Sum(s, mid, idx * 2, left, right) + Sum(mid + 1, e, idx * 2 + 1, left, right)


def Modify(s, e, idx, node, value):
    if node < s or node > e:        # 범위 밖
        return
    if s == e:
        tree[idx] = value
        return
    mid = (s + e) // 2
    Modify(s, mid, idx * 2, node, value)
    Modify(mid + 1, e, idx * 2 + 1, node, value)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


N, M = map(int, input().split())
tree = [0] * (N * 4)
for _ in range(M):
    t, a, b = map(int, input().split())
    if t:
        Modify(0, N-1, 1, a-1, b)
    else:
        if a > b:
            a, b = b, a
        print(Sum(0, N-1, 1, a-1, b-1))
        