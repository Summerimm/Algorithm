N = int(input())
x = []
y = []
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)
print((ymax - ymin) * (xmax - xmin))