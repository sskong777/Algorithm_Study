def solution(brown, yellow):
    answer = []
    for h in range(1, yellow+1):
        if yellow % h == 0:
            w = yellow // h
        if brown == (w+2) * (h+2) - (w*h):
            return [w+2, h+2]