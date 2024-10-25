n = int(input())
answer = 0
data = []
num = 0
for i in range(n): 
    x, y = map(int,input().split())
    data.append([x, y])
for i in range(n - 1):
    answer += abs(data[i][0] - data[i + 1][0]) + abs(data[i][1] - data[i + 1][1])
for i in range(1, n-1):
    stra = abs(data[i+1][0] - data[i-1][0]) + abs(data[i+1][1] - data[i-1][1])
    dis = abs(data[i][0] - data[i+1][0]) + abs(data[i][1] - data[i+1][1]) + abs(data[i][0] - data[i-1][0]) + abs(data[i][1] - data[i-1][1])
    num = max(num, dis - stra)
print(answer - num)