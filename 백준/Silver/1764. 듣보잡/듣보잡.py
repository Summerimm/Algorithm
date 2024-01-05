N, M = map(int, input().split())
dct1, dct2 = {}, {}
for i in range(N):
    dct1[input()] = i
for j in range(M):
    dct2[input()] = i

arr = []
for name in dct1.keys():
    if name in dct2.keys():
        arr.append(name)
arr.sort()

print(len(arr))
for name in arr:
    print(name)