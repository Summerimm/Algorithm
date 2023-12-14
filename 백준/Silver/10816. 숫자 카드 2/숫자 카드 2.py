N = int(input())
nums = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

dct = {}
for i in range(N):
    if nums[i] not in dct.keys():
        dct[nums[i]] = 1
    else:
        dct[nums[i]] += 1

for k in arr:
    if k in dct.keys():
        print(dct[k], end=" ")
    else:
        print("0", end=" ")
print()