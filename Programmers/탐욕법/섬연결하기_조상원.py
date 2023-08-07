import heapq as hq
def solution(n, costs):
    tot = 0
    visited = set()
    costs.sort(key=lambda x : x[2])
    
    parent = [i for i in range(n)]
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union(a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    for a, b, c in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union(a, b)
            tot += c
            
    return tot