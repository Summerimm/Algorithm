x, y, w, h = map(int, input().split())
a = min(w-x, h-y)
b = min(x, y)
print(min(a, b))