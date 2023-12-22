while True:
    sentence = input()
    st = []

    if sentence == '.':
        break
    
    for tmp in sentence:
        if tmp == '[' or tmp == '(':
            st.append(tmp)
        elif tmp == ']':
            if st and st[-1] == '[':
                st.pop()
            else:
                st.append(']')
                break
        elif tmp == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                st.append(')')
                break
    if st:
        print('no')
    else:
        print('yes')
