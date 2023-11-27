def checkHeart():
    for i in range(N):
        for j in range(N):
            if cookie[i][j] == '*':
                return (i+1, j)

def checkLeftArm(heart_i, heart_j):
    cnt = 0
    for j in range(heart_j):
        if cookie[heart_i][j] == '*':
            cnt += 1
    return cnt

def checkRightArm(heart_i, heart_j):
    cnt = 0
    for j in range(heart_j+1, N):
        if cookie[heart_i][j] == '*':
            cnt += 1
        if cookie[heart_i][j] == '_':
            break
    return cnt

def checkWaist(heart_i, heart_j):
    global waist_i, waist_j
    cnt = 0
    for i in range(heart_i+1, N):
        if cookie[i][heart_j] == '*':
            cnt += 1
        if cookie[i][heart_j] == '_':
            waist_i = i-1
            waist_j = heart_j
            break
    return cnt

def checkLeftLeg(waist_i, waist_j):
    cnt = 0
    for i in range(waist_i+1, N):
        if cookie[i][waist_j-1] == '*':
            cnt += 1
        if cookie[i][waist_j-1] == '_':
            break
    return cnt

def checkRightLeg(waist_i, waist_j):
    cnt = 0
    for i in range(waist_i+1, N):
        if cookie[i][waist_j+1] == '*':
            cnt += 1
        if cookie[i][waist_j+1] == '_':
            break
    return cnt

N = int(input())
cookie = [list(map(str, input())) for _ in range(N)]

heart_i, heart_j = checkHeart()
waist_i, waist_j = 0, 0

left_arm_cnt = checkLeftArm(heart_i, heart_j)
right_arm_cnt = checkRightArm(heart_i, heart_j)
waist_cnt = checkWaist(heart_i, heart_j)

left_leg_cnt = checkLeftLeg(waist_i, waist_j)
right_leg_cnt = checkRightLeg(waist_i, waist_j)
print(heart_i+1, heart_j+1)
print(left_arm_cnt, right_arm_cnt, waist_cnt, left_leg_cnt, right_leg_cnt)
