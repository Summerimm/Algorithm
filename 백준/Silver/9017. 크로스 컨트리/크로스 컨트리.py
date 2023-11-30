T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    teamset = set(arr)
    t = len(teamset)
    board = [[0, 0] for _ in range(t + 1)]

    participants = []
    for k in teamset:
        if k not in participants and arr.count(k) == 6:
            participants.append(k)

    cnt = 1
    last = [0] * (t + 1)
    for i in range(N):
        if arr[i] in participants:
            if board[arr[i]][1] < 4:
                board[arr[i]][0] += cnt
            elif board[arr[i]][1] == 4:
                last[arr[i]] = cnt
            board[arr[i]][1] += 1
            cnt += 1

    mn = 1e9
    ans = 0
    for i in range(1, len(teamset)+1):
        if i in participants:
            if board[i][0] < mn:
                mn = board[i][0]
                ans = i
            elif board[i][0] == mn:
                ans = last.index(min(last[ans], last[i]))
    print(ans)
