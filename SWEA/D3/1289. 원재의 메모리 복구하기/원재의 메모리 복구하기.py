T = int(input())
for test_case in range(1, T + 1):
    st = '0'+input()
    ans = 0
    for i in range(1, len(st)):
        if st[i - 1] != st[i]:
            ans += 1
 
    print(f'#{test_case} {ans}')