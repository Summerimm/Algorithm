N = int(input())
p1, p2 = 100, 100
for _ in range(N):
    a, b = map(int, input().split())
    if a < b:
        p1 -= b
    elif b < a:
        p2 -= a
print(p1)
print(p2)