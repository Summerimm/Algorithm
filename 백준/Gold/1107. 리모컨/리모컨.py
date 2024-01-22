target = int(input())
M = int(input())
broken = []
if M != 0:
    broken = list(map(int, input().split()))

# 100에서 +, -만 하는 횟수
min_cnt = abs(target - 100)

# 직접 채널 변경 후 +, -하는 횟수
# 브루트포스를 이용해 고장나지 않은 숫자로 만들 수 있는 모든 수 탐색
for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 각 숫자가 고장났는지 확인 후, 고장났으면 break
        if int(nums[j]) in broken:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_cnt와 비교 후 업데이트
        elif j == len(nums) - 1:
            min_cnt = min(min_cnt, abs(int(nums) - target) + len(nums))

print(min_cnt)