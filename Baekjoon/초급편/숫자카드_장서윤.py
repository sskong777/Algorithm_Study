N = int(input())
my_card = list(map(int, input().split()))
M = int(input())
comp_card = list(map(int, input().split()))

my_card.sort()


def binary(l, r, x):
    while l <= r:
        m = (l + r) // 2

        if my_card[m] == x:
            print(1, end=' ')
            return
        elif my_card[m] <= x:
            l = m + 1
        else:
            r = m - 1
    else:
        print(0, end= ' ')
    return

for x in comp_card:
    binary(0, N-1, x)

'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''