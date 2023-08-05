# 유니온 파인드 : https://blog.naver.com/ndb796/221230967614
# 크루스칼 알고리즘 : https://blog.naver.com/ndb796/221230994142

# 방법 2
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    link = set([costs[0][0]])
    ans = 0

    while True:
        if len(link) == n:
            break

        for cost in costs:
            v1, v2, c = cost
            if v1 in link and v2 in link:
                continue
            if v1 in link or v2 in link:
                link.update([v1, v2])
                ans += c
                break

    return ans

# 방법 1
'''
def solution(n, costs):
    def find(x):
        if x != parents[x]:
            return find(parents[x])
        return x

    # 경로 압축하면 이렇게
    # def find(x):
    # if x != parents[x]:
    #     parents[x] = find(parents[x])
    # return parents[x]

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False

        if a < b:
            parents[b] = a
        else:
            parents[a] = b
        return True

    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]

    ans = 0
    for cost in costs:
        v1, v2, c = cost
        if union(v1, v2):
            ans += c

    return ans
'''

# 방문은 다 하는데 연결 안된게 있을 수 있음, 경로 자체로 해야됨
'''
def solution(n, costs):
    costs.sort(key=lambda x : x[2])
    visited = [0] * n
    ans = 0

    for cost in costs:
        v1, v2, c = cost
        if not visited[v1] or not visited[v2]:
            visited[v1], visited[v2] = 1, 1
            ans += c

    print(costs)
    print(visited)
    return ans
'''

print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]))