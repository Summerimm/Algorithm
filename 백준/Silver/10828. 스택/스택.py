import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    input_string = sys.stdin.readline().split()
    cmd = input_string[0]
    
    if cmd == 'push':
        num = input_string[1]
        stack.append(num)
    
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])