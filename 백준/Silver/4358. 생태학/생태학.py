import sys
input = sys.stdin.readline

td = {}                             # 나무 이름 + 그루 담는 dictionary
total = 0                           # 전체 입력받은 나무 개수
for tree in sys.stdin:
    if tree == '\n':
        break
    else:
        tree = tree.strip('\n')
        total += 1
        if tree in td:
            td[tree] += 1
        else:
            td[tree] = 1
td = sorted(td.items())             # dictionary를 오름차순으로 정렬(리스트 형태)
                                    # [('Ash', 4), ('Aspen', 1), ...]
for t, n in td:
    p = round(n / total * 100, 4)   # 종류별 나무 개수 / 전체 개수 * 100 -> 반올림
    print(f'{t} {p:.4f}')           # f-string으로 정수도 소수점 넷째자리까지 표현