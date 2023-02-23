arr = list(map(int, input()))

if 0 not in arr or len(arr) == 1:
    print(-1)
else:
    if sum(arr) % 3:
        print(-1)
    else:
        arr.sort(reverse=True)
        print(''.join(map(str, arr)))