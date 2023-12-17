L = int(input())
arr = list(map(str, input()))

ans = 0
for i in range(L):
    ans += (ord(arr[i]) - 96) * (31 ** i)
print(ans)