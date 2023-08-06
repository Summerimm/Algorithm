N = int(input())

lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst = sorted(lst, key=lambda x:(x[1], x[0]))

s = lst[0][0]
e = lst[0][1]
cnt = 0
for i in range(1, N):
    a = lst[i][0]
    b = lst[i][1]
    if a >= e:
        s = a
        e = b
        cnt += 1

print(cnt + 1)