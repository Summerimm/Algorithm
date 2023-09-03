# 고층 건물
N = int(input())
arr = list(map(int, input().split()))

ans = 0
# 기준 건물 번호
for i in range(N):
    
    cnt = 0     # 보이는 건물 수
    
    # 기준 건물보다 왼쪽
    for j in range(i-1, -1, -1):
        grad = (arr[i] - arr[j]) / (i - j)
        # 초기 기울기
        if j == i-1:
            tmp = grad
            cnt += 1
            continue
        # 기울기가 이전 기울기보다 작으면 +1
        if grad < tmp:
            cnt += 1
            tmp = grad
        else:
            continue
    
    # 기준 건물보다 오른쪽
    for k in range(i+1, N):
        grad = (arr[k] - arr[i]) / (k - i)
        # 초기 기울기
        if k == i+1:
            tmp = grad
            cnt += 1
            continue
        # 기울기가 이전 기울기보다 크면 +1
        if grad > tmp:
            cnt += 1
            tmp = grad
        else:
            continue
            
    # 큰 값 갱신
    ans = max(cnt, ans)

print(ans)