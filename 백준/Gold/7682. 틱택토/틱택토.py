def win_check(string, char):
    if char == string[0] == string[1] == string[2] or \
        char == string[3] == string[4] == string[5] or \
        char == string[6] == string[7] == string[8] or \
        char == string[0] == string[3] == string[6] or \
        char == string[1] == string[4] == string[7] or \
        char == string[2] == string[5] == string[8] or \
        char == string[0] == string[4] == string[8] or \
        char == string[2] == string[4] == string[6]:
        return True
    return False

while True:
    board = input()
    if board == "end":
        break

    xcnt = board.count('X')
    ocnt = board.count('O')
    xwin = win_check(board, 'X')
    owin = win_check(board, 'O')

    # x가 이길 경우 : x가 이기고 o는 지고 x가 o보다 개수 하나 많음
    if xwin and not owin and xcnt - 1 == ocnt:
        print("valid")
        continue
    # o가 이길 경우 : o가 이기고 x는 지고 o가 x랑 개수 같음
    elif not xwin and owin and xcnt == ocnt:
        print("valid")
        continue
    # 아무도 안 이길 때 : x도 안 이기고 o도 안 이기고 x가 o보다 개수 하나 많음, 개수 합 9
    elif not xwin and not owin and xcnt - 1 == ocnt and xcnt + ocnt == 9:
        print("valid")
        continue
    # 그 외는 불가능
    else:   
        print("invalid") 
