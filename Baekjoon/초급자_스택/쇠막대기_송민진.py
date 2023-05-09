# 시도 2 - 풀이 참고
import sys
input = sys.stdin.readline

stack = []
answer = 0
str = input().strip()
for i in range(len(str)):
    if str[i] == "(":
        stack.append(str[i])
    elif str[i-1] == "(":
        stack.pop()
        answer += len(stack)
    else:
        stack.pop()
        answer += 1

print(answer)