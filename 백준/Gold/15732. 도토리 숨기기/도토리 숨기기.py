def calDotori(mid):
    cnt = 0
    for start, end, step in rules:
        if mid < start:
            continue
        end = min(mid, end)
        cnt += (end - start) // step + 1
    return cnt

def binarySearch():
    left = 1
    right = N
    while left < right:
        mid = (left + right) // 2
        dotori = calDotori(mid)
        if dotori < D:
            left = mid + 1
        else:
            right = mid
    return left

N, K, D = map(int, input().split())
rules = []
for _ in range(K):
    a, b, c = map(int, input().split())
    rules.append((a, b, c))
print(binarySearch())