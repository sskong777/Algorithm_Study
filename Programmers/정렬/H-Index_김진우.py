def solution(citations):
    citations.sort(reverse=True)
    # 인용횟수가 큰것부터 정리하면 큰것보다 큰건 없으니까 1, 2, 3 ... 으로 인덱스 구할 수 있다.
    h_index = 0

    for h in range(1, len(citations) + 1):
        if citations[h - 1] >= h:
            h_index = h

    return h_index


citations = [10, 8, 5, 4, 3]
print(solution(citations))