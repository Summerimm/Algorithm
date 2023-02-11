import sys
input = sys.stdin.readline

# 유클리드 호제법으로 gcd 구한 뒤, num1 * num2 / gcd = lcm 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

dgcd = gcd(b1, b2) # 분모끼리의 최대공약수 1
dlcm = b1 * b2 // dgcd # 더했을 때의 분모 (7 * 5) / 1
n1 = dlcm // b1 * a1 # 더했을 때의 분자1 (35 / 7) * 2
n2 = dlcm // b2 * a2 # 더했을 때의 분자2 (35 / 5) * 3
fgcd = gcd(n1 + n2, dlcm) # 기약분수로 만들기 위함
print((n1 + n2) // fgcd , dlcm // fgcd)