import sys
input = sys.stdin.readline

# 유클리드 호제법
# 기울기 이용 - (1,2)와 (2,4)의 차이는 서로소냐 아니냐의 차이
# 최대공약수가 1이 되는 집합들을 찾아야 함

def gcd(i, j): # 최대공약수 구하는 함수
    while j != 0: # 유클리드 알고리즘
        i, j = j, i % j
    return i

shown = [0 for _ in range(1001)] # shown[n] -> n * n 정사각형 안에 조건을 만족하는 점의 수
shown[1] = 3 # (1,0)(1,1),(1,2)

for i in range(2, 1001):
    cnt = 0
    for j in range(1, i): # 왼쪽 아래 절반 삼각형
        if gcd(i, j) == 1: # 최대공약수가 1, 즉 (i, j)는 기울기가 다른 최초의 점
            cnt += 2 # 대칭
    shown[i] = shown[i-1] + cnt # 누적합

t = int(input())
for _ in range(t):
    n = int(input())
    print(shown[n])