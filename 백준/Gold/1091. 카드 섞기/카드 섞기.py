n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
target = [0, 1, 2] * (n//3)
card = [0] * n
origin = p[:]

cnt = 0
while p != target:
    for i in range(n):
        card[s[i]] = p[i]
    p = card[:]
    cnt += 1
    if p == origin:
        cnt = -1
        break
print(cnt)