import sys

input = sys.stdin.readline

result = []
while True:
    li = input().rstrip()
    stack = []

    if li == ".":
        break

    for i in li:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()  # 맞으면 지워서 stack을 비워줌 0 = yes
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)
