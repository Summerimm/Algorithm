aq = []
bq = []
for _ in range(3):
    a, b = map(int, input().split())
    if a not in aq:
        aq.append(a)
    else:
        aq.remove(a)
    if b not in bq:
        bq.append(b)
    else:
        bq.remove(b)
print(*aq, *bq)
