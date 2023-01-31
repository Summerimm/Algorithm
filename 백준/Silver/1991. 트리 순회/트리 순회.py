n = int(input())

tree = {}

for i in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right] # {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}

def preorder(root): # 전위 순회(root - left - right)
    if root != '.':
        print(root, end='') # root 출력
        preorder(tree[root][0]) # left 재귀돌면서 root 출력 .나오면 right 진행
        preorder(tree[root][1]) # right 재귀돌면서 root 출력

def inorder(root): # 중위 순회(left - root - right)
    if root != '.':
        inorder(tree[root][0])
        print(root, end='') 
        inorder(tree[root][1])

def postorder(root): # 후위 순회(left - right - root)
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')