cnt = 1
st = []
op = []
flag = 1

N = int(input())
for i in range(N):
    num = int(input())
    while cnt <= num:
        st.append(cnt)
        op.append('+')
        cnt += 1
    
    if st[-1] == num:
        st.pop()
        op.append('-')
    
    else:
        flag = 0
        break
    
if not flag:
    print('NO')
else:
    for k in op:
        print(k)