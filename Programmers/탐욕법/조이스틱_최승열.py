def solution(name):
    answer, N = 0, len(name)
    
    def find_dist(idx):
        for i in range(idx, N):
            if name[i] != "A": return N-i
        return 0
    
    def find_diff(s):
        diff = ord(s) - ord("A")
        return min(diff, 26 - diff)
    
    turn = N - 1
    for i in range(N):
        answer += find_diff(name[i])
        dist = find_dist(i+1)
        turn = min(turn, 2*i + dist, i + 2*dist)
        
    return answer + turn