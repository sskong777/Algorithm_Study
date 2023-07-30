import sys
from collections import deque


def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt


def solution(n, wires):
    answer = sys.maxsize  # 최대값 설정
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tmps.pop(i)  # 한개씩 빼면서 계산 시작

        for wire in tmps:  # 빼고난 다음 graph만들어서 BFS
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)

        for idx, g in enumerate(graph):  # 시작점 설정
            if g != []:
                start = idx
                break

        cnts = BFS(graph, start, visited)
        other_cnts = n - cnts

        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
    return answer
