def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        # 처음에 ')' 가 들어오면 False 리턴 + '('들어온 뒤에 ')'들어오면 stack에서 제거
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
