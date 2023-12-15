N = int(input())
flag = 1
for n in range(N):
    num = str(n)
    arr = list(map(str, num))
    tmp = 0
    for k in arr:
        tmp += int(k)
    if n + tmp == N:
        flag = 0
        print(n)
        break
if flag:
    print(0)