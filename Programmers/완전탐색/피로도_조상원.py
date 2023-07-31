import heapq
from collections import deque
def solution(k, dungeons):
    
    def count_possible_dungeons(curr, k):
        cnt = 0
        tmp = k
        for entry, price in curr:
            if entry > tmp:
                return cnt
            tmp -= price
            cnt+=1
        return cnt
        
    dungeons = sorted( dungeons, key = lambda x: x[0], reverse=True)
    print(dungeons)
    ret = []
    num = len(dungeons)
    visited = [0] * num
    dungeon_cnt = 0
    
    def backtrack(depth, curr, ret, k, maxdungeons):
        # print('--------------------------')
        # print('depth', depth, 'curr', curr)
        # print('depth', depth, 'ret', ret)
        if depth == num:
            # print('maxdungeons', count_possible_dungeons(curr, k))
            maxdungeons = max(maxdungeons, count_possible_dungeons(curr, k))
            return maxdungeons
            ret.append(curr[::])
            
        for i in range(len(dungeons)):
            if not visited[i]:
                visited[i] = 1
                curr.append(dungeons[i])
                maxdungeons = backtrack(depth+1, curr, ret, k, maxdungeons)
                
                curr.pop()
                visited[i] = 0
        return maxdungeons
    
    return backtrack(0, [], ret, k, dungeon_cnt)
    
    
