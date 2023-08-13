# N-Queen

def queen(col, row):
    global ans
    check[col] = row
    for i in range(N):
        if i != col and check[i] != 0 and abs(check[i] - check[col]) == abs(i - col):
            check[col] = 0
            return
    if row == N:
        ans += 1
    for j in range(N):
        if check[j] == 0:
            queen(j, row + 1)
        if j == N-1:
            check[col] = 0

N = int(input())
check = [0] * N
ans = 0
for i in range(N):
    queen(i, 1)
print(ans)