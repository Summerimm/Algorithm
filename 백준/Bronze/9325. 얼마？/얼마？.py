T = int(input())
for _ in range(T):
    ans = int(input())
    n = int(input())
    for _ in range(n):
        num, option = map(int, input().split())
        ans += num * option
    print(ans)