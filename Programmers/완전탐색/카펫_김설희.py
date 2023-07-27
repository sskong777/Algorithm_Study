def solution(brown, yellow):
    for x in range(1, brown):
        if yellow == (x - 2) * ((brown + yellow) // x - 2):
            return sorted([x, (brown + yellow) // x], reverse=True)
