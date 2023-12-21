N = int(input())
ans = 0
num = 0
while ans < N:
    num += 1
    strnum = str(num)
    if '666' in strnum:
        ans += 1
print(strnum)
