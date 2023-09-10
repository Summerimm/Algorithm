from collections import deque

N = int(input())
qs = list(map(int, input().split()))
state = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

result = deque()
for i in range(N-1, -1, -1):
    if qs[i] == 0:
        result.append(state[i])

for i in range(M):
    result.append(nums[i])

for i in range(M):
    print(result.popleft(), end=" ")
