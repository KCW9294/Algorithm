def solution(s):
    lst = list(s)
    st = []
    answer = 0
    for _ in range(len(s)):
        for i in lst:
            if len(st)==0:
                st.append(i)
            else:
                if i == ']' and st[-1] == '[':
                    st.pop()
                elif i == '}' and st[-1] == '{':
                    st.pop()
                elif i == ')' and st[-1] == '(':
                    st.pop()
                else:
                    st.append(i)
        if len(st)==0:
            answer += 1
        st = []
        lst.append(lst.pop(0))

    return answer