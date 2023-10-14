def dfs(depth, tmp, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(tmp, maximum)
        minimum = min(tmp, minimum)

    if plus:
        dfs(depth + 1, tmp + arr[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, tmp - arr[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, tmp * arr[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(tmp / arr[depth]), plus, minus, multiply, divide - 1)

N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

dfs(1, arr[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)