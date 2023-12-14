from collections import deque

T = int(input())
for _ in range(T):
    q = deque()
    lst = list(input())
    flag = 1
    for i in range(len(lst)):
        if lst[i] == '(':
            q.append(lst[i])
        elif q and lst[i] == ')':
            q.pop()
        elif not q and lst[i] == ')':
            print("NO")
            flag = 0
            break
    if flag and q:
        print("NO")
    elif flag and not q:
        print("YES")
