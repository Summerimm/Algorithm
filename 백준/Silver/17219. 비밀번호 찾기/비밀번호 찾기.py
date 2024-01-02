N, M = map(int, input().split())
dct = {}
for _ in range(N):
    site, pw = map(str, input().split())
    dct[site] = pw

for _ in range(M):
    find_site = input()
    print(dct[find_site])