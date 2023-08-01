def solution(citations):
    result = []

    for h in range(len(citations) + 1):  # 테스트 케이스 citations = [22, 42] => 2가 정답
        # range(len(citations))으로 하면 [22, 42]일때 정답이 1이 나와서 틀림
        # index가 아니라 실제 개수 끝까지 고려
        more_h = len(list(filter(lambda x: x >= h, citations)))
        print(more_h)
        if h <= more_h:
            result.append(h)

    return result[-1] if result else 0