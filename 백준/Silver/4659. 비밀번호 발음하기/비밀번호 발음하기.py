aeiou = ['a', 'e', 'i', 'o', 'u']
def checkVowel(string):
    for c in string:
        if c in aeiou:
            return True
    return False

def checkThree(pw):
    for i in range(len(pw)-2):
        if pw[i] in aeiou and pw[i+1] in aeiou and pw[i+2] in aeiou:
            return False
        elif pw[i] not in aeiou and pw[i+1] not in aeiou and pw[i+2] not in aeiou:
            return False
    return True

def checkTwo(pw):
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1] and pw[i] != 'e' and pw[i] != 'o':
            return False
    return True

while True:
    pw = input()
    if pw == 'end':
        break
    else:
        if checkVowel(pw) and checkThree(pw) and checkTwo(pw):
            print(f'<{pw}> is acceptable.')
        else:
            print(f'<{pw}> is not acceptable.')