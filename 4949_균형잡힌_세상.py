while True:
    string=input()
    list_string=[]
    
    if string=='.':
        break

    for i in string:
        if i=='(' or i=='[':
            list_string.append(i)
        elif i==')':
            if len(list_string)==0 or list_string[-1]!='(':
                list_string.append(i)
                break
            else:
                del list_string[-1]

        elif i==']':
            if len(list_string)==0 or list_string[-1]!='[':
                list_string.append(i)
                break
            else:
                del list_string[-1]


    if len(list_string)==0:
        print('yes')
    else:
        print('no')