# keys에 key값(idx)을 적어 관리
keys = [[0] * 51 for _ in range(51)]
idx = 1
# 1부터 키 값 할당
for i in range(1, 51):
    for j in range(1, 51):
        keys[i][j] = idx
        idx += 1
dct = {}

def change(r, c, value):
    dct[keys[r][c]] = value

def get_target(key):
    targets = []
    for i in range(1, 51):
        for j in range(1, 51):
            if keys[i][j] == key: targets.append([i, j])
    return targets

def update(command):
    if len(command) == 4:       # "UPDATE r c value"
        ud, r, c, value = command
        r, c = int(r), int(c)
        change(r, c, value)
    if len(command) == 3:       # "UPDATE value1 value2"
        ud, value1, value2 = command
        for i in range(1, 51):
            for j in range(1, 51):
                if keys[i][j] in dct and dct[keys[i][j]] == value1:
                    change(i, j, value2)

def merge(command):
    mg, r1, c1, r2, c2 = command    # "MERGE r1 c1 r2 c2"
    r1, r2, c1, c2 = int(r1), int(r2), int(c1), int(c2)

    if r1 == r2 and c1 == c2:    # 같은 좌표의 경우 무시
        return
    if keys[r1][c1] in dct:      # (r1, c1) 값이 있을 때, (r1, c1)값으로 merge
        targets = get_target(keys[r2][c2])  # (r2, c2)와 연결된 셀들의 r, c 좌표 구하기
        for x, y in targets:
            keys[x][y] = keys[r1][c1]
    elif keys[r2][c2] in dct:    # (r1, c1) 값이 없을 때, (r2, c2)값으로 merge
        targets = get_target(keys[r1][c1])  # (r1, c1)와 연결된 셀들의 r, c 좌표 구하기
        for x, y in targets:
            keys[x][y] = keys[r2][c2]
    else:   # 모두 (r1, c1)의 값으로 통일
        targets = get_target(keys[r2][c2])  # (r2, c2)와 연결된 셀들의 r, c 좌표 구하기
        for x, y in targets:
            keys[x][y] = keys[r1][c1]
        

def ummerge(command):
    global idx
    um, r, c = command  # "UNMERGE r c"
    r, c = int(r), int(c)
    # 완전 탐색하며 r,c와 같은 키값을 같는 값들을 찾아 키 값을 새로 할당
    for i in range(1, 51):
        for j in range(1, 51):
            if i == r and j == c: continue
            if keys[i][j] == keys[r][c]:
                keys[i][j] = idx
                idx += 1

def print_key(command):
    pt, r, c = command
    r, c = int(r), int(c)
    
    if keys[r][c] in dct:
        return dct[keys[r][c]]
    else:
        return "EMPTY"
                
def solution(commands):
    answer = []
    for command in commands:
        command = command.split()
        if command[0] == "UPDATE": update(command)
        elif command[0] == "MERGE": merge(command)
        elif command[0] == "UNMERGE": ummerge(command)
        elif command[0] == "PRINT": 
            answer.append(print_key(command))

    return answer