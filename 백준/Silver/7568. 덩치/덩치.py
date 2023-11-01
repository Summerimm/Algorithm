N = int(input())
lst = [list(map(int, input().split())) + [i] for i in range(N)]
lst.sort(key=lambda x:(x[0], x[1]), reverse=True)

ans = [0] * N
for i in range(N):
    rank = 1
    w1, h1 = lst[i][0], lst[i][1]
    for j in range(i):
        w2, h2 = lst[j][0], lst[j][1]
        if w2 > w1 and h2 > h1:
            rank += 1
    ans[lst[i][2]] = rank
print(*ans)