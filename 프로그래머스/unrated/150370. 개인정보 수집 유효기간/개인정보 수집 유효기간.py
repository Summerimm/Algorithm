def solution(today, terms, privacies):
    ans = []
    
    # 오늘 연, 월, 일
    t_year = int(today[:4])
    t_month = int(today[5:7])
    t_day = int(today[8:])
    
    # 알파벳에 따른 유효기간 딕셔너리에 저장
    dct = {}
    for term in terms:
        dct[term[0]] = int(term[2:])

    # 쿼리 순환
    for idx, query in enumerate(privacies):
        # 해당 고객 연, 월, 일, 약관 타입
        q_year = int(query[:4])
        q_month = int(query[5:7])
        q_day = int(query[8:10])
        q_type = query[11]
        
        # 개월 수를 더했을 때 12 넘어갈 경우 처리
        tmp = dct[q_type]
        yeartmp = tmp // 12
        monthtmp = tmp % 12
        q_year += yeartmp
        q_month += monthtmp
        
        if q_month > 12:
            q_year += 1
            q_month -= 12
        
        # 약관 유효기간 계산 (하루 전까지 유효)
        q_day -= 1
        if q_day == 0:
            q_day = 28
            q_month -= 1
            if q_month == 0:
                q_month = 12
                q_year -= 1
        
        q = [q_year, q_month, q_day]
        t = [t_year, t_month, t_day]
        
        if q < t:
            ans.append(idx+1)
    return ans