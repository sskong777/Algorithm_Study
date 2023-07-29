answer = 0
length = 0


def DFS(k, count, dungeons, visited):
    global answer
    global length
    answer = max(answer, count)  # 최대값 찾기

    for i in range(length):
        if visited[i] == 0 and k >= dungeons[i][0]:  # 방문하지 않았고 던전을 돌수 있는 피로도일때
            visited[i] = 1  # 방문을 할수 있으므로 체크해주고 DFS호출
            # 방문을 했기 때문에 피로도 까주고, count 늘려주고 재귀
            DFS(k-dungeons[i][1], count+1, dungeons, visited)
            # 변수로 따로 저장 안하는 이유는 그거 건드리면 요기 아래로 돌아왔을때 다른 경우 체크할때 다시 다 원래대로 돌려줘야하는데
            # 골치아픔(생각한대로 안됐음)
            visited[i] = 0    # 다시 돌아왔기 때문에 체크 제거


def solution(k, dungeons):
    global answer
    global length
    length = len(dungeons)
    visited = [0] * length
    DFS(k, 0, dungeons, visited)
    return answer
