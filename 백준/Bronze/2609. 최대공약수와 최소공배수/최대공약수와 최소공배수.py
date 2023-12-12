a, b = map(int, input().split())
mn = min(a, b)

for i in range(1, mn+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)
print(gcd * (a // gcd) * (b // gcd))