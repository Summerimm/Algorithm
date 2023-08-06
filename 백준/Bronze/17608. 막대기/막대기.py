# 막대기

N = int(input())

stick = []
for i in range(N):
    stick.append(int(input()))

st = stick[-1]
cnt = 0
for i in range(N-2, -1, -1):
    if stick[i] > st:
        st = stick[i]
        cnt += 1

print(cnt + 1)