def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # cost가 낮은 순으로 정렬
    visited = [0] * n
    visited[costs[0][0]] = 1
    countVisited = 1
    while countVisited != n:
        for cost in costs:
            if visited[cost[0]] == 1 and visited[cost[1]] == 1:
                continue
            if visited[cost[0]] == 1 or visited[cost[1]] == 1:
                visited[cost[0]] = 1
                visited[cost[1]] = 1
                countVisited += 1
                answer += cost[2]
                break
    return answer
