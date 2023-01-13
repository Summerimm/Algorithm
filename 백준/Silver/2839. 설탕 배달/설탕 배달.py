n = int(input())
x = n // 5
y = n // 3
a = []
b = []

for i in range(x+1):
    for j in range(y+1):
        if 5 * i + 3 * j == n:
            a.append(i)
            b.append(j)
            
if a == [] and b == []:
    print(-1)
else:
    add_list = [a[i] + b[i] for i in range(len(a))]
    print(min(add_list))