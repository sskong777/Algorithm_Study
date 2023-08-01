import itertools

def solution(k, dungeons):
    answer = 0
    cases = list(itertools.permutations(dungeons))
    for case in cases:
        hp = k
        tmp = 0
        for dungeon in case:
            if dungeon[0] <= hp:
                tmp += 1
                hp -= dungeon[1]
            answer = max(answer, tmp)
    return answer