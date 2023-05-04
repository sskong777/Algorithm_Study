# [3986] 좋은 단어

# 단어 수
n = int(input())
# 좋은 단어 수
answer = 0

for _ in range(n):
    word = input().rstrip()  # 문자열은~ 리스트로 전환하지 않아도 for문 사용 가능!
    stack = []   # stack = []

    for i in word:
        # 스택이 비어 있지 않고 현재 문자 i와 스택의 맨 위에 있는 문자가 같은 경우에만 True를 반환
        if len(stack) > 0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        answer += 1
print(answer)
