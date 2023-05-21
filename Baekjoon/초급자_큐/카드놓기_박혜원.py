# [18115] 카드놓기

from collections import deque

n = int(input())  # 카드 개수
# 기술을 N번 사용하여 카드를 다 내려놓았을 때, 1, 2, …, N이라면
# 카드 더미(stack)는 N, .., 2, 1로 만들어진다.
# stack를 역순으로 하지않을 경우에는 stack.pop() -> stack.popleft()로 바꿔주면 됨.
stack = [i for i in range(n, 0, -1)]
actions = list(map(int, input().split()))  # 기술
actions.reverse()  # 기술의 순서를 뒤집어서 역순으로 실행
result = deque()

for action in actions:
    if action == 1:
        # 제일 위의 카드 1장을 바닥에 내려놓는다.
        # stack에서 가장 위의 카드를 꺼내(result의 왼쪽에) 넣기
        result.appendleft(stack.pop())

    elif action == 2:
        # 위에서 두 번째 카드를 바닥에 내려놓는다.
        # stack에서 카드를 꺼내 result의 두 번째 위치에 넣기
        result.insert(1, stack.pop())

    elif action == 3:
        # 제일 밑에 있는 카드를 바닥에 내려놓는다.
        # stack에서 카드를 꺼내 result의 가장 오른쪽에 넣기
        result.append(stack.pop())

print(*result)
