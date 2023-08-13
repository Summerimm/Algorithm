# 로봇 프로젝트
def getsum(n):
    s = 0
    e = n-1
    while s < e:
        if arr[s] + arr[e] == W:
            return (arr[s], arr[e])
        elif arr[s] + arr[e] < W:
            s += 1
        elif arr[s] + arr[e] > W:
            e -= 1
    return (0, 0)

while True:
    try:
        W = int(input()) * 10_000_000
        N = int(input())
        arr = [int(input()) for _ in range(N)]
        arr.sort()

        a, b = getsum(N)
        if a == 0 and b == 0:
            print("danger")
        else:
            print("yes", a, b)
    except:
        break