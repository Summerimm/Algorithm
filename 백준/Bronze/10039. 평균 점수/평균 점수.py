s = 0
for _ in range(5):
    tmp = int(input())
    if tmp < 40:
        s += 40
    else:
        s += tmp
print(s // 5)