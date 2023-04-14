n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
card_counts = {}
for card in cards:
    if card in card_counts:
        card_counts[card] += 1
    else:
        card_counts[card] = 1
counts = [card_counts.get(target, 0) for target in targets]
print(*counts)
