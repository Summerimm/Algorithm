import sys
input = sys.stdin.readline

# 높이 H부터 1까지 누적합을 계산하면 
# 높이 i의 배열 값은 높이 i 이상의 모든 석순의 개수가 됨

N, H = map(int, input().split())
# N은 배열에 넣을 횟수
# H는 누적합 받는 배열의 크기

u =  [0] * (H + 1) # up: 석순
d = [0] * (H + 1) # down: 종유석
mn = N # 최소값 초기화
for i in range(N):
    if i % 2 == 0: # 종유석
        d[int(input())] += 1
    else: # 석순
        u[int(input())] += 1

for i in range(H - 1, 0, -1): # 높은 것부터 누적합
    u[i] += u[i + 1]
    d[i] += d[i + 1]

for i in range(1, H + 1):
    if mn > d[H - i + 1] + u[i]:
        mn = d[H - i + 1] + u[i]    # 종유석은 반대로 생각해야 함
        cnt = 1                     # min 처음 나온 경우이므로 cnt 1로 초기화
    elif mn == d[H - i + 1] + u[i]: # min값과 같은 경우 cnt + 1
        cnt += 1
print(mn, cnt)