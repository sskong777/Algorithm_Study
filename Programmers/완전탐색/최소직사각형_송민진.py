def solution(sizes):
    max_x, max_y = 0, 0
    sizes = list(map(lambda x: sorted(x), sizes))
    for s in sizes:
        max_x = max(max_x, s[0])
        max_y = max(max_y, s[1])
    return max_x * max_y