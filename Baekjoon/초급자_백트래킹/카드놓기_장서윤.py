n = int(input())
k = int(input())

card = list()
select = list()
cards = set()

isUsed = [False for _ in range(n)]

for i in range(n):
    card.append(input())


def func(c):
    if c == k:
        cards.add(''.join(select))
        return

    for i in range(n):
        if not isUsed[i]:
            select.append(card[i])
            isUsed[i] = True
            func(c + 1)
            select.pop()
            isUsed[i] = False


func(0)
print(len(cards))
