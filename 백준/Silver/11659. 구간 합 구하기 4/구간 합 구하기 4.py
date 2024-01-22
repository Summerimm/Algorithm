N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 배열
arr = [0] * (N + 1)
arr[1] = nums[0]
for i in range(1, N+1):
    arr[i] = arr[i-1] + nums[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])  