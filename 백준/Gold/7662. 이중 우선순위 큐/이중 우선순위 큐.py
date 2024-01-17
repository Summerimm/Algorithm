import heapq

T = int(input())
for _ in range(T):
    K = int(input())
    visited = [0] * K

    maxheap = []
    minheap = []

    for i in range(K):
        cmd, num = map(str, input().split())
        num = int(num)

        if cmd == 'I':
            heapq.heappush(maxheap, (-num, i))
            heapq.heappush(minheap, (num, i))
            visited[i] = 1
        elif num == 1:
            # 앞에서 이미 삭제된 원소들 처리
            while maxheap and not visited[maxheap[0][1]]:
                heapq.heappop(maxheap)
            if maxheap:
                visited[maxheap[0][1]] = 0
                heapq.heappop(maxheap)
        else:
            # 앞에서 이미 삭제된 원소들 처리
            while minheap and not visited[minheap[0][1]]:
                heapq.heappop(minheap)
            if minheap:
                visited[minheap[0][1]] = 0
                heapq.heappop(minheap)
    
    # 마지막까지 처리 안 된 원소들 처리
    while maxheap and not visited[maxheap[0][1]]:
        heapq.heappop(maxheap)
    while minheap and not visited[minheap[0][1]]:
        heapq.heappop(minheap)

    if not minheap:
        print("EMPTY")
    else:
        print(-maxheap[0][0], minheap[0][0])