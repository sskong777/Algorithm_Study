def solution(s):
    answer = True
    stack = []
    
    if s[0] == ')':
        return False
    
    for a in s:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if len(stack) != 0:
                stack.pop()
    
    if len(stack) != 0:
        answer = False
    else:
        answer = True

    return answer