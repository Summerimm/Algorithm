L = int(input())
string = input()

ans = 0
for i in range(L):
    ans += (ord(string[i]) - 96) * (31 ** i)
print(ans % 1234567891)