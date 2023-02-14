import sys
input = sys.stdin.readline

# 확장 유클리드 호제법
# Kx + 1 = Cy
# Cy - Kx = 1 -> (a, b)가 1이어야 함
# C, K는 0이 아닌 정수, x = s_cur, y = t_cur
# x는 인당 사탕 수, y는 사탕 봉지 수
def extendedEuclidean(a, b):
    s_prev, s_cur = 1, 0
    t_prev, t_cur = 0, 1
    while b != 0:
        q = a // b
        r = a % b
        a, b = b, r
        s_next = s_prev - q * s_cur     # 점화식
        t_next = t_prev - q * t_cur     # 점화식
        s_prev, t_prev = s_cur, t_cur
        s_cur, t_cur = s_next, t_next
    # t_prev가 음수임을 방지
    if t_prev < 0:
        t_prev += K
    # (a, b)가 1이 아니거나 마지막 계산 후 t_cur값이 들어간 t_prev
    if a != 1 or t_prev > 10**9:
        return 'IMPOSSIBLE'
    return t_prev


T = int(input())
for _ in range(T):
    K, C = map(int, input().split())
    # 봉지 당 사탕개수가 1개일 때
    if C == 1:
        # 필요한 봉지 수는 (사람 수 +1)
        if K + 1 > 10**9:
            print('IMPOSSIBLE')
        else:
            print(K + 1)
        continue
    # 사람 수가 한 명일 때
    if K == 1:
        # 1봉지 시키고 C - 1개 나눠주면 됨
        print(1)
        continue
    ans = extendedEuclidean(K, C)
    print(ans)