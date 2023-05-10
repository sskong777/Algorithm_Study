from collections import deque

n = int(input())

cards = deque(i+1 for i in range(n))
result = []

while True:
    if len(cards) == 1:
        break
    result.append(cards.popleft())
    cards.append(cards.popleft())

result.append(cards[0])

for i in result:
    print(i, end = " ")