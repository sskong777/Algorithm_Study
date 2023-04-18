from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
nums = []

cnt = 0
for i in permutations(cards, k):
    nums.append(''.join(i))

print(len(set(nums)))
