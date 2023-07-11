from collections import Counter
def solution(clothes):
    answer = 1
    for c in Counter([c[1] for c in clothes]).values():
        answer *= (c+1)
    return answer-1