parentheis = list(input())

stack = []
mul = 1
ans = 0

for i, p in enumerate(parentheis):
    if p == '(':
        stack.append(p) # stack에 쌓기
        mul *= 2 # ( 시작할 때 2곱하기
    elif p == '[':
        stack.append(p) # stack에 쌓기
        mul *= 3 # [ 시작할 때 3곱하기
    elif p == ')':
        if stack == [] or stack[-1] == '[': # )를 넣을 때 스택이 비어있거나 스택 맨 위가 [일 떄
            ans = 0
            break
        elif parentheis[i-1] == '(': # 가장 안쪽이 ()일 때
            ans += mul # 여태까지 계산한 값을 답에 더해줌
        stack.pop() # ()이든 (())이든 pop
        mul //= 2 # 빠져나올 때마다 괄호 풀었을 때의 값으로 복귀, 열린 괄호가 남아있으면 1이 안 됨

    else: # ']'
        if stack == [] or stack[-1] == '(': # ]를 넣을 때 스택이 비어있거나 스택 맨 위가 (일 떄
            ans = 0
            break
        elif parentheis[i-1] == '[': # 가장 안쪽이 []일 때
            ans += mul # 여태까지 계산한 값을 답에 더해줌
        stack.pop() # []이든 [[]]이든 pop
        mul //= 3 # 빠져나올 때마다 괄호 풀었을 때의 값으로 복귀, 열린 괄호가 남아있으면 1이 안 됨

if stack: # 과정을 끝마쳤는데도 스택에 괄호가 남아있으면
    ans = 0
print(ans)