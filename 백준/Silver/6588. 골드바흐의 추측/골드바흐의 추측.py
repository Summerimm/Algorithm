import sys
input = sys.stdin.readline

r= 1000000
prime = [True for _ in range(r)]
for i in range(2, int(r**0.6)):
    if prime[i] == True:
        for j in range(i * 2, r, i) : 
            if prime[j] == True :
                prime[j] = False            #에라토스테네스의 체

while(True):
    n = int(input())
    if n == 0: 
        break
    for i in range(3, r):
        if prime[i] == True and prime[n - i] == True:
                print(f"{n} = {i} + {n - i}")
                break