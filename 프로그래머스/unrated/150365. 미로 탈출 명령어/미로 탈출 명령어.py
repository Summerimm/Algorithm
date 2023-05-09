import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
s = ['d', 'l', 'r', 'u']
answer = 'z'

def dfs(n, m, x, y, r, c, string, cnt, k):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):   # cnt가 k-최단거리를 넘어버림
        return
    if x == r and y == c and cnt == k:  # 조건에 맞는 문자열 완성(사전 순 고려됨)
        answer = string
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m and string < answer:   # 사전 순으로 작을 때만 dfs
            dfs(n, m, nx, ny, r, c, string+s[i], cnt+1, k)

def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)  # 최단 거리
    
    if k < dist or (k - dist) % 2:
        return "impossible"
    
    dfs(n, m, x, y, r, c, "", 0, k)

    return answer