import sys
sys.setrecursionlimit(100000)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

N, K = map(int, input().split())
ans = (factorial(N) // (factorial(N-K) * factorial(K))) % 10007
print(ans)