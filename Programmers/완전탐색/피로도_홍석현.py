from itertools import combinations,permutations
def solution(k, dungeons):
    answer = -1
    for dungeons in permutations(dungeons,len(dungeons)):
        # 던전 순서 초기화 시작
        # 클리어횟수와 피로도 초기화
        clear = 0
        piro = k
        for dungeon in dungeons:
            # 던전을 클리어 할 수 있으면 
            if dungeon[0] <= piro:
                piro -= dungeon[1]
                clear += 1
        answer = max(answer,clear)
    return answer