n = int(input())
ans = 0
primes = []
arr = [0, 0] + [1] * (n-1)

# 에라토스테네스의 체로 n이하의 소수 저장(primes)
for i in range(2, n+1):
    if arr[i] == 1:
        primes.append(i)
        for j in range(2*i, n+1, i):
            arr[j] = 0

# 투 포인터
end = 0
interval_sum = 0 # start와 end 사이의 구간 합
for start in range(len(primes)):
    while interval_sum < n and end < len(primes): # 구간합이 n보다 크거나 같아질 때까지
        interval_sum += primes[end] # n보다 작으면 다음 숫자를 더해감
        end += 1
    if interval_sum == n: # 구간합이 n과 같아졌을 때
        ans += 1
    interval_sum -= primes[start] # 첫 숫자를 빼고 다시 진행
print(ans)