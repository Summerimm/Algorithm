while True:
    ans = 0
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    ans = M + F
    print(ans)