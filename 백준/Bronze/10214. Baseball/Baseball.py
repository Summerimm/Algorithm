T = int(input())
for _ in range(T):
    Y, K = 0, 0
    for _ in range(9):
        tmp_y, tmp_k = map(int, input().split())
        Y += tmp_y
        K += tmp_k
    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")