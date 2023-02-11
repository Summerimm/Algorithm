def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
for i in range(n):
    snum = input()
    if '(' in snum: # 순환소수일 때 0.6(142857)
        snum = snum.strip(')').replace('0.','')
        notinf, inf  = map(str, snum.split('(')) # 6 142857
        # 분모
        deno = int(len(inf) * '9' + len(notinf) * '0') # 9999990
        # 분자
        if notinf == '': # 0.()일 경우
            notinf = '0'
        nume = int(notinf + inf) - int(notinf) # 6142857 - 6

    else: # 순환소수가 아닐 때
        snum = snum.replace('0.','') # 0을 앞에 붙이기 위함
        deno = 10 ** len(snum)
        nume = int(snum)

    # 기약분수
    g = gcd(deno, nume)
    print(f'{nume // g}/{deno // g}')