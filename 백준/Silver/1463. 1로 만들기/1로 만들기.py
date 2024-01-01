N = int(input())
arr = [0] * (1000001)
arr[2], arr[3] = 1, 1
for i in range(4, N+1):
    if i % 2 == 0 and i % 3 == 0:
        arr[i] = min(arr[i-1] + 1, arr[i//2] + 1, arr[i//3] + 1)
    elif i % 2 == 0:
        arr[i] = min(arr[i-1] + 1, arr[i//2] + 1)
    elif i % 3 == 0:
        arr[i] = min(arr[i-1] + 1, arr[i//3] + 1)
    else:
        arr[i] = arr[i-1] + 1
print(arr[N])