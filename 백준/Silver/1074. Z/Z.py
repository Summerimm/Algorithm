def divide_conquer(x, y, n):
    global cnt
    if x > r or x + n <= r or y > c or y + n <= c:
        cnt += n ** 2
        return 

    if n > 2:
        n //= 2
        divide_conquer(x, y, n)
        divide_conquer(x, y + n, n)
        divide_conquer(x + n, y, n)
        divide_conquer(x + n, y + n, n)
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)
        exit()

N, r, c = map(int, input().split())
cnt = 0
divide_conquer(0, 0, 2**N)