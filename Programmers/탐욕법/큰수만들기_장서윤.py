from collections import deque


def solution(number, k):
    stack = []
    number = deque(number)

    stack.append(number.popleft())  # stack 초기값 설정

    while number:
        n = number.popleft()  # number를 하나씩 빼줌
        # k가 0 보다 크고, stack의 마지막 값이 n보다 작으면
        while k > 0 and stack and stack[-1] < n:
            stack.pop()  # stack 에서 마지막 값을 빼줌
            k -= 1  # k 값도 1 감소시킴
        stack.append(n)

        # number에 남아있는 값을 모두 stack에 넣어줌
    for n in number:
        stack.append(n)

    '''
    값이 내림차순인 경우 number에서 k만큼 숫자가 제거되지 않았기 때문에
    k가 0이 될 때까지 stack에서 pop 해줌
    '''
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)