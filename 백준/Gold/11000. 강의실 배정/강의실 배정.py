# 강의실 배정
import heapq

N = int(input())
q = []
for i in range(N):
    a, b = map(int, input().split())
    q.append((a, b))
q.sort()

endtime = []
heapq.heappush(endtime, q[0][1])
for i in range(1, N):
    # 강의 종료 시간보다 빠를 때
    if q[i][0] < endtime[0]:
        heapq.heappush(endtime, q[i][1]) # 강의실 추가
    # 강의 종료 시간보다 늦을 때
    else:
        heapq.heappop(endtime)
        heapq.heappush(endtime, q[i][1]) # 종료시간 갱신

print(len(endtime))