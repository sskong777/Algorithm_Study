N, M = map(int, input().split())

card = list()


def func(idx, k):
    if k == M:
        print(' '.join(card))
        return

    for i in range(idx, N + 1):
        card.append(str(i))
        func(i, k + 1)
        card.pop()


func(1, 0)
