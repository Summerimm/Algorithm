T = int(input())
for tc in range(1, T+1):
    n = int(input())
    k = round(n**(1/3), 3)
    if int(k) == k:
        print(f'#{tc} {int(k)}')
    else:
        print(f'#{tc} -1')