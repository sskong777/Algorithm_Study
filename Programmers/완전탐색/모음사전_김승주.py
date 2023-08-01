from itertools import product


def solution(word):
    answer = 0
    moeum = ['A', 'E', 'I', 'O', 'U']

    words = []
    for i in range(1, 6):
        words += list(''.join(x) for x in product(moeum, repeat=i))
    words.sort()

    for i in range(len(words)):
        if words[i] == word:
            return i+1
    return answer
