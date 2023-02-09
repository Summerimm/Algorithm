import sys
sys.setrecursionlimit(10 ** 9) # 재귀 허용 깊이를 10**9만큼 늘려줌
input = sys.stdin.readline

# preorder 전위순회(root-left-right)
# inorder 중위순회(left-root-right)
# postorder 후위순회(left-right-root)

# 전위 순회를 했으므로 루트 노드보다 큰 원소가 나오는 지점이 
# 왼쪽 서브 트리와 오른쪽 서브 트리를 나누는 지점과 같다.
# 50 / 30 24 5 28 45 / 98 52 60
# 30 / 24 5 28 / 45
# 24 / 5 / 28
# 5 반환 - 28 반환 - 24 반환 (left-right-root)

# preorder 상태로 입력(예외처리 이용)
nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

# root를 기준으로 Binary Search Tree postorder
def postorder(start, end):
    if start > end: # 탈출조건(숫자 하나만 남았거나 루트노드보다 큰 숫자가 없을 때 mid + 1 한 값이 end를 넘어감)
        return
    mid = end + 1 
    # root 노드보다 큰 값이 없을 경우 end + 1 함으로써 
    # 왼쪽 트리는 start + 1부터 end까지 처리
    # 오른쪽 트리는 start > end로 pass
    for i in range(start + 1, end + 1):
        if nums[i] > nums[start]:
            mid = i # root 노드보다 큰 값이 처음 발견된 인덱스
            break
    postorder(start + 1, mid - 1) # 왼쪽 트리
    postorder(mid, end) # 오른쪽 트리
    print(nums[start]) # 루트 노드

postorder(0, len(nums) - 1) # nums의 index
