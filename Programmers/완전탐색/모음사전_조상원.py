from itertools import product
def solution(word):
    answer = 0
    found = False
    toSort = []
    for i in range(1, 6):
        for combo in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            combo = ''.join(combo)
            toSort.append(combo)
    toSort.sort()
    return toSort.index(word) + 1