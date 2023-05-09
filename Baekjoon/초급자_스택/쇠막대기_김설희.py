stick = input()
stack = []
anw = 0

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append('(')
    # 레이저인지 아닌지 확인해야 함
    else:
        # 레이저이면,
        if stick[i-1] == '(':
            # 스택에서 일단 없애고,
            stack.pop()
            # 스택 개수 만큼 더해서 막대기 2배
            anw += len(stack)
        # 레이저 아니면, 막대기 끝난 거임
        else:
            stack.pop()
            # 잘린 마지막 부분을 고려해서 +1 해줌
            anw += 1

print(anw)