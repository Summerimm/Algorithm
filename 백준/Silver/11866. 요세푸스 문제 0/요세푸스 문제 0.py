N, K = map(int, input().split())
ans = []
v = [0] * N

idx = 0
cnt = 1
while v.count(0) != 0:
    if v[idx] == 0 and cnt == K:
        ans.append(idx + 1)
        v[idx] = 1
        cnt = 1
    elif v[idx] == 0 and cnt != K:
        cnt += 1
    idx = (idx + 1) % N

print("<", end="")
for i in range(N-1):
    print(f"{ans[i]}, ", end="")
print(f"{ans[-1]}>")