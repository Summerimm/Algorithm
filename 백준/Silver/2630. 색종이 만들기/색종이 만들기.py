def divide_conquer(x, y, n):
    global blue, white
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                divide_conquer(x, y, n // 2)
                divide_conquer(x, y + n // 2, n // 2)
                divide_conquer(x + n // 2, y, n // 2)
                divide_conquer(x + n // 2, y + n // 2, n // 2)
                return
    if color:
        blue += 1
    else:
        white += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

divide_conquer(0, 0, N)
print(white)
print(blue)