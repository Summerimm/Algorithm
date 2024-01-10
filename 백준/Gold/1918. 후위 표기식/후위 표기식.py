equation = list(input())

op = {'(': -1, '*': 1, '/': 1, '+': 0, '-': 0}   # 우선순위 별 가중치

ansstack = []
opstack = []
for c in equation:
    if c.isalpha():
        ansstack.append(c)
    else:
        # 여는 괄호면 일단 넣기
        if c == '(':
            opstack.append(c)
        # 닫는 괄호면 여는 괄호 나올 때까지 빼서 결과에 넣기
        elif c == ')':
            while opstack[-1] != '(':
                tmp = opstack.pop()
                ansstack.append(tmp)
            opstack.pop()
        # opstack을 확인 후 최상단 기호의 우선순위가 더 낮으면 넣기
        elif opstack and op[opstack[-1]] < op[c]:
            opstack.append(c)
        # opstack을 확인 후 최상단 기호의 우선순위가 더 높거나 같으면 
        # 최상단 기호가 우선순위 더 낮을 때까지 결과에 옮기고 넣기
        elif opstack and op[opstack[-1]] >= op[c]:
            while opstack and op[opstack[-1]] >= op[c]:
                tmp = opstack.pop()
                ansstack.append(tmp)
            opstack.append(c)
        elif not opstack:
            opstack.append(c)
            
while opstack:
    tmp = opstack.pop()
    ansstack.append(tmp)
    
print(''.join(map(str, ansstack)))