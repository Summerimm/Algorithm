N = int(input())

arr = []
for _ in range(N):
    word = input()
    if (len(word), word) not in arr:
        arr.append((len(word), word))

arr.sort()
for i in range(len(arr)):
    print(arr[i][1])