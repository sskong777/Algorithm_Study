def quick_sort(arr, pivot):
    tail = arr

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x >= pivot]

    return len(left), len(right)


def solution(citations):
    answer = 0

    citations.sort()
    length = len(citations)

    for h in range(1, length + 1):
        min_, max_ = quick_sort(citations, h)

        if min_ <= h <= max_:
            answer = max(answer, h)

        if max_ < h:
            break

    return answer