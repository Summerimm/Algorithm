from collections import deque

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    visited = [0 for _ in range(10000)]
    q = deque()
    q.append([a, ''])
    visited[a] = 1

    while q:
        num, cmd = q.popleft()

        if num == b:
            print(cmd)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = 1
            q.append([d, cmd + 'D'])
        
        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = 1
            q.append([s, cmd + 'S'])
        
        l = num // 1000 + num % 1000 * 10
        if not visited[l]:
            visited[l] = 1
            q.append([l, cmd + 'L'])

        r = num // 10 + num % 10 * 1000
        if not visited[r]:
            visited[r] = 1
            q.append([r, cmd + 'R'])