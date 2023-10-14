N = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

ans = N
for i in range(N):
    if arr[i] >= b:
        arr[i] -= b
    else:
        arr[i] = 0
    ans += arr[i] // c
    if arr[i] % c != 0:
        ans += 1

print(ans)