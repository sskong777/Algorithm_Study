from collections import deque
def solution(s):
    answer = True
    d = deque([])
    for c in s:
        # 괄호가 없는 경우 추가
        if not d:
            d.append(c)
        else:
            # 다음 확인할게 닫힘 괄호이고 마지막이 열림 괄호이면
            if c == ')' and d[-1] == '(':
                d.pop()
            else:
                d.append(c)
    # 다 닫지 못한경우
    if d:
        return False

    return True