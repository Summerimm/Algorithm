from copy import deepcopy

N = int(input())
arr = list(map(int, input().split()))
arrcopy = deepcopy(list(set(arr)))
arrcopy.sort()

ansdct = {}
for i in range(len(arrcopy)):
    ansdct[arrcopy[i]] = i

for i in range(N-1):
    print(ansdct[arr[i]], end=" ")
print(ansdct[arr[-1]])