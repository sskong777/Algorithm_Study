def solution(n, wires):
    # Tree 생성
    T = {}
    for w1, w2 in wires:
        T.setdefault(w1, []).append(w2)
        T.setdefault(w2, []).append(w1)
    
    # dfs로 tree의 size를 계산하는 함수
    def size(i):
        s = 0
        for t in T[i]:
            if visited[t]: continue
            visited[t] = 1
            s += size(t) + 1
        return s
    
    _min = 100
    for w1, w2 in wires:
        visited = [0] * (n + 1)
        visited[w1] = 1
        visited[w2] = 1
        _min = min(_min, abs(size(w1) - size(w2)))
        
    return _min