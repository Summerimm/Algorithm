import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int,input().split()))
large = tmp; small = tmp

for i in range(n-1):
    a, b, c = map(int,input().split())
    large = [max(large[0], large[1]) + a, max(large) + b, max(large[1],large[2]) + c]
    small = [min(small[0], small[1]) + a, min(small) + b, min(small[1],small[2]) + c]

print(max(large), min(small))