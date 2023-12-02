N = int(input())
order = list(map(int, input().split()))

ans = [N] * N
ans[order[0]] = 1

for i in range(1, N):
    cnt = 0
    for j in range(N):
        if cnt == order[i] and ans[j] == N:
            ans[j] = i+1
            break
        elif ans[j] > i:
            cnt += 1
print(*ans)
