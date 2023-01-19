n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    tree_length = 0
    for d in tree:
        if d >= mid:
            tree_length += d - mid
            
    if tree_length >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)