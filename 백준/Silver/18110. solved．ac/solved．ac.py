N = int(input())

if N == 0:
    print(0)
else:
    levels = [int(input()) for _ in range(N)]
    levels.sort()

    tmp = int(N * 0.15 + 0.5)
    lower = tmp
    upper = N - tmp

    print(int(sum(levels[lower:upper]) / (upper - lower) + 0.5))