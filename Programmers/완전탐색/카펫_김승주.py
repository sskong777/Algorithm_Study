# 카펫의 가로 길이는 세로 길이 보다 길거나 같음
def solution(brown, yellow):
    answer = []
    # 갈색 격자의 수가 8이상 5000이하이므로 이므로 가로의 최소 길이는 3, 1688 이하
    for i in range(3, 2500):
        j = 1
        while j <= i:
            if (i * j) - (i*2 + (j-2)*2) == yellow and i >= j:
                if (i*j) - yellow == brown:
                    return [i, j]
            j += 1
    return answer
