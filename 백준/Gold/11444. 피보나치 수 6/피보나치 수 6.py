import sys
input = sys.stdin.readline

# 행렬 제곱
def power(matrix, n):
    if n == 1:
        return matrix
    elif n % 2:
        return mul(power(matrix, n - 1), matrix)
    else:
        return power(mul(matrix, matrix), n // 2)

# 행렬 곱셈
def mul(a, b):
    tmp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            s = 0
            for k in range(2):
                s += a[i][k] * b[k][j]
                tmp[i][j] = s % 1000000007
    return tmp

N = int(input())
matrix = [[1, 1], [1, 0]]
init = [[1], [1]]
if N < 3:
    print(1)
else:
    print(mul(power(matrix, N-2), init)[0][0])