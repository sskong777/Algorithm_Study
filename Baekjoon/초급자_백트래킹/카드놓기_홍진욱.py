from itertools import permutations

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

combinations = set(permutations(cards, k))
unique_integers = set(''.join(combination) for combination in combinations)

print(len(unique_integers))
