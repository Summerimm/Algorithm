N, K = map(int, input().split())
lst = list(map(int, input().split()))
sumlst = [0]

s = 0
for i in range(N):
    s = s + lst[i]
    sumlst.append(s)

left = 0
right = K
ans = -1e9  # -100 * 100000
for i in range(N-K+1):
    ans = max(ans, sumlst[right] - sumlst[left])
    left += 1
    right += 1
print(ans)