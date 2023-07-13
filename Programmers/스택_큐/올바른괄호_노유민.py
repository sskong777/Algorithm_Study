def solution(s):
    answer = True
    li=[]
    for i in s:
        if len(li)==0:
            li.append(i)
        else:
            if li[-1]=='(' and i==')':
                li.pop()
            else:
                li.append(i)
    if len(li)==0:
        answer=True
    else:
        answer= False
                

    return answer