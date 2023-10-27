# 집합
import sys
from collections import deque

input = sys.stdin.readline
m = int(input())
S = deque()

for _ in range(m):
    cmd = input().rstrip('\n')
    if cmd == 'all':
        S = [i for i in range(1, 21)]
    elif cmd == 'empty':
        S = deque()
    else:
        subcmd, num = cmd.split()
        num = int(num)
        if subcmd == 'add' and num not in S:
            S.append(num)
        elif subcmd == 'remove' and num in S:
            S.remove(num)
        elif subcmd == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif subcmd == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)