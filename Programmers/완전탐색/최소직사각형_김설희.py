def solution(sizes):
    maxs = []
    mins = []
    for size in sizes:
        maxs.append(max(size))
        mins.append(min(size))

    return max(maxs) * max(mins)