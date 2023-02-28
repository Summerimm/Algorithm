T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = 0
    for i in range(M):
        if arr[0][i] != 'W':
            ans += 1
        if arr[-1][i] != 'R':
            ans += 1

    cnt = []
    for j in range(1, N-1):
        wcnt = arr[j].count('B') + arr[j].count('R')
        bcnt = arr[j].count('W') + arr[j].count('R')
        rcnt = arr[j].count('W') + arr[j].count('B')
        cnt.append([wcnt, bcnt, rcnt])

    comblst = []
    for i in range(1, N-1):
        for j in range(N-1-i):
            comb = '0' * (N-2-i-j) + '1' * i + '2' * j
            comblst.append(comb)

    alst = []
    for a in comblst:
        tmp = 0
        for i, c in enumerate(a):
            tmp += cnt[i][int(c)]
        alst.append(tmp)

    print(f'#{tc} {min(alst)+ans}')