from queue import PriorityQueue
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
prime = list(map(int, input().split()))

q = PriorityQueue()     # 우선순위 큐
for num in prime:
    q.put(num)          # 주어진 소수들 넣기

for i in range(N):      # 큐에서 N번 빼면 그 때의 값이 N번째 값
    num = q.get()
    for j in range(K):  # 뺀 값에 소수를 곱해서 push
        new_num = num * prime[j]
        q.put(new_num)

        if num % prime[j] == 0: # 2 * 3(X)/ 3 * 2(O) -> 중복제거 위함
            break
else:
    print(num)