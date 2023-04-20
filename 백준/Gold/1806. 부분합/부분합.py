# 부분합
N, S = map(int, input().split())
arr = list(map(int, input().split()))


s, e = 0, -1     # 투 포인터
partialSum = 0  # 부분합
tmp = 0         # 현재까지 길이 저장
ans = 100000

while e < N:
    if partialSum < S:
        e += 1
        tmp += 1
        if e < N:
            partialSum += arr[e]
    elif partialSum >= S:
        partialSum -= arr[s]
        ans = min(ans, tmp)
        s += 1
        tmp -= 1
if ans == 100000:
    ans = 0
print(ans)