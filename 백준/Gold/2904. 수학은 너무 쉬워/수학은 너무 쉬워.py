import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 에라토스테네스의 체
maxv = 1000001
sieve = [0, 0] +[1] * maxv
for i in range(2, maxv + 1):
    if sieve[i] == 0:
        continue
    for j in range(i**2, maxv + 1, i):
        sieve[j] = 0

# 100만까지 소수만 저장하는 배열 primelist
primelist = []
for i in range(maxv + 1):
    if sieve[i]:
        primelist.append(i)

# 균형점수 / 이동횟수를 세기 위해 더 필요한 배열
totalp = [0] * len(primelist) # 모든 수에 대해서 각 소수가 몇 번 쓰였는지(n으로 나누어 균형점수 구할 수 있음)
inputp = [[0] * len(primelist) for _ in range(n)] # 각 수에 대해서 소수가 몇 번 쓰였는지(균형점수와 비교하여 각 수가 가지고 있는 소수가 더 적으면 이동횟수 셀 수 있음)
for i, num in enumerate(nums):
    for j, p in enumerate(primelist):
        if num == 1:
            break
        while num % p == 0:
            num //= p
            totalp[j] += 1
            inputp[i][j] += 1

# 얻을 수 있는 가장 큰 점수(균형점수) ans1 / 이동횟수 ans2
ans1, ans2 = 1, 0
for i in range(len(totalp)):
    ans1 *= primelist[i]**(totalp[i] // n)
    for j in range(len(inputp)):
        if inputp[j][i] < totalp[i] // n:
            ans2 += totalp[i] // n - inputp[j][i]
print(ans1, ans2)