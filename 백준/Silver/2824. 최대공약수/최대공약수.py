n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
mula = 1
mulb = 1
for num in a:
    mula *= num
for num in b:
    mulb *= num

if mula < mulb:
    mula, mulb = mulb, mula

while mulb != 0:
    r = mula % mulb
    mula = mulb
    mulb = r

print(str(mula)[-9:])