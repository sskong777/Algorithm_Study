def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort()
    return max(w for w, _ in sizes) * max(h for _, h in sizes)
