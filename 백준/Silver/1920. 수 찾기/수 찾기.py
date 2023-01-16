n = int(input())
ans_list = set(map(int, input().split()))
m = int(input())
unknown = list(map(int, input().split()))

for i in range(m):
    print(1) if unknown[i] in ans_list else print(0)