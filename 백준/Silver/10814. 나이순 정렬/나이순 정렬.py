N = int(input())
arr = []
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, i, name))

arr.sort()
for i in range(N):
    print(arr[i][0], arr[i][2])