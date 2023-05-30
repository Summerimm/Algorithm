def solution(survey, choices):
    scoreboard = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    
    for i in range(len(survey)):
        score = choices[i]
        disagree_type = survey[i][0]
        agree_type = survey[i][1]
        if score > 4:
            scoreboard[agree_type] += score - 4
        else:
            scoreboard[disagree_type] += 4 - score
    print(scoreboard)
    
    if scoreboard['R'] >= scoreboard['T']:
        answer += 'R'
    else: 
        answer += 'T'
        
    if scoreboard['C'] >= scoreboard['F']:
        answer += 'C'
    else: 
        answer += 'F'
        
    if scoreboard['J'] >= scoreboard['M']:
        answer += 'J'
    else: 
        answer += 'M'
        
    if scoreboard['A'] >= scoreboard['N']:
        answer += 'A'
    else: 
        answer += 'N'

    return answer