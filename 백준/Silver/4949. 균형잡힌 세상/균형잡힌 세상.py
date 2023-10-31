while True:
    temp = input()
    if temp!='.':
        stack = []
        go_break = False
        for i in temp:
            if i=='(':
                stack.append(i)
            elif i==')':
                if not stack:
                    print('no')
                    go_break = True
                    break
                else:
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        print('no')
                        go_break = True
                        break
            elif i=='[':
                stack.append(i)
            elif i==']':
                if not stack:
                    print('no')
                    go_break = True
                    break
                else:
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        print('no')
                        go_break = True
                        break
            else:
                continue
        if not go_break:
            if not stack:
                print('yes')
            else:
                print('no')
    else:
        break
