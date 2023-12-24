def math_round(num):
    if num >= 0:
        return int(num + 0.5)
    else:
        return int(num - 0.5)

def mode():
    set_array = set(arr)
    mx = 0
    for k in set_array:
        cnt = arr.count(k)
        if mx < cnt:
            mx = cnt
    
    for k in set_array:
        if arr.count(k) == mx:
            ans.append(k)
    ans.sort()

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = []    # 최빈값 후보 배열

# 반올림
print(math_round(sum(arr) / N))

# 중앙값
print(arr[N//2])

# 최빈값
mode()
if len(ans) > 1:
    print(ans[1])   # 두 번째로 작은 값
else:
    print(ans[0])   # 최빈값이 하나인 경우

# 범위
print(max(arr) - min(arr))