V, E = map(int, input().split())
INF = 1e9
arr = [[INF] * (V) for _ in range(V)]

for i in range(V):
    for j in range(V):
        if i == j:
            arr[i][j] = 0

for i in range(E):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for k in range(V):
    for i in range(V):
        for j in range(V):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

mx = 0
for i in range(V):
    for j in range(V):
        mx = max(mx, arr[i][j])

if mx > 6:
    print('Big World!')
else:
    print('Small World!')