parent = []


# root 노드 확인
def find(x):
    global parent

    # 루트 노트가 아닌 경우 찾을 때까지 재귀
    if parent[x] != x:
        return find(parent[x])

    return x


# 두 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    # 더 작은 쪽을 루트노드로 설정함
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0
    global parent

    parent = [x for x in range(n)]  # parent는 자기 자신으로 초기값 설정
    costs.sort(key=lambda x: x[2])  # 비용을 기준으로 오름차순 정렬

    for a, b, cost in costs:  # 비용이 낮은 간선부터 높은 간선까지 loop 반복
        if find(a) != find(b):  # 루트 노드가 다른 경우에만 union 수행함
            union(a, b)
            answer += cost

    return answer
