N = int(input())
info = []
for _ in range(N):
    arr = list(input().split())
    info.append(arr[1:])
    info.sort()

dash = '--'
answer = []
for i in range(N):
    if i == 0:
        for j in range(len(info[i])):
            answer.append(dash * j + info[i][j])
    else:
        idx = 0     # 이전 리스트와 현재 리스트 비교하여 겹치는 원소 개수
        for j in range(len(info[i])):
            # 앞 리스트의 원소와 현재 리스트의 원소가 다르거나 앞 리스트 길이가 더 짧을 경우
            if info[i-1][j] != info[i][j] or len(info[i-1]) <= j:
                break
            # 겹치는 원소 존재
            idx = j + 1
        for num in range(idx, len(info[i])):
            answer.append(dash * num + info[i][num])

for ans in answer:
    print(ans)