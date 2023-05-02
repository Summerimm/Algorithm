import math

def check(start, end, binaryNum):
    if start == end:
        return binaryNum[start]
    mid = (start + end) // 2
    left = check(start, mid-1, binaryNum)
    if not left or (left == '1' and binaryNum[mid] == '0'):
        return False
    right = check(mid+1, end, binaryNum)
    if not right or (right == '1' and binaryNum[mid] == '0'):
        return False
    return binaryNum[mid]

def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num).lstrip('0b')       # 주어진 숫자를 이진수로 변환
        l1 = len(b)     # 이진수로 변환했을 때 길이
        l2 = 2**(int(math.log2(l1)) + 1) - 1 # 주어진 숫자를 이진수로 바뀌었을 때 포화이진트리가 되기 위한 길이
        b = b.zfill(l2) # 포화이진트리 길이만큼 왼쪽에 0 채우기
        
        if check(0, len(b)-1, b):
            answer.append(1)
        else:
            answer.append(0)
                
    return answer