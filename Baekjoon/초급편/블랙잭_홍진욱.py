from itertools import combinations

target = list(map(int, input().split()))
cards = list(map(int, input().split()))
maximum = 0

for comb in combinations(cards, 3):
    s = sum(comb)
    if maximum <= s <= target[1]:
        maximum = s

print(maximum)
