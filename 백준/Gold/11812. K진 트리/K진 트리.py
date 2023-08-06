# K진 트리

import sys
input = sys.stdin.readline

# 같은 depth에 있는 최댓값: 등비 수열의 합
# (K ** depth - 1) // (K - 1)
def maxvalue(depth):
    if depth <= 0:
        return 0

    return (K ** depth - 1) // (K - 1)

# 해당 노드의 depth 찾기
def find_depth(node):
    depth = 1
    while True:
        if maxvalue(depth) >= node:
            return depth
        depth += 1

# 최소 공통 조상 찾으며 count
def findLCA(a, b, ans):
    # 초기값 depth 찾기
    depth_a = find_depth(a)
    depth_b = find_depth(b)

    # depth가 깊은 쪽을 a로 switch
    if depth_a < depth_b:
        a, b = b, a
        depth_a, depth_b = depth_b, depth_a

    # depth가 깊은 쪽을 depth가 같게 올려주기
    while depth_a != depth_b:
        # 부모 = (node + K - 2) // K
        a = (a + K - 2) // K
        depth_a -= 1
        ans += 1

    # 조상이 같아질 때까지 부모 노드 올라가기
    while a != b:
        a = (a + K - 2) // K
        b = (b + K - 2) // K
        ans += 2
    
    return ans

N, K, Q = map(int, input().split())

for i in range(Q):
    x, y = map(int, input().split())

    # K = 1일 경우 부모찾기 때문에 O(N)이 됨
    if K == 1:
        print(abs(x - y))
        continue
    
    print(findLCA(x, y, 0))