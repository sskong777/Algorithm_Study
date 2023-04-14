def get_closest(deck, target):

    left, right = 0, len(deck) - 1
    closest =  1000000000
    while left <= right:
        mid = (left + right) // 2
        if abs(deck[mid] - target) < abs(closest):
            closest = deck[mid]
        if deck[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return closest

def get_score(sel):
    return abs(max(sel) - min(sel))

decks = []

player = list(map(int, input().split()))
for _ in range(3):
    deck = list(map(int, input().split()))
    deck.sort()
    decks.append(deck)

ans =  1000000000

for i in range(player[0]):
    sel = [decks[0][i]]
    sel.append(get_closest(decks[1], sel[0]))
    sel.append(get_closest(decks[2], sel[0]))
    ans = min(ans, get_score(sel))
    sel[2] = get_closest(decks[2], sel[1])
    ans = min(ans, get_score(sel))

print(ans)
