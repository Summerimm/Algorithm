# 하늘에서 별똥별잉 빗발친다
N, M, L, K = map(int, input().split())
stars = []
for _ in range(K):
    c, r = map(int, input().split())
    stars.append((r, c))

# 기준점 2개의 x, y좌표를 기준으로 모서리 생성
ans = K
for x, _ in stars:
    for _, y in stars:
        cnt = K
        for a, b in stars:
            if x <= a <= x + L + 1 and y <= b <= y + L + 1:
                cnt -= 1
        ans = min(ans, cnt)
print(ans)