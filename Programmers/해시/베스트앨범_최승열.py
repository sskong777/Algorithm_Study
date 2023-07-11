import heapq
def solution(genres, plays):
    album = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in album: 
            album[g]["count"] += p
            heapq.heappush(album[g]["songs"], (-p, i))
        else: 
            album[g] = {"count": p, "songs": [(-p, i)]}
    rank = {a["count"]: a["songs"] for a in album.values()}
    answer = []
    for r in sorted(rank, reverse=True):
        answer.append(heapq.heappop(rank[r])[1])
        if rank[r]: answer.append(heapq.heappop(rank[r])[1])
    return answer