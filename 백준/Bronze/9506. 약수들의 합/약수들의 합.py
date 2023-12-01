while True:
    n = int(input())
    tmp = 0
    arr = []
    if n == -1:
        break
    else:
        for i in range(1, n):
            if n % i == 0:
                tmp += i
                arr.append(i)
        if tmp == n:
            print(f'{n} = ', end="")
            for k in range(len(arr)-1):
                print(f'{arr[k]} + ', end="")
            print(f'{arr[-1]}')
        else:
            print(f'{n} is NOT perfect.')
            