'''
문제 잘못이해해서 테스트케이스 1/2번의 런타임오류 뜨시는분을 위한 설명 (코드X)
https://school.programmers.co.kr/questions/41372
'''

def solution(tickets):

    result = ["ICN"]
    visited = [0] * len(tickets)
    answer = []
    def dfs(v, word):
        if v == len(tickets) and sum(visited) == len(tickets):
            answer.append(result[:]) # 복사해서 넣기!!
            return
        else:
            for i, ticket in enumerate(tickets):
                start, end = ticket
                if start == result[-1] and visited[i] == 0:
                    visited[i] = 1
                    result.append(end)
                    dfs(v + 1, end)
                    result.pop() # 조건에 안맞으면 다른 경로를 탐색하도록 되돌려주기
                    visited[i] = 0 # 이것도 마찬가지

    dfs(0, "ICN")
    answer.sort() # 답 여러 개일 수도 있으니까

    return answer[0]

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))