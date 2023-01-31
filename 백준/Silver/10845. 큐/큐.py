import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    input_string = sys.stdin.readline().split()
    cmd = input_string[0]
    
    if cmd == 'push':
        num = input_string[1]
        queue.append(num)
    
    elif cmd == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif cmd == 'size':
        print(len(queue))

    elif cmd == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif cmd == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])