N, new, P = map(int, input().split())
if N == 0:
    print(1)
else:
    arr = list(map(int, input().split()))

    if N == P and arr[-1] >= new:
        print(-1)
    else:
        ans = N + 1
        for i in range(N):
            if arr[i] <= new:
                ans = i + 1
                break
        print(ans)
