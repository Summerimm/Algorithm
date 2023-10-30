from collections import deque
from bisect import bisect_left

P = int(input())
for _ in range(P):
    T, *arr = map(int, input().split())
    
    lst = deque()
    lst.append(arr[0])

    ans = 0
    for i in range(1, 20):
        if arr[i] > max(lst):
            lst.append(arr[i])
        else:
            idx = bisect_left(lst, arr[i])
            pre_lst = [lst[i] for i in range(idx)]
            post_lst = [lst[i] for i in range(idx, len(lst))]
            lst = pre_lst + [arr[i]] + post_lst
            ans += len(post_lst)
    print(T, ans)