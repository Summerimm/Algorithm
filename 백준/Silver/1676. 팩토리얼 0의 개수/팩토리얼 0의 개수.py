N = int(input())
ans = 0

tmp = 1
for i in range(N, 0, -1):
    tmp *= i

strtmp = str(tmp)
num = list(map(str, strtmp))
for i in range(len(num)-1, -1, -1):
    if num[i] == '0':
        ans += 1
    else:
        break
print(ans)