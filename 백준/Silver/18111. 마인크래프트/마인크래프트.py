N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

# 브루트포스
ans = 1e9
height = 0
for m in range(257): # 땅 최대 높이 이내에서 기준 높이 선정
    take_block = 0  # 없애서 인벤토리에 넣는 블럭 수
    use_block = 0   # 인벤토리에서 사용하는 블럭 수
    # 모든 좌표 탐색
    for i in range(N):
        for j in range(M):
            if ground[i][j] > m:
                take_block += ground[i][j] - m
            else:
                use_block += m - ground[i][j]
    
    if use_block > take_block + B:
        continue
    
    tmp  = take_block * 2 + use_block
    
    if ans >= tmp:
        ans = tmp
        height = m

print(ans, height)
