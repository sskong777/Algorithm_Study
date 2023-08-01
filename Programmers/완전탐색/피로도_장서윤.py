answer = 0


def dfs(k, cnt, dungeons, visited):
    global answer

    for i in range(len(dungeons)):
        answer = max(answer, cnt)
        if not visited[i] and k >= dungeons[i][0]:  # 체력이 최소 필요 피로도 보다 큰 경우
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False  # 방문 여부 지워줌

    if len(dungeons) == answer:  # 던전의 크기보다 커질 수 없으므로 가지치기함
        return


def solution(k, dungeons):
    visited = [False for _ in range(len(dungeons))]
    dfs(k, 0, dungeons, visited)

    return answer