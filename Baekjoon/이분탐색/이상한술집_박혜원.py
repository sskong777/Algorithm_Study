# [13702] 이상한술집

# n 주전자의 개수
# k 인원수
n, m = map(int, input().split())
drink_list = [int(input()) for _ in range(n)]
start, end = 1, max(drink_list)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for drink in drink_list:
        total += (drink // mid)
    # mid 값으로 몇 명을 줄 수 있는지계산 하여 k명과 비교
    if total >= m:
        answer = mid
        start = mid+1
    else:
        end = mid-1


print(answer)
