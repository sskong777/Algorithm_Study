# Visited 활용한 백트래킹 (DFS) 풀이
# 테스트 8 기준 132.66ms
def solution(k, dungeons):
    num = [0, 0] # num[0] 에는 max값을, num[1] 에는 현재 방문한 count를 저장.
    v = [0] * len(dungeons)

    def backtrack(energy):
        for i, (min_energy, energy_req) in enumerate(dungeons):
            if v[i] or energy < min_energy: 
                num[0] = max(num) # 최대 방문 수와 현재 방문한 수 중 더 큰 값을 저장
                continue
            v[i] = 1 # 방문 Flag
            num[1] += 1 # 방문한 숫자 + 1
            backtrack(energy - energy_req)
            v[i] = 0 # 백트랙킹
            num[1] -= 1
    backtrack(k)
    
    return num[0]

# permutation 사용 
# 테스트 8 기준 102.62ms
from itertools import permutations
def solution(K, dungeons):
    answer = 0
    for i in range(1, len(dungeons)+1):
        dungeon_perm = permutations(dungeons, i)
        for path in dungeon_perm:
            k, count = K, 0
            for req, use in path:
                if k < req: break
                k -= use
                count += 1
            answer = max(answer, count)
    return answer


# DFS 풀이
# 테스트 8 기준 31.3ms
def solution(k, d):
    ans = []
    for i, (_min, req) in enumerate(d):
        if k >= _min:
            res = solution(k - req, d[:i]+d[i+1:]) + 1
            ans.append(res)
    return max(ans) if ans else 0

# 위 코드를 숏코딩
# 테스트 8 기준 56.75ms
def solution(k, d):
    return max([solution(k - req, d[:i]+d[i+1:]) + 1 for i, (_min, req) in enumerate(d) if k >= _min] or [0])