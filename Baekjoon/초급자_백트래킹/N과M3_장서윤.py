N, M = map(int, input().split())

card = list()

def func(k):
    if len(card) == M:
        print(' '.join(card))
        return

    for i in range(1, N + 1):
        card.append(str(i))
        func(k + 1)
        card.pop()

func(1)
