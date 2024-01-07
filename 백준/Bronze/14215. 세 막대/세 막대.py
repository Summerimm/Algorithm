tri = list(map(int, input().split()))
tri.sort()
if tri[0] + tri[1] > tri[2]:
    print(sum(tri))
else:
    print(2 * (tri[0] + tri[1]) - 1)