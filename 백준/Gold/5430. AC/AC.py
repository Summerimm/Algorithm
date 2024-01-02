from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = deque(input()[1:-1].split(','))

    if n == 0:
        arr = deque()
    
    cnt = 0
    flag = 1
    for c in p:
        if c == 'R':
            cnt += 1
        elif c == 'D':
            if len(arr) < 1:
                flag = 0
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag:
        if cnt % 2:
            arr.reverse()
        print('[' + ','.join(arr) + ']')