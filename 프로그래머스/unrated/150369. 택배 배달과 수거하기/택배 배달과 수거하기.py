def solution(cap, n, deliveries, pickups):
    answer = 0
    # greedy하게 풀이, 최대한 멀리 나가서 돌아오기 (거리 * 2)
    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    delivernum = 0      # 배달해야 할 양
    pickupnum = 0    # 수거해야 할 양
    for i in range(n):
        delivernum += deliveries[i]
        pickupnum += pickups[i]
        
        while delivernum > 0 or pickupnum > 0:   
            # 배달이 더 뒤에 있을 수도, 수거가 더 뒤에 있을 수도 있음
            # 가장 먼 곳에서 배달 혹은 수거 처리
            delivernum -= cap
            pickupnum -= cap
            # 음수라면 앞에서 가는 길에 처리 가능하단 것
            answer += (n - i) * 2
        
    return answer