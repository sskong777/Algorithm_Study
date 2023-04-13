N = int(input())
my_card = list(map(int, input().split()))
M = int(input())
comp_card = list(map(int, input().split()))

my_card.sort()

card = dict()


for i in my_card:
    if i in card:
        card[i] += 1
    else:
        card[i] = 1

def binary(l, r, x):
    while l <= r:
        m = (l + r) // 2

        if my_card[m] == x:
            print(card[x], end=' ')
            return
        elif my_card[m] <= x:
            l = m + 1
        else:
            r = m - 1
    else:
        print(0, end=' ')
    return


for x in comp_card:
    binary(0, N - 1, x)
