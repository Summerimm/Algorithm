import sys
input = sys.stdin.readline

exp = input().split('-')
num = []
for i in exp:
    tmp = list(map(int, i.split('+')))
    s = sum(tmp)
    num.append(s)

ans = num[0]
for i in range(1, len(num)):
    ans -= num[i]
print(ans)