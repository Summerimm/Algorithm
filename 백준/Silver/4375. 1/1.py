while True:
    try:
        n = int(input()) # 3
        digit = '1' # 자릿수
        while True:
            one = int(digit)
            if one % n == 0:
                print(len(str(one)))
                break
            else:
                digit += '1' # 11, 111, 1111...
    except:
        break