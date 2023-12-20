from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    while q:
        mx = max(q)
        tmp = q.popleft()
        M -= 1

        if tmp == mx:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            q.append(tmp)
            if M < 0:
                M = len(q) - 1