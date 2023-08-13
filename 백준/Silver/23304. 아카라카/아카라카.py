def check(S ,n):
    if n == 0:
        return 1
    preS = S[:n]
    postS = S[-n:]
    if preS == preS[::-1] and postS == postS[::-1]:
        if check(preS, len(preS) // 2) and check(postS, len(postS) // 2):
            return 1
        else: return 0
    else:
        return 0

S = input()
n = len(S) // 2

if S == S[::-1]:
    if check(S, n) == 1:
        print("AKARAKA")
    else:
        print("IPSELENTI")
else:
    print("IPSELENTI")