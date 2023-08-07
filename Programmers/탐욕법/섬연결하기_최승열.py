
def solution(n, costs):
    def find(n):
        if parent[n] != n:
            parent[n] = find(parent[n])
        return parent[n]

    def union(a, b):
        a, b = find(a), find(b)
        if a > b: parent[a] = b
        else: parent[b] = a
    
    answer = 0
    parent = list(range(n))
    costs.sort(key=lambda x:x[2])
    
    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost
    return answer