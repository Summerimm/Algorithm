N, K = map(int, input().split())
lst = []
for _ in range(N):
    num, gold, silver, bronze = map(int, input().split())
    lst.append((gold, silver, bronze, num))

lst = sorted(lst, key=lambda x: (x[0], x[1], x[2]), reverse=True)
for i in range(N):
    if lst[i][3] == K:
        idx = i

leaderboard = [0] * N
tmp = 0
rank = 1
for i in range(N):
    if i == 0:
        leaderboard[i] = rank
    else:
        if lst[i-1][0] == lst[i][0] and lst[i-1][1] == lst[i][1] and lst[i-1][2] == lst[i][2]:
            leaderboard[i] = rank
            tmp += 1
        else:
            rank += tmp + 1
            tmp = 0
            leaderboard[i] = rank

print(leaderboard[idx])