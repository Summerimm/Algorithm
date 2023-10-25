h, w, n, m = map(int, input().split())
row = (w - 1) // (m + 1) + 1
col = (h - 1) // (n + 1) + 1
print(row * col)