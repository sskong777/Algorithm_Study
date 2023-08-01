def solution(k, dungeons):

    answer = -1
    visited = [False] * len(dungeons)

    def dfs(i, k, count):
        nonlocal answer, visited

        answer = max(answer, count)

        for i in range(len(dungeons)):
            if visited[i] == False and k >= dungeons[i][0] and k-dungeons[i][1] >= 0:
                visited[i] = True
                dfs(i, k-dungeons[i][1], count+1)
                visited[i] = False

    dfs(0,  k, 0)
    return answer
