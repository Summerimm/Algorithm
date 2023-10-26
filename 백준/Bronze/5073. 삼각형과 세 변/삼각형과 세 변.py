nums = [0, 0, 0]
while True:
    a, b, c = map(int, input().split())
    nums[0], nums[1], nums[2] = a, b, c
    nums.sort()
    if nums[0] == 0:
        break
    elif nums[2] >= nums[1] + nums[0]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")