m, n = map(int, input().split())
num_list = list(map(int, input().split()))

start = 0
end = 0
plus = 0 # 부분배열의 합
cnt = 0 # 경우의 수


while(start != m and end != m):
    plus = sum(num_list[start:end+1])
    if plus == n:
        cnt += 1
        start += 1
        continue
    elif plus < n:
        end += 1
        continue
    else:
        start += 1
        continue

print(cnt)