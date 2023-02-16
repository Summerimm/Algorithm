T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    s = 0
    while nums != []:
        mx = max(nums)
        idx = nums.index(mx)
        nums1 = nums[:idx+1]
        nums= nums[idx+1:]
        for n1 in nums1:
            s += mx - n1
    print(f'#{tc} {s}')