while True:
    try: 
        n = int(input())
    except: 
        break
    s = 0 # sum
    i = 0 # 자릿수
    while True:
        i += 1
        s = s * 10 + 1
        if s % n == 0:
            print(i)
            break