# 뒤집힌 덧셈

x, y = input().split()
z = int(x[::-1]) + int(y[::-1])
print(int(str(z)[::-1]))