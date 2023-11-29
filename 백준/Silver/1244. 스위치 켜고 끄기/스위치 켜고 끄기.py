def switch(k):
    if arr[k]:
        arr[k] = 0
    else:
        arr[k] = 1

def boy_switch(num, N):
    for i in range(1, N+1):
        if i % num == 0:
            switch(i)

def girl_switch(num, N):
    if N % 2:
        half = N // 2 + 1
        if num >= half:
            diff = N - num
        else:
            diff = num - 1
    else:
        half = N // 2
        if num >= half + 1:
            diff = N - num
        else:
            diff = num - 1
    switch(num)
    for i in range(1, diff+1):
        if arr[num-i] == arr[num+i]:
            switch(num-i)
            switch(num+i)
        else:
            break

N = int(input())
arr = [0] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:
        boy_switch(num, N)
    else:
        girl_switch(num, N)

for i in range(1, N+1):
    print(arr[i], end=" ")
    if i % 20 == 0:
        print()
