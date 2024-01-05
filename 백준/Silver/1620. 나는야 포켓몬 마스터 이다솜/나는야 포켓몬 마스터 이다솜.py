N, M = map(int, input().split())
dct = {}
for i in range(N):
    dct[i+1] = input()

rev_dct = dict(map(reversed, dct.items()))

for _ in range(M):
    question = input()
    if question.isnumeric():
        question = int(question)
        print(dct[question])
    else:
        print(rev_dct[question])
