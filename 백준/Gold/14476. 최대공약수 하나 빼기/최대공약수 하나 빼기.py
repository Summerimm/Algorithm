import sys, math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 누적합 이용
# pf_gcd: 0 ~ i까지의 gcd 저장, sf_gcd: i~n-1까지의 gcd를 저장
pf_gcd = [0] * (n + 1)
sf_gcd = [0] * (n + 1)

pf_gcd[0] = nums[0]
for i in range(1, n):
    pf_gcd[i] = math.gcd(pf_gcd[i - 1], nums[i])

sf_gcd[n - 1] = nums[n - 1]
for i in range(n - 2, -1, -1):
    sf_gcd[i] = math.gcd(sf_gcd[i + 1], nums[i])


ans = []
for i in range(n):
    final = math.gcd(pf_gcd[i - 1], sf_gcd[i + 1]) # ([0, i - 1]까지의 gcd와 [i + 1, n - 1]까지의 gcd)의 gcd
    if nums[i] % final == 0: # 최종 gcd가 k의 약수일 때
        continue
    ans.append((final, nums[i]))

print(' '.join(map(str, ans[0])) if ans else -1)

# ----------------------------------------------------------------
# 시간초과

# def gcd(i, j):
#     while j != 0:
#         i, j = j, i % j
#     return i

# for i in range(n):
#     if i == 0:
#         gcdarr = nums[1]
#     else:
#         gcdarr = nums[0]
#     for num in nums:
#         if num == nums[i]:
#             continue
#         gcdarr = gcd(gcdarr, num) # 앞에서부터 최대공약수를 좁혀감
#     if gcdarr > mx:
#         mx = gcdarr
# mx = max(ans)
# out = nums[ans.index(mx)]

# if out % mx == 0:
#     print(-1)
# else:
#     print(mx, out)